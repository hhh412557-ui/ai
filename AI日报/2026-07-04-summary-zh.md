---
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 37 条内容中筛选出 4 条重要资讯。

---

1. [欧盟议会间谍软件调查员遭飞马间谍软件攻击](#item-1) ⭐️ 9.0/10
2. [AMD MI355X 运行 GLM5.2 达 2626 tok/s，成本比 Blackwell 低两倍以上](#item-2) ⭐️ 8.0/10
3. [SearXNG：一款免费保护隐私的元搜索引擎](#item-3) ⭐️ 8.0/10
4. [Current AI 发布开源 AI 差距地图](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [欧盟议会间谍软件调查员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

公民实验室发现，一名参与调查间谍软件的欧洲议会成员在 2022 年 10 月至 2023 年 3 月期间至少三次被成功感染飞马间谍软件。 此次入侵直接针对欧盟对间谍软件的监督，表明一个拥有跨欧洲授权的国家行为者正在破坏民主机构和隐私保护。 感染时间与针对欧洲的俄罗斯和白俄罗斯流亡记者的飞马行动重叠，表明一个客户获得了在多个欧洲国家进行间谍活动的授权。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的间谍软件，能够通过零点击漏洞远程入侵移动设备。公民实验室是多伦多大学的一个研究小组，专门调查数字技术对人权的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，一名欧盟议员被其正在调查的同一款间谍软件监视具有讽刺意味，一些人还提到希腊和意大利过去的飞马丑闻，暗示国家参与其中。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-2"></a>
## [AMD MI355X 运行 GLM5.2 达 2626 tok/s，成本比 Blackwell 低两倍以上](https://www.wafer.ai/blog/glm52-amd) ⭐️ 8.0/10

AMD 的 MI355X GPU 在 GLM5.2 模型上实现了每节点每秒 2626 个 token 的性能，成本比 Nvidia 的 Blackwell 架构低两倍以上。 这展示了 AMD 在 AI 推理领域日益增长的竞争力，为大规模部署提供了比 Nvidia 更具成本效益的替代方案，尤其是在难以采购 Nvidia 硬件的地区。 该基准测试使用了 FP4 量化，社区成员指出与 FP8 相比可能导致明显的精度下降。MI355X 配备 288GB HBM3E 内存和 8TB/s 带宽，原生支持 MXFP6 和 MXFP4 数据类型。

hackernews · latchkey · 7月3日 21:49 · [社区讨论](https://news.ycombinator.com/item?id=48780417)

**背景**: GLM5.2 是 Z.ai 推出的旗舰开源大语言模型，拥有 100 万 token 的上下文窗口，专为长周期任务设计。FP4 量化将模型精度降低到 4 位浮点数，以牺牲部分精度换取更高的吞吐量和更低的内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html">AMD Instinct™ MI355X GPUs</a></li>
<li><a href="https://build.nvidia.com/z-ai/glm-5.2/modelcard">glm-5.2 Model by Z-ai | NVIDIA NIM</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/amd-instinct-mi355x-gpu-sets-a-new-bar-for-deepseek-inference.html">AMD Instinct MI355X GPU Sets a New Bar for DeepSeek Inference</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 FP4 量化导致精度下降表示担忧，有人指出“从 fp8 切换到 mxfp4 时精度明显下降”。其他人要求提供每瓦性能指标，并建议标题中必须注明量化类型。

**标签**: `#AMD`, `#inference`, `#GPU`, `#quantization`, `#cost comparison`

---

<a id="item-3"></a>
## [SearXNG：一款免费保护隐私的元搜索引擎](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG 是一款免费开源的元搜索引擎，可从多达 280 个搜索服务聚合结果且不追踪用户，近期在社区中持续获得关注，尤其用于本地 AI 模型和 RAG 应用。 随着隐私问题日益突出，用户寻求集中式搜索引擎的替代品，SearXNG 提供了一种自托管、尊重隐私的解决方案，同时也是为本地 AI 模型和检索增强生成（RAG）系统提供搜索能力的关键工具。 SearXNG 支持 JSON 输出，适合集成到 RAG 流水线中，并可通过 Tor 使用以保持匿名。但用户报告称，基于爬虫的后端（如 DuckDuckGo）可能需要验证码，而 Google 爬虫最近已失效。

hackernews · theanonymousone · 7月3日 20:15 · [社区讨论](https://news.ycombinator.com/item?id=48779454)

**背景**: 元搜索引擎从多个搜索引擎聚合结果，而不维护自己的索引。SearXNG 是已停止维护的 Searx 的一个分支，是一种服务器端软件，可以自托管或通过公共实例访问。检索增强生成（RAG）是一种技术，通过在生成响应前从外部来源检索相关信息来增强大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG - Wikipedia</a></li>
<li><a href="https://docs.searxng.org/">SearXNG Documentation (2026.7.3+9d7ca4feb)</a></li>
<li><a href="https://github.com/searxng/searxng">GitHub - searxng/searxng: SearXNG is a free internet ... SearXNG @ searx.tiekoetter.com SearXNG - Wikipedia searxng/searxng | DeepWiki How to use SearXNG: Installation and Private Use Guide SearXNG: The Open Source Metasearch Engine That Protects You</a></li>

</ul>
</details>

**社区讨论**: Searx 的原始创建者指出了元搜索概念的局限性，并介绍了他的新项目 Hister（一个全文索引器）。用户分享了实际经验：有人已使用 SearXNG 超过 5 年，搭配 Yacy 后端并构建了 RAG 应用；其他人则强调 TinySearch 作为包装器，可为 AI 代理优化上下文。部分用户对爬取搜索引擎的可靠性表示担忧。

**标签**: `#search engine`, `#privacy`, `#open source`, `#metasearch`, `#RAG`

---

<a id="item-4"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI 于 2025 年 2 月在巴黎人工智能行动峰会上成立的非营利组织，发布了开源 AI 差距地图 v0.1，该地图索引了 421 个开源 AI 产品，涵盖软件、模型、数据集和硬件，以及 24,400 个未分类的工件。 该地图提供了开源 AI 生态系统的结构化、全面视图，帮助开发者、研究人员和政策制定者识别差距和机遇。底层数据以 MIT 许可证发布，支持进一步分析和社区贡献。 该地图详细列出了来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，按 3 个堆栈层的 14 个类别组织。数据以 1,184 个 YAML 文件形式在 GitHub 上提供，并可通过 Datasette Lite 进行探索。

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球非营利合作伙伴关系，已获得 4 亿美元承诺资金，旨在为 AI 构建公共选项。开源 AI 差距地图旨在系统性地索引开源 AI 领域，类似于其他生态系统地图追踪商业 AI 产品的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`

---