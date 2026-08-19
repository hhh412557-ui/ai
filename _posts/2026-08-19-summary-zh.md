---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 21 条内容中筛选出 4 条重要资讯。

---

1. [Mojo 编程语言在 Apache 2 下开源](#item-1) ⭐️ 9.0/10
2. [Turbovec 将谷歌的 TurboQuant 向量搜索引入 Rust](#item-2) ⭐️ 8.0/10
3. [苹果以 5%佣金取代欧盟核心技术费](#item-3) ⭐️ 8.0/10
4. [Cerebras CS-4 性能与功耗翻倍](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo 编程语言在 Apache 2 下开源](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Modular 已根据 Apache 2 许可证发布了 Mojo 编译器和工具链，兑现了 2023 年 5 月做出的承诺。此前一周，Mojo 1.0 刚刚发布。 在宽松许可证下开源 Mojo 有助于社区更广泛地采用和贡献，可能加速其作为 AI 和 GPU 编程高性能语言的发展。此举符合开源基础 AI 基础设施的趋势。 Mojo 最初旨在成为 Python 的超集，但该目标在 2025 年 8 月左右被放弃。该语言现在专注于使用受 Python 启发的语法进行 GPU 编程，并基于 MLIR 编译器框架构建，从而能够针对各种硬件加速器进行优化。

rss · Simon Willison · 8月18日 21:39

**背景**: Mojo 是 Modular Inc. 开发的系统编程语言，专为高性能 AI 基础设施设计。它采用类似 Python 的语法，但包含受 Rust 启发的静态类型和借用检查等功能。Apache 2 许可证是一种宽松的开源许可证，允许用户自由使用、修改和分发软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://www.infoworld.com/article/4081105/revisiting-mojo-a-faster-python.html">Revisiting Mojo : A faster Python? | InfoWorld</a></li>

</ul>
</details>

**标签**: `#Mojo`, `#open source`, `#programming language`, `#AI`, `#compiler`

---

<a id="item-2"></a>
## [Turbovec 将谷歌的 TurboQuant 向量搜索引入 Rust](https://github.com/RyanCodrai/turbovec) ⭐️ 8.0/10

Turbovec 是谷歌 TurboQuant 算法在 Rust 中的一个新实现，用于向量搜索，可实现内存高效且快速的相似性搜索。据报道，它可将 1000 万份文档压缩至仅 4GB，适合本地和隐私优先的应用。 该项目将最先进的量化方法引入 Rust 生态系统，可能改善本地搜索应用的性能和内存使用。它可以帮助开发者构建高效、保护隐私的搜索工具，而无需依赖云服务。 Turbovec 使用 Rust 构建，旨在与流行的向量搜索库 FAISS 兼容。该项目在 GitHub 上开源，社区成员正在讨论将其编译为 WASM 用于浏览器扩展，以及提供 SQLite 绑定以便集成。

hackernews · fittingopposite · 8月18日 18:07 · [社区讨论](https://news.ycombinator.com/item?id=49349898)

**背景**: 向量搜索是一种通过将项目表示为高维向量并使用最近邻搜索来查找相似项的技术。量化通过压缩向量来减少内存占用，从而实现更快、更可扩展的搜索。TurboQuant 是谷歌最近推出的一种算法，可在最小精度损失下实现高压缩率，而 Turbovec 将其引入 Rust。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://github.com/Firmamento-Technologies/TurboQuant">GitHub - Firmamento-Technologies/TurboQuant: Near-optimal ...</a></li>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出 FAISS 已不再是领先技术，并引用了基准测试网站。用户对内存节省和更快的开发潜力感到兴奋，也有人建议改进 README 以促进采用。此外，还有对编译为 WASM 用于浏览器扩展以及 SQLite 绑定的兴趣。

**标签**: `#vector-search`, `#rust`, `#quantization`, `#information-retrieval`, `#machine-learning`

---

<a id="item-3"></a>
## [苹果以 5%佣金取代欧盟核心技术费](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/) ⭐️ 8.0/10

苹果宣布对其欧盟 App Store 政策进行更改，将核心技术费替换为对 App Store 之外分发的应用的数字交易收取 5%的佣金，并取消了初始获取费和商店服务费。 这简化了开发者的费用结构，并解决了苹果与欧盟委员会在商业条款和替代分发方面的分歧，可能缓解监管紧张局势，并影响开发者在欧盟的成本和策略。 新条款还取消了初始获取费和商店服务费。苹果将继续要求对替代分发的应用进行公证，以维护用户安全。

hackernews · newusertoday · 8月18日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=49348055)

**背景**: 核心技术费于 2024 年初推出，是苹果为遵守欧盟《数字市场法案》而采取的措施，在应用安装量超过 100 万次后，对每次首次年度安装收取 0.50 欧元。新的 5%佣金取代了这种按安装次数收费的方式，适用于在 App Store 之外分发的应用，而通过 App Store 销售的应用将对数字商品和服务支付 26%的佣金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/">Apple announces changes for apps in the European Union - Apple</a></li>
<li><a href="https://www.cnbc.com/2026/08/18/apple-eu-app-store-fees-iphone.html">Apple overhauls EU app store fees to resolve payments clash</a></li>
<li><a href="https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/">Apple overhauls its EU App Store fees, loosens rules for alternative app stores | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一。一些人质疑苹果为何在已经收取开发者计划费用的情况下还需要核心技术佣金，而另一些人则注意到对 Netflix 和 Spotify 等阅读器应用的改进，这些应用从 2026 年 10 月 1 日起可以在没有可操作链接的情况下推广应用外优惠。

**标签**: `#Apple`, `#EU`, `#App Store`, `#regulation`, `#developer fees`

---

<a id="item-4"></a>
## [Cerebras CS-4 性能与功耗翻倍](https://newsletter.semianalysis.com/p/cerebrass-next-generation-cs-4-fast) ⭐️ 8.0/10

Cerebras 发布了其下一代 CS-4 系统，与上一代相比，AI 工作负载的性能和功耗均翻倍。CS-4 是新的 Cerebras Nexus 平台架构的首个迭代产品。 CS-4 的显著性能提升可能加速大规模 AI 模型的训练，并可能影响 AI 硬件领域的竞争格局。它为训练大规模模型的组织提供了基于 GPU 系统之外的另一种选择。 CS-4 采用 2D 环形互连拓扑，可支持高达 50 万亿参数的模型，尽管目前尚不存在这样的模型。该系统旨在提供前所未有的规模化解码性能。

rss · Semianalysis · 8月19日 01:32

**背景**: Cerebras 以其晶圆级引擎（WSE）而闻名，这是一种单一的晶圆级集成处理器，包含计算、内存和互连结构。CS-4 基于 2024 年 3 月推出的 WSE-3 架构，该架构拥有 4 万亿个晶体管和 90 万个 AI 优化核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/cs4">Product - System - Cerebras</a></li>
<li><a href="https://www.theregister.com/systems/2026/08/19/cerebras-cs-4-rack-systems-juice-chips-for-every-last-drop-of-ai-performance/5289286">Cerebras CS-4 rack systems juice chips for every last drop of AI performance</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Cerebras`, `#semiconductors`, `#machine learning`, `#high-performance computing`

---