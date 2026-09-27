---
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 16 条内容中筛选出 2 条重要资讯。

---

1. [DeepSeek 的 DSec 在 160 台服务器上运行 38 万个并发沙箱](#item-1) ⭐️ 8.0/10
2. [SemiAnalysis 发布 Intel Panther Lake 与 18A 免费拆解报告](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 的 DSec 在 160 台服务器上运行 38 万个并发沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek 发表论文，介绍了 DeepSeek Elastic Compute（DSec）——一个生产级沙箱平台，通过统一 SDK 对外暴露 FnCall、容器、microVM 和完整虚拟机四种沙箱后端。该系统据称在 160 台基于 Epyc 的服务器节点上支撑了 38 万个并发沙箱，社区直呼这一规模“疯狂”。 大规模沙箱是智能体训练与评测的前提，因为每个智能体都需要一个隔离环境来安全执行代码。如果 DSec 的数据经得起验证，它将降低运行数十万条并行智能体轨迹的基础设施门槛，从而可能加速大模型智能体的强化学习式训练与评测。 DSec 将 FnCall、容器、microVM 和完整虚拟机四种隔离级别统一在同一个 SDK 之下，让工作负载自行权衡启动延迟与隔离强度。38 万并发沙箱这一数字是在 160 台基于 Epyc 的节点上实现的，不过摘要中并未给出具体的单机密度和延迟数据。

hackernews · shenli3514 · 9月26日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**背景**: 沙箱是一种安全机制，用于隔离运行中的程序，防止故障或漏洞扩散到系统其他部分。弹性计算指资源根据实时需求动态分配与释放，而这正是一个承载数十万个短生命周期智能体环境的平台所需要的。DeepSeek 是推出 R1 和 V3 模型的中国 AI 实验室，此次发表该工作，显示其正从模型训练向智能体基础设施扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">[2609.22978] DeepSeek Elastic Compute ( DSec ): A Sandbox...</a></li>
<li><a href="https://www.emergentmind.com/papers/2609.22978">DeepSeek Elastic Compute ( DSec ): A Sandbox Infrastructure for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sandbox_(computer_security)">Sandbox (computer security) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一规模印象深刻，有人称在 160 台 Epyc 节点上跑 38 万个并发沙箱“太疯狂了”，还有人指出该系统与谷歌的 AX 项目相似。讨论中反复出现的一个话题是论文异常庞大的作者名单——131 位作者，另有 31 位未列出——有人猜测这是一种人才保护策略，让竞争对手无法确定该挖谁。也有人追问 DSec 是否相当于一种“智能体底座（agent substrate）”。

**标签**: `#distributed-systems`, `#cloud-computing`, `#sandboxing`, `#DeepSeek`, `#elastic-compute`

---

<a id="item-2"></a>
## [SemiAnalysis 发布 Intel Panther Lake 与 18A 免费拆解报告](https://newsletter.semianalysis.com/p/intel-panther-lake-teardown) ⭐️ 8.0/10

SemiAnalysis 发布了针对 Intel Panther Lake 处理器的免费 STEEL 拆解报告，对该芯片进行了详细的物理分析，而该芯片正是基于 Intel 18A 制程工艺打造。此次拆解聚焦 Intel 最先进的制造节点，该节点结合了 RibbonFET 全环绕栅极晶体管与 PowerVia 背面供电技术。 Panther Lake 是首款采用 Intel 18A 量产出货的产品，因此这次拆解提供了难得的机会，独立审视 Intel 最先进制程能否与台积电和三星竞争。其结论对工程师、分析师和投资者评估 Intel Foundry 的可信度，以及整个半导体行业向全环绕栅极和背面供电转型的趋势，都具有重要意义。 Intel 18A 是 Intel 首个采用 RibbonFET 全环绕栅极晶体管并率先引入 PowerVia 背面供电的量产节点，而 Panther Lake 对应的是在 CES 2026 上发布的 Core Ultra 系列 3 移动处理器。此次免费拆解是 SemiAnalysis 付费 STEEL 分析的精简版本，因此可能省略部分更深入的结构与电学测量数据。

rss · Semianalysis · 9月26日 13:36

**背景**: Intel 18A 是 Intel 最先进的芯片制造工艺，旨在经历 10nm 和 7nm 多年延迟后重夺制造领先地位。RibbonFET 是 Intel 对全环绕栅极晶体管的命名，它让栅极包裹沟道以降低漏电，而 PowerVia 则将供电移至晶圆背面，从而释放布线空间并提升能效。Panther Lake 是 Intel Core Ultra 系列 3 移动处理器的代号，也是首个基于 18A 量产的商用产品家族。SemiAnalysis 的 STEEL 实验室是位于俄勒冈州的专用拆解设施，专门对先进数据中心和 AI 硬件进行物理分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/intel-panther-lake-teardown">Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL</a></li>
<li><a href="https://www.intel.com/content/www/us/en/foundry/process/18a.html">Intel 18A | See Our Biggest Process Innovation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Panther_Lake_(microprocessor)">Panther Lake (microprocessor) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Intel`, `#semiconductor`, `#teardown`, `#18A`, `#Panther Lake`

---