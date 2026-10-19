---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 25 条内容中筛选出 2 条重要资讯。

---

1. [vLLM v0.32.0 发布：新增通用 HF 解析器与低精度 KV 缓存支持](#item-1) ⭐️ 8.0/10
2. [RepRapMicron：开源微米级 3D 打印机项目](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.32.0 发布：新增通用 HF 解析器与低精度 KV 缓存支持](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 8.0/10

vLLM v0.32.0 是一个重大版本，包含来自 363 位贡献者的 814 次提交，引入了通用的 Hugging Face 工具/推理解析器（读取检查点的 response_template），并在 SM8x、SM90、SM100、SM12x 和 ROCm 平台上扩展了低精度 KV 缓存支持（NVFP4、FP8）。此外还带来了 Model Runner V2 改进、通过预编译 FlashInfer 内核加快启动、新模型支持（EmbeddingGemma 2、MiniCPM-V 4.7、Nemotron 3.5 ASR）以及多项安全修复。 此版本通过消除对模型特定解析器的需求，显著降低了部署具有工具调用和推理能力的模型的门槛，而广泛的低精度 KV 缓存支持则减少了内存占用并提升了跨硬件的吞吐量。这些变化直接惠及运行大规模 LLM 推理的 AI/ML 基础设施团队，尤其是在长上下文和高并发工作负载中。 值得注意的具体细节包括：GLM-5.x 在 SM100 上默认使用 FP8 KV 缓存（每个 rank 的 KV 内存减半，吞吐量提升 2.3-5.5%，但 TTFT 增加 7-11%）；SM90 上的 `fp8_ds_mla` 为 GLM-5.3-Flash 带来高达 31% 的输出吞吐量提升；ROCm 获得了 4 位 `ultraquant_4bit` KV 缓存，密度约为 FP8 的 2 倍。破坏性变更包括放弃 Python 3.10、限制默认 CORS 来源、要求 `transformers>=5.16.1,<5.20.0`，以及移除级联注意力和 `mamba_cache_mode="all"`。

github · khluu · 10月18日 06:50

**背景**: vLLM 是一个高吞吐量的 LLM 推理和服务引擎，使用 PagedAttention 管理 KV 缓存，即在生成过程中存储注意力键值张量的内存。将 KV 缓存量化为较低精度（如 FP8 或 NVFP4）可减少其内存占用，从而在内存中容纳更多 token，支持更长的上下文或更高的并发。Hugging Face 检查点可以在 `tokenizer_config.json` 中定义 `response_template`，描述其推理、内容和工具调用的线格式，新的 `hf` 解析器读取该元数据，从而避免编写模型特定的解析代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/tool_calling/">Tool Calling - vLLM</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的社区讨论表明，vLLM 的 NVFP4 KV 缓存精度与 FP8 大致相当，用户指出 vLLM 在量化实验方面比 llama.cpp 有显著提升。部分用户对 KV 缓存量化仍持怀疑态度，但共识倾向于认为 FP8 是长上下文部署的实用默认选择。

**标签**: `#vllm`, `#llm-inference`, `#kv-cache`, `#quantization`, `#release`

---

<a id="item-2"></a>
## [RepRapMicron：开源微米级 3D 打印机项目](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 8.0/10

RepRapMicron 项目（μRepRap）是一个开源计划，旨在开发能够进行微米级分辨率制造的 3D 打印机，将 RepRap 理念扩展到微尺度制造。该项目最近在 GitHub 和 Hacker News 上引起关注，讨论聚焦于其普及微芯片制造的潜力。 如果成功，该项目可以使爱好者和小型实验室能够制造微结构甚至简单的集成电路，大幅降低微纳制造的门槛。这与开源硬件的广泛趋势一致，并可能激发微流控、传感器和电子等领域的创新。 该项目旨在实现微米级分辨率，最近的原型机打印出了 0.650 毫米的 3DBenchy 模型，证明了可行性，但距离亚微米能力仍有差距。挑战包括进一步提高分辨率、提高打印速度以及开发能证明其精度价值的实际应用。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**背景**: RepRap 是一个历史悠久的开源项目，旨在创建可自我复制的 3D 打印机，使增材制造对个人用户变得可及。微米级 3D 打印通常需要昂贵的专用设备，如双光子聚合系统，这些设备对爱好者来说难以获得。RepRapMicron 旨在通过开源硬件设计将这种精度带到桌面级机器上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://makeprintable.com/reprap-micron-achieves-0-650mm-3dbenchy-print/">RepRap Micron Achieves 0.650mm 3DBenchy Print - makeprintable</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与 18 世纪 90 年代精密工程的突破相提并论，如拉姆斯登的分度机和莫兹利的车床，认为这可能是一次类似的范式转变。一些人对 DIY 芯片制造表示兴奋，而另一些人则质疑在这种尺度下自我复制的可行性。

**标签**: `#3D printing`, `#microfabrication`, `#open hardware`, `#RepRap`, `#precision engineering`

---