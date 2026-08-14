---
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 34 items, 3 important content pieces were selected

---

1. [Spaghettifying DRAM: New Exploit Achieves Ring-0 via DRAM Scrambling](#item-1) ⭐️ 9.0/10
2. [Google Unveils Gemini 3.7 Flash with Competitive Pricing](#item-2) ⭐️ 8.0/10
3. [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast, 7x Faster](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Spaghettifying DRAM: New Exploit Achieves Ring-0 via DRAM Scrambling](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

Security researcher Christopher Domas released a new technique called 'Spaghettifying DRAM' that exploits DRAM addressing and scrambling to achieve ring-0 privilege escalation. The technique is demonstrated on AMD Jaguar (family 16h) CPUs and uses a Z3 solver to reverse-engineer the DRAM scrambling transform. This research reveals a novel hardware-level attack surface that bypasses security mechanisms like PSP private memory, SMRAM, and C6 idle-state protections, potentially affecting console security and system-level access. It highlights the growing complexity of DRAM as an attack surface, with implications for both older and newer CPU architectures. The technique works by solving the DRAM scrambling transform using Z3, allowing an attacker to find aliases for protected memory regions in the 'spaghettified' view of memory. The README notes that Zen 3 has a different base address for memory controller registers, but the exploit's applicability to newer CPUs remains unclear.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: DRAM addressing and scrambling are used to improve performance and reliability, but they also create a complex mapping between physical addresses and actual memory cells. Row hammer attacks exploit DRAM bit flips, while this new technique goes further by reverse-engineering the scrambling to access protected memory regions. Ring-0 is the highest privilege level in the CPU, and gaining it typically allows full system control.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking _everything_ on the CPU with DRAM scrambling · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Row_hammer">Row hammer - Wikipedia</a></li>
<li><a href="https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_pessl.pdf">DRAMA: Exploiting DRAM Addressing</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the research, praising Christopher Domas's work and anticipating his Black Hat talk. Some raised questions about the exploit's applicability to newer CPUs, noting that it currently works on AMD Jaguar (2013) and that Zen 3 has different base addresses. Others speculated about the impact on console security, particularly Xbox and PlayStation.

**Tags**: `#security`, `#DRAM`, `#exploit`, `#hardware`, `#ring-0`

---

<a id="item-2"></a>
## [Google Unveils Gemini 3.7 Flash with Competitive Pricing](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google has introduced Gemini 3.7 Flash, a new multimodal model designed for fast agentic workflows, coding, and complex reasoning. It is offered at an introductory price of $0.375 per million input tokens and $1.875 per million output tokens, with a 1M token context window. Gemini 3.7 Flash represents a significant step in making advanced AI capabilities more accessible and affordable, potentially intensifying competition in the low-cost model segment. Its strong performance in vision and coding tasks could attract developers and enterprises seeking cost-effective solutions. The model supports text, image, speech, and video input, and outputs text. It has a maximum output of 65,536 tokens and is available through multiple providers on OpenRouter. The introductory pricing is scheduled to double on December 31, 2026, which has drawn attention from the community.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Background**: Gemini 3.7 Flash is part of Google's Gemini model family, which includes various sizes optimized for different use cases. Flash models are typically designed for low-cost, high-volume tasks such as summarization and parsing, while Pro models offer higher intelligence. The release follows the recent launch of Gemini 3.6 Flash, indicating a rapid iteration cycle.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://openrouter.ai/google/gemini-3.7-flash">Gemini 3 . 7 Flash - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Community members have shared practical tests, such as image-to-HTML and SVG generation, noting that Gemini 3.7 Flash performs well but Opus 5 remains superior in some tasks. Some users question the pricing strategy, especially the scheduled price increase, and compare it favorably to alternatives like GPT-5.6 Luna. Others speculate on the absence of a Gemini 3.5 Pro release and the frequent updates to Flash models.

**Tags**: `#AI`, `#Google`, `#Gemini`, `#LLM`, `#Machine Learning`

---

<a id="item-3"></a>
## [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast, 7x Faster](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

OpenAI and Cerebras announced GPT-5.6 Sol Ultrafast, a new API service tier that runs the model up to 14x faster, delivering up to 750 output tokens per second. In evaluations, it answered 2,500 HLE questions in 11 hours and 11 minutes, achieving comparable accuracy to Claude Fable 5 nearly 7x faster. This collaboration marks a significant milestone in LLM inference speed, potentially enabling real-time applications and more iterative reasoning. It could reshape the competitive landscape by making high-speed inference a key differentiator for AI services. Ultrafast mode is initially available to a select group of customers, with access expanding over time. Cerebras claims no quality compromise, but community members note that neither company explicitly states the model is 1:1 identical to standard GPT-5.6 Sol, and pricing details have not been announced.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**Background**: Cerebras Systems is known for its wafer-scale engine, a chip that is 58x larger and 15x faster than GPUs, designed for ultra-fast AI training and inference. GPT-5.6 Sol is OpenAI's latest model, and Claude Fable 5 is Anthropic's Mythos-class model released in June 2026. The HLE (Humanity's Last Exam) is a benchmark used to evaluate frontier AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the speed gains but raise concerns about accuracy trade-offs and evaluation methodology. Some users note the lack of explicit confirmation that Ultrafast is identical to standard Sol, and the absence of pricing information, suggesting it might be expensive or still in gauging interest phase.

**Tags**: `#AI`, `#LLM`, `#hardware`, `#OpenAI`, `#Cerebras`

---