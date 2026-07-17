---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 64 items, 7 important content pieces were selected

---

1. [Firefox Runs Inside Another Browser via WebAssembly](#item-1) ⭐️ 9.0/10
2. [Moonshot AI Releases Kimi K3, a Frontier Open-Weight Model](#item-2) ⭐️ 8.0/10
3. [LM Studio Bionic: AI Agent for Open Models](#item-3) ⭐️ 8.0/10
4. [New arXiv Book on Mathematics of Data Science](#item-4) ⭐️ 8.0/10
5. [GPT-5.6 Codex Bug Can Delete $HOME Directory](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds Endorses AI in Linux Kernel](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Runs Inside Another Browser via WebAssembly](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, allowing it to run inside another browser like Chrome. The demo uses a WebSocket-based Wisp protocol to proxy all network traffic through Puter's server. This is a groundbreaking technical achievement that pushes the boundaries of WebAssembly, demonstrating that even a complex, full-featured browser can run inside another browser. It opens up possibilities for browser-in-browser applications, security testing, and portable computing environments. The project used an estimated $25,000 worth of AI tokens (Claude Opus and Fable) for debugging and JIT research, but cost much less due to a subscription plan. The 233MB gecko.wasm file and 18MB chrome-assets.tar.zst are loaded, and end-to-end encryption is supported for HTTPS traffic.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a binary instruction format that allows code written in languages like C++ to run in web browsers at near-native speed. Traditionally, browsers are native applications that cannot be nested inside another browser. This project compiles the Gecko rendering engine (Firefox's core) to Wasm, overcoming the limitation that browser code cannot open arbitrary network connections by using a WebSocket proxy.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HeyPuter/firefox-wasm">GitHub - HeyPuter/ firefox -wasm: Firefox in WebAssembly · GitHub</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=48926939">Show HN: Firefox in WebAssembly | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many impressed by the engineering effort and the $25k token cost. Some raised concerns about the server scaling required to proxy traffic, and the team confirmed they had to scale up servers to handle the HN traffic spike.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#Wasm`, `#demo`

---

<a id="item-2"></a>
## [Moonshot AI Releases Kimi K3, a Frontier Open-Weight Model](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI released Kimi K3, a 2.8-trillion-parameter open-weight model with a 1M-token context window, on July 16, 2026. It features Kimi Delta Attention (KDA) and native visual understanding, with pricing at $3/$15 per million tokens. Kimi K3 represents a significant step in Chinese AI labs driving toward commoditized frontier intelligence, offering competitive performance against US models at lower cost. Its open-weight release could accelerate AI adoption and shift value toward hardware and infrastructure. The model has 2.8 trillion parameters and uses a hybrid linear attention mechanism called Kimi Delta Attention (KDA) with Attention Residuals. Pricing is $3 per million input tokens and $15 per million output tokens, with a cached rate of $0.3, matching Anthropic's Sonnet series pricing.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models allow anyone to download and use the trained parameters, offering more transparency than closed APIs. Moonshot AI, based in Beijing, is one of China's 'AI Tiger' companies focusing on large language models. Kimi K3 is positioned as a frontier model competitive with top US models like those from Anthropic and OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/">Kimi API Platform</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K3? Moonshot's 2.8T, 1M-Context Flagship</a></li>

</ul>
</details>

**Discussion**: Community comments highlight Kimi K3's high pricing for a Chinese open-weight model but note it may be justified if truly frontier-level. Some see Chinese labs commoditizing intelligence to drive hardware sales, while others question the sustainability of massive training investments. Technical details like 1M context and benchmark comparisons to Sol/Fable are discussed.

**Tags**: `#AI`, `#LLM`, `#open-source`, `#pricing`, `#China`

---

<a id="item-3"></a>
## [LM Studio Bionic: AI Agent for Open Models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio has launched Bionic, a new AI agent app designed for local open models, enabling coding and document tasks with features like automatic checkpointing and voice input. Bionic brings agentic capabilities to local open models, offering enterprises and developers a secure, cost-effective alternative to cloud-based frontier models while maintaining data privacy. Bionic supports flexible model execution: run locally, via LM Link, or through LM Studio Secure Cloud for larger frontier open models. It includes automatic checkpointing in Work projects, saving every change the agent makes.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: LM Studio is a popular desktop app for running open-source large language models locally. Bionic extends this by adding an agentic harness that can autonomously perform tasks like coding and document manipulation, similar to tools like Codex but focused on local models.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic : the AI agent for open models</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic , a new AI agent app for open... - 9to5Mac</a></li>
<li><a href="https://fast.io/resources/ai-agent-checkpointing-resume/">AI Agent Checkpointing: Save State and Resume Guide | Fastio</a></li>

</ul>
</details>

**Discussion**: Community feedback is generally positive, with users praising the familiar UI and smooth integration with existing LM Studio models. Some users expressed concerns about the business model shift toward cloud services, while others see potential for enterprise adoption and local AI agents.

**Tags**: `#AI agents`, `#local LLMs`, `#open source`, `#developer tools`, `#LM Studio`

---

<a id="item-4"></a>
## [New arXiv Book on Mathematics of Data Science](https://arxiv.org/abs/2607.11938) ⭐️ 8.0/10

A new book titled 'Mathematics of Data Science' has been posted on arXiv, starting with high-dimensional intuition and covering fundamental mathematical concepts for modern data science. This resource addresses the critical need for a strong mathematical foundation in data science, helping practitioners understand high-dimensional phenomena that break classical intuition. The book emphasizes high-dimensional intuition, including spikiness and volumes, and connects these concepts to model fitting, training, and optimization in machine learning.

hackernews · Anon84 · Jul 16, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48939896)

**Background**: Data science often relies on high-dimensional data where traditional geometric intuition fails. Understanding these mathematical principles is essential for effective model building and avoiding common pitfalls.

**Discussion**: Commenters praised the book's focus on high-dimensional intuition, noting its importance for modern data science. One user highlighted that statistics remains the top priority skill for data scientists, while another emphasized the evolving nature of the field and the need for strong judgment.

**Tags**: `#data science`, `#mathematics`, `#high-dimensional statistics`, `#machine learning`, `#education`

---

<a id="item-5"></a>
## [GPT-5.6 Codex Bug Can Delete $HOME Directory](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

OpenAI has confirmed a bug in GPT-5.6's Codex where, under full access mode without sandboxing, the model may mistakenly delete the user's $HOME directory instead of a temporary directory. This bug highlights the serious risks of granting AI coding agents full system access without proper sandboxing, potentially causing irreversible data loss for developers. The bug occurs when full access mode is enabled, Codex runs without sandboxing or auto review, and the model attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex is an AI coding agent by OpenAI that can autonomously write and execute code. It offers different permission modes: Read Only, Default/Agent, and Full Access. Sandboxing isolates agent execution from the host system to prevent damage. Without sandboxing, a coding agent with full access can perform destructive actions like deleting files.

<details><summary>References</summary>
<ul>
<li><a href="https://daehnhardt.com/blog/2026/02/06/codex-cli-part-2-security-controls-and-safe-edits/">Codex CLI Part 2 — Security Controls & Safe Editing</a></li>
<li><a href="https://www.firecrawl.dev/blog/ai-agent-sandbox">AI Agent Sandbox: How to Safely Run Autonomous Agents in 2026</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-6"></a>
## [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab, led by Mira Murati, released Inkling, an open-weights Mixture-of-Experts multimodal model with 975B total parameters (41B active), trained on 45 trillion tokens of text, images, audio, and video, under the Apache-2.0 license. This release strengthens the US open-weights ecosystem with a competitive alternative to Chinese open models, and its Apache-2.0 license encourages broad customization and fine-tuning via the Tinker platform. The model card and training data documentation are notably sparse, providing minimal details on data sources. Additionally, a smaller variant Inkling-Small (276B total, 12B active) is promised but not yet released.

rss · Simon Willison · Jul 16, 15:35

**Background**: A Mixture-of-Experts (MoE) transformer uses multiple specialized subnetworks (experts) with a gating mechanism that activates only a subset of experts per input, enabling large total parameters with lower computational cost. Open-weights models make trained parameters publicly available for use and modification, often under permissive licenses like Apache-2.0, which allows free use, modification, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model">Open - weights Model | LLM Knowledge Base</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#AI model release`

---

<a id="item-7"></a>
## [Linus Torvalds Endorses AI in Linux Kernel](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator and top maintainer of Linux, publicly declared that Linux is not an anti-AI project and that AI is a clearly useful tool, dismissing objections from those who dislike AI. This strong endorsement from the most authoritative figure in the Linux community signals a major shift in open-source attitudes toward AI, potentially influencing the entire ecosystem to embrace AI tools in development. Torvalds stated that while there are other questions about AI, such as its economic impact, the question of its usefulness is no longer in doubt, and anyone who doubts it clearly hasn't used it.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linux is the world's largest open-source operating system kernel, with contributions from thousands of developers worldwide. Linus Torvalds has been its lead maintainer since 1991, and his opinions carry immense weight in the open-source community. AI tools, especially large language models (LLMs), have been controversial in some open-source circles due to concerns about licensing, ethics, and reliability.

**Tags**: `#Linux`, `#AI`, `#Open Source`, `#Linus Torvalds`

---