---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 37 items, 4 important content pieces were selected

---

1. [EU Parliament Spyware Investigator Hacked with Pegasus](#item-1) ⭐️ 9.0/10
2. [AMD MI355X Runs GLM5.2 at 2626 tok/s, Over 2x Lower Cost Than Blackwell](#item-2) ⭐️ 8.0/10
3. [SearXNG: A Free Privacy-Respecting Metasearch Engine](#item-3) ⭐️ 8.0/10
4. [Current AI Launches Open Source AI Gap Map](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Spyware Investigator Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 9.0/10

Citizen Lab discovered that a member of the European Parliament committee investigating spyware was successfully infected with Pegasus spyware on at least three occasions between October 2022 and March 2023. This breach directly targets the EU's oversight of spyware, suggesting a state actor with cross-European authorization is undermining democratic institutions and privacy protections. The infections overlapped with a Pegasus campaign targeting Russian and Belarusian exiled journalists in Europe, indicating a single Pegasus customer with authorization to spy in multiple European countries.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by Israeli firm NSO Group, capable of remotely compromising mobile devices via zero-click exploits. Citizen Lab is a University of Toronto research group that investigates digital threats to human rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony of an EU parliament member being spied on by the same spyware they were investigating, and some pointed to past Pegasus scandals in Greece and Italy, suggesting state involvement.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-2"></a>
## [AMD MI355X Runs GLM5.2 at 2626 tok/s, Over 2x Lower Cost Than Blackwell](https://www.wafer.ai/blog/glm52-amd) ⭐️ 8.0/10

AMD's MI355X GPU achieves 2626 tokens per second per node for the GLM5.2 model, delivering over 2x lower cost compared to Nvidia's Blackwell architecture. This demonstrates AMD's growing competitiveness in AI inference, offering a cost-effective alternative to Nvidia for large-scale deployments, especially in regions where Nvidia hardware is hard to source. The benchmark uses FP4 quantization, which community members note may cause noticeable accuracy degradation compared to FP8. The MI355X features 288GB HBM3E memory and 8TB/s bandwidth, with native support for MXFP6 and MXFP4 datatypes.

hackernews · latchkey · Jul 3, 21:49 · [Discussion](https://news.ycombinator.com/item?id=48780417)

**Background**: GLM5.2 is a flagship open-source large language model from Z.ai with a 1M-token context window, designed for long-horizon tasks. FP4 quantization reduces model precision to 4-bit floating point, trading some accuracy for higher throughput and lower memory usage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html">AMD Instinct™ MI355X GPUs</a></li>
<li><a href="https://build.nvidia.com/z-ai/glm-5.2/modelcard">glm-5.2 Model by Z-ai | NVIDIA NIM</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/amd-instinct-mi355x-gpu-sets-a-new-bar-for-deepseek-inference.html">AMD Instinct MI355X GPU Sets a New Bar for DeepSeek Inference</a></li>

</ul>
</details>

**Discussion**: Community members expressed concerns about FP4 quantization causing accuracy degradation, with one noting 'noticeable accuracy degradation when switching from fp8 to mxfp4'. Others requested performance-per-watt metrics and suggested that quantization type should be mandatory in headlines.

**Tags**: `#AMD`, `#inference`, `#GPU`, `#quantization`, `#cost comparison`

---

<a id="item-3"></a>
## [SearXNG: A Free Privacy-Respecting Metasearch Engine](https://github.com/searxng/searxng) ⭐️ 8.0/10

SearXNG, a free and open-source metasearch engine that aggregates results from up to 280 search services without tracking users, continues to gain traction in the community, especially for use with local AI models and RAG applications. As privacy concerns grow and users seek alternatives to centralized search engines, SearXNG offers a self-hosted, privacy-respecting solution that also serves as a key tool for providing search capabilities to local AI models and retrieval-augmented generation (RAG) systems. SearXNG supports JSON output, making it suitable for integration with RAG pipelines, and can be used over Tor for anonymity. However, users report that scraping-based backends like DuckDuckGo may require CAPTCHA solving, and Google scraping recently stopped working.

hackernews · theanonymousone · Jul 3, 20:15 · [Discussion](https://news.ycombinator.com/item?id=48779454)

**Background**: A metasearch engine aggregates results from multiple search engines without maintaining its own index. SearXNG is a fork of the now-discontinued Searx, and is server-side software that can be self-hosted or accessed via public instances. Retrieval-augmented generation (RAG) is a technique that enhances large language models by retrieving relevant information from external sources before generating a response.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG - Wikipedia</a></li>
<li><a href="https://docs.searxng.org/">SearXNG Documentation (2026.7.3+9d7ca4feb)</a></li>
<li><a href="https://github.com/searxng/searxng">GitHub - searxng/searxng: SearXNG is a free internet ... SearXNG @ searx.tiekoetter.com SearXNG - Wikipedia searxng/searxng | DeepWiki How to use SearXNG: Installation and Private Use Guide SearXNG: The Open Source Metasearch Engine That Protects You</a></li>

</ul>
</details>

**Discussion**: The original creator of Searx noted the limitations of the metasearch concept and pointed to his new project, Hister, a full-text indexer. Users shared practical experiences: one has used SearXNG daily for over 5 years with Yacy backends and built RAG applications, while others highlighted TinySearch as a wrapper that optimizes context for AI agents. Some expressed concerns about reliability when scraping search engines.

**Tags**: `#search engine`, `#privacy`, `#open source`, `#metasearch`, `#RAG`

---

<a id="item-4"></a>
## [Current AI Launches Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, which indexes 421 open source AI products across software, models, datasets, and hardware, along with 24,400 uncategorized artifacts. This map provides a structured, comprehensive view of the open source AI ecosystem, helping developers, researchers, and policymakers identify gaps and opportunities. The underlying data is released under an MIT license, enabling further analysis and community contributions. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across 3 stack layers. The data is available as 1,184 YAML files on GitHub, and can be explored via Datasette Lite.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership backed by $400 million in committed capital, aiming to build a public option for AI. The Open Source AI Gap Map is an attempt to systematically index the open source AI landscape, similar to how other ecosystem maps track commercial AI offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/jul/3/open-source-ai-gap-map/">Open Source AI Gap Map | Simon Willison’s Weblog</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`

---