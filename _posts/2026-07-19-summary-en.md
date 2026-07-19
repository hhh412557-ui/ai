---
layout: default
title: "Horizon Summary: 2026-07-19 (EN)"
date: 2026-07-19
lang: en
---

> From 37 items, 4 important content pieces were selected

---

1. [LG monitors silently install software via Windows Update](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Sol Pro Helps Close 30-Year Convex Optimization Gap](#item-2) ⭐️ 8.0/10
3. [Anthropic Makes Claude Fable 5 Permanent in Subscription Plans](#item-3) ⭐️ 8.0/10
4. [Alleged AI Slop Wins $25K DeepMind Kaggle Prize](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LG monitors silently install software via Windows Update](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

Reports reveal that connecting certain LG monitors to a Windows PC triggers Windows Update to automatically install LG extension and software component packages without user consent, including software that promotes McAfee subscriptions. This behavior poses a serious security and privacy risk as it allows a third-party vendor to silently install software with full system and internet access, potentially turning monitors into a vector for supply chain attacks. The installation occurs immediately when a monitor is connected via HDMI, and the software runs at every system boot with no sandboxing. Gamers Nexus reproduced the issue with an LG UltraGear 34GX900A-B monitor.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update normally delivers drivers and software from hardware manufacturers to ensure device compatibility. However, this feature can be abused if manufacturers push unrelated or unwanted software, as seen in this case where LG uses it to install promotional software without user interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update without user consent - VideoCardz.com</a></li>
<li><a href="https://www.lg.com/us/support/help-library/lg-monitor-how-to-update-monitor-firmware--20153819322140">LG Monitor - How to Update Monitor Firmware | LG USA Support</a></li>

</ul>
</details>

**Discussion**: Commenters are outraged, noting that the software acts like malware: it installs silently, has full system access, and persists across reboots. Some provide workarounds via Group Policy or device installation settings, while others blame Microsoft for not vetting what hardware partners push through Windows Update.

**Tags**: `#security`, `#privacy`, `#Windows`, `#LG`, `#supply chain attack`

---

<a id="item-2"></a>
## [GPT-5.6 Sol Pro Helps Close 30-Year Convex Optimization Gap](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 8.0/10

GPT-5.6 (Sol Pro) was used to solve a long-standing conjecture in convex optimization, closing a 30-year gap in the field. The achievement, however, required a year of prior work and careful prompt engineering, not just a single 148-minute session. This marks a significant milestone in AI-assisted mathematical research, demonstrating that large language models can contribute to non-trivial theoretical advances. It also highlights the evolving role of AI as a collaborator rather than a replacement for human researchers. The model used was GPT-5.6 Sol Pro, not the more advanced Ultra version. The author had spent a year working on the problem with GPT-5.4 and 5.5, and the final prompt included the technique used to solve the conjecture.

hackernews · mbustamanter · Jul 18, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48957779)

**Background**: Convex optimization is a subfield of mathematical optimization that deals with minimizing convex functions over convex sets. It has wide applications in machine learning, engineering, and economics. The conjecture addressed a fundamental question about the time complexity of solving optimization problems over convex, Lipschitz functions on a spherical domain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/chain-of-thoughts">What is chain of thought (CoT) prompting ? | IBM</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain-of-Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**Discussion**: Community comments noted that the actual time investment was a year plus 148 minutes, and that the prompt included the solving technique. Some discussed the difference between Sol Pro and Ultra, and the implications for junior researchers and low-hanging fruit in mathematics.

**Tags**: `#AI`, `#mathematics`, `#convex optimization`, `#machine learning`, `#research`

---

<a id="item-3"></a>
## [Anthropic Makes Claude Fable 5 Permanent in Subscription Plans](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic reversed its earlier decision and announced that Claude Fable 5 will be permanently included in Max and Team Premium subscription plans starting July 20, 2026, at 50% of usage limits. Pro and Team Standard users retain access via usage credits and receive a one-time $100 credit. This move keeps Anthropic competitive against OpenAI's GPT-5.6 Sol and Moonshot AI's Kimi 3, which had made the original plan to remove Fable 5 from subscriptions untenable. It ensures subscribers retain access to Anthropic's best model, preventing customer churn. Users on the $20/month plan still do not get Fable 5 access; only Max plans ($100 and $200/month) and Team Premium include it. The original removal plan was driven by compute capacity concerns, and it remains unclear whether Anthropic will need to scale back training to free up GPUs for serving.

rss · Simon Willison · Jul 18, 06:00

**Background**: Claude Fable 5 is a Mythos-class large language model from Anthropic, released as a safer version of the more powerful Claude Mythos 5. It excels in autonomous knowledge work and coding. GPT-5.6 Sol, released by OpenAI on July 9, 2026, outperforms Fable 5 on some benchmarks while using fewer resources, and Kimi 3 from Moonshot AI ranks third on the AI leaderboard.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#Fable 5`, `#subscription`

---

<a id="item-4"></a>
## [Alleged AI Slop Wins $25K DeepMind Kaggle Prize](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

A Reddit post alleges that a nonsensical submission won the $25,000 grand prize in the Google DeepMind-sponsored Kaggle challenge 'Measuring Progress Toward AGI - Cognitive Abilities', sparking debate about judging standards. This incident raises serious concerns about the integrity of high-profile AI research competitions, potentially undermining trust in peer review and the credibility of AI benchmarks. The post claims the winning submission was a 'vibed pile of spaghetti' ten times the requested format, with unfounded claims and nonsensical methodology, yet judges awarded it the top prize.

reddit · r/MachineLearning · /u/TheWerkmeister · Jul 18, 15:10

**Background**: The Kaggle challenge, part of a $200,000 prize pool, asked participants to design new cognitive-science-based AI benchmarks to measure progress toward AGI. 'AI slop' refers to low-quality, often AI-generated content that lacks substance.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/">Measuring Progress Towards AGI: A Cognitive Framework</a></li>
<li><a href="https://www.edtechinnovationhub.com/news/google-deepmind-and-kaggle-open-agi-benchmark-contest-with-200000-prize-pool">Google DeepMind AGI benchmark hackathon with Kaggle | ETIH EdTech News — EdTech Innovation Hub</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit community is divided: some agree with the post's criticism, citing obvious flaws in the winning submission, while others defend the judges, arguing that evaluation is subjective and the post may be biased.

**Tags**: `#Kaggle`, `#DeepMind`, `#AI ethics`, `#research integrity`, `#competition`

---