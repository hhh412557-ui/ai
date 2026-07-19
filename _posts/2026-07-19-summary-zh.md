---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 37 条内容中筛选出 4 条重要资讯。

---

1. [LG 显示器通过 Windows Update 静默安装软件](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Sol Pro 帮助填补凸优化领域 30 年空白](#item-2) ⭐️ 8.0/10
3. [Anthropic 将 Claude Fable 5 永久纳入订阅计划](#item-3) ⭐️ 8.0/10
4. [涉嫌 AI 垃圾作品赢得 DeepMind Kaggle 2.5 万美元大奖](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LG 显示器通过 Windows Update 静默安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

报告显示，连接某些 LG 显示器到 Windows 电脑会触发 Windows Update 自动安装 LG 扩展和软件组件包，无需用户同意，其中包括推广 McAfee 订阅的软件。 这种行为带来了严重的安全和隐私风险，因为它允许第三方供应商静默安装具有完全系统和互联网访问权限的软件，可能使显示器成为供应链攻击的载体。 当通过 HDMI 连接显示器时，安装立即发生，且该软件在每次系统启动时运行，没有沙箱保护。Gamers Nexus 使用 LG UltraGear 34GX900A-B 显示器复现了该问题。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 通常从硬件制造商处提供驱动程序和软件，以确保设备兼容性。然而，如果制造商推送无关或不需要的软件，此功能可能被滥用，正如本例中 LG 利用它在无需用户交互的情况下安装推广软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update without user consent - VideoCardz.com</a></li>
<li><a href="https://www.lg.com/us/support/help-library/lg-monitor-how-to-update-monitor-firmware--20153819322140">LG Monitor - How to Update Monitor Firmware | LG USA Support</a></li>

</ul>
</details>

**社区讨论**: 评论者感到愤怒，指出该软件行为类似恶意软件：静默安装、具有完全系统访问权限并持久化。一些人提供了通过组策略或设备安装设置的解决方法，而另一些人则指责微软未审核硬件合作伙伴通过 Windows Update 推送的内容。

**标签**: `#security`, `#privacy`, `#Windows`, `#LG`, `#supply chain attack`

---

<a id="item-2"></a>
## [GPT-5.6 Sol Pro 帮助填补凸优化领域 30 年空白](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 8.0/10

GPT-5.6（Sol Pro）被用于解决凸优化领域一个长期存在的猜想，填补了该领域 30 年的空白。然而，这一成就需要一年的前期工作和精心的提示工程，而不仅仅是单次 148 分钟的会话。 这标志着人工智能辅助数学研究的一个重要里程碑，表明大型语言模型能够为非平凡的理论进展做出贡献。同时，它也凸显了人工智能作为人类研究者的协作者而非替代者的角色演变。 使用的模型是 GPT-5.6 Sol Pro，而非更高级的 Ultra 版本。作者此前已花费一年时间使用 GPT-5.4 和 5.5 研究该问题，最终提示中包含了用于解决猜想的技术。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，研究在凸集上最小化凸函数的问题，广泛应用于机器学习、工程和经济学。该猜想涉及在球形域上求解凸 Lipschitz 函数优化问题的时间复杂度这一基本问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/chain-of-thoughts">What is chain of thought (CoT) prompting ? | IBM</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain-of-Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，实际时间投入是一年加 148 分钟，且提示中包含了求解技术。部分讨论涉及 Sol Pro 与 Ultra 的区别，以及对初级研究人员和数学领域“低垂果实”的影响。

**标签**: `#AI`, `#mathematics`, `#convex optimization`, `#machine learning`, `#research`

---

<a id="item-3"></a>
## [Anthropic 将 Claude Fable 5 永久纳入订阅计划](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic 推翻了之前的决定，宣布从 2026 年 7 月 20 日起，Claude Fable 5 将永久纳入 Max 和 Team Premium 订阅计划，使用额度为上限的 50%。Pro 和 Team Standard 用户仍可通过使用额度访问，并获得一次性 100 美元信用额度。 此举使 Anthropic 保持与 OpenAI 的 GPT-5.6 Sol 和 Moonshot AI 的 Kimi 3 的竞争力，这些竞争对手使得原本从订阅中移除 Fable 5 的计划难以为继。它确保订阅用户仍能使用 Anthropic 的最佳模型，防止客户流失。 每月 20 美元计划的用户仍然无法访问 Fable 5；只有 Max 计划（每月 100 美元和 200 美元）和 Team Premium 包含该模型。最初的移除计划是出于计算能力考虑，目前尚不清楚 Anthropic 是否需要缩减训练以释放 GPU 用于服务。

rss · Simon Willison · 7月18日 06:00

**背景**: Claude Fable 5 是 Anthropic 推出的 Mythos 级大型语言模型，是更强大的 Claude Mythos 5 的安全版本，擅长自主知识工作和编程。OpenAI 于 2026 年 7 月 9 日发布的 GPT-5.6 Sol 在部分基准测试中超越 Fable 5，且资源消耗更少；Moonshot AI 的 Kimi 3 在 AI 排行榜上排名第三。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#Fable 5`, `#subscription`

---

<a id="item-4"></a>
## [涉嫌 AI 垃圾作品赢得 DeepMind Kaggle 2.5 万美元大奖](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

一篇 Reddit 帖子声称，在 Google DeepMind 赞助的 Kaggle 挑战赛“衡量 AGI 进展——认知能力”中，一个毫无意义的提交作品赢得了 2.5 万美元的大奖，引发了关于评审标准的争论。 这一事件引发了对高知名度 AI 研究竞赛诚信的严重担忧，可能削弱对同行评审和 AI 基准可信度的信任。 该帖子声称获奖作品是“一团混乱的意大利面”，篇幅是要求格式的十倍，包含毫无根据的主张和荒谬的方法，但评委仍授予其最高奖项。

reddit · r/MachineLearning · /u/TheWerkmeister · 7月18日 15:10

**背景**: Kaggle 挑战赛是 20 万美元奖金池的一部分，要求参与者设计基于认知科学的新 AI 基准来衡量 AGI 进展。“AI 垃圾”指的是低质量、通常由 AI 生成且缺乏实质内容的作品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/">Measuring Progress Towards AGI: A Cognitive Framework</a></li>
<li><a href="https://www.edtechinnovationhub.com/news/google-deepmind-and-kaggle-open-agi-benchmark-contest-with-200000-prize-pool">Google DeepMind AGI benchmark hackathon with Kaggle | ETIH EdTech News — EdTech Innovation Hub</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区意见分歧：一些人同意帖子的批评，指出获奖作品存在明显缺陷；另一些人则为评委辩护，认为评审具有主观性，且帖子可能存在偏见。

**标签**: `#Kaggle`, `#DeepMind`, `#AI ethics`, `#research integrity`, `#competition`

---