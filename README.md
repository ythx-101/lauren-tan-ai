# 土豆 Lauren Tan 的 AI 用法全集

> A Chinese-language field guide to how Lauren Tan (@poteto), principal engineer at SpaceXAI working on Grok Bot and Cursor and author of pstack, works with AI coding agents: the trust ladder, verification skills, the inner/outer loop, and her November 2026 shift from multi-agent adversarial review to deterministic checks and formal verification (TLA+, Kani, Lean, /statechart). It indexes 99 of her posts, talks and interviews plus 13 third-party write-ups, with English quotes kept verbatim. Read it at https://ythx-101.github.io/lauren-tan-ai/ (plain-text version: [llms-full.txt](https://ythx-101.github.io/lauren-tan-ai/llms-full.txt)).

**土豆 Lauren Tan（@poteto）的 AI 用法全集：给想把编程 agent 用好的开发者和 AI 从业者，把她散落在 X、GitHub、演讲里的方法论整理成一页可查的中文长文，含 99 条原帖索引和 13 篇第三方解读。**

在线阅读：<https://ythx-101.github.io/lauren-tan-ai/>

## 三种视图

| 视图 | 文件 | 说明 |
|---|---|---|
| 长文 | [`index.html`](https://ythx-101.github.io/lauren-tan-ai/) | 方法论综合 + 99 条原帖索引 + 13 篇第三方解读，主阅读入口 |
| 星云图 | [`graph.html`](https://ythx-101.github.io/lauren-tan-ai/graph.html) | 99 条原帖按时间排列的同心盘 |
| 星系 | [`galaxy.html`](https://ythx-101.github.io/lauren-tan-ai/galaxy.html) | 把每条内容画成一颗星，按主题聚成星系 |

## 内容目录

`index.html` 的章节：

1. 一句话核心：产量来自信任，不来自多开 agent
2. 工具栈演变：从终端里编排 CLI agent，到在 GUI 和云端搭一个能自己跑的厨房
3. 信任阶梯：一级一级往上爬，没有捷径
4. 验证技能：一个 CLI，加一张 Feature Map
5. 纠正即消除：每次纠正 agent，都想想怎么让这个问题彻底消失
6. 新员工比喻：agent 是永远失忆、但很好教的新员工
7. 技能化失败模式：pstack 和 /poteto-mode，把观察到的失败模式全部变成技能
8. 内环 / 外环：Grok Bot 是外环，Cursor Projects 是内环
9. token 花在环境上：前期投入环境，长期反而省
10. 辟谣「她没说过的话」：流传最广的几句话，她本人没说过
11. 按时间查原帖：99 条条目索引
12. 第三方解读：13 篇，按发布时间排

## 本地打开（快速开始）

这是纯静态站，不需要安装任何东西。

```bash
git clone https://github.com/ythx-101/lauren-tan-ai.git
cd lauren-tan-ai
# 直接双击 index.html 即可；
# 如果想避开浏览器对本地文件的限制，起一个本地服务：
python3 -m http.server
```

## 怎么用

先读方法论，再按 `#编号` 跳到原帖。例如 `index.html#e64` 直接定位到第 64 条；第三方解读用 `#t1` … `#t10`。

加条目后可运行自检（零依赖，只需 Python 3）：

```bash
python3 scripts/check_links.py
```

## FAQ

**Lauren Tan / poteto 是谁？**
页面首屏写的是：Lauren Tan，X 账号 @poteto，SpaceXAI 首席工程师，负责 Grok Bot 和 Cursor。

**什么是「信任阶梯」（Trust Ladder）？**
她自己走过的阶梯：从同时盯 1～5 个对话的微操，到当 "meat proxy"，再到用验证技能给 agent "手和眼睛"、准备好环境，最后 agent 自己合并 PR，她早上看提交历史（#64、#59，第三方整理见 T7）。核心观点是吞吐量来自信任，而不是开更多 agent（#13）。

**pstack 是什么，在哪里？**
她的个人技能集和工程原则，把观察到的失败模式全部变成技能（#13）。代码在 <https://github.com/cursor/plugins/tree/main/pstack>。名字在调侃 gstack，两人同姓、没有亲属关系（#30）。

**「内环 / 外环」指什么？**
"cursor projects are my inner loop and grok bot is my outer loop"（#64）。外环 Grok Bot 盯 Slack、X、邮件、Linear，发现问题后发给对应的 Cursor Project；内环 Cursor Projects 的协调者 agent 不亲自干活，只委派和编排。

**网上流传的「2,500 PRs/月」等数字可信吗？**
页面原话：这些数字都是她本人自述，未独立核实。页面还列出了出入：X 标题写 2,500，口播约 2,000（T4、T8）。她也强调 2,500 个 PR 不等于 2,500 个功能（#64）。

**哪些流传的话她本人没说过？**
例如 "Chief of Staff + 3 managers + 16 workers"、"只有 1% 的人用对了 GrokBot"、"$850,000 offer"。页面核对了两份完整逐字稿，都没有这些原话。详见 `index.html` 的「需要注意 / 未核实」一节（#caveats）。

**内容多久更新、怎么纠错？**
没有固定更新周期。发现错误或遗漏，欢迎提 Issue 或 PR。

## 适用场景 / 和同类资料的区别

适合想系统了解 Lauren Tan 的 agent 工作方式、想查某句话出处的人。相对零散的推文串和单篇解读，这里：按主题汇总；每个观点标了原帖编号；区分她本人原话和第三方解读；单列辟谣与未核实项。

## English summary

A curated Chinese-language guide to how **Lauren Tan (@poteto)** uses AI coding agents and an agentic workflow, with Cursor and Grok Bot. It synthesizes her methodology — the trust ladder, verification skills (a CLI plus a feature map), the inner/outer loop (Cursor Projects and Grok Bot), and **pstack**, her set of skills and engineering principles — and indexes 99 of her posts, articles, talks and interviews plus 13 third-party write-ups. Quotes stay in English; the Chinese text is the curator's summary. Numbers such as PR counts are self-reported and unverified.

## 来源与声明

- 引文保留英文原文，中文为整理者的概括；原文版权归原作者。
- 文中的 PR 数、token 数均为 Lauren Tan 本人自述，未独立核实。

## 第三方资源署名

- 字体：[得意黑 Smiley Sans](https://github.com/atelier-anchor/smiley-sans)，SIL OFL 1.1；本仓库只放了子集 `fonts/smiley-sans-subset.woff2`。
- [d3](https://d3js.org) v7.9.0（`lib/d3.min.js`），ISC 许可，版权归 Mike Bostock，文件头保留了版权行。
- 星系页致敬 [Kat ⊷ the Poet Engineer (@poetengineer__)](https://x.com/poetengineer__/status/2110060584138084373)。
- 胸像点云（`art/bust-points.js`）：seedream-5.0 生成的白色大理石女性胸像图，按明暗对比采样（已去掉水印区），用于星系页。

## 作者

整理：青月（X [@YuLin807](https://x.com/YuLin807)）。
