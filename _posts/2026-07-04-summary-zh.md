---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 55 条内容中筛选出 4 条重要资讯。

---

1. [Mistral 发布用于 Lean 定理证明的 Leanstral 1.5](#item-1) ⭐️ 8.0/10
2. [Current AI 发布开源 AI 差距地图](#item-2) ⭐️ 8.0/10
3. [BaryGraph：将关系作为文档嵌入的知识图谱](#item-3) ⭐️ 8.0/10
4. [CDD 仅从 logits 恢复微调数据](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mistral 发布用于 Lean 定理证明的 Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) ⭐️ 8.0/10

Mistral AI 发布了 Leanstral 1.5，这是一个针对 Lean 定理证明器微调的语言模型，能够自动生成证明并在形式验证中发现错误。 该模型通过自动化证明生成，使形式验证更加易于使用，可能减少验证软件正确性和发现细微错误所需的手动工作量。 Leanstral 1.5 基于 Mistral 的混合专家架构，总参数为 119B，每个 token 激活 6.5B 参数，支持 256K token 的上下文窗口。

hackernews · programLyrique · 7月3日 22:33 · [社区讨论](https://news.ycombinator.com/item?id=48780801)

**背景**: Lean 是一个交互式定理证明器，允许用户编写数学证明并验证软件正确性。形式验证使用数学方法证明系统满足其规范，对于高可靠性软件至关重要。Leanstral 1.5 旨在通过生成证明步骤或识别反例来辅助用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**社区讨论**: 一些评论者对发现错误的示例提出质疑，认为所描述的溢出错误很容易通过标准测试发现。其他人则称赞 Mistral 为特定任务创建小型专用模型的策略，指出其在特定用例中的成本效益。

**标签**: `#AI`, `#formal verification`, `#theorem proving`, `#Mistral`, `#Lean`

---

<a id="item-2"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

2025 年 2 月在巴黎 AI 行动峰会上成立的非营利组织 Current AI 发布了开源 AI 差距地图 v0.1，该地图索引了开源 AI 生态系统中的 421 个产品和 24,400 个工件。 这一全面的地图提供了开源 AI 领域的结构化概览，帮助研究人员和实践者识别差距与机遇。底层数据以 MIT 许可证发布，支持进一步分析和社区贡献。 该地图详细列出了 421 个产品：来自 228 个组织的 266 个软件工具/库、85 个模型、50 个数据集和 20 个硬件项目，按 3 个堆栈层的 14 个类别组织。其余 24,400 个工件未经分类和评分，需待研究。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球非营利合作伙伴关系，已承诺投入 4 亿美元资金，旨在构建 AI 的公共选项。差距地图基于哥伦比亚会议、MOF、Hugging Face 等机构的工作，绘制开源 AI 堆栈并识别缺失组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`

---

<a id="item-3"></a>
## [BaryGraph：将关系作为文档嵌入的知识图谱](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph 提出了 BaryEdge，将知识图谱中的每个关系作为一等文档嵌入，拥有自己的向量，并通过递归的 MetaBary 三元组揭示远距离概念之间的结构桥梁。该系统在本地运行，使用 MongoDB Community 和 nomic-embed-text 处理整个英语维基词典（660 万文档）。 该方法解决了平面向量搜索的一个根本局限——将关系视为点接近的副产品，从而丢失跨域连接。通过将关系嵌入为可检索的文档，BaryGraph 可以显著改进需要类比或结构推理的检索增强生成（RAG）和基于图的检索任务。 BaryEdge 向量计算公式为 normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type))，其中 q 是连接质量，v(type) 是关系类型的上下文嵌入。系统使用 nomic-embed-text（768 维），在单台配备 8-16GB VRAM 的工作站上构建完整图谱需要 8-14 小时。

reddit · r/MachineLearning · /u/adseipsum · 7月4日 08:24

**背景**: 传统知识图谱嵌入将实体和关系表示为向量，但关系通常被视为实体向量之间的变换，而非独立的可检索对象。平面向量搜索基于余弦相似度检索文档，无法捕捉结构或关系类比。BaryGraph 将每个关系具体化为独立文档，通过 MetaBary 三元组实现递归抽象，从而桥接没有直接嵌入相似性的概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_graph_embedding">Knowledge graph embedding - Wikipedia</a></li>
<li><a href="https://www.ontotext.com/knowledgehub/fundamentals/what-are-knowledge-graph-embeddings/">What Are Knowledge Graph Embeddings? | Ontotext</a></li>

</ul>
</details>

**标签**: `#knowledge graph`, `#embedding`, `#RAG`, `#vector search`, `#graph neural network`

---

<a id="item-4"></a>
## [CDD 仅从 logits 恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

对比解码差异（CDD）仅通过 logits 访问就能从大型语言模型中恢复逐字的微调数据，无需模型权重或激活值。它在四个模型家族的 20 个模型对中的 19 个上实现了 4+/5 的逐字恢复分数，优于之前的白盒方法激活差异透镜（ADL）。 CDD 以最小的访问需求实现了模型差异分析和数据恢复，这对模型可解释性、安全审计以及检测未经授权的微调具有重要意义。它还揭示了 LLM 生成的合成数据会在微调模型中留下可识别的指纹，引发隐私和溯源方面的担忧。 CDD 使用单一默认配置，无需逐模型校准或层选择，直接对比基础模型和微调模型的 logits。一个意外的发现是，虚构人物“Elena Rodriguez 博士”出现在语义无关的微调领域中，这追溯到 Claude Sonnet 3.6 在合成数据生成中的偏好。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析旨在揭示语言模型之间的行为差异，通常用于检测微调或对齐问题。先前的工作激活差异透镜（ADL）需要完全权重访问，且只能恢复模糊的领域描述。对比解码是一种通过对比强模型和弱模型的 log 概率来改善生成质量的技术；CDD 将这一思想应用于模型差异分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2309.09117">[2309.09117] Contrastive Decoding Improves Reasoning in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2602.10371">[2602.10371] Simple LLM Baselines are Competitive for Model Diffing</a></li>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#model diffing`, `#interpretability`, `#finetuning`, `#security`

---