---
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 14 条内容中筛选出 2 条重要资讯。

---

1. [AI 以低成本首次击败顶尖 Stratego 玩家](#item-1) ⭐️ 9.0/10
2. [Redis 创始人 antirez 发布本地大模型推理工具 ds4](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 以低成本首次击败顶尖 Stratego 玩家](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10

研究人员发布了一种新算法，相关成果发表在《Nature》论文和 arXiv 预印本（2511.07312）中。该算法能够击败最优秀的人类 Stratego 玩家，且训练所用对局数比 DeepMind 的 DeepNash 少约 34 倍。尽管 Stratego 属于隐藏信息游戏，该方法仍实现了更强的棋力，而这类游戏曾让 AI 数十年难以攻克。 这标志着 AI 在不完美信息博弈领域取得重大进展，此类博弈包括扑克、谈判以及关键信息被隐藏的现实战略决策。效率的大幅提升表明，解决这些问题所需的算力可能远低于此前设想，从而有望降低研究和应用的门槛。 据社区讨论，该算法所玩对局数比 DeepMind 的 DeepNash 少约 34 倍，但最终棋力却强得多。Stratego 的隐藏信息意味着最佳着法取决于玩家并不掌握的信息，这使得前瞻搜索从根本上变得困难。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: Stratego 是一款 1946 年推出的双人棋盘游戏，每位玩家的棋子对对手隐藏，玩家必须通过对局推断敌方棋子的身份。在 AI 领域，这类游戏被称为不完美信息博弈，与象棋、围棋等所有棋子都可见的完美信息博弈相对。DeepMind 于 2022 年推出的 DeepNash 是此前用强化学习和搜索攻克 Stratego 的重要尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stratego">Stratego - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2007.13544">Combining Deep Reinforcement Learning and Search for Imperfect ...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，效率提升——比 DeepNash 少 34 倍对局——是让该 AI 真正可行的关键，因为隐藏信息使前瞻搜索无法进行。一些人对看似简单的 Stratego 竟难倒 AI 表示惊讶，还有人回忆起童年时棋子被悄悄做标记，以此不公平地揭示隐藏信息。

**标签**: `#AI`, `#game-playing`, `#imperfect-information`, `#reinforcement-learning`, `#Stratego`

---

<a id="item-2"></a>
## [Redis 创始人 antirez 发布本地大模型推理工具 ds4](https://dwarfstar.sh/) ⭐️ 8.0/10

以创建 Redis 闻名的 Salvatore Sanfilippo（网名 antirez）发布了 ds4（DwarfStar 4），这是一个用 C 语言编写的精简推理引擎，可在高内存 Mac、CUDA 和 ROCm 机器上本地运行前沿开源权重的大语言模型。该项目支持 DeepSeek V4 与 V4.1 Flash、GLM 5.x 以及 Qwen3.8 Flash Next，涵盖文本与视觉模型，并提供本地 API。 这一发布之所以重要，是因为它出自一位备受尊敬的系统程序员之手，提供了一种在本地硬件上运行超大规模开源权重模型的轻量方式，减少了对云端推理的依赖。这也表明，对于拥有高端工作站和 Apple Silicon 设备的用户来说，前沿规模模型的本地推理正变得切实可行。 ds4-agent 无需单独的 HTTP 服务器即可直接运行推理，将 token 历史与实时模型状态保存在一起，显示预填充进度，并使用各模型原生的工具格式，为 DeepSeek 和 GLM 提供了专用模板。该引擎刻意保持精简并针对特定模型系列进行优化，这限制了希望在同一平台上运行任意模型的用户的灵活性。

hackernews · fibo · 10月2日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49936575)

**背景**: antirez 是一位意大利程序员，最广为人知的成就是创建了被广泛使用的内存数据存储 Redis。近年来他公开撰文谈论使用大语言模型进行编程，而 ds4 正是他进军本地推理引擎的作品。本地运行大语言模型意味着在自己的硬件上执行模型，而不是把提示发送到云端 API，这可以提升隐私性、降低延迟并控制成本，但需要大量内存和算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez / ds 4 : DeepSeek 4 Flash and PRO local inference ...</a></li>
<li><a href="https://dwarfstar.sh/">DwarfStar 4 ( ds 4 ): Local DeepSeek V4.1, Qwen and GLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Salvatore_Sanfilippo">Salvatore Sanfilippo - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论总体积极：一位用户维护着 ds4 的共享库分支，提供 FFI 绑定和 Go 支持（ds4go）；另一位用户表示 ds4 是其 M5 Max 128GB 上最好的启动器，运行 Qwen 3.8 Flash 已超过一周，速度快且上下文窗口超长。其他人分享了相关项目，包括受 DwarfStar 启发、面向 Intel Xe-LP 的推理引擎，以及面向高端 Apple Silicon 的 Local Code 测试版；也有用户提到模型偶尔会遗忘先前内容，但这可能源于智能体框架而非 ds4 本身。

**标签**: `#LLM`, `#local inference`, `#Redis`, `#antirez`, `#Hacker News`

---