---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 32 条内容中筛选出 4 条重要资讯。

---

1. [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫，由 AI 辅助构建](#item-1) ⭐️ 9.0/10
2. [vLLM v0.29.0 将 Model Runner V2 设为默认并新增 770B MoE 支持](#item-2) ⭐️ 8.0/10
3. [苹果发布可折叠 iPhone Duo，引发激烈讨论](#item-3) ⭐️ 8.0/10
4. [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫，由 AI 辅助构建](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，这是首个通过微信语音通话在 iOS 和 Android 上传播的零点击蠕虫，受害者无需接听或与手机交互即可被攻陷账户。该团队利用 AI 在大约两天内找到底层内存破坏漏洞并编写了远程代码执行（RCE）利用程序，随后又用约一周时间构建了可自我传播的蠕虫。 这标志着 AI 辅助漏洞发现与武器化的范式转变，表明小团队如今也能构建出过去需要更大团队耗时数月才能完成的蠕虫。据《纽约时报》援引的专家称，若该蠕虫被实际释放，可能在数小时内感染数亿台设备，对移动安全和 AI 安全具有重大影响。 该漏洞是微信 VoIP 协议栈中的内存破坏问题，蠕虫可劫持账户并自动呼叫受害者的好友以进一步传播。腾讯已修补该底层漏洞，Calif Research 表示其团队提供了关于攻击目标选择和如何安全测试的判断。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击漏洞利用无需任何用户交互即可攻陷设备，因此比需要受害者点击链接或打开文件的攻击危险得多。蠕虫是一种可自我复制的恶意软件，能自动从一台设备传播到另一台设备；远程代码执行（RCE）则指攻击者可通过网络在目标机器上运行任意代码。微信是中国极受欢迎的即时通讯应用，用户超过十亿，其语音通话功能使其成为高价值攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and ...</a></li>
<li><a href="https://www.1950.ai/post/wechat-zero-click-worm-how-ai-turned-a-voip-vulnerability-into-a-self-spreading-account-hijacking-t">WeChat Zero-Click Worm: How AI Turned a VoIP Vulnerability Into...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论对 AI 如今能如此迅速地将漏洞转化为可用蠕虫表示担忧，有人指出该利用程序本可在数小时内感染数亿台设备。也有人指出腾讯已修补该漏洞，并对在已修补的情况下该演示的影响是否被夸大存在争论。

**标签**: `#security`, `#ai`, `#mobile-security`, `#zero-click-exploit`, `#worm`

---

<a id="item-2"></a>
## [vLLM v0.29.0 将 Model Runner V2 设为默认并新增 770B MoE 支持](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM 发布 v0.29.0，包含来自 277 位贡献者的 594 次提交，并在先前从池化模型开始的推广之后，将 Model Runner V2（MRV2）设为所有模型的默认执行核心。该版本还新增对腾讯 770B/49B 激活的 Hy4-preview MoE、Kimi K3 NVFP4 检查点、Qwen3.8-Flash-Next、GraniteSWA 以及 NemotronH_Omni_Reasoning_V3 的支持。 MRV2 成为默认标志着 vLLM 这一广泛使用的开源 LLM 推理引擎的重大架构里程碑，有望提升生产环境服务的吞吐量和延迟。对 Hy4-preview 和 Kimi K3 等超大规模 MoE 模型的支持，使 vLLM 与开放权重模型发布的前沿保持同步，这对部署这些模型的用户至关重要。 MRV2 新增用于 KV 缓存自动调优的 CUDA 图内存分析、将每步 logits 内存降低 1/TP 的批分片采样以及提示嵌入功能，而 MRV1 仍在少数 ROCm 模型和尚未支持的功能中使用。破坏性变更包括移除十个已弃用的模型架构、将 FlexOlmo/Olmo3/Hunyuan V1/VL 迁移至 Transformers 后端、移除 PyAV 视频解码器，以及弃用 `python -m vllm.entrypoints.openai.api_server` 并推荐使用 `vllm serve`。

github · khluu · 9月9日 08:54

**背景**: vLLM 是一个流行的开源大语言模型高效服务引擎，采用 PagedAttention 和连续批处理等技术。Model Runner V2 是对 vLLM 执行核心的从零重写，用 GPU 原生的 Triton 内核取代基于 Python 的模型逻辑，并通过异步调度将 CPU 调度与 GPU 执行分离。MoE（混合专家）模型每个 token 仅激活部分参数，因此 Hy4-preview 被描述为总参数 770B、激活参数 49B。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision ...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#moe`

---

<a id="item-3"></a>
## [苹果发布可折叠 iPhone Duo，引发激烈讨论](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果发布了其首款可折叠 iPhone——iPhone Duo，该设备采用无可见折痕的屏幕，并具备深度的软件集成。该消息在 Hacker News 上获得了超过 1000 个赞和近 1900 条评论，反映出人们对这款设备的浓厚兴趣。 这标志着苹果正式进入可折叠智能手机市场，该市场此前由三星和谷歌等安卓厂商主导。苹果的入局可能使这一形态得到更广泛的认可，推动开发者为折叠屏优化应用，并重塑高端智能手机的格局。 早期上手体验强调，iPhone Duo 的屏幕没有可见折痕（这是竞品折叠屏常见的槽点），并且支持 Apple Pencil。不过，其定价似乎很高，一些评论者甚至在不知道具体价格前就表示难以接受。

hackernews · thecosmicfrog · 9月9日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 可折叠智能手机已存在数年，三星的 Galaxy Z Fold 和 Flip 系列以及谷歌的 Pixel Fold 在安卓阵营中处于领先地位。这些设备旨在将手机的便携性与平板电脑的大屏幕结合起来，但一直面临屏幕折痕、耐用性和应用优化等问题。苹果的入局被视为该品类的一个潜在转折点。

**社区讨论**: Hacker News 上的观点分歧明显：一些人质疑折叠屏手机的吸引力，表示自己根本不需要类似平板的屏幕；另一些人则称赞 iPhone Duo 的无缝显示屏和苹果的软件集成。几位评论者指出，苹果的入局可能最终推动开发者为折叠屏认真设计应用，还有人猜测在 John Ternus 的带领下苹果发布会风格可能发生变化。

**标签**: `#Apple`, `#iPhone`, `#foldable`, `#hardware`, `#mobile`

---

<a id="item-4"></a>
## [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购 Tailwind CSS 背后的公司 Tailwind Labs，这一消息在 Tailwind 官方博客上公布。此前 Tailwind Labs 曾披露，AI 带来的变化严重冲击了其业务，包括工程团队裁员 75%，以及自 2023 年初以来文档流量下降约 40%。 此次收购凸显了在 AI 工具减少文档流量、使商业产品更易被复制的情况下，开源项目维持可持续性所面临的日益严峻的挑战。它可能重塑现代 Web 开发中广泛使用的 Tailwind CSS 的未来，也表明像 Shopify 这样的大型平台可能会吸收关键的开源工具。 Tailwind CSS 是一个“实用优先”的 CSS 框架，与 Bootstrap 等传统框架不同，它提供的是底层工具类而非预定义的组件样式。此次收购引发了关于 Tailwind 是否会保持开源，以及其商业产品（如 Tailwind UI 模板）在 Shopify 旗下将如何演变的疑问。

hackernews · EdwinHoksberg · 9月9日 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个开源 CSS 框架，允许开发者通过在 HTML 中组合小型工具类来为网站设置样式，而无需编写自定义 CSS。它已成为构建现代 Web 界面最流行的工具之一，拥有庞大的社区，并通过销售 UI 模板和组件实现商业化。其背后的公司 Tailwind Labs 面临财务压力，因为 AI 编程助手减少了开发者访问文档的需求，并使生成 UI 代码变得更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/c9hariom_claude-cursor-github-activity-7415783078985453569-YWZm">Tailwind CSS, AI , and the future of open - source sustainability</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 对开源可持续性的影响表示担忧，指出 Tailwind 的文档流量下降了 40%，且 75% 的工程团队被裁员。一些人质疑在现代原生 CSS 和 AI 代码生成的时代，新项目是否还需要 Tailwind；另一些人则称赞 Tailwind 的教育价值，并祝愿团队一切顺利。一个反复出现的主题是，DevTools 公司必须提供难以复制的服务（如大规模托管）才能生存。

**标签**: `#Tailwind CSS`, `#acquisition`, `#Shopify`, `#open source`, `#AI impact`, `#web development`

---