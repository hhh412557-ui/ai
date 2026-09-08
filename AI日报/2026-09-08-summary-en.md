---
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 21 items, 4 important content pieces were selected

---

1. [Researcher Factors 1990s CA's RSA Keys Using Modern GPU](#item-1) ⭐️ 8.0/10
2. [TPU Inference Externalization Accelerates with InferenceX](#item-2) ⭐️ 8.0/10
3. [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records](#item-3) ⭐️ 8.0/10
4. [Yandex Researchers Propose KV Cache as Agent Runtime](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Researcher Factors 1990s CA's RSA Keys Using Modern GPU](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

A security researcher successfully factored the RSA keys of a 1990s Certificate Authority using a modern consumer GPU, taking about two days to crack a 512-bit certificate. The work demonstrates the practical feasibility of breaking legacy encryption that was once considered secure. This highlights the fragility of historical encryption standards and raises concerns about retroactive decryption of recorded traffic. It underscores the importance of forward secrecy and the need to phase out weak key lengths, as governments or adversaries may archive encrypted data for future decryption. The researcher targeted a 512-bit RSA key, which is far shorter than modern recommendations (e.g., 2048-bit or higher). The cracking was performed on a consumer GPU, and the researcher noted that much of the traffic from that era did not use ephemeral keys, making it vulnerable to retroactive decryption.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA encryption relies on the difficulty of factoring the product of two large prime numbers; a longer key makes factoring computationally infeasible. Certificate Authorities (CAs) are trusted entities that issue digital certificates, which are used to secure communications such as HTTPS. In the 1990s, shorter key lengths like 512-bit were common, but advances in hardware and algorithms have made them vulnerable to brute-force or factorization attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.encryptionconsulting.com/education-center/what-is-rsa/">What is RSA ? How does an RSA work? | Encryption Consulting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_authority">Certificate authority</a></li>
<li><a href="https://ieeexplore.ieee.org/document/7284337/">Bulk GCD Computation Using a GPU to Break Weak RSA Keys | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**Discussion**: Commenters expressed fascination with the 'reverse archaeology' aspect of breaking legacy systems, while others raised concerns about the implications for privacy and the potential for governments to decrypt archived anonymous communications. Some also noted the irony of the SSL report receiving automatic 'F' grades, and one commenter emphasized the need to verify LLM-generated explanations, as they can be plausible but incorrect.

**Tags**: `#RSA`, `#cryptography`, `#security`, `#historical`, `#GPU cracking`

---

<a id="item-2"></a>
## [TPU Inference Externalization Accelerates with InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

Google's TPU externalization is advancing rapidly with the InferenceX initiative, claiming up to 50% better performance per dollar for inference workloads. This marks a significant push to commercialize TPUs externally, challenging NVIDIA's CUDA dominance. This development could reshape the AI hardware landscape by offering a viable alternative to NVIDIA's GPUs, potentially eroding the CUDA moat. Cloud providers and AI companies may gain more choices and cost savings, intensifying competition in the AI accelerator market. The article highlights Ironwood (TPUv7) as the first generation where Google competes for external inference workloads, with chips available for direct purchase or cloud rental. Future software externalization efforts include optimizing speculative decoding, disaggregated prefill, and KV-cache offloading.

rss · Semianalysis · Sep 7, 20:00

**Background**: TPU (Tensor Processing Unit) is Google's custom AI accelerator, traditionally used internally for its own services. Externalization refers to making TPUs available to external customers, either as hardware or cloud services. NVIDIA's CUDA software ecosystem has long been a key advantage, locking developers into its hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://howaiworks.ai/blog/google-tpuv7-ironwood-announcement-2025">Google TPUv7 Ironwood : Challenging Nvidia</a></li>
<li><a href="https://fourweekmba.com/ai-google-tpu-selling-renting-compute-alphabet-q2-2026/">Google Is Selling TPUs and Renting Outside... - FourWeekMBA</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#AI hardware`, `#Inference`, `#CUDA`, `#Cloud computing`

---

<a id="item-3"></a>
## [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An LLM-guided program evolution approach improved 10 best-known sum-of-radii solutions on the Packomania csqv benchmark for N=101-114, achieving gains of 2.4% to 5.4% in 15 iterations at a total LLM cost of $27.72. The results were independently accepted by Packomania. This demonstrates a novel, cost-effective application of LLMs to program evolution, achieving concrete improvements on a long-standing optimization benchmark. It suggests that LLM-guided search can discover algorithmic improvements that human experts have missed, potentially impacting fields like optimization and automated algorithm design. The approach starts from a simple seed solver and iteratively evolves it via LLM-proposed changes, guided by a scoreboard and history, with an independent verifier accepting or rejecting each candidate. The paper is available on arXiv (2609.05093), with code and solutions on GitHub, and the benchmark is hosted at packomania.com/csqv/csqv.html.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic optimization problem where the goal is to arrange circles within a container to maximize or minimize a certain metric, such as the sum of radii. Packomania is a long-standing repository of best-known packings maintained by Eckard Specht since 1998. LLM-guided program evolution is a technique where large language models propose modifications to code, iteratively improving algorithms based on feedback from evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM-Guided Program Evolution for Circle Packing :Breaking 10...</a></li>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#AI research`

---

<a id="item-4"></a>
## [Yandex Researchers Propose KV Cache as Agent Runtime](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

Yandex researchers published a blog post proposing the use of the KV cache as an agent runtime to enhance LLM interactivity, building on their prior work Hogwild! Inference and AsyncReasoning. The post includes a preview of a Qwen3.8-27B agent playing DOOM interactively using these techniques. This research direction suggests that modifying the inference state (KV cache) could be a new axis for improving agent capabilities, potentially enabling more responsive and interactive LLM systems without retraining. It highlights an under-explored area between the model and the harness, which could influence future LLM agent design. The KV cache stores intermediate attention results during inference, and modifying it can allow concurrent or asynchronous reasoning. The blog post references Hogwild! Inference, which runs multiple LLM instances in parallel sharing the same attention cache, and AsyncReasoning, a training-free method for asynchronous reasoning.

reddit · r/MachineLearning · /u/_puhsu · Sep 7, 09:03

**Background**: In LLM inference, the KV cache stores key-value pairs from previous tokens to avoid recomputation, but it is typically treated as a static memory. Traditional agent designs separate the model from the harness (external logic), and changing the model is costly. This proposal treats the KV cache as a dynamic runtime environment that can be manipulated to achieve interactivity, offering a middle ground between modifying the model and the harness.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.06261">[2504.06261] Hogwild! Inference: Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/abs/2512.10931">[2512.10931] Asynchronous Reasoning: Training-Free Interactive Thinking LLMs</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#LLM agents`, `#inference`, `#interactivity`, `#research`

---