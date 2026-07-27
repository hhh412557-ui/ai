---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 50 items, 4 important content pieces were selected

---

1. [LLMs + Theorem Provers: The Future of Code Verification](#item-1) ⭐️ 9.0/10
2. [vLLM v0.26.0: Inkling support, DeepSeek-V4 optimizations, flexible attention](#item-2) ⭐️ 8.0/10
3. [PGSimCity Visualizes PostgreSQL Internals as an Interactive City](#item-3) ⭐️ 8.0/10
4. [MonkeyOCRv2: 0.7B Model Tops Open-Source Document Parsing](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LLMs + Theorem Provers: The Future of Code Verification](https://www.imperialviolet.org/2026/07/26/zstd-lean.html) ⭐️ 9.0/10

The article argues that programming languages with built-in theorem provers will enable LLMs to formally verify code against specifications, drastically reducing the need for traditional testing. It highlights Verus for Rust as a step in this direction. This vision could transform software development by shifting the programmer's role from writing tests to writing formal specs, potentially eliminating entire categories of bugs. It also addresses the reliability concerns of LLM-generated code, making AI-assisted programming safer. The author mentions that formal verification is exhaustive, unlike testing which is probabilistic. Community comments note that writing formal specs may be as hard as writing correct code, and that costs (e.g., $150k in API tokens for a Lean 4 formalization of Ethereum's VM) remain a barrier.

hackernews · zdw · Jul 26, 20:53 · [Discussion](https://news.ycombinator.com/item?id=49062291)

**Background**: Theorem provers are tools that automatically prove mathematical theorems, and when embedded in programming languages, they can verify that code meets its formal specification. Formal verification exhaustively checks all possible inputs, unlike testing which only covers a subset. LLMs (Large Language Models) like GPT-4 can generate code, but often produce bugs; combining them with theorem provers could ensure correctness.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the vision, with gz09 calling it the future and noting Verus as a good start. Jhsto highlights cost concerns, citing a $150k API token estimate for a Lean 4 formalization. davemp cautions that writing correct specs may be as hard as writing correct code, referencing the Curry-Howard isomorphism.

**Tags**: `#theorem proving`, `#formal verification`, `#LLM`, `#programming languages`, `#Rust`

---

<a id="item-2"></a>
## [vLLM v0.26.0: Inkling support, DeepSeek-V4 optimizations, flexible attention](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 introduces full support for the Inkling model family, including base modeling, CUDA graphs, Hopper FA4 relative attention, speculative decoding, LoRA, and NVFP4 quantization. It also delivers significant performance optimizations for DeepSeek-V4, such as a specialized routing kernel (2.94% E2E TPOT improvement) and fused_topk_bias (1.5-2x kernel speedup). This release strengthens vLLM as a leading open-source LLM inference engine by supporting cutting-edge models like Inkling and DeepSeek-V4, which are critical for production AI deployments. The flexible attention backends and KV offloading improvements enable more efficient inference for hybrid and large-scale models, benefiting the entire AI/ML community. The release includes 411 commits from 212 contributors, with new features like fp32 lm_head via head_dtype, per-KV-cache-group attention backend selection, and matured KV offloading with tiered secondary storage. The Rust frontend now supports multimodal video and audio, and Transformers 5.13.0 migration is underway for models like Olmo and MistralLarge3.

github · khluu · Jul 27, 01:06

**Background**: vLLM is a high-performance inference engine for large language models (LLMs), widely used for serving models in production. The Inkling model family is a general-purpose multimodal model supporting text, image, and audio inputs. DeepSeek-V4 is a large MoE model that benefits from specialized kernel optimizations. NVFP4 is a 4-bit floating-point quantization format from NVIDIA, optimized for Blackwell hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2603.05451v1">FlashAttention-4: Algorithm and Kernel Pipelining Co-Design ... - arXiv</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#CUDA`, `#AI/ML`

---

<a id="item-3"></a>
## [PGSimCity Visualizes PostgreSQL Internals as an Interactive City](https://nikolays.github.io/PGSimCity/) ⭐️ 8.0/10

PGSimCity is an open-source interactive 3D visualization that simulates PostgreSQL's internal processes, such as backend processes, shared buffers, and WAL, as a city metaphor. It was released on GitHub and has gained high engagement on Hacker News. This tool makes complex database internals accessible and engaging, lowering the barrier for developers to understand PostgreSQL's scheduling and architecture. It could inspire similar visualizations for other systems like Kubernetes or cloud computing. The visualization uses a 3D city layout where buildings represent different components like backend towers and shared buffers plaza. It includes an auto-guided tour, but community feedback suggests making it more interactive and less noisy.

hackernews · jonbaer · Jul 27, 00:19 · [Discussion](https://news.ycombinator.com/item?id=49063754)

**Background**: PostgreSQL uses a multi-process architecture where the postmaster forks a backend process for each client connection. Background processes like checkpointer and WAL writer manage shared memory and data durability. Understanding these internals traditionally requires reading architecture diagrams or documentation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NikolayS/pgsimcity">GitHub - NikolayS/ PGSimCity : An explorable 3D city that shows how...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49063754">PGSimCity - How PostgreSQL Works | Hacker News</a></li>
<li><a href="https://blog.algomaster.io/p/postgresql-internal-architecture">How PostgreSQL Works: Internal Architecture Explained</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive, praising the innovative approach and visual appeal. However, users suggest improvements: reducing visual noise in the tour, adding interactivity (e.g., entering a query to trace its flow), and renaming the project to avoid trademark issues with SimCity.

**Tags**: `#PostgreSQL`, `#visualization`, `#database internals`, `#open source`, `#simulation`

---

<a id="item-4"></a>
## [MonkeyOCRv2: 0.7B Model Tops Open-Source Document Parsing](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247907283&idx=2&sn=5df8a52712c79f67232ca9672d4cc34e) ⭐️ 8.0/10

MonkeyOCRv2 achieves state-of-the-art open-source document parsing performance across 17 languages with only 0.7 billion parameters, using a novel parameter specialization technique. The model and data are fully open-sourced. This challenges the prevailing trend of scaling up model sizes, demonstrating that efficient parameter specialization can achieve superior results with a fraction of the parameters. It makes high-quality multilingual document parsing more accessible for deployment on resource-constrained devices. MonkeyOCRv2 achieves 83.3% on a benchmark, outperforming the previous best open-source model dots.mocr which uses a much larger vision encoder. The model is built on a visual-text pretrained foundation and replaces original encoders to consistently improve performance across five document AI tasks.

rss · 量子位 · Jul 26, 04:30

**Background**: Document parsing involves extracting structured information (like text, tables, and layouts) from documents such as PDFs and scanned images. Traditional OCR systems often require separate pipelines for detection and recognition, while recent vision-language models combine these steps but tend to be large (e.g., 7B+ parameters). Parameter specialization is a technique where different parts of a model are trained to handle specific subtasks, improving efficiency without increasing total parameter count.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Yuliang-Liu/MonkeyOCRv2">GitHub - Yuliang-Liu/ MonkeyOCRv 2 : MonkeyOCRv 2 Vision Encoder...</a></li>
<li><a href="https://arxiv.org/html/2607.11562">MonkeyOCRv 2 : A Visual-Text Foundation Model for Document AI</a></li>
<li><a href="https://huggingface.co/papers/2607.11562">Paper page - MonkeyOCRv 2 : A Visual-Text Foundation Model for...</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#document parsing`, `#multilingual`, `#efficient AI`, `#open-source`

---