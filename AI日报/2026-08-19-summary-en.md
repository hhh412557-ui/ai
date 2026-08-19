---
title: "Horizon Summary: 2026-08-19 (EN)"
date: 2026-08-19
lang: en
---

> From 21 items, 4 important content pieces were selected

---

1. [Mojo Programming Language Goes Open Source Under Apache 2](#item-1) ⭐️ 9.0/10
2. [Turbovec Brings Google's TurboQuant Vector Search to Rust](#item-2) ⭐️ 8.0/10
3. [Apple Replaces Core Technology Fee with 5% Commission in EU](#item-3) ⭐️ 8.0/10
4. [Cerebras CS-4 Doubles AI Performance and Power](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo Programming Language Goes Open Source Under Apache 2](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Modular has released the Mojo compiler and toolchain under the Apache 2 license, fulfilling a promise made in May 2023. This follows the release of Mojo 1.0 last week. Open-sourcing Mojo under a permissive license enables broader community adoption and contribution, potentially accelerating its growth as a high-performance language for AI and GPU programming. This move aligns with the trend of open-sourcing foundational AI infrastructure. Mojo was originally intended to be a superset of Python, but that goal was abandoned around August 2025. The language now focuses on GPU programming with Python-inspired syntax, and it is built on the MLIR compiler framework, enabling optimization for various hardware accelerators.

rss · Simon Willison · Aug 18, 21:39

**Background**: Mojo is a systems programming language developed by Modular Inc., designed for high-performance AI infrastructure. It uses a syntax reminiscent of Python but includes features like static typing and a borrow checker inspired by Rust. The Apache 2 license is a permissive open-source license that allows users to use, modify, and distribute the software freely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://www.infoworld.com/article/4081105/revisiting-mojo-a-faster-python.html">Revisiting Mojo : A faster Python? | InfoWorld</a></li>

</ul>
</details>

**Tags**: `#Mojo`, `#open source`, `#programming language`, `#AI`, `#compiler`

---

<a id="item-2"></a>
## [Turbovec Brings Google's TurboQuant Vector Search to Rust](https://github.com/RyanCodrai/turbovec) ⭐️ 8.0/10

Turbovec is a new Rust implementation of Google's TurboQuant algorithm for vector search, enabling memory-efficient and fast similarity search. It reportedly compresses 10 million documents to just 4GB, making it suitable for local and privacy-first applications. This project brings a state-of-the-art quantization method to the Rust ecosystem, potentially improving performance and memory usage for local search applications. It could enable developers to build efficient, privacy-preserving search tools without relying on cloud services. Turbovec is built in Rust and aims to be compatible with FAISS, a popular vector search library. The project is open-source on GitHub, and community members are discussing potential WASM compilation for browser extensions and SQLite bindings for easier integration.

hackernews · fittingopposite · Aug 18, 18:07 · [Discussion](https://news.ycombinator.com/item?id=49349898)

**Background**: Vector search is a technique for finding similar items by representing them as high-dimensional vectors and using nearest-neighbor search. Quantization reduces the memory footprint of these vectors by compressing them, enabling faster and more scalable search. TurboQuant is a recent algorithm from Google that achieves high compression with minimal accuracy loss, and Turbovec brings this to Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://github.com/Firmamento-Technologies/TurboQuant">GitHub - Firmamento-Technologies/TurboQuant: Near-optimal ...</a></li>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that FAISS is no longer state-of-the-art, referencing benchmark sites. Users are excited about the memory savings and potential for faster development, and some suggest improvements to the README for better adoption. There is also interest in WASM compilation for browser extensions and SQLite bindings.

**Tags**: `#vector-search`, `#rust`, `#quantization`, `#information-retrieval`, `#machine-learning`

---

<a id="item-3"></a>
## [Apple Replaces Core Technology Fee with 5% Commission in EU](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/) ⭐️ 8.0/10

Apple announced changes to its EU App Store policies, replacing the Core Technology Fee with a 5% commission on digital transactions in apps distributed outside the App Store, and eliminating the initial acquisition fee and store services fee. This simplifies the fee structure for developers and resolves Apple's disagreements with the European Commission over business terms and alternative distribution, potentially easing regulatory tensions and impacting developer costs and strategies in the EU. The new terms also eliminate the initial acquisition fee and store services fee. Apple will continue to require notarization for alternatively distributed apps to maintain user safety.

hackernews · newusertoday · Aug 18, 16:21 · [Discussion](https://news.ycombinator.com/item?id=49348055)

**Background**: The Core Technology Fee was introduced in early 2024 as part of Apple's compliance with the EU Digital Markets Act, charging €0.50 per first annual install after one million installs. The new 5% commission replaces this per-install fee for apps distributed outside the App Store, while apps sold through the App Store will pay a 26% commission on digital goods and services.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/">Apple announces changes for apps in the European Union - Apple</a></li>
<li><a href="https://www.cnbc.com/2026/08/18/apple-eu-app-store-fees-iphone.html">Apple overhauls EU app store fees to resolve payments clash</a></li>
<li><a href="https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/">Apple overhauls its EU App Store fees, loosens rules for alternative app stores | TechCrunch</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed reactions. Some question why Apple needs the Core Technology Commission when it already charges a developer program fee, while others note improvements for reader apps like Netflix and Spotify, which can now promote out-of-app offers without an actionable link starting October 1, 2026.

**Tags**: `#Apple`, `#EU`, `#App Store`, `#regulation`, `#developer fees`

---

<a id="item-4"></a>
## [Cerebras CS-4 Doubles AI Performance and Power](https://newsletter.semianalysis.com/p/cerebrass-next-generation-cs-4-fast) ⭐️ 8.0/10

Cerebras has announced its next-generation CS-4 system, which doubles the performance and power of its predecessor for AI workloads. The CS-4 is the first iteration of the new Cerebras Nexus Platform Architecture. The CS-4's significant performance boost could accelerate large-scale AI model training, potentially impacting the competitive landscape of AI hardware. It offers an alternative to GPU-based systems for organizations training massive models. The CS-4 uses a 2D torus interconnect topology, which can support models up to 50 trillion parameters, though no such model currently exists. The system is designed to deliver unprecedented decode performance at scale.

rss · Semianalysis · Aug 19, 01:32

**Background**: Cerebras is known for its Wafer Scale Engine (WSE), a single wafer-scale integrated processor that includes compute, memory, and interconnect fabric. The CS-4 builds on the WSE-3 architecture, which was introduced in March 2024 and features 4 trillion transistors and 900,000 AI-optimized cores.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/cs4">Product - System - Cerebras</a></li>
<li><a href="https://www.theregister.com/systems/2026/08/19/cerebras-cs-4-rack-systems-juice-chips-for-every-last-drop-of-ai-performance/5289286">Cerebras CS-4 rack systems juice chips for every last drop of AI performance</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Cerebras`, `#semiconductors`, `#machine learning`, `#high-performance computing`

---