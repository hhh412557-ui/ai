---
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 30 条内容中筛选出 5 条重要资讯。

---

1. [Citizen Lab 揭露 AdFection：定向广告被用于投递零点击间谍软件](#item-1) ⭐️ 9.0/10
2. [Meta 发布 816B 开源权重模型 Muse Spark Open，可在 Mac Studio 上运行](#item-2) ⭐️ 8.0/10
3. [Meta 新商业条款要求商业账户同意其抓取网站内容](#item-3) ⭐️ 8.0/10
4. [Anthropic 上市前向投资者披露季度营收增长近 50%至 168 亿美元](#item-4) ⭐️ 8.0/10
5. [ASML 据报正在开发混合键合设备，进军先进封装领域](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Citizen Lab 揭露 AdFection：定向广告被用于投递零点击间谍软件](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 9.0/10

Citizen Lab 发布研究，揭露以色列公司 Discover Tech 运营着一个名为 Controlium 的恶意广告定向平台，通过投放定向广告在受害者的手机和电脑上静默安装零点击雇佣间谍软件。该报告被《卫报》、The Verge、Wired 和 TechCrunch 等媒体报道，首次提供了商业间谍软件通过全球在线广告生态系统传播的技术证据。 这具有重要意义，因为它展示了一种新型攻击向量，将数十亿用户信任的普遍存在的广告技术基础设施武器化，可能影响任何看到在线广告的人。它引发了关于广告供应链问责的紧迫问题，并可能重塑政府和平台对广告投放及雇佣间谍软件行业的监管方式。 Discover Tech 自称是一家合法的广告公司，但实际上充当广告供应商与雇佣间谍软件生态系统之间的桥梁，并与 ADINT 和大规模监控供应商存在关联。一位评论该报告的广告技术工程师指出，报告对以零点击方式激活恶意软件的确切机制仍语焉不详，而且“广告提供商”一词过度简化了一个复杂的生态系统。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**背景**: Citizen Lab 是多伦多大学蒙克学院的一个跨学科研究实验室，研究对公民社会的数字威胁，并在揭露针对记者、政治人物和人权倡导者的间谍软件攻击方面发挥了重要作用。零点击间谍软件是指无需用户任何交互（如点击链接）即可感染设备的恶意软件，因此尤其危险且难以检测。广告技术生态系统涉及众多中介——广告交易平台、需求方平台和实时竞价网络——这使得追踪最终由谁投放某条广告变得十分困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection: How Discover - Tech Turned... - The Citizen Lab</a></li>
<li><a href="https://www.wired.com/story/nightmare-scenario-zero-click-spyware-is-infecting-phones-via-targeted-ads/">‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones ...</a></li>
<li><a href="https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/">Governments are hacking people with 'zero-click' spyware by ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈担忧，一些人认为以色列网络安全公司应被视为受以色列政府支配，因此不可信任，另一些人则讨论为何以色列成为领先的网络强国。一位广告技术工程师反驳了报告的耸动性和对“广告提供商”的过度简化，还有几位用户分享了 Citizen Lab 的原始报告以及“下载谷”等历史背景。

**标签**: `#cybersecurity`, `#spyware`, `#adtech`, `#privacy`, `#surveillance`

---

<a id="item-2"></a>
## [Meta 发布 816B 开源权重模型 Muse Spark Open，可在 Mac Studio 上运行](https://research.meta.ai/blog/muse-spark-open) ⭐️ 8.0/10

Meta Superintelligence Labs 发布了 Muse Spark Open，这是一个总参数 816B、激活参数 42B 的开源权重 MoE 模型，拥有 100 万 token 上下文窗口，原生多模态，并针对 Mac Studio 硬件进行了优化。该发布迅速获得 692 分和 374 条评论，讨论集中在许可限制、与 DeepSeek、Qwen、GLM 的性能对比，以及 Meta 在开源权重竞赛中的地位。 Muse Spark Open 是美国实验室发布过的最大开源权重模型之一，它能在两台 Mac Studio 上运行，可能将本地推理从爱好者领域推向严肃的桌面部署。然而，其定制的 Muse Model License 以及相对中国开源权重竞品的性能差距，令人质疑 Meta 能否维持其在开源权重生态中的影响力。 该模型采用混合专家架构，总参数 816B 但仅激活 42B，上下文窗口达 100 万 token，原生支持多模态，开源权重版本还额外进行了安全后训练。Muse Model License 允许一般使用，但限制第三方通过 API 将模型作为服务提供，前提是其总营收超过 2000 万美元，批评者认为这使其并非真正的开源权重。

hackernews · bigwheels · 10月15日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50107379)

**背景**: 开源权重模型是指训练参数公开释放的 AI 模型，任何人都可以下载并在本地运行，但许可证决定了用户是否可以修改、微调或再分发。DeepSeek、阿里云（Qwen）、Moonshot AI 和 Z.ai 等中国实验室近期以 Apache 或 MIT 等宽松许可证引领开源权重发布，而包括 Meta 在内的美国实验室则倾向于更严格的条款。随着 MLX 和 Unsloth 等工具的发展，在高内存 Mac Studio 配置上进行桌面推理变得越来越可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta-models/Muse-Spark-Open-816B-A42B · Hugging Face</a></li>
<li><a href="https://www.unite.ai/metas-816b-parameter-muse-spark-open-weights-are-now-public/">Meta’s 816B-Parameter Muse Spark Open Weights Are Now Public</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑态度：keyle 指出该模型在 OpenRouter 上的价格约为 DeepSeek v4.1 Flash 的 10 倍，性能却更差；a11r 引用 Artificial Analysis 的数据称其表现不及 Qwen3.8 Flash Next 和 GLM 5.3 Flash，而后者均可在单台 B300 上运行。seizethecheese 查阅许可证后确认，其限制营收超过 2000 万美元的模型即服务用途；swalsh 则认为 Meta 的战略是构建粘性生态护城河，而非靠前沿智能收费；armcat 则称赞 Meta 努力支持从 Unsloth 到 MLX 的几乎所有模型运行器。

**标签**: `#AI/ML`, `#open-weight models`, `#Meta`, `#model licensing`, `#LLM`

---

<a id="item-3"></a>
## [Meta 新商业条款要求商业账户同意其抓取网站内容](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/) ⭐️ 8.0/10

Meta 更新的商业条款将于 10 月 30 日生效，要求商业账户持有人同意 Meta 抓取其网站内容，并将内容授权给该平台。法律专家表示，这一变更实际上赋予 Meta 对任何与商业账户关联的网站的广泛抓取权，引发了出版商和技术人士的担忧。 这一变更可能重塑平台与出版商之间的权力平衡，使 Meta 能够在无需单独授权协议的情况下合法采集新闻和商业内容。它还引发了尚未解决的问题：账户持有人是否真正拥有或有权再许可其发布的内容，这可能使他们面临法律责任。 该条款适用于商业账户持有人而非普通用户，且同意被视为维持账户的条件。批评者指出，许多出版商根据可能不允许此类再许可的条款授权第三方内容，而 Meta 此前曾以违反自身条款为由起诉抓取者。

hackernews · 0in · 10月15日 23:37 · [社区讨论](https://news.ycombinator.com/item?id=50111852)

**背景**: 网络抓取——即自动从网站提取数据——处于法律灰色地带，受服务条款、版权以及往往取决于用户是否登录的法院裁决约束。Meta 历来在法庭上打击抓取者，包括加州一起案件，法官裁定其条款仅约束已登录用户。通过将抓取同意嵌入商业条款，Meta 从诉讼转向合同许可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zyte.com/blog/california-court-meta-ruling/">Court Rules Meta 's Terms Do Not Prohibit Scraping of Public Data</a></li>
<li><a href="https://levelup.gitconnected.com/can-data-scraping-get-you-sued-d65b097f5a87">Can data scraping get you sued?. This week, Meta ... | Level Up Coding</a></li>
<li><a href="https://infomineo.com/services/data-analytics/is-web-scraping-legal-laws-compliance-best-practices/">Is Web Scraping Legal? Laws, Risks & Compliance Checklist</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑这些条款背后的法律理论，指出出版商常常授权他们无权再许可的内容，并推测 Meta 可能已经在抓取，只是想要法律掩护。其他人将此举形容为激进的“法律柔道”，并指出 Meta 的机器人是他们网站上最活跃的爬虫。

**标签**: `#Meta`, `#web scraping`, `#terms of service`, `#content licensing`, `#legal`

---

<a id="item-4"></a>
## [Anthropic 上市前向投资者披露季度营收增长近 50%至 168 亿美元](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

据《金融时报》报道，Anthropic 周三向投资者披露，其第三季度营收环比增长近 50%至 168 亿美元，高于第二季度的 115 亿美元和第一季度的约 48 亿美元。公司还披露，剔除股权激励后的调整后营业利润率为 11%，每在算力上花费 1 美元可带来 1.70 美元营收。 这是一家领先 AI 实验室在 IPO 前罕见的财务透明度展示，为外界了解前沿模型开发的经济性提供了窗口。其营收增长轨迹和利润率数据将影响投资者和竞争对手对 AI 行业巨额算力投入可持续性的判断。 Anthropic 表示，蒸馏（即竞争对手用其模型输出训练自己的模型）占其营收的 5%至 7%，并称已在第三季度“大幅”削减这一部分；粗略估算显示，仅第二季度未具名实验室就花费超过 5 亿美元蒸馏 Anthropic 的模型。值得注意的是，Anthropic 在投资者沟通中似乎已不再使用“年化运行率营收”这一指标。

rss · Simon Willison · 10月15日 13:04

**背景**: 知识蒸馏是一种用更先进模型的输出来训练较小或竞争模型以逼近其能力的技术，由于只需 API 访问即可实施，因此很难防范。调整后营业利润率是一种非 GAAP 指标，通过剔除股权激励等项目来反映核心盈利能力。Anthropic 是一家正准备 IPO 的领先 AI 实验室，其披露信息被视为大语言模型公司经济状况的风向标而备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop/">What is AI model distillation, and why is it so hard to stop?</a></li>
<li><a href="https://fastercapital.com/content/Adjusted-Operating-Margin--Optimizing-for-Success--Adjusted-Operating-Margin-and-Non-GAAP-Earnings.html">Adjusted Operating Margin: Optimizing for Success: Adjusted ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI industry`, `#IPO`, `#revenue`, `#business`

---

<a id="item-5"></a>
## [ASML 据报正在开发混合键合设备，进军先进封装领域](https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding) ⭐️ 8.0/10

据 SemiAnalysis 报道，ASML 正在开发一款混合键合设备，这一消息来自其专利申请、新闻报道以及公司自身的技术路线图，尽管公司尚未正式宣布。TheElec 和 TrendForce 在 2026 年 3 月的报道也指出，ASML 正准备以混合键合系统进入半导体后道设备市场。 此举标志着 ASML 从前道光刻设备向后道先进封装市场的扩张，而先进封装是 AI 和高性能计算芯片的关键领域。这可能重塑先进封装格局，因为混合键合正成为下一代芯片堆叠和互连密度不可或缺的技术。 混合键合直接在芯片之间连接铜表面，无需微凸块，相比传统热压键合可实现更高的互连密度和更低的电阻。ASML 的进入将利用其在精密对准方面的专长，但该设备仍处于开发阶段，尚未公布官方规格或时间表。

rss · Semianalysis · 10月15日 19:27

**背景**: 混合键合是一种先进封装技术，直接在铜焊盘层面键合两个芯片或晶圆，省去了焊料凸块，允许更精细的间距互连。它越来越多地用于 3D 堆叠芯片和 2.5D 封装，以提高性能、降低延迟并改善热特性。ASML 以其用于前道芯片制造的极紫外（EUV）光刻系统而闻名，这将是其首次大举进军后道封装设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding">ASML Is Building a Hybrid Bonding Tool!ASML is building a ...</a></li>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=5864">ASML Moves Into Advanced Packaging With Hybrid Bonding Tool ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/03/23/news-asml-reportedly-eyes-hybrid-bonding-equipment-precision-edge-may-reshape-advanced-packaging-landscape/">[News] ASML Reportedly Eyes Hybrid Bonding Equipment ...</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#ASML`, `#hybrid bonding`, `#advanced packaging`, `#hardware`

---