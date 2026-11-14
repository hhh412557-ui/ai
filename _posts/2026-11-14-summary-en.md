---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 30 items, 3 important content pieces were selected

---

1. [GGML, the tensor library behind llama.cpp, hits v1.0.0](#item-1) ⭐️ 8.0/10
2. [FAA issues nationwide ground stop after telecom outage, lifted 4.5 hours later](#item-2) ⭐️ 8.0/10
3. [Scaling a 1T-Parameter MoE to 1,300 Tokens/s per GPU on 384 GH200s with TorchTitan](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GGML, the tensor library behind llama.cpp, hits v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) ⭐️ 8.0/10

GGML, the foundational tensor library that powers llama.cpp, has officially released version 1.0.0. This marks the first major version milestone for the project, signaling its maturity after years of active development. GGML is the computational engine behind llama.cpp, which has become the de facto standard for local LLM inference and underpins tools like Ollama and LM Studio. A v1.0.0 release signals stability and maturity for the entire local AI ecosystem, affecting developers and users who run models on consumer hardware. The release is hosted on the ggml-org GitHub repository, and community members note that regular updates often bring 5–10% performance improvements on the same hardware. One user reported a benchmark improvement from 4:22 to 3:59 on a 50K-token prompt after upgrading.

hackernews · cobychapple · Nov 14, 02:28 · [Discussion](https://news.ycombinator.com/item?id=50493062)

**Background**: GGML is a general-purpose tensor library written in C/C++ that provides the low-level computation needed for running machine learning models. It was created by Georgi Gerganov and is co-developed alongside llama.cpp, an open-source library for running large language models locally. llama.cpp has become the core of almost all local inference tools, including Ollama and LM Studio, enabling AI on consumer hardware without cloud services.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml-org/ggml: Tensor library for machine learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project for continuously finding new ways to speed up code on the same hardware, with one noting a 5–10% speed boost per monthly upgrade. Others described ggml and llama.cpp as "the Linux of the AI world" and highlighted their usability on older or less powerful hardware like AMD cards with Vulkan support.

**Tags**: `#ggml`, `#llama.cpp`, `#local-ai`, `#machine-learning`, `#open-source`

---

<a id="item-2"></a>
## [FAA issues nationwide ground stop after telecom outage, lifted 4.5 hours later](https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247) ⭐️ 8.0/10

On November 13, 2026, the FAA ordered a nationwide ground stop shortly before 4 p.m. Eastern time after a telecommunications outage affected every U.S. Air Route Traffic Control Center, disrupting radio frequencies and radar feeds used by controllers; the stop was lifted about 4.5 hours later. This is the first nationwide ground stop since January 2023 and highlights the fragility of critical infrastructure that depends on private telecommunications networks, affecting thousands of flights and passengers across the U.S. The outage appears to be linked to a telecommunications network overseen by L3Harris Technologies that handles crucial radio frequencies for air-traffic controllers, and officials noted that new equipment and technology being patched into the system was overwhelming the older system.

hackernews · zulln · Nov 13, 21:05 · [Discussion](https://news.ycombinator.com/item?id=50489641)

**Background**: The FAA's air traffic control system relies on a private telecommunications network to transmit radio communications and radar data between controllers and pilots. A ground stop is a directive that halts all departures at affected airports or across the system when capacity or safety is compromised. In 2009, a similar outage of the FAA Telecommunications Infrastructure caused significant disruptions, and the recent event has drawn comparisons to that failure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_FAA_communication_outage">2026 FAA communication outage - Wikipedia</a></li>
<li><a href="https://www.aerotime.aero/articles/faa-nationwide-ground-stop-atc-communications-november-2026">ATC communications outage impacting flights across US - AeroTime</a></li>
<li><a href="https://www.ainonline.com/aviation-news/air-transport/2026-11-13/citing-communication-fault-faa-issues-us-ground-stop">Citing Telecommunications Outage, FAA Issues Nationwide ...</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News discussed the 2009 FAA telecom outage as a similar failure mode and shared emerging explanations, including a report that the outage affected an L3Harris network handling radio frequencies. Some criticized the sparse official information, while others highlighted a White House briefing stating that new equipment was overwhelming the older system, underscoring the need for a complete system overhaul.

**Tags**: `#FAA`, `#critical-infrastructure`, `#outage`, `#aviation`, `#systems-reliability`

---

<a id="item-3"></a>
## [Scaling a 1T-Parameter MoE to 1,300 Tokens/s per GPU on 384 GH200s with TorchTitan](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

A team working with TorchTitan and PyTorch maintainers scaled a ~1T-parameter Mixture-of-Experts model to ~1,300 tokens/s per GPU on 384 GH200 GPUs, achieving a 14X throughput improvement over their starting point. They shared practical lessons on using FSDP plus Expert Parallelism instead of Pipeline Parallelism, and on optimizations like full activation checkpointing, offloading to Grace CPUs, and the Muon optimizer. This work demonstrates that PyTorch-native tooling like TorchTitan can handle trillion-parameter MoE training at scale on modern hardware, providing a viable open-source alternative to proprietary frameworks. The detailed lessons on sharding strategies and communication hiding are highly valuable for practitioners training large models on GPU clusters with slower interconnects. The team used 384-way FSDP with 4-way Expert Parallelism kept strictly within a node, avoiding Pipeline Parallelism to reduce iteration time. Key optimizations included full activation checkpointing (4X speedup), offloading checkpoint activations to Grace CPUs over the 900 GB/s C2C link, and using Muon instead of Adam to fit 64k-token sequences; FlexShard enabled sharding experts by whole expert to avoid communication during Newton-Schulz iterations.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**Background**: Mixture-of-Experts (MoE) is a technique where multiple expert sub-networks specialize in different parts of the input space, allowing models to scale to trillions of parameters with less compute per token. TorchTitan is a PyTorch-native platform for large-scale training, and GH200 is a GPU from NVIDIA that combines a Grace CPU and Hopper GPU with a high-speed link, used in the JUPITER supercomputer. FSDP (Fully Sharded Data Parallel) shards model weights across GPUs, while Expert Parallelism distributes experts across devices, and Pipeline Parallelism splits layers into stages.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch / torchtitan : A PyTorch native platform for training...</a></li>
<li><a href="https://arxiv.org/abs/2410.06511">[2410.06511] TorchTitan : One-stop PyTorch native solution for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#large-scale-training`, `#mixture-of-experts`, `#PyTorch`, `#distributed-training`, `#GPU-optimization`

---