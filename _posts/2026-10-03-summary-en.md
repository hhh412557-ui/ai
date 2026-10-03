---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 14 items, 2 important content pieces were selected

---

1. [AI Finally Beats Top Stratego Players on a Budget](#item-1) ⭐️ 9.0/10
2. [Redis creator antirez releases ds4 for local LLM inference](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI Finally Beats Top Stratego Players on a Budget](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10

Researchers have published a new algorithm, detailed in a Nature paper and an arXiv preprint (2511.07312), that defeats the best human Stratego players while training on roughly 34 times fewer games than DeepMind's DeepNash. The method achieves stronger play despite Stratego's hidden-information nature, which had stumped AI for decades. This marks a major advance in AI for imperfect-information games, a class that includes poker, negotiation, and real-world strategic decision-making where key information is hidden. The dramatic efficiency gain suggests these problems may be tractable with far less compute than previously assumed, potentially lowering barriers for research and applications. The algorithm reportedly played about 34 times fewer games than DeepMind's DeepNash yet ended up much stronger, according to community discussion. Stratego's hidden information means the best move depends on information the player does not have, making lookahead search fundamentally difficult.

hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

**Background**: Stratego is a two-player board game launched in 1946 in which each player's pieces are hidden from the opponent, so players must infer the identities of enemy pieces through play. In AI, such games are called imperfect-information games, as opposed to perfect-information games like chess and Go where all pieces are visible. DeepMind's DeepNash, introduced in 2022, was a major prior effort to master Stratego using reinforcement learning and search.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stratego">Stratego - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2007.13544">Combining Deep Reinforcement Learning and Search for Imperfect ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the efficiency gain—34 times fewer games than DeepNash—as the critical piece that makes the AI work at all, since hidden information makes lookahead search impossible. Some expressed surprise that Stratego, which feels simple, had stumped AI, and one noted childhood memories of subtly marked pieces as an unfair way to reveal hidden information.

**Tags**: `#AI`, `#game-playing`, `#imperfect-information`, `#reinforcement-learning`, `#Stratego`

---

<a id="item-2"></a>
## [Redis creator antirez releases ds4 for local LLM inference](https://dwarfstar.sh/) ⭐️ 8.0/10

Salvatore Sanfilippo, known online as antirez and best known as the creator of Redis, has released ds4 (DwarfStar 4), a narrow C inference engine for running frontier open-weight large language models locally on high-memory Mac, CUDA, and ROCm machines. The project supports DeepSeek V4 and V4.1 Flash, GLM 5.x, and Qwen3.8 Flash Next, including text and vision models, with local APIs. The release matters because it comes from a highly respected systems programmer and offers a lightweight way to run very large open-weight models on local hardware, reducing reliance on cloud inference. It also signals that local inference for frontier-scale models is becoming practical for users with high-end workstations and Apple Silicon machines. ds4-agent runs inference directly without a separate HTTP server, keeps token history and live model state together, shows prefill progress, and uses each model's native tool format, with dedicated templates for DeepSeek and GLM. The engine is deliberately narrow and optimized for specific model families, which limits flexibility for users who want to run arbitrary models on the same platform.

hackernews · fibo · Oct 2, 18:01 · [Discussion](https://news.ycombinator.com/item?id=49936575)

**Background**: antirez is an Italian programmer best known for creating Redis, the widely used in-memory data store. In recent years he has written publicly about using LLMs for coding, and ds4 is his entry into local inference engines. Running large language models locally means executing the model on your own hardware instead of sending prompts to a cloud API, which can improve privacy, latency, and cost control but requires substantial memory and compute.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez / ds 4 : DeepSeek 4 Flash and PRO local inference ...</a></li>
<li><a href="https://dwarfstar.sh/">DwarfStar 4 ( ds 4 ): Local DeepSeek V4.1, Qwen and GLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Salvatore_Sanfilippo">Salvatore Sanfilippo - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely positive: one user maintains a fork of ds4 as shared libraries with FFI bindings and Go support (ds4go), and another says ds4 has been the best launcher on their M5 Max 128GB, running Qwen 3.8 Flash for over a week with fast performance and long context. Others shared related projects, including an Intel Xe-LP inference engine inspired by DwarfStar and a TestFlight beta of Local Code for high-end Apple Silicon, while one user noted occasional model forgetfulness that might stem from the agentic harness rather than ds4 itself.

**Tags**: `#LLM`, `#local inference`, `#Redis`, `#antirez`, `#Hacker News`

---