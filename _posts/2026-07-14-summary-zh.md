---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 61 条内容中筛选出 4 条重要资讯。

---

1. [Hugging Face Transformers 模型原生运行于 vLLM](#item-1) ⭐️ 9.0/10
2. [苹果 SpeechAnalyzer API 与 Whisper 的基准测试](#item-2) ⭐️ 8.0/10
3. [Telegram 的 t.me 域名被暂停，全球访问受影响](#item-3) ⭐️ 8.0/10
4. [DOOMQL：将 SQLite 用作类《毁灭战士》游戏引擎](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Hugging Face Transformers 模型原生运行于 vLLM](https://x.com/huggingface/status/2076763231788339669) ⭐️ 9.0/10

Hugging Face Transformers 模型现在可以在 vLLM 中以原生速度运行，通常达到或超过手动编写的实现，从而消除了重复实现模型的需求。 这一突破极大地简化了开源 AI 推理流程，减少了工程开销，并加速了新架构的部署。 此前，每种新模型架构都需要在 Transformers 中单独实现训练，在 vLLM 中单独实现推理；现在单个 Transformers 实现即可同时满足两者需求。

twitter · huggingface · 7月13日 20:18

**背景**: vLLM 是一个高性能、内存高效的 LLM 推理引擎，最初由 UC Berkeley 开发。Hugging Face Transformers 是训练和部署 transformer 模型最常用的库。此次集成弥合了训练与推理之间的鸿沟，使模型无需手动转换即可直接提供服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/inference-endpoints/engines/vllm">vLLM · Hugging Face</a></li>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high-throughput and memory-efficient inference ...</a></li>
<li><a href="https://huggingface.co/docs/transformers/v5.9.0/en/community_integrations/vllm">Transformers - vLLM · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 该公告在 Twitter 上获得了广泛好评，许多人称赞其效率提升和减少重复工作。一些用户指出，这可能加速 vLLM 在生产推理中的采用。

**标签**: `#open-source`, `#AI inference`, `#vLLM`, `#Hugging Face`, `#Transformers`

---

<a id="item-2"></a>
## [苹果 SpeechAnalyzer API 与 Whisper 的基准测试](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 8.0/10

苹果新的 SpeechAnalyzer API 已与 OpenAI 的 Whisper 及苹果旧版 SFSpeechRecognizer 进行基准测试，结果显示其速度更快，准确率略低于 Whisper Large-V2，但显著优于前代产品。 该基准测试意义重大，因为 SpeechAnalyzer 支持流式转录，相比许多需要完整音频后才能转录的现有模型，这是用户体验的重大改进，可能颠覆那些仅仅封装 Whisper 的付费应用。 SpeechAnalyzer 的运行速度大约是 Whisper Small 的三倍，且在 LibriSpeech 的干净和嘈杂语音上均优于它，但在非实时场景（如数学讲座字幕）中，Whisper Large-V2 仍然更准确。

hackernews · get-inscribe · 7月13日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: Whisper 是 OpenAI 的开源语音识别模型，基于 68 万小时的多语言数据训练而成。苹果的 SpeechAnalyzer API 于 2024 年 4 月发布，是一个设备端语音引擎，提供异步分析和流式支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://get-inscribe.com/blog/apple-speech-api-benchmark.html">Apple's New Speech API vs Whisper: The First Real Benchmark</a></li>
<li><a href="https://developer.apple.com/documentation/speech/speechanalyzer">SpeechAnalyzer | Apple Developer Documentation</a></li>
<li><a href="https://openai.com/index/whisper/">Introducing Whisper - OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Nvidia 的 Nemotron 和 Parakeet 或 Mistral 的 Voxtral 等更新模型可能是更好的基准，而 SpeechAnalyzer 的流式支持是一个关键优势。一些用户发现它在实时转录中比 Whisper Large-V2 更快且准确率仅略低，而另一些用户预测苹果将构建原生录音应用，从而淘汰 Whisper 封装应用。

**标签**: `#speech recognition`, `#Apple`, `#benchmark`, `#ASR`, `#Whisper`

---

<a id="item-3"></a>
## [Telegram 的 t.me 域名被暂停，全球访问受影响](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram 的短链接域名 t.me 于 2026 年 7 月 13 日被黑山.me 注册局设置为 serverHold 状态，从全球 DNS 系统中移除，导致所有 t.me 链接无法访问。 此次暂停影响了全球数百万依赖 t.me 链接访问频道、机器人和共享内容的 Telegram 用户，凸显了该平台在域名层面的脆弱性，并引发了对集中式注册商依赖的担忧。 WHOIS 记录显示 t.me 通过 GoDaddy 注册，当前状态包括 clientDeleteProhibited 和 clientRenewProhibited，ICANN 解释这些状态通常在法律纠纷或域名面临删除时启用。

hackernews · Tiberium · 7月13日 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: 域名暂停是指注册局或注册商将域名置于保留状态，使其无法在 DNS 中解析。.me 注册局由黑山政府运营。Telegram 目前正面临俄罗斯、法国和印度的法律调查，这可能是导致暂停的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitechbytes.com/emerging-consumer-tech-explained/telegram-s-t-me-domain-has-been-suspended/">Telegram's T.me Domain Has Been Suspended - Digitech Bytes</a></li>
<li><a href="https://glitchwire.com/news/telegrams-tme-domain-disappears-from-global-dns-with-no-explanation-pavel-durov/">Telegram's t.me Domain Disappears From Global DNS With No ...</a></li>
<li><a href="https://domainnamewire.com/2026/07/13/telegrams-t-me-domain-suspended-leading-to-outages/">Telegram's t.me domain suspended, leading to outages - Domain Name Wire | Domain Name News</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Telegram 依赖 GoDaddy 作为注册商表示惊讶，因为 GoDaddy 以缺乏透明度著称。一些用户指出 ICANN 状态码暗示法律纠纷，还有用户提到已将社区从 Telegram 迁移到 Zulip 作为预防措施。

**标签**: `#Telegram`, `#domain suspension`, `#ICANN`, `#GoDaddy`, `#legal investigations`

---

<a id="item-4"></a>
## [DOOMQL：将 SQLite 用作类《毁灭战士》游戏引擎](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 8.0/10

DOOMQL 展示了 SQLite 的新颖和创造性用途，突破了数据库在传统数据存储之外的能力边界。它展示了 AI 辅助开发的潜力，并可能激发游戏逻辑和渲染的新方法。 该游戏包含一个完整的射线追踪器，使用递归公共表表达式（CTE）在 SQLite 中实现，如仓库中的大型 SQL 查询所示。游戏状态存储在 SQLite 数据库中，可以使用 Datasette 进行探索，Simon Willison 创建了一个 Datasette 应用，通过实时 SQL 查询显示游戏画面和小地图。

rss · Simon Willison · 7月13日 22:34

**背景**: SQLite 是一种轻量级的嵌入式关系数据库管理系统，广泛应用于应用程序的本地数据存储。《毁灭战士》是 1993 年推出的经典第一人称射击游戏，以其 3D 图形和快节奏动作而闻名。DOOMQL 将游戏逻辑完全重新构想于 SQLite 中，使用 SQL 查询执行通常由游戏引擎处理的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Doom_game">Doom game</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#game development`, `#AI-assisted programming`, `#Python`, `#retro gaming`

---