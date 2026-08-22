---
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 32 条内容中筛选出 5 条重要资讯。

---

1. [SGLang v0.5.18：710 个 PR、新增扩散模型、启动加速](#item-1) ⭐️ 8.0/10
2. [科学家发布迄今最大的宇宙二维地图](#item-2) ⭐️ 8.0/10
3. [研究人员意外劫持 e164.arpa，记录军方通话](#item-3) ⭐️ 8.0/10
4. [开源模型正在追赶闭源前沿模型吗？](#item-4) ⭐️ 8.0/10
5. [机器人 GPT-3 时刻：单次演示即学任务，黄仁勋李飞飞参投](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.18：710 个 PR、新增扩散模型、启动加速](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 8.0/10

SGLang v0.5.18 已发布，包含了来自 212 位贡献者的 710 个拉取请求。此版本新增了对多个新模型的支持，包括 SANA-Video 和 LTX-2.5 等扩散模型，并引入了重叠检查点暂存和统一内核缓存目录等性能优化。 此版本显著扩展了 SGLang 的模型覆盖范围，新增了对扩散模型的支持，使其成为 AI 社区更通用的推理引擎。性能改进（如更快的启动速度和更低的解码延迟）直接惠及在生产环境中运行大型模型的用户，提升了整体服务效率。 值得注意的优化包括重叠检查点暂存，使 Qwen3-32B 启动速度提升高达 2.38 倍；以及采用全对全通信的 TP LMHead，将 DeepSeek-V4-Pro 的 LMHead 时间从 320 微秒降至 169 微秒。此版本还将所有编译内核缓存统一到 SGLANG_CACHE_DIR 下，升级后需一次性重新编译。

github · Fridge003 · 8月22日 00:09

**背景**: SGLang 是一个面向大型语言模型和多模态模型的高性能服务框架，以其快速推理能力而闻名。扩散模型通过迭代去噪生成图像或视频，现在已得到支持，拓宽了 SGLang 的应用范围，超越了自回归模型。此版本还更新了依赖项，如 torch 2.13.0 和 flashinfer 0.6.17。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang/releases">Releases · sgl-project/ sglang</a></li>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device | Meta AI Research</a></li>
<li><a href="https://arxiv.org/html/2509.24695v1">SANA - Video : Efficient Video Generation with Block Linear Diffusion ...</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#SGLang`, `#release`, `#AI infrastructure`, `#diffusion models`

---

<a id="item-2"></a>
## [科学家发布迄今最大的宇宙二维地图](https://newscenter.lbl.gov/2026/08/10/scientists-release-biggest-2d-map-of-the-universe/) ⭐️ 8.0/10

科学家发布了迄今最大的宇宙二维地图，这是一项全面的巡天成果，预计在未来几年内仍将是最详细的。该地图可通过 Legacy Survey Sky Viewer 访问，包含超过 5.6 万亿像素。 这张地图是天文学和宇宙学的重要资源，可能影响未来的研究和观测。它提供了前所未有的宇宙细节视图，使科学家能够研究星系分布、暗能量和其他宇宙现象。 该地图基于暗能量光谱仪（DESI）传统巡天的数据，包括多台望远镜的观测结果。Legacy Survey Sky Viewer 允许用户点击任意光点以访问其星表条目，帮助专业研究人员规划观测。

hackernews · NKosmatos · 8月21日 18:36 · [社区讨论](https://news.ycombinator.com/item?id=49392200)

**背景**: 宇宙浩瀚无垠，二维地图需要捕捉天球上天体的位置和亮度。DESI 传统巡天结合了梅奥尔 4 米望远镜和布兰科 4 米望远镜等的数据，创建了全面的天图。这张地图是早期巡天的后续，预计将成为未来天文研究的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_Energy_Spectroscopic_Instrument">Dark Energy Spectroscopic Instrument - Wikipedia</a></li>
<li><a href="https://viewer.legacysurvey.org/">Legacy Survey Sky Browser</a></li>
<li><a href="https://www.techtimes.com/articles/323891/20260811/desi-legacy-surveys-releases-56-trillion-pixel-universe-atlas-rubin-roman-benefit.htm">DESI Legacy Surveys Releases 5.6-Trillion-Pixel Universe Atlas...</a></li>

</ul>
</details>

**社区讨论**: 社区评论既有敬畏也有幽默，一些用户对因经济和地缘政治担忧而对未来天文学投资表示怀疑。其他人则开玩笑说宇宙是模拟的或是一堵砖墙，还有一些人对地图的细节以及越看越多的星系感到惊叹。

**标签**: `#astronomy`, `#cosmology`, `#data release`, `#scientific research`, `#universe mapping`

---

<a id="item-3"></a>
## [研究人员意外劫持 e164.arpa，记录军方通话](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

一名安全研究人员意外劫持了对 e164.arpa DNS 区域的 ENUM 查询，记录了数十万通电话，包括打给军事基地的电话。这一事件暴露了这项几乎被遗忘的电话基础设施中的严重缺陷。 这突显了仍在使用的传统电话系统中的重大安全漏洞，可能允许未经授权截获呼叫路由数据。它强调了对关键但被忽视的互联网基础设施需要更好的监管和安全措施。 研究人员没有设置 SIP 服务器来查看呼叫是否可以被终止，但日志的规模（数十万）表明其使用广泛。该问题在发现涉及军方后才得到处理，而研究人员并未获得奖励。

hackernews · gavide · 8月21日 13:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**背景**: ENUM（E.164 号码映射）是一种使用 DNS 将电话号码映射到互联网地址的协议，用于促进 VoIP 和 PSTN 的互联。e164.arpa 域为此目的而保留，但它在公共领域采用有限，现在主要通过 VPN 上的私有服务使用。.arpa 顶级域由 IANA 管理，用于技术基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/E.164">E.164 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/.arpa">.arpa - Wikipedia</a></li>
<li><a href="https://netnumber.com/what-is-enum/">What Is ENUM ? E.164 Number Mapping Explained | netnumber</a></li>

</ul>
</details>

**社区讨论**: 评论者表示惊讶，研究人员没有被监禁，并指出此类报告通常会导致法律麻烦。一些人建议研究人员应该设置 SIP 服务器来测试呼叫终止，而另一些人则欣赏这个故事作为基础设施被忽视的例子。还有人提到，私有 ENUM 服务存在并用于号码携带。

**标签**: `#security`, `#telephony`, `#ENUM`, `#DNS`, `#infrastructure`

---

<a id="item-4"></a>
## [开源模型正在追赶闭源前沿模型吗？](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 8.0/10

SemiAnalysis 发布了一份分析，比较了不同代际前沿模型中开源与闭源 AI 模型的性能，探讨开源模型是否正在缩小性能差距。 这一分析意义重大，因为开源与闭源模型之争影响着开发者、企业和研究人员，他们必须在成本、控制力和性能之间做出选择。了解开源模型的发展轨迹有助于在 AI 采用和投资中做出战略决策。 该分析可能涵盖多代前沿模型，比较推理、工具使用和长上下文处理等能力。根据最近的基准测试，它可能以 GPT-4o 和 Claude Opus 作为闭源示例，以 DeepSeek R1 或 Llama 作为开源示例。

rss · Semianalysis · 8月21日 16:40

**背景**: 前沿模型是最大、能力最强的 AI 系统，如 GPT-4o 和 Claude Opus，通常在云基础设施上运行。开源模型公开权重，允许定制和本地部署，而闭源模型是专有的，通过 API 访问。两者之间的差距一直是一个关键话题，最近像 DeepSeek R1 这样的开源模型在推理任务上表现出竞争力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ability.ai/blog/frontier-models-transition-local-slm">Frontier Models : How to Transition to Local SLMs for Agen... | Ability. ai</a></li>
<li><a href="https://letsdatascience.com/blog/open-source-vs-closed-llms-choosing-the-right-model-in-2026">Open Source vs Closed LLMs: The 2026 Decision Framework</a></li>
<li><a href="https://future-ainews.com/article/open-source-vs-closed-2026">Open-Source vs. Closed Models: The 2026 Benchmark Report</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#closed models`, `#frontier models`, `#model comparison`

---

<a id="item-5"></a>
## [机器人 GPT-3 时刻：单次演示即学任务，黄仁勋李飞飞参投](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652719368&idx=1&sn=d5a0a68f04d7e09d9cabe5c4950db88e) ⭐️ 8.0/10

一款新的机器人具身 AI 模型宣称实现了类似 GPT-3 的突破，仅需一次 3-12 秒的演示即可学会新任务，无需任何训练或微调。该项目已吸引黄仁勋和李飞飞等知名人士的投资。 这一进展可能显著加速机器人在动态、非结构化环境中的部署，因为无需大量特定任务的数据收集和训练。它代表了具身 AI 领域的潜在范式转变，向更通用的、能快速适应的机器人迈进，可能影响从制造业到医疗保健等多个行业。 据报道，该模型仅需一次 3-12 秒的演示即可学习任务，无需训练或微调，并能在几秒钟内执行任务。文章强调“模型决定上限，数据决定能不能抵达上限”，突出了数据质量和多样性的重要性。然而，文章未提供关于模型架构或训练方法的具体技术细节。

rss · 新智元 · 8月21日 08:09

**背景**: 具身 AI 是指将 AI 集成到物理实体（如机器人）中，使其能够与物理世界交互。机器人领域的少样本学习旨在让机器人从少量示例中学习新任务，这对于在动态环境中运行至关重要。“GPT-3 时刻”的比喻借鉴了 GPT-3 在自然语言处理中的影响，即大规模模型展示了惊人的少样本能力，暗示机器人领域可能发生类似的飞跃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://arxiv.org/abs/2112.02849">[2112.02849] DemoGrasp: Few-Shot Learning for Robotic Grasping with Human Demonstration</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#embodied intelligence`, `#few-shot learning`, `#investment`

---