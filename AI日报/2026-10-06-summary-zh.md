---
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 28 条内容中筛选出 3 条重要资讯。

---

1. [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 并引入快速重启](#item-1) ⭐️ 8.0/10
2. [Reflection AI 发布 501B 开源权重 MoE 模型 Beam](#item-2) ⭐️ 8.0/10
3. [Opus 5.5 AI 智能体发现两种室温磁性半导体候选材料](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.31.0 发布：优化 DeepSeek-V4.1-Flash 并引入快速重启](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM v0.31.0 正式发布，包含来自 307 位贡献者（其中 96 位新贡献者）的 717 个提交，核心亮点是 DeepSeek-V4.1-Flash 性能优化和新的权重缓存预加载守护进程。该版本将搭载 V4.1 NVFP4 压缩 KV 缓存的 FlashMLA mega attention 设为 SM100 默认实现，并新增 `vllm preload` 命令行工具以实现引擎快速重启。 vLLM 是目前使用最广泛的高吞吐 LLM 推理引擎之一，因此这些优化会直接影响在 NVIDIA 最新硬件上部署 DeepSeek-V4.1-Flash 等大型 MoE 模型的成本和延迟。快速重启功能还能减少频繁重新加载量化权重的生产部署的停机时间。 该版本还加入了 Model Runner V2 投机解码、MoonEP 均衡 EP all2all、`--max-num-active-seqs` 等新调度控制，以及若干破坏性变更，包括移除 `tokenizer_mode="slow"`、将按请求的多模态 kwargs 限制在 `--trust-request-mm-kwargs` 之后。基于 CRIU 的实验性引擎快照（`vllm snapshot create/restore`）目前仅支持已完全初始化的 TP1 引擎。

github · khluu · 10月5日 06:44

**背景**: vLLM 是一个开源的大语言模型推理与服务引擎，以 PagedAttention 和高吞吐批处理著称。DeepSeek-V4.1-Flash 是 DeepSeek 推出的模型，vLLM 通过 FlashMLA 等优化内核提供支持，FlashMLA 是 DeepSeek 的高效多头潜在注意力内核库。NVFP4 是一种 4 位浮点格式，用于压缩 KV 缓存，相比 FP8 可将显存占用减少约一半。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/ DeepSeek - V 4 . 1 - Flash | vLLM Recipes</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>
<li><a href="https://benpouladian.com/turboquant-and-dynamo-why-the-market/">TurboQuant and Dynamo: Why the Market Has the Memory Thesis...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#deepseek`, `#gpu-optimization`, `#release`

---

<a id="item-2"></a>
## [Reflection AI 发布 501B 开源权重 MoE 模型 Beam](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

Reflection AI 发布了 Beam，这是一个稀疏混合专家（MoE）开源权重模型，总参数量 5010 亿、激活参数 230 亿，面向编程、推理和智能体任务。该模型在来自网络和专有授权数据集的 23.8 万亿高质量 token 上预训练，并额外投入了强化学习。 Beam 为日益被 DeepSeek、Moonshot 等中国实验室主导的开源权重领域增添了一个重要的西方模型，让开发者多了一个可下载、可自托管的高能力选择。它的发布可能加剧在效率与开放性上的竞争，对任何基于前沿开源模型进行开发或评测的人都很重要。 Beam 总参数量 5010 亿，预填充和解码阶段均激活 230 亿参数；据社区对比，其训练 token 量为 28 万亿，而 DeepSeek V4.1 Flash 为总参数 5520 亿、激活 80 亿/160 亿、训练 45 万亿 token。在一个近期病毒式传播的网格谜题泛化实验中，Beam 据称达到 95.5% 的覆盖率，介于 Opus 5（92.5%）和另一模型之间。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 稀疏混合专家（MoE）模型包含许多独立的“专家”子网络，但每个 token 只被路由到其中一小部分，因此总参数量可以很大而单 token 计算量保持较低；“激活参数”指某个 token 实际用到的那部分参数。开源权重模型会公开训练好的权重供他人下载运行，但许可证条款各不相同，且与同时公开代码和数据的完全开源 AI 有区别。开源权重领域已带有地缘政治色彩：DeepSeek、阿里巴巴等中国实验室以宽松许可证发布大模型，而许多美国实验室则让前沿模型保持闭源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者欢迎又一个开源权重发布，但对其竞争力持怀疑态度，有人指出 Beam“更大却仍不如现有的更小的免费中国模型”，并警告依赖单一国家模型的风险。其他人则深入对比了它与 DeepSeek V4.1 Flash 在参数、激活参数和预训练 token 上的差异，并强调泛化实验证明了其超越记忆的真实能力。

**标签**: `#open-weight models`, `#mixture-of-experts`, `#large language models`, `#AI research`, `#model release`

---

<a id="item-3"></a>
## [Opus 5.5 AI 智能体发现两种室温磁性半导体候选材料](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors) ⭐️ 8.0/10

一个由 Claude Opus 5.5 AI 智能体组成的团队利用密度泛函理论（DFT）模拟，识别出两种室温反铁磁半导体候选材料——一种是新设计的化合物，另一种是 1999 年首次合成的材料。该团队在 vals.ai 上公开了完整的计算过程、代码以及候选材料清单。 能够在室温下工作的磁性半导体有望推动下一代计算机存储和自旋电子器件的发展，这是材料科学领域长期未解的难题。这一结果也检验了由大语言模型驱动的智能体能否切实加速科学发现，因此引发了研究界的兴奋与质疑。 智能体在两种近似水平上运行了量子力学 DFT 模拟：较快的 PBE+U 和较慢但通常更准确的 HSE06，带隙和自旋窗口数据来自后者。这些候选材料是反铁磁性的，即净磁性为零但仍能按自旋对电子进行分类，且该工作仍属于计算预测，尚未经过实验验证。

hackernews · outlier99 · 10月5日 21:00 · [社区讨论](https://news.ycombinator.com/item?id=49970667)

**背景**: 密度泛函理论（DFT）是材料科学中的标准计算方法，利用量子力学预测晶体性质，无需先合成材料。磁性半导体将磁有序与半导体行为结合在一起，但要在室温或更高温度下实现磁有序并保持栅极可调性一直难以实现。基于大语言模型的 AI 智能体正越来越多地应用于科学工作流程，以比人类更快的速度搜索庞大的参数空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors">Two Room-Temperature Antiferromagnetic Semiconductor ...</a></li>
<li><a href="https://www.nature.com/articles/ncomms13497">A room-temperature magnetic semiconductor from a ...</a></li>
<li><a href="https://www.science.org/doi/10.1126/science.adl0823">Is it possible to create magnetic semiconductors that ... - AAAS</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了明显的怀疑态度，有人将此次公告与 LK-99 复现失败相提并论，并质疑智能体是否只是运行了标准的 DFT 模拟。还有人批评文章对磁性的介绍方式以及强调“室温”可能具有误导性，同时也有观点认为这类 AI 驱动的发现可能会越来越常见。

**标签**: `#AI-for-Science`, `#Materials-Science`, `#Magnetic-Semiconductors`, `#DFT`, `#LLM-Agents`

---