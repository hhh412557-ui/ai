---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 32 items, 3 important content pieces were selected

---

1. [Anthropic Releases Claude Fable 5.2 and Mythos 5.2](#item-1) ⭐️ 8.0/10
2. [Infineon produces first functional power devices on 300mm SiC wafers](#item-2) ⭐️ 8.0/10
3. [Show HN: Browser tool maps every satellite pass over any location](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 8.0/10

Anthropic released Claude Fable 5.2 and Claude Mythos 5.2, the latest versions of its Mythos-class models, with Fable 5.2 available for general use and Mythos 5.2 restricted to vetted partners. The release prompted extensive discussion on Hacker News, where users reported concrete results such as a 36x speedup on a 600k-line Fortran codebase and raised questions about benchmark methodology. This release matters because it shows Anthropic iterating rapidly on its most capable model line while maintaining a two-tier access strategy that balances capability with safety safeguards. The reported real-world coding gains and long-horizon agentic performance could affect developers and enterprises choosing models for complex software engineering tasks. Fable 5.2 and Mythos 5.2 share the same underlying model, but Fable 5.2 includes classifiers that redirect flagged requests on cybersecurity, biology/chemistry, and model distillation to the less capable Claude Opus. Community members noted that Fable 5.2 can consume a 5-hour token budget in half an hour during intensive code review, and some questioned why Anthropic compared different models on different benchmarks.

hackernews · lairv · Nov 9, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50429068)

**Background**: Claude Mythos is Anthropic's most advanced model series, first previewed as Claude Mythos Preview and initially withheld from public release due to its ability to find software vulnerabilities. In June 2026, Anthropic released Claude Fable 5 as a safeguarded, generally available version of the same underlying model, alongside Claude Mythos 5 for restricted access. Fable 5.1 and Mythos 5.1 followed in September 2026, and industry estimates put the Mythos model at approximately 8 trillion parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-2">Introducing Claude Fable 5 . 2 and Claude Mythos 5 . 2 \ Anthropic</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was largely positive but critical: one user reported a 36x speedup on a 600k-line Fortran codebase and open-sourced the results, while another found 7 serious bugs in a code review but noted the model burned through a 5-hour token budget in 30 minutes. Others questioned benchmark fairness, asking why Anthropic stacked Fable xHigh against Carbon Med and omitted Carbon from a cyber benchmark, and speculated about a release cadence mirroring OpenAI.

**Tags**: `#AI/ML`, `#LLM`, `#Anthropic`, `#model-release`, `#benchmarking`

---

<a id="item-2"></a>
## [Infineon produces first functional power devices on 300mm SiC wafers](https://www.infineon.com/press-release/2026/infpr202611-028) ⭐️ 8.0/10

Infineon announced on November 9, 2026, that it has fabricated the industry's first functional power devices on 300-millimeter silicon carbide (SiC) wafers, marking a major manufacturing milestone. This breakthrough demonstrates the feasibility of scaling SiC power devices to 300mm, which could significantly reduce manufacturing costs and accelerate the adoption of wide-bandgap semiconductors in electric vehicles, renewable energy, and industrial power applications. Infineon leveraged existing 300mm silicon equipment for the SiC process, though challenges remain in crystal growth and defect control for larger SiC boules; the company also recently announced a €1.1 billion investment in a 300mm GaN power semiconductor facility in Villach.

hackernews · sshah03 · Nov 9, 18:25 · [Discussion](https://news.ycombinator.com/item?id=50429430)

**Background**: Silicon carbide is a wide-bandgap semiconductor material with a bandgap of about 3 eV, enabling power devices to operate at higher voltages, frequencies, and temperatures than traditional silicon. Historically, SiC wafers have been limited to 150mm or 200mm diameters, and transitioning to 300mm is difficult due to challenges in crystal growth and wafer processing. Infineon's achievement follows Wolfspeed's demonstration of a 300mm SiC crystal in January 2026, highlighting rapid progress in the field.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sic-wafers.com/300-mm-silicon-carbide-wafers-materials-manufacturing-barriers-and-the-path-to-industrial-scale-wide-bandgap-semiconductors/">300 mm Silicon Carbide Wafers: Materials, Manufacturing ...</a></li>
<li><a href="https://www.wolfspeed.com/company/news-events/news/wolfspeed-achieves-300mm-silicon-carbide-sic-technology-breakthrough/">Wolfspeed Achieves 300 mm Silicon Carbide (SiC) Technology ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wide-bandgap_semiconductor">Wide-bandgap semiconductor</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that the transition to 300mm took so long, given that 300mm silicon equipment has existed for years, and questioned whether Wolfspeed had already achieved 300mm. Others noted Infineon's lack of focus on LLM hardware despite its proximity to AI talent, and some called for renewed DRAM production in Europe.

**Tags**: `#semiconductors`, `#silicon-carbide`, `#manufacturing`, `#power-electronics`, `#infineon`

---

<a id="item-3"></a>
## [Show HN: Browser tool maps every satellite pass over any location](https://www.watched.earth/) ⭐️ 8.0/10

A developer launched watched.earth, a browser-based tool that finds every satellite that passed over any location in the last 7 days using SGP4 propagation on the CelesTrak catalog (17k+ objects) and displays real Sentinel-2, Landsat, and NASA imagery from those passes. The project demonstrates how complex orbital mechanics and multiple satellite imagery sources can be integrated into a fast, user-friendly web app, making satellite data accessible to non-experts and potentially useful for environmental monitoring, agriculture, and education. All ~17k objects are rendered on the GPU, solving Kepler's equation every frame, and the tool corrects Sentinel-2 timestamp offsets of 5-10 minutes to accurately match satellite passes; it only shows real images and does not store user location.

hackernews · a585gupt · Nov 9, 17:51 · [Discussion](https://news.ycombinator.com/item?id=50428907)

**Background**: SGP4 is a widely used orbit propagation algorithm that takes Two-Line Element (TLE) sets from catalogs like CelesTrak and predicts satellite positions. Kepler's equation relates the geometric properties of an orbit and is fundamental to orbital mechanics. Sentinel-2 and Landsat are Earth observation satellite missions that provide free, high-resolution imagery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simplified_perturbations_models">Simplified perturbations models - Wikipedia</a></li>
<li><a href="https://celestrak.org/satcat/">CelesTrak : Satellite Catalog (SATCAT)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kepler's_equation">Kepler's equation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project as beautifully executed and a standout combination of style and substance, with one noting that even if AI wrote the code, knowing what to ask for is a feat. Some offered constructive criticism about AI-generated styling cues (e.g., font choices, punchy sentences) that make the site feel 'vibe coded,' and one user expressed interest in higher-resolution imagery for a reasonable price.

**Tags**: `#satellite-imagery`, `#geospatial`, `#webgl`, `#orbital-mechanics`, `#show-hn`

---