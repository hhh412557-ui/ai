---
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 29 条内容中筛选出 4 条重要资讯。

---

1. [Shopify 放弃 React Native，转向原生 Swift 和 Kotlin](#item-1) ⭐️ 8.0/10
2. [OpenAI 发布由 Codex Harness 驱动的托管 Agents API](#item-2) ⭐️ 8.0/10
3. [研究者质疑能否将未发表的数学想法托付给 OpenAI](#item-3) ⭐️ 8.0/10
4. [trynix.dev 借助 qemu-wasm 在浏览器中启动任意 Nix 包](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify 放弃 React Native，转向原生 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布其移动应用将放弃 React Native，回归使用 Swift（iOS）和 Kotlin（Android）的原生开发。这篇工程博客详细说明了这一重大架构决策的逆转，并在 Hacker News 上引发了 897 分、609 条评论的激烈讨论。 这是一家大型公司逆转重要跨平台决策的高调案例，可能影响其他大型工程团队在 React Native 与原生开发之间的权衡。它凸显了代码共享与平台特定性能、工具链及团队扩展之间的取舍。 Shopify 的举措意味着 iOS 和 Android 将分别使用 Swift 和 Kotlin 代码库，以放弃共享的 JavaScript 逻辑来换取对平台 API 的直接访问和原生性能。讨论中提到 Shopify 拥有约 3000 名工程师，这引发了关于一个相对简单的应用是否需要如此庞大团队的质疑。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源框架，允许开发者使用 React 和 JavaScript 构建 iOS 和 Android 应用，并在平台间共享大量代码。Swift 是苹果为 iOS 和 macOS 打造的编译型语言，而 Kotlin 是 JetBrains 的语言，谷歌于 2019 年将其采纳为 Android 的首选语言。原生开发通常能提供更好的性能和平台集成，但需要独立的代码库和专业团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**社区讨论**: 评论者意见严重分歧：一些人认为 React Native 从来就是错误选择，原生团队效率更高；另一些人则质疑 Shopify 的工程规模，并分享了借助 AI 辅助从 React Native 迁移到原生的经历。一个反复出现的主题是，对 Shopify 的应用复杂度是否需要 3000 名工程师表示怀疑。

**标签**: `#React Native`, `#mobile development`, `#Swift`, `#Kotlin`, `#engineering management`

---

<a id="item-2"></a>
## [OpenAI 发布由 Codex Harness 驱动的托管 Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 发布了一款托管的 Agents API，这是一项由 Codex harness 驱动的托管服务，负责编排、长时间运行的会话以及工具调用。它让开发者可以以声明式方式定义智能体，而无需自行构建智能体循环和运行时。 这标志着向“智能体即服务”的重要转变，OpenAI 接管了开发者过去必须自行构建的 harness，可能重塑智能体工具的打包和销售方式。这也加剧了与其他厂商（如 Anthropic 的 Claude Managed Agents）在托管智能体服务上的竞争。 该服务基于 Codex harness 构建，支持长时间运行的会话和工具调用，但也引发了关于凭证和状态存储位置以及智能体如何访问本地数据的疑问。开发者仍可根据需求在 Agents API、Agents SDK 和 Responses API 之间进行选择。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**背景**: 智能体 harness（也称智能体脚手架）是围绕大语言模型的软件基础设施，使其能够作为自主智能体运行——负责智能体循环、工具执行、沙箱和追踪。从零构建 harness 是一个深坑，因此许多团队依赖开源库，但这些库仍与特定环境耦合。托管 harness 让你以声明式方式定义智能体（选择模型、挂载工具、编写指令），而由平台负责编排和执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人认为托管 harness 对没有文件系统的开发者（如 Cloudflare Workers）有价值，另一些人则认为远程托管是倒退的，因为真正的难点在于安全地提供本地数据访问。一个反复出现的观点是，harness 高度个性化，就像 .vimrc，因此原子化的构建块可能优于一刀切的托管产品。

**标签**: `#OpenAI`, `#AI Agents`, `#API`, `#Developer Tools`, `#LLM Infrastructure`

---

<a id="item-3"></a>
## [研究者质疑能否将未发表的数学想法托付给 OpenAI](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

一场由 Mathstodon 帖子引发、在 Hacker News 上获得 692 条评论和 757 个点赞的讨论，引发了人们的担忧：OpenAI 可能在未注明来源的情况下，使用了研究者在与模型交互过程中分享的未发表数学想法。争论的核心在于，据报道正以惊人速度解决开放数学问题的 OpenAI 内部模型，是否受益于合作研究者提供的新鲜训练数据。 这件事之所以重要，是因为它涉及研究诚信、署名规范和 AI 合作的伦理问题，可能使数学家不愿再与 AI 公司分享未发表成果。如果研究者无法确信自己的想法会得到署名，推动数学进步的开放交流就可能受到损害，从而影响学术界和 AI 行业。 评论者指出，OpenAI 据称在得知某重大数学证明有可能存在于某模型的训练数据中后不久，就从仍在训练中的模型生成了 3000 亿个输出 token，这让一些人觉得可疑。也有人认为两种情况可以同时成立：模型可能记住聊天内容以改进潜在表示，而基于可验证数学的大规模强化学习也能发现与具体聊天无关的真正超人技巧。

hackernews · pred_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: Mathstodon 是面向数学家的 Mastodon 服务器，属于去中心化的 fediverse，数学和研究文化的讨论常在此进行。OpenAI 已向许多研究者提供免费或付费的模型访问权限，其内部模型据报能快速解决开放问题，这引发了研究者的未发表想法是否被吸收进训练数据的疑问。署名是数学界的核心规范，因此未经注明就使用他人想法被视为严重不当行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://joinmastodon.org/">Mastodon - Decentralized social media</a></li>
<li><a href="https://samjshah.com/2023/07/01/mastodon-mathstodon-join-us/">Mastodon??? MATHStodon !!! Join Us! | Continuous Everywhere but...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decentralized_identifier">Decentralized identifier - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧但普遍担忧：有人将 OpenAI 比作人类合作者，认为不署名发表将极不道德；也有人认为模型的发现可能与具体聊天无关。还有人对 OpenAI 生成 token 的时机表示怀疑，并质疑 AI 究竟是在真正解决开放问题，还是只是在制造进步的假象。

**标签**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#mathematics`, `#attribution`

---

<a id="item-4"></a>
## [trynix.dev 借助 qemu-wasm 在浏览器中启动任意 Nix 包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria 发布了 trynix.dev 项目，它利用 qemu-wasm 在浏览器中完全运行一个 x86_64 Linux 虚拟机，并能加载过去 13 年内的任意 Nix 包，包可通过 URL 直接寻址，例如 https://trynix.dev/?pkg=python3%403.6.2。他还发布了 trynix-preview，这是一个 GitHub Action，会在 Pull Request 中评论一个链接，让评审者无需服务器即可在浏览器中启动该 PR 的构建。 这让可复现环境可以仅通过普通 URL 即时分享，可能改变代码评审、教学以及历史软件调试的方式，无需本地安装或云端基础设施。它也展示了基于 WebAssembly 的浏览器虚拟化已经发展到何种程度，有望降低任何人检查和运行 Nix 构建软件的门槛。 该虚拟机由 ktock 的 qemu-wasm 项目驱动，该项目将 QEMU 编译为 WebAssembly；包可通过 URL 寻址，因此像 2017 年的 Python 3.6.2 这样的特定版本只需点击即可加载。trynix-preview GitHub Action 会在 Pull Request 中添加一条评论，链接到可在浏览器中启动的构建，整个过程不涉及服务器端组件。

rss · Simon Willison · 9月10日 23:44

**背景**: Nix 是由 Eelco Dolstra 于 2003 年开发的纯函数式包管理器，它将软件包视为不可变的值，从而实现可复现构建和声明式系统配置。QEMU 是广泛使用的开源机器模拟器和虚拟化工具，而 qemu-wasm 是一个将 QEMU 编译为 WebAssembly 的项目，使其能够在网页浏览器中运行。WebAssembly 是一种可移植的二进制指令格式，可让高性能代码以接近原生的速度在浏览器中运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#qemu`, `#virtualization`, `#reproducible-builds`

---