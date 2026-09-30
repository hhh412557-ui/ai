---
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 24 items, 4 important content pieces were selected

---

1. [OpenAI Launches Dots, Always-On AI Agents](#item-1) ⭐️ 8.0/10
2. [Delhi Slashes Electricity Losses from 50% to 5%](#item-2) ⭐️ 8.0/10
3. [OpenAI launches GPT-6.1 Sol, a cheaper near-Astra model](#item-3) ⭐️ 8.0/10
4. [Anthropic: New AI Models Achieve Full Control Flow Hijacks](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Launches Dots, Always-On AI Agents](https://openai.com/index/introducing-dots/) ⭐️ 8.0/10

OpenAI announced Dots at DevDay 2026 on September 29, 2026 — always-on AI agents powered by GPT-6 Astra, each running on its own cloud computer and browser to autonomously complete long workflows. One Dot is included with Pro and Business Premium plans, and the agents can access over 4,000 apps through plugins. Dots marks OpenAI's push into consumer always-on agents, arriving just weeks after Meta released its competing Muse agent, and it signals a strategic shift from chat-based assistants toward persistent cloud-based agents that could reshape how people use computers. The launch intensifies competition in the AI agent market and raises concerns about platform lock-in, since deep integrations and accumulated work history make switching providers much harder than swapping models. Each Dot gets its own cloud computer and browser, and the product is powered by GPT-6 Astra with plugin access to more than 4,000 apps; one Dot is bundled with Pro and Business Premium subscriptions. The launch also comes amid scrutiny over safety incidents involving OpenAI's technology, and observers note that always-on agents raise security issues previously seen in open-source projects like OpenClaw and Meta's Muse.

hackernews · alvis · Sep 29, 17:07 · [Discussion](https://news.ycombinator.com/item?id=49896604)

**Background**: Always-on agents are AI systems that run continuously in the cloud rather than only responding when a user types a prompt, allowing them to execute multi-step tasks autonomously over long periods. OpenAI had demonstrated agent API capabilities as early as DevDay 2024 and released consumer agent products in 2025, but its agent offerings have lagged behind competitors; Meta's Muse, released weeks before Dots, is considered its primary rival in agentic AI. Platform lock-in refers to the difficulty and cost of switching providers once a service becomes deeply embedded in a user's workflows and data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oflight.co.jp/en/columns/openai-dots-always-on-personal-agent-2026">OpenAI dots Explained: Always - On Agent , Safety, Pricing | Oflight Inc.</a></li>
<li><a href="https://www.datacamp.com/blog/openai-dots">OpenAI Dots : Always - On Agents in ChatGPT, Explained | DataCamp</a></li>
<li><a href="https://www.nytimes.com/2026/09/29/technology/openai-dots-ai-agents.html">OpenAI Unveils Dots, New A.I. Agents to Rival Meta’s Muse - The New York Times</a></li>

</ul>
</details>

**Discussion**: Commenters debated platform lock-in, with one arguing that always-on agents tie users deeply to a provider because integrations and work history make them effectively "your computer on the cloud," and another suspecting closed-model companies want an abstraction layer to limit model access. Others questioned the blurry distinctions between Codex, ChatGPT Work, and Dots, with some more bullish on Meta's Muse as a consumer play, while one commenter predicted always-on agents mark the end of the PC era and are aimed at non-technical users and future AI natives rather than today's tech-savvy crowd.

**Tags**: `#OpenAI`, `#AI agents`, `#product launch`, `#platform lock-in`, `#Hacker News`

---

<a id="item-2"></a>
## [Delhi Slashes Electricity Losses from 50% to 5%](https://spectrum.ieee.org/delhi-electricity-loss) ⭐️ 8.0/10

An IEEE Spectrum article details how Delhi reduced its electricity losses from roughly 50% to about 5%, a dramatic turnaround for a major city grid. The achievement is being widely discussed online, with readers highlighting the near-elimination of load shedding and the role of privatization and anti-theft measures. Delhi's success shows that even severe grid inefficiency and rampant electricity theft can be reversed, offering a replicable model for other Indian states and developing cities. It also directly improves residents' quality of life by ending frequent, damaging power cuts and surges. The reduction was driven largely by curbing non-technical losses such as theft, which was rampant among businesses, residents, and even utility employees, rather than by purely technical upgrades. Insulating neighborhood power lines to prevent illegal hookups had the unintended side effect of giving monkeys safe 'roads' between neighborhoods.

hackernews · rbanffy · Sep 29, 12:43 · [Discussion](https://news.ycombinator.com/item?id=49892245)

**Background**: In India, electricity distribution losses are measured as AT&C (Aggregated Technical and Commercial) losses, combining physical transmission losses with billing and collection shortfalls. Delhi privatized its distribution companies (DISCOMs) in 2002 in a politically risky move intended to insulate the sector from political interference and improve efficiency. Nationwide reform programs like UDAY and RDSS have also helped lower losses across India over the past two decades.

<details><summary>References</summary>
<ul>
<li><a href="https://energy.economictimes.indiatimes.com/news/power/power-distribution-privatisation-the-why-comes-first-the-how-comes-later/120918651">Power distribution privatisation : The why comes first, the how comes...</a></li>
<li><a href="https://powerline.net.in/2021/09/23/a-success-story/">A Success Story: How distribution privatisation turned the national...</a></li>
<li><a href="https://globechart.com/energy/electricity-grid-losses/">Electricity Grid Losses | T&D Losses Around the World - GlobeChart</a></li>

</ul>
</details>

**Discussion**: Commenters with firsthand experience emphasized that eliminating load shedding was the truly revolutionary change, recalling days when power cuts and surges forced people to unplug appliances. Others noted unintended consequences like monkeys using insulated lines as highways, and proposed aggressive solar, battery, and rooftop adoption as India's next energy step.

**Tags**: `#energy`, `#infrastructure`, `#india`, `#policy`, `#hackernews`

---

<a id="item-3"></a>
## [OpenAI launches GPT-6.1 Sol, a cheaper near-Astra model](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI announced GPT-6.1 Sol, an upgrade to GPT-6 Sol positioned just below the flagship GPT-6 Astra, priced at $2 per million input tokens, $0.10 per million cached input tokens, and $10 per million output tokens. It is available through the OpenAI API as gpt-6.1-sol and is not yet available in ChatGPT. The release intensifies price competition among frontier AI labs, with cached input pricing 50% below GPT-6 Sol's and 95% below standard input pricing, directly challenging cheaper rivals like DeepSeek and pressuring Anthropic. It signals that token cost, not just raw capability, is becoming the main battleground for developer adoption. OpenAI automatically caches prompts of 1024 tokens or more, and GPT-6.1 Sol bills a cache write on each cached prompt whether or not the cached prefix is read again. On Devin's leaderboard, at low effort it scores 58.1% for $0.21 per task, up from 50.5% for GPT-6 Sol at the same setting, the highest score of any model under $0.30 per task.

hackernews · crorella · Sep 29, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49896586)

**Background**: OpenAI's GPT-6 series includes the flagship GPT-6 Astra, which tops benchmarks like FrontierMath and ARC-AGI-3 and has a 1M-token context window, and the mid-tier Sol line. DeepSeek is a Chinese AI company known for open-weight models such as DeepSeek-V3, a 671B-parameter Mixture-of-Experts model, that compete largely on low pricing. Anthropic's Opus models are OpenAI's other main frontier rival.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6.1-sol">GPT - 6 . 1 Sol - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://devin.ai/blog/gpt-6-1-sol">GPT - 6 . 1 Sol is now available in Devin | Devin</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical: some said they now default to DeepSeek for its far lower cost and negligible intelligence gap, while others reported that GPT-6 Sol and Luna were regressions from Sol 5.6 and that they had switched to Opus 5.5. Several highlighted the 50% cheaper cache pricing as the real headline, and one noted that token price becoming the main battleground is ominous for the industry and investors.

**Tags**: `#OpenAI`, `#LLM`, `#AI pricing`, `#model release`, `#AI competition`

---

<a id="item-4"></a>
## [Anthropic: New AI Models Achieve Full Control Flow Hijacks](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 8.0/10

Anthropic's Frontier Red Team evaluated several models on 100 randomly selected tasks from its internal Binary Exploitation benchmark and found that GLM-5.3 achieved full control flow hijacks in 4% of trials, while Claude Mythos Preview did so in 6%. Earlier models such as Claude Opus 4.6 and GLM-5.2 failed to succeed in any of the trials. This marks a meaningful threshold crossing in AI cyber capabilities, as models can now autonomously perform a class of exploitation that previously defeated them entirely. It raises concerns about the spread of advanced offensive cyber techniques, especially since GLM-5.3 is an open-weights model from China, potentially lowering barriers for malicious actors. The evaluation used 100 randomly selected tasks from an internal Binary Exploitation benchmark, and success rates remain low (4% and 6%), indicating the capability is emerging rather than mature. GLM-5.3 is Z.ai's latest flagship model, built on the same base model as GLM-5.2 with improvements driven entirely by post-training, and it is notable as an open-weights model.

rss · Simon Willison · Sep 29, 22:20

**Background**: Binary exploitation involves finding and leveraging memory corruption bugs in compiled software to hijack a program's control flow and execute attacker-chosen code. A full control flow hijack means the attacker gains complete control over the instruction pointer, often using techniques like return-oriented programming (ROP) to bypass modern defenses. Anthropic's Frontier Red Team stress-tests AI systems to assess their cybersecurity and national security implications, and this benchmark measures whether models can autonomously perform such exploits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/team/frontier-red-team">Frontier Red Team Research \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Return-oriented_programming">Return-oriented programming - Wikipedia</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.3">zai-org/ GLM - 5 . 3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#cyber capabilities`, `#binary exploitation`, `#Anthropic`, `#AI research`

---