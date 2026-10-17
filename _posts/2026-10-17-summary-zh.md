---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 20 条内容中筛选出 3 条重要资讯。

---

1. [Llama.cpp 在越狱 PS5 上原生运行，支持 GGUF 模型推理](#item-1) ⭐️ 8.0/10
2. [Claude 揭示 ECDSA 曲线种子源自 lrand48 随机数生成器](#item-2) ⭐️ 8.0/10
3. [Apple MLX 在 Mac Studio 集群上运行近万亿参数 Muse Spark Open 模型](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Llama.cpp 在越狱 PS5 上原生运行，支持 GGUF 模型推理](https://github.com/cobanov/PS5LM) ⭐️ 8.0/10

一个名为 PS5LM 的新项目（由 cobanov 托管在 GitHub 上）通过 llama.cpp 在越狱的 PlayStation 5 上原生运行 GGUF 格式的大语言模型，将游戏机转变为通用 AI 推理机。 这表明越狱可以将锁定的消费级硬件重新利用为通用计算机，可能为运行本地 AI 模型提供低成本替代方案，并激发对其他游戏机或嵌入式设备的类似尝试。 该项目能以 2 位量化运行类似 Qwen 3.8B 的模型，适用于需要持续 token 流的长期任务，且类似硬件如 BC250（PS5 APU 的缩减版）也可能适用。

hackernews · Anon84 · 10月16日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50122431)

**背景**: llama.cpp 是一个开源 C/C++ 库，用于高效推理大语言模型，通常与 GGUF 文件格式的量化模型一起使用。越狱 PlayStation 5 涉及利用软件或硬件漏洞绕过索尼的限制，允许执行未签名的代码。该项目结合这些概念，在游戏机上原生运行 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://grokipedia.com/page/PlayStation_5_jailbreak">PlayStation 5 jailbreak</a></li>
<li><a href="https://huggingface.co/TheBloke/CodeLlama-13B-GGUF">TheBloke/CodeLlama-13B- GGUF · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者对于将 PS5 重新利用为通用计算机表示兴奋，一些人指出了服务器监控和安全录像分析等实际应用。其他人则担心在 GitHub 上托管此类项目可能引发索尼的法律行动，并建议使用替代托管平台。还有人提到在 BC250 卡上运行该项目的可能性。

**标签**: `#llama.cpp`, `#PS5`, `#jailbreak`, `#GGUF`, `#AI inference`

---

<a id="item-2"></a>
## [Claude 揭示 ECDSA 曲线种子源自 lrand48 随机数生成器](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic 的研究显示，其 AI 模型 Claude 发现了 NIST ECDSA 曲线种子（P-192、P-224、P-256、P-384、P-521）的起源，确定它们是使用 C 库的 lrand48 随机数生成器并以 Unix 时间戳为种子生成的，解决了一个长达数十年的密码学谜团。 这一发现解决了关于 NIST 椭圆曲线参数如何生成的长期谜团，驳斥了它们被故意弱化的阴谋论，并展示了 AI 解决复杂密码学难题的潜力。 种子是在数月内生成的，第五个二进制种子（B-163）仍无法解释，可能是由于公布值中的笔误；该方法不能排除通过搜索时间戳来选择具有特定属性的曲线的可能性。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: ECDSA（椭圆曲线数字签名算法）是最广泛使用的椭圆曲线密码学标准，由 NIST 于 2000 年作为 FIPS 186-2 的一部分采纳。标准曲线（P-192、P-224、P-256、P-384、P-521）由包括种子值在内的参数定义，种子值旨在允许验证曲线是随机生成的。然而，确切的生成过程从未被完全解释，导致了对潜在后门的猜测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>
<li><a href="https://saweis.net/posts/nist-curve-seed-origins.html">How were the NIST ECDSA curve parameters generated?</a></li>
<li><a href="https://www.ibm.com/docs/en/zos/3.1.0?topic=functions-lrand48-pseudo-random-number-generator">lrand 48 () — Pseudo- random number generator</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一发现表示惊讶和幽默，一些人指出它驳斥了多年的阴谋论。其他人指出，生成方法并不能证明曲线没有被选择用于特定属性，还有人提出无法解释的 B-163 种子可能是由于笔误。

**标签**: `#cryptography`, `#ECDSA`, `#NIST`, `#AI research`, `#random number generation`

---

<a id="item-3"></a>
## [Apple MLX 在 Mac Studio 集群上运行近万亿参数 Muse Spark Open 模型](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

Apple ML Research 演示了使用新发布的 MLX 分布式推理，在四台 Mac Studio 组成的集群上运行 Meta 的近万亿参数 Muse Spark Open 模型，生成速度超过每秒 36 个 token。该版本使得在 Apple 芯片上本地推理前沿级模型成为可能，可从单台配备最高 512GB 统一内存的 Mac Studio 扩展到多台机器。 这标志着本地和端侧推理的一个重要里程碑，表明消费级 Mac 集群能够处理以前需要昂贵云基础设施或专用 GPU 服务器的模型。它可能使前沿 AI 对注重隐私和数据控制的研究人员和开发者更加普及。 演示中对 Meta 模型使用了 4 位量化，而与 Qwen 的对比则使用原生 BF16，这引发了关于基准公平性的质疑。报告的每秒 36 个 token 是在 8,192 token 上下文长度下测得的，一些人认为这对于现代用例来说不够。

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**背景**: MLX 是 Apple 专为 Apple 芯片上的机器学习设计的开源数组框架，利用统一内存架构在本地运行模型。分布式推理允许多台 Mac 协同工作，汇集内存和计算资源来处理单机无法容纳的大型模型。Muse Spark Open 是 Meta 最近发布的开放权重模型，针对编码和代理工作流优化，拥有近万亿参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/mlx-distributed-inference">Local and Distributed Large LLM Inference with MLX and RDMA ...</a></li>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>
<li><a href="https://contracollective.com/blog/mlx-distributed-inference-multi-mac-cluster-2026">MLX Distributed Inference: Multi-Mac Cluster Setup for Local ...</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了对基准公平性的担忧，指出将 4 位量化的 Meta 模型与 BF16 的 Qwen 模型进行比较具有误导性。一些人分享了实际基准测试，显示单台 M5 Ultra 和 M5 Max 机器可以有效运行 DeepSeek 和 GLM 等其他模型，而另一些人则批评了宣传框架和有限的 8K 上下文长度。

**标签**: `#mlx`, `#apple`, `#local-inference`, `#llm`, `#distributed-computing`

---