---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 29 items, 4 important content pieces were selected

---

1. [Shopify abandons React Native for native Swift and Kotlin](#item-1) ⭐️ 8.0/10
2. [OpenAI Launches Hosted Agents API Powered by Codex Harness](#item-2) ⭐️ 8.0/10
3. [Researchers Question Trusting OpenAI with Unpublished Math Ideas](#item-3) ⭐️ 8.0/10
4. [trynix.dev boots any Nix package in the browser via qemu-wasm](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify abandons React Native for native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is moving its mobile apps away from React Native and back to fully native development using Swift for iOS and Kotlin for Android. The engineering blog post details the reversal of a major architectural bet, and the news has sparked a large debate with 897 points and 609 comments on Hacker News. This is a high-profile case of a major company reversing a significant cross-platform bet, which could influence how other large engineering organizations weigh React Native against native development. It highlights the trade-offs between code sharing and platform-specific performance, tooling, and team scaling. Shopify's move means separate Swift and Kotlin codebases for iOS and Android, trading shared JavaScript logic for direct access to platform APIs and native performance. The discussion notes Shopify has around 3,000 engineers, raising questions about whether such a large team is necessary for a relatively simple app.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework from Meta that lets developers build iOS and Android apps using React and JavaScript, sharing much of the code across platforms. Swift is Apple's compiled language for iOS and macOS, while Kotlin is JetBrains' language that Google adopted as its preferred language for Android in 2019. Native development typically offers better performance and platform integration but requires separate codebases and specialized teams.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**Discussion**: Commenters are sharply divided: some argue React Native was always the wrong choice and that native teams are more efficient, while others question Shopify's engineering scale and share anecdotes of AI-assisted migrations from React Native to native. A recurring theme is skepticism about whether 3,000 engineers are justified for Shopify's app complexity.

**Tags**: `#React Native`, `#mobile development`, `#Swift`, `#Kotlin`, `#engineering management`

---

<a id="item-2"></a>
## [OpenAI Launches Hosted Agents API Powered by Codex Harness](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI released a hosted Agents API, a managed service powered by the Codex harness that handles orchestration, long-running sessions, and tool use for cloud agents. It lets developers define agents declaratively instead of building their own agent loop and runtime. This marks a major shift toward "agent-as-a-service," where OpenAI manages the harness that developers previously had to build themselves, potentially reshaping how agent tooling is packaged and sold. It also intensifies competition with similar managed agent offerings from other providers like Anthropic's Claude Managed Agents. The service is built on the Codex harness and supports long-running sessions and tool use, but it raises questions about where credentials and state live and how agents access local data. Developers can still choose between the Agents API, the Agents SDK, and the Responses API depending on their needs.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: An agent harness (also called agent scaffolding) is the software infrastructure surrounding a large language model that lets it act as an autonomous agent — handling the agent loop, tool execution, sandboxing, and tracing. Building a harness from scratch is a deep rabbit hole, so many teams rely on open-source libraries, but those are still coupled to a specific environment. A managed harness lets you define an agent declaratively (pick a model, attach tools, write instructions) while the platform runs orchestration and execution.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents | OpenAI API</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some see value in a managed harness for developers without a filesystem (e.g., Cloudflare Workers), while others argue remote hosting is backwards because the real friction is securely provisioning local data access. A recurring view is that harnesses are deeply personal, like a .vimrc, so atomic building blocks may beat a one-size-fits-all hosted product.

**Tags**: `#OpenAI`, `#AI Agents`, `#API`, `#Developer Tools`, `#LLM Infrastructure`

---

<a id="item-3"></a>
## [Researchers Question Trusting OpenAI with Unpublished Math Ideas](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A Hacker News discussion, sparked by a Mathstodon post and amplified by 692 comments and 757 upvotes, raises concerns that OpenAI may have used researchers' unpublished mathematical ideas shared during model interactions without attribution. The debate centers on whether OpenAI's internal models, reportedly solving open math problems at a surprising rate, benefited from fresh training data supplied by collaborating researchers. This matters because it touches on research integrity, attribution norms, and the ethics of AI collaborations, potentially deterring mathematicians from sharing unpublished work with AI companies. If researchers cannot trust that their ideas will be credited, the open exchange that drives mathematical progress could be undermined, affecting both academia and the AI industry. Commenters note that OpenAI reportedly generated 300 billion output tokens from a model still in training shortly after learning there was a credible chance a major math proof was in that model's training data, which some find suspicious. Others argue that both things can be true: models may memorize chat content to improve latent representations, while reinforcement learning on verifiable math with massive compute can discover genuinely superhuman techniques unrelated to specific chats.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Mathstodon is a Mastodon server for mathematicians, part of the decentralized fediverse, where discussions about math and research culture take place. OpenAI has given many researchers free or paid access to its models, and internal models have been reported to solve open problems quickly, raising questions about whether researchers' unpublished ideas are being absorbed into training data. Attribution is a core norm in mathematics, so using someone's idea without credit is considered serious misconduct.

<details><summary>References</summary>
<ul>
<li><a href="https://joinmastodon.org/">Mastodon - Decentralized social media</a></li>
<li><a href="https://samjshah.com/2023/07/01/mastodon-mathstodon-join-us/">Mastodon??? MATHStodon !!! Join Us! | Continuous Everywhere but...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decentralized_identifier">Decentralized identifier - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are divided but broadly concerned: some compare OpenAI to a human collaborator and argue that publishing without attribution would be highly unethical, while others suggest the model's discoveries may be independent of specific chats. Several express suspicion about the timing of OpenAI's token generation and question whether AI is truly solving open problems or merely creating an illusion of progress.

**Tags**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#mathematics`, `#attribution`

---

<a id="item-4"></a>
## [trynix.dev boots any Nix package in the browser via qemu-wasm](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria launched trynix.dev, a project that uses qemu-wasm to boot an x86_64 Linux virtual machine entirely in the browser and load any Nix package from the past 13 years, with packages addressable by URL such as https://trynix.dev/?pkg=python3%403.6.2. He also released trynix-preview, a GitHub Action that comments a link on a pull request so reviewers can boot the PR's build in the browser without any server. This makes reproducible environments instantly shareable as plain URLs, which could transform code review, education, and debugging of historical software without requiring local setup or cloud infrastructure. It also demonstrates how far browser-based virtualization with WebAssembly has come, potentially lowering the barrier for anyone to inspect and run Nix-built software. The VM is powered by ktock's qemu-wasm project, which compiles QEMU to WebAssembly, and packages are URL-addressable so a specific version like Python 3.6.2 from 2017 can be loaded with a click. The trynix-preview GitHub Action adds a comment to pull requests linking to a browser-bootable build, with no server-side component involved.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a purely functional package manager developed in 2003 by Eelco Dolstra that treats packages as immutable values, enabling reproducible builds and declarative system configuration. QEMU is a widely used open-source machine emulator and virtualizer, and qemu-wasm is a project that compiles QEMU to WebAssembly so it can run inside a web browser. WebAssembly is a portable binary instruction format that lets high-performance code run in browsers at near-native speed.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_(package_manager)">Nix (package manager)</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#qemu`, `#virtualization`, `#reproducible-builds`

---