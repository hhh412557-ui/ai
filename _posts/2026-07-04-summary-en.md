---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 75 items, 5 important content pieces were selected

---

1. [Elevated CO2 in Rooms Impairs Decision-Making](#item-1) ⭐️ 8.0/10
2. [Mistral Releases Leanstral 1.5 for Lean 4 Theorem Proving](#item-2) ⭐️ 8.0/10
3. [SearXNG: A Free, Privacy-Focused Metasearch Engine](#item-3) ⭐️ 8.0/10
4. [Open Source AI Gap Map Launched](#item-4) ⭐️ 8.0/10
5. [Josh W. Comeau reports 50%+ sales drop due to AI](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Elevated CO2 in Rooms Impairs Decision-Making](https://blog.mikebowler.ca/2026/07/03/co2-and-decision-making/) ⭐️ 8.0/10

A blog post argues that elevated CO2 levels in indoor spaces impair decision-making, sparking discussion about awareness, scientific validity, and potential tech solutions like CO2 monitors in wearables. This matters because poor indoor air quality is a widespread but often overlooked issue that could be silently reducing productivity and cognitive performance in offices, schools, and homes. Integrating CO2 sensors into consumer devices could raise awareness and drive behavioral changes to improve ventilation. The post references CO2 levels reaching 2000 ppm in classrooms, while some commenters note that submarines operate at thousands of ppm without apparent ill effects, citing a study finding no deficits even at 15,000 ppm. This highlights ongoing debate about the threshold at which CO2 becomes cognitively harmful.

hackernews · gslin · Jul 4, 06:32 · [Discussion](https://news.ycombinator.com/item?id=48783117)

**Background**: Carbon dioxide (CO2) is a colorless, odorless gas produced by human respiration. In indoor spaces with poor ventilation, CO2 can accumulate to levels that may affect cognitive function. While high concentrations are known to cause drowsiness and headaches, the exact impact on decision-making at moderate levels is still debated.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Carbon_dioxide">Carbon dioxide - Wikipedia</a></li>
<li><a href="https://www.ourmental.health/mind-body-connection/how-air-quality-affects-your-brain-the-cognitive-impact-of-indoor-pollution">Air Quality and Cognitive Function : The Brain-Air Connection Explained</a></li>
<li><a href="https://www.co2meter.com/blogs/news/co2-sensor-nasa-wearable-co2-monitor">NASA Wearable CO 2 Monitor uses CozIR Sensor – CO 2 Meter</a></li>

</ul>
</details>

**Discussion**: The community is divided: some advocate for integrating CO2 monitors into wearables to raise awareness, while others question the scientific basis, citing submarine studies showing no cognitive deficits at high CO2 levels. A teacher's anecdote about 2000 ppm in classrooms adds real-world weight to the concern.

**Tags**: `#CO2 monitoring`, `#indoor air quality`, `#productivity`, `#health`, `#technology`

---

<a id="item-2"></a>
## [Mistral Releases Leanstral 1.5 for Lean 4 Theorem Proving](https://mistral.ai/news/leanstral-1-5/) ⭐️ 8.0/10

Mistral AI has released Leanstral 1.5, a 119B total parameter model (6.5B active) specialized for Lean 4 theorem proving, achieving state-of-the-art results on the ProofNet benchmark. This model makes formal verification more accessible by delivering high performance in a relatively small, efficient model, potentially accelerating the adoption of formal methods in software verification and mathematics. Leanstral 1.5 is a Mixture of Experts (MoE) model with 119B total parameters but only 6.5B active per token, and is released under the Apache-2.0 license. It supports a 256k context window and is optimized for automated theorem proving and autoformalization.

hackernews · programLyrique · Jul 3, 22:33 · [Discussion](https://news.ycombinator.com/item?id=48780801)

**Background**: Lean 4 is a proof assistant and programming language for formal verification, allowing users to write and verify mathematical proofs and software correctness. The ProofNet benchmark consists of undergraduate-level mathematical theorems for evaluating autoformalization and formal proving capabilities. Leanstral 1.5 builds on Mistral's expertise in efficient language models to bring state-of-the-art performance to this specialized domain.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/leanstral-1-5/">Leanstral 1.5: Proof Abundance for All</a></li>
<li><a href="https://docs.mistral.ai/models/model-cards/leanstral-1-5">Leanstral 1.5 - Mistral AI | Mistral Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's practical utility for specific tasks like OCR and file analysis, with one user noting the cost-effectiveness of Mistral's small models. Some criticism points to the benchmark comparisons being outdated, while others question the novelty of the bug-finding example. There is also interest from users without prior Lean knowledge about the model's usability.

**Tags**: `#AI`, `#theorem proving`, `#Lean`, `#Mistral`, `#formal verification`

---

<a id="item-3"></a>
## [SearXNG: A Free, Privacy-Focused Metasearch Engine](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG is a free, open-source metasearch engine that aggregates results from multiple search engines without tracking or profiling users. It is a community-maintained fork of the original Searx project, which is no longer actively developed. SearXNG provides a privacy-respecting alternative to mainstream search engines, allowing users to avoid tracking and data collection. It is widely used by privacy-conscious individuals and developers, and can be self-hosted for full control. SearXNG supports multiple backends including Google, DuckDuckGo, Bing, and Wikipedia, and offers features like JSON output for integration with other applications. Users can choose from over 70 public instances or host their own via Docker.

hackernews · theanonymousone · Jul 3, 20:15 · [Discussion](https://news.ycombinator.com/item?id=48779454)

**Background**: A metasearch engine does not crawl the web itself; instead, it sends user queries to multiple search engines and combines their results. This approach can improve privacy by distributing queries across providers, but may be slower and sometimes trigger CAPTCHAs from upstream engines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG - Wikipedia</a></li>
<li><a href="https://github.com/searxng/searxng">GitHub - searxng/searxng: SearXNG is a free internet metasearch engine which aggregates results from various search services and databases. Users are neither tracked nor profiled. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metasearch_engine">Metasearch engine</a></li>

</ul>
</details>

**Discussion**: The original Searx creator noted the limitations of the metasearch concept and has moved on to a new project called Hister. Users reported that SearXNG works well but can be slower than direct search, and some public instances may be blocked by the GFW or rate-limited by providers like DuckDuckGo.

**Tags**: `#search engine`, `#privacy`, `#open source`, `#metasearch`, `#self-hosted`

---

<a id="item-4"></a>
## [Open Source AI Gap Map Launched](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit backed by $400 million, launched the Open Source AI Gap Map v0.1, indexing 421 products across the open source AI stack to identify gaps and guide development. This comprehensive mapping provides a public resource for the AI community to understand the open source ecosystem, highlight underdeveloped areas, and prioritize investments, potentially accelerating innovation and reducing duplication. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three stack layers: model components, product/UX, and infrastructure.

rss · Simon Willison · Jul 3, 22:04

**Background**: Open source AI includes publicly available models, datasets, and tools that anyone can use, modify, and distribute. The AI stack typically consists of multiple layers such as hardware, infrastructure, models, and applications. Current AI is a global non-profit partnership founded at the AI Action Summit in Paris in February 2025, with $400 million committed to building a public option for AI.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>

</ul>
</details>

**Tags**: `#open source AI`, `#ecosystem mapping`, `#AI infrastructure`, `#non-profit initiative`

---

<a id="item-5"></a>
## [Josh W. Comeau reports 50%+ sales drop due to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau, a prominent web development educator, reported that sales of his online courses have dropped by over 50%, with his latest launch on track to sell only a third of typical numbers, attributing the decline to AI. This signals a major disruption in the developer education market, as learners question job security and turn to LLMs for free personalized tutoring, threatening the business model of paid courses. Comeau's third course, Whimsical Animations, is on track to sell roughly one-third of a typical launch, and multiple other course creators report similar revenue declines of 50% or more.

rss · Simon Willison · Jul 3, 21:25

**Background**: Josh W. Comeau is a well-known front-end developer educator whose courses on CSS and animations are highly regarded. LLMs (Large Language Models) like ChatGPT can act as personalized tutors, providing step-by-step explanations and adapting to individual needs, which reduces the incentive to buy structured courses.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/age-of-awareness/ai-in-education-personalized-learning-with-llms-57405e34446a">AI in Education: Personalized Learning with LLMs | Medium</a></li>
<li><a href="https://www.brevitytechnology.ca/llms-in-education-personalized-learning-and-teaching/">LLMs in Education: Personalized Learning and Teaching - Brevity...</a></li>
<li><a href="https://whimsy.joshwcomeau.com/">Whimsical Animations , a new course from Josh W. Comeau</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer education`, `#online courses`, `#industry trends`

---