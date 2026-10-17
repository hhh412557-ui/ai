---
layout: default
title: "Horizon Summary: 2026-10-17 (EN)"
date: 2026-10-17
lang: en
---

> From 20 items, 3 important content pieces were selected

---

1. [Llama.cpp runs natively on jailbroken PS5, enabling GGUF model inference](#item-1) ⭐️ 8.0/10
2. [Claude reveals ECDSA curve seeds came from lrand48 RNG](#item-2) ⭐️ 8.0/10
3. [Apple MLX runs near-trillion-parameter Muse Spark Open on Mac Studio cluster](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Llama.cpp runs natively on jailbroken PS5, enabling GGUF model inference](https://github.com/cobanov/PS5LM) ⭐️ 8.0/10

A new project called PS5LM (hosted on GitHub by cobanov) enables native execution of GGUF-format large language models via llama.cpp on a jailbroken PlayStation 5, turning the console into a general-purpose AI inference machine. This demonstrates how jailbreaking can repurpose locked-down consumer hardware into a general-purpose computer, potentially offering a low-cost alternative for running local AI models and inspiring similar efforts on other consoles or embedded devices. The project runs models like Qwen 3.8B at 2-bit quantization, which is viable for long-running tasks that require a constant token stream, and similar hardware such as the BC250 (a cut-down PS5 APU) could also work.

hackernews · Anon84 · Oct 16, 18:32 · [Discussion](https://news.ycombinator.com/item?id=50122431)

**Background**: llama.cpp is an open-source C/C++ library for efficient inference of large language models, often used with the GGUF file format for quantized models. Jailbreaking a PlayStation 5 involves exploiting software or hardware vulnerabilities to bypass Sony's restrictions, allowing unsigned code execution. This project combines these concepts to run AI models natively on the console.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://grokipedia.com/page/PlayStation_5_jailbreak">PlayStation 5 jailbreak</a></li>
<li><a href="https://huggingface.co/TheBloke/CodeLlama-13B-GGUF">TheBloke/CodeLlama-13B- GGUF · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about repurposing the PS5 as a general-purpose computer, with some noting practical applications like server monitoring and security footage analysis. Others raised concerns about hosting such projects on GitHub due to potential legal action from Sony, and suggested alternative hosting. The possibility of running the project on BC250 cards was also mentioned.

**Tags**: `#llama.cpp`, `#PS5`, `#jailbreak`, `#GGUF`, `#AI inference`

---

<a id="item-2"></a>
## [Claude reveals ECDSA curve seeds came from lrand48 RNG](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic research shows that its AI model Claude discovered the origins of the NIST ECDSA curve seeds (P-192, P-224, P-256, P-384, P-521) by determining they were generated using the C library's lrand48 random-number generator seeded with Unix timestamps, solving a decades-old cryptographic mystery. This finding resolves a long-standing mystery about how NIST's elliptic curve parameters were generated, debunking conspiracy theories that they were deliberately weakened, and demonstrates AI's potential to solve complex cryptographic puzzles. The seeds were generated over a period of months, and the fifth binary seed (B-163) remains unexplained, possibly due to a typo in the published value; the method does not rule out the possibility that curves were selected for specific properties by searching over timestamps.

hackernews · ahlCVA · Oct 16, 18:55 · [Discussion](https://news.ycombinator.com/item?id=50122800)

**Background**: ECDSA (Elliptic Curve Digital Signature Algorithm) is the most widely used elliptic curve cryptography standard, adopted by NIST in 2000 as part of FIPS 186-2. The standard curves (P-192, P-224, P-256, P-384, P-521) are defined by parameters including a seed value, which was intended to allow verification that the curve was generated randomly. However, the exact generation process was never fully explained, leading to speculation about potential backdoors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>
<li><a href="https://saweis.net/posts/nist-curve-seed-origins.html">How were the NIST ECDSA curve parameters generated?</a></li>
<li><a href="https://www.ibm.com/docs/en/zos/3.1.0?topic=functions-lrand48-pseudo-random-number-generator">lrand 48 () — Pseudo- random number generator</a></li>

</ul>
</details>

**Discussion**: Commenters expressed amazement and humor at the finding, with some noting that it debunks years of conspiracy theories. Others pointed out that the method of generation doesn't prove the curves weren't selected for specific properties, and one suggested the unexplained B-163 seed might be due to a typo.

**Tags**: `#cryptography`, `#ECDSA`, `#NIST`, `#AI research`, `#random number generation`

---

<a id="item-3"></a>
## [Apple MLX runs near-trillion-parameter Muse Spark Open on Mac Studio cluster](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

Apple ML Research demonstrated running Meta's near-trillion-parameter Muse Spark Open model on a cluster of four Mac Studios using the newly released MLX distributed inference, achieving over 36 tokens per second. The release enables local inference of frontier-class models on Apple silicon, scaling from a single Mac Studio with up to 512GB unified memory to multiple machines. This marks a significant milestone for local and on-device inference, showing that a cluster of consumer Macs can handle models that previously required expensive cloud infrastructure or specialized GPU servers. It could democratize access to frontier AI for researchers and developers who prioritize privacy and control over their data. The demonstration used 4-bit quantization for the Meta model, while comparisons with Qwen used native BF16, raising questions about benchmark fairness. The reported 36 tokens per second was measured at an 8,192-token context length, which some consider insufficient for modern use cases.

hackernews · antipaul · Oct 16, 13:43 · [Discussion](https://news.ycombinator.com/item?id=50118320)

**Background**: MLX is Apple's open-source array framework designed for machine learning on Apple silicon, leveraging the unified memory architecture to run models locally. Distributed inference allows multiple Macs to work together, pooling their memory and compute to handle models too large for a single machine. Muse Spark Open is Meta's recently released open-weight model optimized for coding and agentic workflows, with nearly one trillion parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/mlx-distributed-inference">Local and Distributed Large LLM Inference with MLX and RDMA ...</a></li>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>
<li><a href="https://contracollective.com/blog/mlx-distributed-inference-multi-mac-cluster-2026">MLX Distributed Inference: Multi-Mac Cluster Setup for Local ...</a></li>

</ul>
</details>

**Discussion**: Commenters raised concerns about benchmark fairness, noting that comparing a 4-bit Meta model against a BF16 Qwen model is misleading. Some shared real-world benchmarks showing that single M5 Ultra and M5 Max machines can run other models like DeepSeek and GLM effectively, while others criticized the promotional framing and the limited 8K context length.

**Tags**: `#mlx`, `#apple`, `#local-inference`, `#llm`, `#distributed-computing`

---