---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 32 items, 4 important content pieces were selected

---

1. [Calif Research Unveils WeWorm: First Zero-Click Worm via WeChat Calls, Built with AI](#item-1) ⭐️ 9.0/10
2. [vLLM v0.29.0 Makes Model Runner V2 Default, Adds 770B MoE Support](#item-2) ⭐️ 8.0/10
3. [Apple Announces Foldable iPhone Duo, Sparking Heated Debate](#item-3) ⭐️ 8.0/10
4. [Shopify acquires Tailwind Labs, the company behind Tailwind CSS](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Calif Research Unveils WeWorm: First Zero-Click Worm via WeChat Calls, Built with AI](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, the first zero-click worm that spreads through WeChat voice calls on both iOS and Android, compromising accounts without the victim answering or interacting with the phone. The team used AI to find the underlying memory corruption bug and write a remote code execution (RCE) exploit in about two days, then built the self-propagating worm in roughly one more week. This marks a paradigm shift in AI-assisted vulnerability discovery and weaponization, showing that a small team can now build a worm at a scale that previously required months of work by a larger team. Had it been deployed, experts quoted by the New York Times said it could have infected hundreds of millions of devices within hours, raising major implications for mobile security and AI safety. The vulnerability was a memory corruption issue in WeChat's VoIP stack, and the worm could hijack accounts and automatically call the victim's friends to propagate further. Tencent has since patched the underlying vulnerability, and Calif Research says it provided the judgment about what to target and how to test safely.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit compromises a device without any user interaction, making it far more dangerous than attacks that require a victim to click a link or open a file. A worm is self-replicating malware that spreads automatically from device to device, and remote code execution (RCE) means an attacker can run arbitrary code on a target machine over a network. WeChat is a massively popular messaging app in China with over a billion users, and its voice-calling feature made it a high-value target.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and ...</a></li>
<li><a href="https://www.1950.ai/post/wechat-zero-click-worm-how-ai-turned-a-voip-vulnerability-into-a-self-spreading-account-hijacking-t">WeChat Zero-Click Worm: How AI Turned a VoIP Vulnerability Into...</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights alarm at how quickly AI can now turn a vulnerability into a working worm, with some noting the exploit could have infected hundreds of millions of devices within hours. Others point out that Tencent has already patched the flaw, and some debate whether the demo's impact is overstated given the patch.

**Tags**: `#security`, `#ai`, `#mobile-security`, `#zero-click-exploit`, `#worm`

---

<a id="item-2"></a>
## [vLLM v0.29.0 Makes Model Runner V2 Default, Adds 770B MoE Support](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM released v0.29.0 with 594 commits from 277 contributors, making Model Runner V2 (MRV2) the default execution core for all models after the rollout began with pooling models. The release also adds support for Tencent's 770B/49B-active Hy4-preview MoE, Kimi K3 NVFP4 checkpoints, Qwen3.8-Flash-Next, GraniteSWA, and NemotronH_Omni_Reasoning_V3. MRV2 becoming the default marks a major architectural milestone for vLLM, the widely used open-source LLM inference engine, potentially improving throughput and latency for production serving. Support for very large MoE models like Hy4-preview and Kimi K3 keeps vLLM aligned with the frontier of open-weight model releases, which matters for anyone deploying these models. MRV2 gains CUDA graph memory profiling for KV cache auto-sizing, batch-sharded sampling that cuts per-step logits memory by 1/TP, and prompt embeds, while MRV1 remains in use for a few ROCm models and unsupported features. Breaking changes include removal of ten deprecated model architectures, migration of FlexOlmo/Olmo3/Hunyuan V1/VL to the Transformers backend, removal of the PyAV video decoder, and deprecation of `python -m vllm.entrypoints.openai.api_server` in favor of `vllm serve`.

github · khluu · Sep 9, 08:54

**Background**: vLLM is a popular open-source engine for serving large language models efficiently, using techniques like PagedAttention and continuous batching. Model Runner V2 is a from-scratch rewrite of vLLM's execution core, replacing Python-based model logic with GPU-native Triton kernels and separating CPU scheduling from GPU execution via async dispatch. MoE (Mixture-of-Experts) models activate only a subset of parameters per token, which is why Hy4-preview is described as 770B total with 49B active.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision ...</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#moe`

---

<a id="item-3"></a>
## [Apple Announces Foldable iPhone Duo, Sparking Heated Debate](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

Apple has announced the iPhone Duo, its first foldable iPhone, which features a seamless display without a visible crease and deep software integration. The announcement drew over 1,000 upvotes and nearly 1,900 comments on Hacker News, reflecting intense interest in the device. This marks Apple's entry into the foldable smartphone market, a segment previously dominated by Android manufacturers like Samsung and Google. Apple's move could legitimize the form factor, push developers to optimize apps for foldables, and reshape the premium smartphone landscape. Early hands-on impressions highlight that the Duo's screen has no visible crease, a common complaint on rival foldables, and that Apple Pencil support is included. However, pricing appears high, with some commenters balking at the cost even before knowing the exact figure.

hackernews · thecosmicfrog · Sep 9, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49630931)

**Background**: Foldable smartphones have existed for several years, with Samsung's Galaxy Z Fold and Flip series and Google's Pixel Fold leading the Android side. These devices aim to combine the portability of a phone with the larger screen of a tablet, but they have struggled with issues like screen creases, durability, and app optimization. Apple's entry is seen as a potential turning point for the category.

**Discussion**: Opinions on Hacker News are sharply divided: some question the appeal of a foldable phone, saying they would never need a tablet-like screen, while others praise the Duo's seamless display and Apple's software integration. Several commenters note that Apple's entry could finally push developers to properly design apps for foldables, and some speculate about a shift in Apple's keynote style under John Ternus.

**Tags**: `#Apple`, `#iPhone`, `#foldable`, `#hardware`, `#mobile`

---

<a id="item-4"></a>
## [Shopify acquires Tailwind Labs, the company behind Tailwind CSS](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify has acquired Tailwind Labs, the company behind the popular utility-first CSS framework Tailwind CSS, as announced on the official Tailwind blog. The acquisition comes after Tailwind Labs disclosed that AI-driven changes had severely impacted its business, including a 75% reduction in its engineering team and a 40% drop in documentation traffic since early 2023. This acquisition highlights the growing challenge of sustaining open-source projects when AI tools reduce traffic to documentation and make it easier to replicate commercial offerings. It could reshape the future of Tailwind CSS, a widely used framework in modern web development, and signals how major platforms like Shopify may absorb critical open-source tooling. Tailwind CSS is a utility-first CSS framework that differs from traditional frameworks like Bootstrap by providing low-level utility classes instead of predefined component styles. The acquisition raises questions about whether Tailwind will remain open source and how its commercial products, such as Tailwind UI templates, will evolve under Shopify.

hackernews · EdwinHoksberg · Sep 9, 13:27 · [Discussion](https://news.ycombinator.com/item?id=49626190)

**Background**: Tailwind CSS is an open-source CSS framework that lets developers style websites by composing small utility classes directly in HTML, rather than writing custom CSS. It has become one of the most popular tools for building modern web interfaces, with a large community and a commercial side that sells UI templates and components. Tailwind Labs, the company behind it, has faced financial pressure as AI coding assistants reduced the need for developers to visit documentation and made it easier to generate UI code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/c9hariom_claude-cursor-github-activity-7415783078985453569-YWZm">Tailwind CSS, AI , and the future of open - source sustainability</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about AI's impact on open-source sustainability, noting that Tailwind's documentation traffic dropped 40% and 75% of its engineering team was laid off. Some questioned whether Tailwind is still necessary for new projects given modern vanilla CSS and AI code generation, while others praised Tailwind's educational value and wished the team well. A recurring theme was that DevTools companies must offer hard-to-replicate services like hosting at scale to survive.

**Tags**: `#Tailwind CSS`, `#acquisition`, `#Shopify`, `#open source`, `#AI impact`, `#web development`

---