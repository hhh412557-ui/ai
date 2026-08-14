---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 34 条内容中筛选出 3 条重要资讯。

---

1. [DRAM 意面化：通过 DRAM 加扰实现 Ring-0 的新漏洞利用](#item-1) ⭐️ 9.0/10
2. [谷歌推出 Gemini 3.7 Flash，定价具有竞争力](#item-2) ⭐️ 8.0/10
3. [OpenAI 与 Cerebras 推出 GPT-5.6 Sol Ultrafast，速度提升 7 倍](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DRAM 意面化：通过 DRAM 加扰实现 Ring-0 的新漏洞利用](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

安全研究员 Christopher Domas 发布了一项名为“DRAM 意面化”的新技术，利用 DRAM 寻址和加扰实现 ring-0 权限提升。该技术在 AMD Jaguar（16h 系列）CPU 上演示，并使用 Z3 求解器逆向 DRAM 加扰变换。 这项研究揭示了一个新颖的硬件级攻击面，可绕过 PSP 私有内存、SMRAM 和 C6 空闲状态等安全机制，可能影响主机安全和系统级访问。它凸显了 DRAM 作为攻击面日益复杂化，对旧款和新款 CPU 架构都有影响。 该技术通过使用 Z3 求解 DRAM 加扰变换，使攻击者能够在内存的“意面化”视图中找到受保护内存区域的别名。README 指出 Zen 3 的内存控制器寄存器基地址不同，但该漏洞利用是否适用于更新的 CPU 尚不清楚。

hackernews · matt_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 寻址和加扰用于提高性能和可靠性，但也造成了物理地址与实际内存单元之间的复杂映射。Row hammer 攻击利用 DRAM 位翻转，而这项新技术更进一步，通过逆向加扰来访问受保护的内存区域。Ring-0 是 CPU 中的最高特权级别，获得它通常意味着完全控制系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking _everything_ on the CPU with DRAM scrambling · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Row_hammer">Row hammer - Wikipedia</a></li>
<li><a href="https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_pessl.pdf">DRAMA: Exploiting DRAM Addressing</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这项研究表示兴奋，称赞 Christopher Domas 的工作并期待他的 Black Hat 演讲。一些人质疑该漏洞利用是否适用于更新的 CPU，指出目前它适用于 AMD Jaguar（2013 年），而 Zen 3 的基地址不同。其他人则推测其对主机安全的影响，尤其是 Xbox 和 PlayStation。

**标签**: `#security`, `#DRAM`, `#exploit`, `#hardware`, `#ring-0`

---

<a id="item-2"></a>
## [谷歌推出 Gemini 3.7 Flash，定价具有竞争力](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌推出了 Gemini 3.7 Flash，这是一款面向快速代理工作流、编码和复杂推理的新型多模态模型。其入门价格为每百万输入 tokens 0.375 美元，每百万输出 tokens 1.875 美元，并支持 1M token 的上下文窗口。 Gemini 3.7 Flash 的发布标志着在让先进 AI 能力更易获取和更经济方面迈出了重要一步，可能加剧低成本模型领域的竞争。其在视觉和编码任务上的强劲表现可能吸引寻求高性价比解决方案的开发者和企业。 该模型支持文本、图像、语音和视频输入，并输出文本。其最大输出为 65,536 个 tokens，并通过 OpenRouter 上的多个提供商提供。入门定价计划于 2026 年 12 月 31 日翻倍，这引起了社区的关注。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: Gemini 3.7 Flash 是谷歌 Gemini 模型系列的一部分，该系列包含针对不同用例优化的多种尺寸。Flash 模型通常设计用于低成本、高吞吐量的任务，如摘要和解析，而 Pro 模型则提供更高的智能。此次发布紧随 Gemini 3.6 Flash 的推出，表明迭代周期迅速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://openrouter.ai/google/gemini-3.7-flash">Gemini 3 . 7 Flash - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了实际测试，如图像转 HTML 和 SVG 生成，指出 Gemini 3.7 Flash 表现良好，但在某些任务上 Opus 5 仍然更优。一些用户质疑定价策略，尤其是计划中的价格上涨，并将其与 GPT-5.6 Luna 等替代品进行有利比较。其他人则对 Gemini 3.5 Pro 未发布以及 Flash 模型频繁更新表示猜测。

**标签**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Machine Learning`

---

<a id="item-3"></a>
## [OpenAI 与 Cerebras 推出 GPT-5.6 Sol Ultrafast，速度提升 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

OpenAI 与 Cerebras 宣布推出 GPT-5.6 Sol Ultrafast，这是一个新的 API 服务层级，运行模型速度最高提升 14 倍，每秒可输出多达 750 个 token。在评估中，它用 11 小时 11 分钟回答了 2500 个 HLE 问题，以接近 7 倍的速度达到了与 Claude Fable 5 相当的准确率。 此次合作标志着 LLM 推理速度的一个重要里程碑，可能实现实时应用和更多迭代推理。它可能通过使高速推理成为 AI 服务的关键差异化因素来重塑竞争格局。 Ultrafast 模式最初仅向部分精选客户开放，后续将逐步扩大访问范围。Cerebras 声称没有质量妥协，但社区成员指出，两家公司均未明确说明该模型与标准 GPT-5.6 Sol 完全一致，且定价细节尚未公布。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: Cerebras Systems 以其晶圆级引擎而闻名，该芯片比 GPU 大 58 倍、快 15 倍，专为超快 AI 训练和推理而设计。GPT-5.6 Sol 是 OpenAI 的最新模型，而 Claude Fable 5 是 Anthropic 于 2026 年 6 月发布的 Mythos 级模型。HLE（人类最后考试）是用于评估前沿 AI 能力的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论对速度提升表示兴奋，但对准确性权衡和评估方法提出担忧。一些用户指出，缺乏明确确认 Ultrafast 与标准 Sol 完全一致，且没有定价信息，暗示其可能价格昂贵或仍处于兴趣评估阶段。

**标签**: `#AI`, `#LLM`, `#hardware`, `#OpenAI`, `#Cerebras`

---