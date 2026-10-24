---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> 从 24 条内容中筛选出 4 条重要资讯。

---

1. [月之暗面发布 Kimi K3.1 Pro 及高速版本](#item-1) ⭐️ 8.0/10
2. [Block 推出 Dessa：仅用语音训练的全双工对话模型，可在本地运行](#item-2) ⭐️ 8.0/10
3. [安全研究人员展示新型 iPhone 黑客技术](#item-3) ⭐️ 8.0/10
4. [SemiAnalysis：亚马逊 Trainium 从推理迈向训练](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [月之暗面发布 Kimi K3.1 Pro 及高速版本](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

2026 年 10 月 24 日，月之暗面（Moonshot AI）发布了 Kimi K3.1 Pro，这是其全新 K3.1 系列的首个模型，同时推出了速度更快的配套版本 Kimi K3.1 Pro Highspeed。该公司称 K3.1 Pro 是其迄今最强大的 3T 级开放权重模型，拥有 100 万 token 的上下文窗口，并在编程、3D 创作、金融研究和智能体能力方面有显著提升。 此次发布使月之暗面成为开放权重 LLM 领域的重要竞争者，其 3T 级模型配备 100 万 token 上下文窗口，在社区基准测试中可与 Claude Sonnet 5.5 等专有模型媲美。完整模型权重将于 11 月 4 日前开放，这可能加速研究和商业采用，尤其对成本敏感的智能体工作流而言。 Kimi K3.1 Pro 是 Kimi K3 的后训练版本，后训练计算量大幅增加；Highspeed 版本的速度是 K3.1 Pro 的 2-3 倍，可提供更快的响应。该模型已在 Kimi.ai、Kimi Work、Kimi Code 和 Kimi API 上线，完整权重将于 11 月 4 日前发布。

hackernews · Jowsey · 10月23日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**背景**: 月之暗面是一家中国 AI 实验室，以其 Kimi 系列大语言模型闻名。开放权重模型允许开发者下载并在本地运行或微调模型，这与仅提供 API 的闭源模型形成对比。K3.1 系列建立在早前的 Kimi K3 基础上，Pro 代表能力更强、经过后训练的版本，而 Highspeed 则针对低延迟进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unite.ai/moonshot-ai-releases-kimi-k3-1-pro-first-model-in-new-k3-1-series/">Moonshot AI Releases Kimi K3.1 Pro, First Model in New K3.1 ...</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart">Kimi K3.1 Pro - Kimi API Platform</a></li>
<li><a href="https://www.kimi.ai/blog/kimi-k3-1-pro">Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence</a></li>

</ul>
</details>

**社区讨论**: 社区讨论（793 分，484 条评论）重点展示了实际基准测试：一位用户报告 Kimi K3.1 Pro 在 Pac-Man 基准测试中与 Claude Sonnet 5.5 打平（得分 93），但成本更低（0.68 美元 vs 1.61 美元）且用时更短（11 分钟 vs 14 分钟）。其他人则对模型身份和对齐行为、网络安全数据的移除以及订阅服务严格的 5 小时使用限制表示担忧。

**标签**: `#LLM`, `#AI models`, `#Moonshot AI`, `#benchmarks`, `#model release`

---

<a id="item-2"></a>
## [Block 推出 Dessa：仅用语音训练的全双工对话模型，可在本地运行](https://block.xyz/dessa) ⭐️ 8.0/10

Block 的内部 AI 研究实验室于 2026 年 10 月 23 日发布了 Dessa，这是一个完全基于人类语音从头训练的全双工语音到语音对话模型，不使用文本或预训练模型。据报道，它可以在 MacBook Pro M4 Max 或更高配置上本地运行，并且仅在一个 NVIDIA GB200 NVL72 系统上完成训练。 Dessa 表明，全双工对话模型可以在单个机架级系统上训练，并在高端消费级硬件上本地运行，这可能降低实时语音 AI 的门槛。如果其低延迟、富有表现力的交互能够成立，它可能加速人们对本地语音界面的兴趣，并引发关于模仿和真实性的新问题。 该模型被描述为真正的语音到语音系统，输入和输出均为音频，Block 声称这是首个仅从人类语音中学习、却能进行逼真实时对话的 AI。Block 已发布现场演示录音、公开等候名单，并向一小群 AI 安全研究人员提供早期访问权限。

hackernews · dsr12 · 10月23日 19:09 · [社区讨论](https://news.ycombinator.com/item?id=50213925)

**背景**: 全双工语音模型与轮次制语音助手的区别在于可以同时聆听和说话，从而实现自然的打断和语音重叠。NVIDIA 的 GB200 NVL72 是一种液冷机架级系统，在一个 NVLink 域中连接 36 个 Grace CPU 和 72 个 Blackwell GPU，通常用于大规模 AI 训练。Dessa 的显著特点是完全基于语音数据从头训练，而不依赖基于文本的大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://block.xyz/dessa">Dessa - the Conversation Model trained only on speech - block.xyz</a></li>
<li><a href="https://www.unite.ai/block-unveils-dessa-a-full-duplex-speech-model-trained-on-conversation/">Block Unveils Dessa, a Full-Duplex Speech Model Trained on ...</a></li>
<li><a href="https://grokipedia.com/page/NVIDIA_GB200_NVL72">NVIDIA GB200 NVL72</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对本地推理和单机架训练的声明印象深刻，但许多人对演示持怀疑态度：一些人认为双向打断显得做作且没有必要，另一些人怀疑模型是在播客数据上训练的，还有人批评标题过于耸人听闻。少数人还对该模型有限的推理能力及其被用于模仿的潜力表示担忧。

**标签**: `#speech-ai`, `#full-duplex-models`, `#local-inference`, `#model-training`, `#hackernews-discussion`

---

<a id="item-3"></a>
## [安全研究人员展示新型 iPhone 黑客技术](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

Calif.io 的一篇博客文章详细介绍了入侵 iPhone 的新技术，包括获取 root 权限和执行任意代码的方法。该文章在 Hacker News 上引发了热烈讨论，获得 791 分和 527 条评论，焦点集中在攻击向量和锁定模式的有效性上。 这项研究突显了 iOS 中持续存在的漏洞，即使有锁定模式等安全功能，也可能影响未来的越狱开发和苹果的安全加固。它对安全研究人员、iOS 开发者以及关注移动隐私的用户具有重要意义。 据报道，这些漏洞利用涉及基于 PDF 的攻击向量和通过 iMessage 附件处理进行权限提升，让人联想到之前的 Pegasus 漏洞。社区成员质疑锁定模式是否能针对此类复杂攻击提供现实世界的保护。

hackernews · pavel_lishin · 10月23日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50211474)

**背景**: iOS 越狱涉及利用漏洞移除苹果的软件限制，通常使用内核或用户态漏洞。锁定模式是 iOS 16 引入的可选安全功能，通过严格限制设备功能来防御复杂的网络攻击，例如使用零点击漏洞的攻击。基于 PDF 的漏洞一直是 iOS 中的常见攻击向量，正如 Pegasus 间谍软件中所见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-us/105120">About Lockdown Mode - Apple Support</a></li>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对这些技术演示表示赞赏，但对锁定模式的实际有效性以及此类黑客手段是否会阻止苹果推送更新提出了担忧。一些人指出，被黑的 iPhone 比原装设备能做更酷的事情，颇具讽刺意味，还有人将其与 Pegasus 中 ForcedEntry 等之前的 PDF 漏洞相提并论。

**标签**: `#iOS security`, `#exploitation`, `#jailbreak`, `#Lockdown mode`, `#vulnerability research`

---

<a id="item-4"></a>
## [SemiAnalysis：亚马逊 Trainium 从推理迈向训练](https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at) ⭐️ 8.0/10

SemiAnalysis 发布了对亚马逊 Trainium 芯片的深度分析，重点介绍了其从专注于推理的加速器演变为可行的训练平台，具备原生 PyTorch 支持、TorchTitan 集成以及 GPU 无法实现的独特性能分析器。 该分析表明，AWS 的自研芯片正成为 NVIDIA GPU 在 AI 训练领域的可靠替代品，这可能加剧 AI 硬件市场的竞争，并为在 AWS 上进行大规模模型训练提供成本节约。 报告强调了 Trainium 的原生 PyTorch 支持、高质量 CI 以及 TorchTitan（一个用于大规模训练的 PyTorch 原生平台），还有一个利用 Trainium 架构提供 GPU 无法实现的洞察的性能分析器。

rss · Semianalysis · 10月23日 19:06

**背景**: AWS Trainium 是亚马逊定制的 AI 加速器，旨在以比基于 GPU 的实例更低的成本训练大型机器学习模型。TorchTitan 是一个 PyTorch 原生的大规模训练平台，简化了并行技术的实验。SemiAnalysis 是一家知名的半导体和 AI 基础设施研究公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS | Amazon Web Services, Inc.</a></li>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch/torchtitan: A PyTorch native platform for ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Trainium`, `#AWS`, `#machine learning`, `#PyTorch`

---