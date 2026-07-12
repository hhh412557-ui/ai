---
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 45 items, 3 important content pieces were selected

---

1. [Grok Build CLI Uploads Entire Repo, Including Secrets](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Outperforms Physicians in Response Quality](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Grok Build CLI Uploads Entire Repo, Including Secrets](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

A security researcher discovered that xAI's Grok Build CLI uploads the entire repository contents, including sensitive files like .env, to xAI servers regardless of what the agent reads. This privacy flaw undermines developer trust in AI coding tools, as it exposes secrets and proprietary code to a third party without explicit consent. The CLI uploads every tracked file's content plus git history, independent of what the agent reads, and transmits file contents verbatim and unredacted.

hackernews · jhoho · Jul 12, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48877371)

**Background**: Grok Build is a terminal-based coding agent powered by Grok 4.5, released in beta for SuperGrok and X Premium Plus subscribers. Many AI coding tools upload code to cloud models for processing, but the extent of data sent is often unclear to users.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock and concern, with some noting they already sandbox other tools like Claude to prevent such data leakage. Others pointed out that many coding agents behave similarly, but the lack of transparency is the core issue.

**Tags**: `#privacy`, `#security`, `#AI coding tools`, `#xAI`, `#data leakage`

---

<a id="item-2"></a>
## [GPT-5.6 Outperforms Physicians in Response Quality](https://x.com/sama/status/2075985056846451123) ⭐️ 9.0/10

Sam Altman announced that physicians found fewer flaws in GPT-5.6 responses compared to those written by physicians themselves. This suggests GPT-5.6 may surpass human experts in medical communication, potentially transforming clinical decision support and patient education. GPT-5.6 is a family of models released by OpenAI on July 9, 2026, with variants Luna, Terra, and Sol; the Sol variant achieves state-of-the-art results in coding, science, and cybersecurity.

twitter · sama · Jul 11, 16:46

**Background**: Large language models like GPT-5.6 are trained on vast text data to generate human-like responses. In medical AI, evaluating response quality often involves comparing AI outputs to those of human physicians using rubrics or expert review. Altman's claim indicates GPT-5.6's responses were judged superior by physicians themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GPT-5.6`, `#healthcare`, `#medical AI`, `#OpenAI`

---

<a id="item-3"></a>
## [vLLM v0.25.0: Model Runner V2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 makes Model Runner V2 the default execution path for all dense models, removes the legacy PagedAttention implementation, and introduces a new Streaming Parser Engine along with support for several new models like LLaVA-OneVision-2 and GLM-5. This release marks a major architectural shift in vLLM, improving performance and modularity by standardizing on Model Runner V2, which benefits all users of dense models. The removal of PagedAttention simplifies the codebase and signals full adoption of newer attention backends. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers modeling backend has been optimized to match native vLLM performance, and the release includes 558 commits from 232 contributors.

github · khluu · Jul 11, 20:06

**Background**: vLLM is a high-performance inference engine for large language models, originally known for its PagedAttention algorithm that efficiently manages the key-value cache. Model Runner V2 is a redesigned execution core that addresses technical debt and improves modularity, performance, and support for advanced features like speculative decoding and multimodal inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#model serving`

---