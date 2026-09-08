---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 21 条内容中筛选出 4 条重要资讯。

---

1. [研究人员用现代 GPU 破解了 90 年代 CA 的 RSA 密钥](#item-1) ⭐️ 8.0/10
2. [TPU 推理外部化加速推进，InferenceX 登场](#item-2) ⭐️ 8.0/10
3. [LLM 引导的程序进化打破 10 项圆填充纪录](#item-3) ⭐️ 8.0/10
4. [Yandex 研究人员提出将 KV 缓存用作代理运行时](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [研究人员用现代 GPU 破解了 90 年代 CA 的 RSA 密钥](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

一名安全研究人员使用现代消费级 GPU 成功分解了 1990 年代一家证书颁发机构的 RSA 密钥，破解一个 512 位证书大约耗时两天。这项工作证明了破解曾被认为安全的旧式加密在实际中是可行的。 这凸显了历史加密标准的脆弱性，并引发了对已记录流量进行追溯性解密的担忧。它强调了前向保密的重要性以及淘汰弱密钥长度的必要性，因为政府或对手可能会存档加密数据以备将来解密。 研究人员针对的是 512 位 RSA 密钥，这远短于现代建议的长度（如 2048 位或更高）。破解是在消费级 GPU 上完成的，研究人员指出，那个时代的许多流量并未使用临时密钥，因此容易受到追溯性解密的影响。

hackernews · ahlCVA · 9月8日 01:16 · [社区讨论](https://news.ycombinator.com/item?id=49604637)

**背景**: RSA 加密依赖于将两个大素数的乘积进行因式分解的难度；密钥越长，因式分解在计算上就越不可行。证书颁发机构（CA）是受信任的实体，负责签发数字证书，这些证书用于保护 HTTPS 等通信。在 1990 年代，512 位等较短的密钥长度很常见，但硬件和算法的进步使它们容易受到暴力破解或因式分解攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.encryptionconsulting.com/education-center/what-is-rsa/">What is RSA ? How does an RSA work? | Encryption Consulting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_authority">Certificate authority</a></li>
<li><a href="https://ieeexplore.ieee.org/document/7284337/">Bulk GCD Computation Using a GPU to Break Weak RSA Keys | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**社区讨论**: 评论者对破解旧系统的“逆向考古”方面表示着迷，而其他人则对其对隐私的影响以及政府解密存档匿名通信的可能性表示担忧。一些人还指出 SSL 报告自动获得“F”评级的讽刺意味，一位评论者强调需要验证 LLM 生成的解释，因为它们可能看似合理但实际错误。

**标签**: `#RSA`, `#cryptography`, `#security`, `#historical`, `#GPU cracking`

---

<a id="item-2"></a>
## [TPU 推理外部化加速推进，InferenceX 登场](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

谷歌的 TPU 外部化进程正通过 InferenceX 计划快速推进，声称推理工作负载每美元性能提升高达 50%。这标志着谷歌大力推动 TPU 对外商业化，挑战 NVIDIA 的 CUDA 主导地位。 这一进展可能重塑 AI 硬件格局，为 NVIDIA GPU 提供可行的替代方案，可能削弱 CUDA 的护城河。云服务商和 AI 公司或将获得更多选择和成本节约，加剧 AI 加速器市场的竞争。 文章强调 Ironwood（TPUv7）是谷歌首代面向外部推理工作负载竞争的芯片，可直接购买或通过云租赁。未来的软件外部化工作包括优化投机解码、分离式预填充和 KV 缓存卸载等。

rss · Semianalysis · 9月7日 20:00

**背景**: TPU（张量处理单元）是谷歌自研的 AI 加速器，传统上仅用于内部服务。外部化是指将 TPU 提供给外部客户，无论是硬件还是云服务。NVIDIA 的 CUDA 软件生态系统一直是其关键优势，将开发者锁定在其硬件上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://howaiworks.ai/blog/google-tpuv7-ironwood-announcement-2025">Google TPUv7 Ironwood : Challenging Nvidia</a></li>
<li><a href="https://fourweekmba.com/ai-google-tpu-selling-renting-compute-alphabet-q2-2026/">Google Is Selling TPUs and Renting Outside... - FourWeekMBA</a></li>

</ul>
</details>

**标签**: `#TPU`, `#AI hardware`, `#Inference`, `#CUDA`, `#Cloud computing`

---

<a id="item-3"></a>
## [LLM 引导的程序进化打破 10 项圆填充纪录](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

一种 LLM 引导的程序进化方法在 Packomania csqv 基准上改进了 N=101-114 的 10 个最佳已知半径和解决方案，在 15 次迭代中实现了 2.4%至 5.4%的改进，总 LLM 成本为 27.72 美元。结果已被 Packomania 独立接受。 这展示了 LLM 在程序进化中的新颖且成本效益高的应用，在长期存在的优化基准上取得了具体改进。这表明 LLM 引导的搜索可以发现人类专家遗漏的算法改进，可能影响优化和自动算法设计等领域。 该方法从简单的种子求解器开始，通过 LLM 提出的更改迭代进化，由记分板和历史记录引导，并由独立验证器接受或拒绝每个候选。论文可在 arXiv（2609.05093）上获取，代码和解决方案在 GitHub 上，基准托管在 packomania.com/csqv/csqv.html。

reddit · r/MachineLearning · /u/SIGH_I_CALL · 9月7日 16:54

**背景**: 圆填充是一个经典的优化问题，目标是在容器内排列圆以最大化或最小化某个度量，例如半径和。Packomania 是自 1998 年以来由 Eckard Specht 维护的长期最佳已知填充的存储库。LLM 引导的程序进化是一种技术，其中大型语言模型提出代码修改，基于评估反馈迭代改进算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM-Guided Program Evolution for Circle Packing :Breaking 10...</a></li>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>

</ul>
</details>

**标签**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#AI research`

---

<a id="item-4"></a>
## [Yandex 研究人员提出将 KV 缓存用作代理运行时](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

Yandex 研究人员发表了一篇博客文章，提出将 KV 缓存用作代理运行时，以增强 LLM 的交互性，该工作基于他们之前的研究 Hogwild! Inference 和 AsyncReasoning。文章中预览了一个使用这些技术交互式玩 DOOM 的 Qwen3.8-27B 代理。 这一研究方向表明，修改推理状态（KV 缓存）可能成为提升代理能力的新维度，有望在不重新训练的情况下实现更灵敏、更交互的 LLM 系统。它强调了模型与外部框架之间一个未被充分探索的领域，可能影响未来 LLM 代理的设计。 KV 缓存存储推理过程中的中间注意力结果，修改它可以实现并发或异步推理。该博客文章引用了 Hogwild! Inference（并行运行多个 LLM 实例并共享同一注意力缓存）和 AsyncReasoning（一种无需训练的异步推理方法）。

reddit · r/MachineLearning · /u/_puhsu · 9月7日 09:03

**背景**: 在 LLM 推理中，KV 缓存存储先前 token 的键值对以避免重复计算，但通常被视为静态内存。传统的代理设计将模型与外部框架（外部逻辑）分离，而修改模型成本高昂。该提议将 KV 缓存视为可操作的动态运行时环境，以实现交互性，提供了修改模型与修改外部框架之间的中间方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.06261">[2504.06261] Hogwild! Inference: Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/abs/2512.10931">[2512.10931] Asynchronous Reasoning: Training-Free Interactive Thinking LLMs</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**标签**: `#KV cache`, `#LLM agents`, `#inference`, `#interactivity`, `#research`

---