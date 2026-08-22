---
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 32 items, 5 important content pieces were selected

---

1. [SGLang v0.5.18: 710 PRs, New Diffusion Models, Faster Startup](#item-1) ⭐️ 8.0/10
2. [Scientists Release Largest 2D Map of the Universe](#item-2) ⭐️ 8.0/10
3. [Researcher Accidentally Hijacks e164.arpa, Logs Military Calls](#item-3) ⭐️ 8.0/10
4. [Are Open Models Catching Up to Closed Frontier Models?](#item-4) ⭐️ 8.0/10
5. [Robotics GPT-3 Moment: Learn Tasks from Single Demo, Backed by Huang and Li](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.18: 710 PRs, New Diffusion Models, Faster Startup](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 8.0/10

SGLang v0.5.18 has been released, incorporating 710 pull requests from 212 contributors. This release adds support for several new models, including diffusion models like SANA-Video and LTX-2.5, and introduces performance optimizations such as overlapped checkpoint staging and a unified kernel cache directory. This release significantly expands SGLang's model coverage to include diffusion models, making it a more versatile inference engine for the AI community. The performance improvements, such as faster startup and reduced decode latency, directly benefit users running large models in production, enhancing overall serving efficiency. Notable optimizations include overlapped checkpoint staging that speeds up Qwen3-32B startup by up to 2.38x, and a TP LMHead with all-to-all that reduces LMHead time on DeepSeek-V4-Pro from 320us to 169us. The release also unifies all compiled-kernel caches under SGLANG_CACHE_DIR, requiring a one-time recompilation after upgrade.

github · Fridge003 · Aug 22, 00:09

**Background**: SGLang is a high-performance serving framework for large language models and multimodal models, known for its fast inference capabilities. Diffusion models, which generate images or videos by iteratively denoising, are now supported, broadening SGLang's applicability beyond autoregressive models. The release also updates dependencies like torch 2.13.0 and flashinfer 0.6.17.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang/releases">Releases · sgl-project/ sglang</a></li>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device | Meta AI Research</a></li>
<li><a href="https://arxiv.org/html/2509.24695v1">SANA - Video : Efficient Video Generation with Block Linear Diffusion ...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#SGLang`, `#release`, `#AI infrastructure`, `#diffusion models`

---

<a id="item-2"></a>
## [Scientists Release Largest 2D Map of the Universe](https://newscenter.lbl.gov/2026/08/10/scientists-release-biggest-2d-map-of-the-universe/) ⭐️ 8.0/10

Scientists have released the largest 2D map of the universe, a comprehensive survey that is expected to remain the most detailed for years. The map is accessible via the Legacy Survey Sky Viewer, which contains over 5.6 trillion pixels. This map is a significant resource for astronomy and cosmology, likely to influence future research and observations. It provides an unprecedented detailed view of the universe, enabling scientists to study galaxy distribution, dark energy, and other cosmic phenomena. The map is based on data from the Dark Energy Spectroscopic Instrument (DESI) Legacy Surveys, which includes observations from multiple telescopes. The Legacy Survey Sky Viewer allows users to click on any point of light to access its catalog entry, aiding professional researchers in planning observations.

hackernews · NKosmatos · Aug 21, 18:36 · [Discussion](https://news.ycombinator.com/item?id=49392200)

**Background**: The universe is vast, and mapping it in two dimensions involves capturing the positions and brightness of celestial objects across the sky. The DESI Legacy Surveys combine data from telescopes like the Mayall 4-meter telescope and the Blanco 4-meter telescope to create a comprehensive atlas. This map is a follow-up to earlier surveys and is expected to be a benchmark for future astronomical research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_Energy_Spectroscopic_Instrument">Dark Energy Spectroscopic Instrument - Wikipedia</a></li>
<li><a href="https://viewer.legacysurvey.org/">Legacy Survey Sky Browser</a></li>
<li><a href="https://www.techtimes.com/articles/323891/20260811/desi-legacy-surveys-releases-56-trillion-pixel-universe-atlas-rubin-roman-benefit.htm">DESI Legacy Surveys Releases 5.6-Trillion-Pixel Universe Atlas...</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of awe and humor, with some users expressing skepticism about future investment in astronomy due to economic and geopolitical concerns. Others joked about the universe being a simulation or a brick wall, while some marveled at the map's detail and the humbling realization that more galaxies appear the closer we look.

**Tags**: `#astronomy`, `#cosmology`, `#data release`, `#scientific research`, `#universe mapping`

---

<a id="item-3"></a>
## [Researcher Accidentally Hijacks e164.arpa, Logs Military Calls](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

A security researcher accidentally hijacked ENUM queries to the e164.arpa DNS zone, logging hundreds of thousands of phone calls, including those to military bases. The incident exposed a critical flaw in the largely forgotten telephony infrastructure. This highlights a significant security vulnerability in a legacy telephony system that is still in use, potentially allowing unauthorized interception of call routing data. It underscores the need for better oversight and security measures for critical but neglected internet infrastructure. The researcher did not set up a SIP server to see if calls could be terminated, but the scale of the log (hundreds of thousands) indicates widespread use. The issue was only addressed after military involvement was discovered, and the researcher was not rewarded.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: ENUM (E.164 Number Mapping) is a protocol that uses DNS to map telephone numbers to internet addresses, facilitating VoIP and PSTN interconnection. The e164.arpa domain is reserved for this purpose, but it has seen limited public adoption and is now mostly used via private services over VPNs. The .arpa TLD is managed by IANA for technical infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/E.164">E.164 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/.arpa">.arpa - Wikipedia</a></li>
<li><a href="https://netnumber.com/what-is-enum/">What Is ENUM ? E.164 Number Mapping Explained | netnumber</a></li>

</ul>
</details>

**Discussion**: Commenters expressed amazement that the researcher wasn't jailed, noting that such reporting often leads to legal trouble. Some suggested the researcher should have set up a SIP server to test call termination, while others appreciated the story as an example of infrastructure falling through the cracks. There was also interest in the fact that private ENUM services exist and are used for number porting.

**Tags**: `#security`, `#telephony`, `#ENUM`, `#DNS`, `#infrastructure`

---

<a id="item-4"></a>
## [Are Open Models Catching Up to Closed Frontier Models?](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 8.0/10

SemiAnalysis published an analysis comparing open-source and closed-source AI models across different generations of frontier models, examining whether open models are closing the performance gap. This analysis is significant because the open vs. closed model debate affects developers, enterprises, and researchers who must choose between cost, control, and performance. Understanding the trajectory of open models informs strategic decisions in AI adoption and investment. The analysis likely covers multiple generations of frontier models, comparing capabilities such as reasoning, tool use, and long-context handling. It may reference specific models like GPT-4o and Claude Opus as closed examples, and DeepSeek R1 or Llama as open examples, based on recent benchmarks.

rss · Semianalysis · Aug 21, 16:40

**Background**: Frontier models are the largest, most capable AI systems like GPT-4o and Claude Opus, typically running on cloud infrastructure. Open-source models are publicly available with weights, allowing customization and local deployment, while closed models are proprietary and accessed via APIs. The gap between them has been a key topic, with recent open models like DeepSeek R1 showing competitive performance in reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ability.ai/blog/frontier-models-transition-local-slm">Frontier Models : How to Transition to Local SLMs for Agen... | Ability. ai</a></li>
<li><a href="https://letsdatascience.com/blog/open-source-vs-closed-llms-choosing-the-right-model-in-2026">Open Source vs Closed LLMs: The 2026 Decision Framework</a></li>
<li><a href="https://future-ainews.com/article/open-source-vs-closed-2026">Open-Source vs. Closed Models: The 2026 Benchmark Report</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#closed models`, `#frontier models`, `#model comparison`

---

<a id="item-5"></a>
## [Robotics GPT-3 Moment: Learn Tasks from Single Demo, Backed by Huang and Li](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652719368&idx=1&sn=d5a0a68f04d7e09d9cabe5c4950db88e) ⭐️ 8.0/10

A new embodied AI model for robotics claims a GPT-3-like breakthrough, learning new tasks from a single 3-12 second demonstration without any training or fine-tuning. The project has attracted investment from prominent figures including Jensen Huang and Fei-Fei Li. This advancement could significantly accelerate the deployment of robots in dynamic, unstructured environments by eliminating the need for extensive task-specific data collection and training. It represents a potential paradigm shift in embodied AI, moving toward more general-purpose robots that can adapt quickly, which may impact industries from manufacturing to healthcare. The model reportedly learns from a single demonstration of 3-12 seconds, without training or fine-tuning, and can execute the task within seconds. The article highlights that 'the model determines the upper limit, and data determines whether that limit can be reached,' emphasizing the importance of data quality and diversity. However, specific technical details about the model architecture or training methodology are not provided in the article.

rss · 新智元 · Aug 21, 08:09

**Background**: Embodied AI refers to AI systems integrated into physical entities, such as robots, that can interact with the physical world. Few-shot learning in robotics aims to enable robots to learn new tasks from a small number of examples, which is crucial for operating in dynamic environments. The 'GPT-3 moment' metaphor draws a parallel to the impact of GPT-3 in natural language processing, where large-scale models demonstrated remarkable few-shot capabilities, suggesting a similar leap in robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://arxiv.org/abs/2112.02849">[2112.02849] DemoGrasp: Few-Shot Learning for Robotic Grasping with Human Demonstration</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#AI`, `#embodied intelligence`, `#few-shot learning`, `#investment`

---