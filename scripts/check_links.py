#!/usr/bin/env python3
"""零依赖自检：站内锚点、本地资源引用、条目数。用法：python3 scripts/check_links.py"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "graph.html", "galaxy.html"]
problems = []


def is_dynamic(v):
    return any(c in v for c in "'+`{}$") or v.startswith("javascript:")


def is_external(v):
    return re.match(r"^(https?:|//|mailto:|data:|tel:)", v) is not None


for page in PAGES:
    text = (ROOT / page).read_text(encoding="utf-8")
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    for m in re.finditer(r'\b(?:href|src)=(["\'])(.*?)\1', text):
        v = m.group(2).strip()
        if not v or is_dynamic(v) or is_external(v):
            continue
        if v.startswith("#"):
            if len(v) > 1 and v[1:] not in ids:
                problems.append(f"{page}: 缺少锚点 id {v}")
            continue
        path, _, frag = v.partition("#")
        path = path.split("?")[0]
        if not path:
            continue
        target = (ROOT / page).parent / path
        if not target.exists():
            problems.append(f"{page}: 本地文件不存在 {v}")
        elif frag and target.suffix == ".html":
            tids = set(re.findall(r'\bid=["\']([^"\']+)["\']', target.read_text(encoding="utf-8")))
            if frag not in tids:
                problems.append(f"{page}: {path} 中缺少锚点 id #{frag}")

# 条目数：index.html 的 id="eN" 数量 vs galaxy-data.js 的 meta.subtitle
index = (ROOT / "index.html").read_text(encoding="utf-8")
n_entries = len(set(re.findall(r'\bid=["\']e(\d+)["\']', index)))
try:
    data = (ROOT / "galaxy-data.js").read_text(encoding="utf-8")
    m = re.search(r'"subtitle"\s*:\s*"[^"]*?(\d+)\s*stars', data)
    expected = int(m.group(1)) if m else None
except OSError:
    expected = None
if expected is None:
    print("警告: 读不到 galaxy-data.js 的 star 数，跳过条目数检查")
elif expected != n_entries:
    problems.append(f"条目数不一致: index.html 有 {n_entries} 个 id=eN，galaxy-data.js 写 {expected} stars")

if problems:
    print("发现问题:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"OK: 锚点和本地引用完好，条目数 {n_entries}")
