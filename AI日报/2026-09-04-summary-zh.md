---
title: "Horizon Summary: 2026-09-04 (ZH)"
date: 2026-09-04
lang: zh
---

> 从 22 条内容中筛选出 3 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Astra，ARC-AGI-3 得分接近满分](#item-1) ⭐️ 10.0/10
2. [Verisign 提议终止三级 .name 域名](#item-2) ⭐️ 8.0/10
3. [用 LLM 将 1993 年 Amiga 游戏移植到 Godot](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Astra，ARC-AGI-3 得分接近满分](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI 发布了新一代旗舰模型 GPT-6 Astra，在 ARC-AGI-3 基准测试中取得 99.9% 的得分，并在 Artificial Analysis 编码代理指数上取得重大进步。该模型现已开始向用户推出。 此次发布标志着 AI 发展的重要里程碑，GPT-6 Astra 在 ARC-AGI-3 上接近满分的表现表明其向更通用的推理能力迈出了一大步。编码基准的提升可能提高开发者的生产力，并加速 AI 在各行业的应用。 ARC-AGI-3 的 99.9% 得分是在特定 harness 配置下取得的，OpenAI 指出，如果没有该配置，得分约为 30%。该模型在 Artificial Analysis 编码代理指数（由 DeepSWE、Terminal-Bench v2.1 和 SWE-Atlas-QnA 组成）上也取得了重大进步。

hackernews · kibae · 9月3日 18:41 · [社区讨论](https://news.ycombinator.com/item?id=49554643)

**背景**: ARC-AGI-3 是一个交互式推理基准测试，旨在通过挑战 AI 代理探索新环境并即时获取目标来衡量其类人智能。Artificial Analysis 编码代理指数是由多个编码基准组成的综合得分，用于评估 AI 代理在真实软件工程任务上的表现。GPT-6 Astra 是 OpenAI 持续推出的大型语言模型系列的一部分，是 GPT-5 的后续版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/">How enabling two settings tripled our scores on the ARC-AGI-3 benchmark | OpenAI</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 ARC-AGI-3 的评分表表示怀疑，指出 99.9% 的数字在没有特定 harness 的情况下具有误导性，且其他基准测试仅显示适度改进。一些用户质疑演示中强调自主购物的做法，而另一些用户则将其与 François Chollet 关于衡量智能的工作相类比，认为进步可能仍是技能获取而非真正的 AGI。

**标签**: `#AI`, `#OpenAI`, `#GPT-6`, `#large language models`, `#ARC-AGI`

---

<a id="item-2"></a>
## [Verisign 提议终止三级 .name 域名](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

Verisign 提议终止所有三级 .name 域名（例如 john.smith.name），这将影响现有注册，并释放相应的二级域名（smith.name）供新注册。该提案目前正在由 ICANN 审议。 这一政策变化可能破坏现有域名注册的稳定性，并助长域名抢注，与 ICANN 确保互联网唯一标识符系统稳定安全运行的使命相悖。它影响现有的 .name 注册者，并引发对注册机构问责制和域名所有权可靠性的更广泛担忧。 该提案专门针对三级 .name 域名，而不影响像 dvt.name 这样的二级域名。Verisign 未提及是否会在一定时期内保留释放的二级域名以防止抢注，这留下了重大空白。

hackernews · pavel_lishin · 9月3日 14:54 · [社区讨论](https://news.ycombinator.com/item?id=49550772)

**背景**: .name 顶级域旨在支持个人姓名，允许在二级（如 jane.name）和三级（如 jane.doe.name）注册。三级注册是原始方案的一部分，但采用率较低。Verisign 根据与 ICANN 的合同运营 .name 注册局，域名政策的变更需要 ICANN 批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.opensrs.com/support/solutions/articles/201000063568--name-domain-policies">A Domain Resellers Guide to . NAME Domain Policies : OpenSRS...</a></li>
<li><a href="https://webmasters.stackexchange.com/questions/85024/clarify-terminology-top-level-domain-second-level-domain-and-apex-domain">Clarify terminology: top level domain , second level domain , and apex...</a></li>
<li><a href="https://support.enom.com/support/solutions/articles/201000127176--name-domain-policies">NAME Domain Policies : Enom Customer Support</a></li>

</ul>
</details>

**社区讨论**: 评论者对终止表示担忧，有人建议 Verisign 应停止新注册但尊重现有注册。其他人指出这与 ICANN 的使命相矛盾，并存在域名抢注风险，而一些人澄清二级域名不受影响。少数人将其与域名租赁的固有风险相类比。

**标签**: `#ICANN`, `#domain names`, `#policy`, `#internet governance`, `#Verisign`

---

<a id="item-3"></a>
## [用 LLM 将 1993 年 Amiga 游戏移植到 Godot](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

开发者使用 Claude Fable 5 成功将他 1993 年用 MC68000 汇编编写的 Amiga 游戏移植到 Godot 引擎，并在一个晚上内实现了可运行的游戏。LLM 使用 vasm 汇编代码，直到二进制与原始版本完全一致，除了 108 字节的差异，这是由于原始 AsmOne 内存快照造成的。 这展示了 LLM 在复古计算和遗留代码移植中的实用高价值用例，可能降低保存和现代化经典软件的门槛。它还突出了 LLM 处理低级汇编并生成字节相同输出的能力，这可能激发类似的游戏保存和迁移项目。 原始游戏于 1993 年在巴格达使用 MC68000 汇编构建，并使用 AsmOne 汇编，该汇编器直接汇编到内存；发布文件是运行中游戏的内存快照，而非干净的汇编输出。LLM 在开发者的 Mac 上使用 vasm 进行迭代，直到二进制与原始版本匹配，除了 108 字节的差异，开发者从未独立验证这一点。

hackernews · rabahs · 9月3日 14:28 · [社区讨论](https://news.ycombinator.com/item?id=49550375)

**背景**: Amiga 是 20 世纪 80-90 年代的经典个人电脑，以其定制硬件和汇编编程而闻名。MC68000 汇编是用于 Amiga 的 Motorola 68000 CPU 的低级语言。vasm 是一个可移植的汇编器，支持多种 CPU，而 AsmOne 是 Amiga 的集成汇编环境，直接汇编到内存。移植此类遗留代码通常需要手动重写，但 LLM 可以协助将汇编翻译成 Godot 中的 GDScript 等现代语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>
<li><a href="https://aminet.net/package/dev/asm/ASM-One">Aminet - dev/asm/ASM-One.lha Asm One 1.02 Manual : Rune Gram-Madsen : Free Download ... ASM-One Macro Assembler - HandWiki Commodore Software - ASM-One v1.02 Manual ASM-One Page - theflamearrows.info ASM-One Macro Assembler - EverybodyWiki Bios & Wiki Asm One 1.02 Manual : Free Download, Borrow, and Streaming ...</a></li>
<li><a href="https://en.wikibooks.org/wiki/68000_Assembly">68000 Assembly - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**社区讨论**: 评论者对原始的汇编工作表示钦佩，并分享了使用 LLM 移植复古游戏的类似经验，例如将 ZX81 游戏转换为 Go。一些人讨论了技术细节，如使用硬件寄存器与系统友好调用的区别，另一些人则指出该游戏与《Gods: Into the Wonderful》相似。

**标签**: `#LLM`, `#retrocomputing`, `#game development`, `#code porting`, `#Godot`

---