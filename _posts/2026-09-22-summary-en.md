---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 33 items, 4 important content pieces were selected

---

1. [Xiaomi Releases MiMo v2.6 Open-Weight Models with Live Training Dashboard](#item-1) ⭐️ 8.0/10
2. [Spymarks: How Digital Watermarks Become Surveillance Tools](#item-2) ⭐️ 8.0/10
3. [Bryan Cantrill's Retrospective on Sun Microsystems' Strategic Failures](#item-3) ⭐️ 8.0/10
4. [TypeSafe AI Launches Jev, a 'System One' Decision Model](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Xiaomi Releases MiMo v2.6 Open-Weight Models with Live Training Dashboard](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

Xiaomi released the MiMo-V2.6 series, a family of natively omnimodal open-weight language models, including MiMo-V2.6-Pro (1.02T total / 42B activated parameters) and MiMo-V2.6-Flash (309B total / 15B activated parameters), along with a detailed technical report and a real-time training dashboard. The release emphasizes transparent training methodology, with the company publishing reinforcement learning scaling details and live metrics throughout training. This release marks a significant contribution to the open-weight AI ecosystem, as Xiaomi provides unusually comprehensive transparency into model training, which could influence how other labs share their methodologies. It also intensifies the global competition in open models, particularly between Chinese and US developers, and gives researchers and developers new high-performance models to experiment with locally. MiMo-V2.6-Pro is Xiaomi's most capable model to date, while Flash is a more efficient variant; both are natively omnimodal. The technical report details that the model processes 1,568 prompts per training step, generates 16 attempts per prompt, and accumulates 2.7–3.7B training tokens each step, with checkpoints available on Hugging Face.

hackernews · volf_ · Sep 21, 20:12 · [Discussion](https://news.ycombinator.com/item?id=49792730)

**Background**: MiMo is a family of large language models developed by Xiaomi, first introduced in 2025, and used as the key AI model in Xiaomi's ecosystem. Open-weight models are those whose parameters are publicly accessible, allowing anyone to download, run, and modify them, in contrast to closed models accessed only via APIs. Xiaomi's release includes a live training dashboard, which is a web tool that displays real-time metrics during model training, serving as both a transparency measure and an educational resource.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1wi9ebm/xiaomi_mimo_26_live_training_dashboard/">Xiaomi MiMo 2.6 Live Training Dashboard : r/LocalLLaMA - Reddit</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters praised Xiaomi's transparency, with one calling the real-time dashboard an incredible learning tool and noting the comprehensive technical report. Others debated geopolitical implications, arguing China may win the AI race due to energy infrastructure advantages, while some expressed skepticism about benchmark results, particularly where certain models surpass others. The discussion also highlighted specific model sizes and shared example outputs like pelican SVG renderings.

**Tags**: `#AI`, `#open-source`, `#language-models`, `#Xiaomi`, `#benchmarks`

---

<a id="item-2"></a>
## [Spymarks: How Digital Watermarks Become Surveillance Tools](https://brand.io/article/spymarks/) ⭐️ 8.0/10

An article on brand.io argues that digital watermarks are evolving into 'spymarks'—covert tracking mechanisms embedded in content that enable pervasive surveillance and ad attribution. The piece sparked a 246-point discussion with 45 comments debating detection, prevention, and whether the term is fair. If watermarks are routinely scanned by device drivers and reported back, every image, video, or text displayed on a screen could become a tracking beacon, affecting anyone who views digital content. This reframes watermarking from a content-integrity tool into an advertising and surveillance infrastructure, raising major privacy concerns. Commenters note that spymarks are essentially steganography—hidden data in a cover medium—and that reliable prevention would require byte-for-byte verification of content at each trusted stage. Others point out that text-based watermarking (e.g., choosing between 'winding' and 'curving') may need many bits to be dependable and could distort writing style.

hackernews · possibilistic · Sep 21, 23:03 · [Discussion](https://news.ycombinator.com/item?id=49794615)

**Background**: Digital watermarking traditionally embeds an identifier into a signal (image, video, audio) so the source can be traced later, such as forensic marks in streaming or counterfeit deterrence. Steganography is the broader practice of hiding information within another medium, and steganalysis is its detection. Ad attribution is the process of crediting conversions to specific ads or touchpoints, traditionally done via online tracking models like last-click.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_watermarking">Digital watermarking - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography - Wikipedia</a></li>
<li><a href="https://www.kpitarget.com/understanding-horizons-ad-attribution-tracking/">Location & Foot Traffic Ad Attribution Tracking | KPItarget</a></li>

</ul>
</details>

**Discussion**: Commenters debated the term 'spymark'—some find it needlessly negative compared to 'invisible watermark,' citing positive uses like counterfeit detection and SynthID. Others worry about driver-level scanning for ad attribution, propose byte-for-byte content verification as a defense, and question the reliability and stylistic cost of text watermarking.

**Tags**: `#watermarking`, `#steganography`, `#privacy`, `#surveillance`, `#advertising`

---

<a id="item-3"></a>
## [Bryan Cantrill's Retrospective on Sun Microsystems' Strategic Failures](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

Bryan Cantrill, a former Distinguished Engineer at Sun Microsystems and now CTO of Oxide Computer Company, published a blog post titled "What Sun got wrong" analyzing the strategic and technical mistakes that led to the company's decline. The post sparked a large Hacker News discussion with 542 points and 313 comments from industry veterans sharing firsthand experiences. Sun Microsystems was once a dominant force in workstations, servers, and enterprise software, and its decline offers enduring lessons about missed market pivots, proprietary lock-in, and competition from open-source alternatives like Linux. The discussion highlights how these historical mistakes remain relevant for today's technology companies facing similar strategic decisions. Community members pointed to specific missteps such as Sun briefly canceling Solaris on x86 in 2002, which damaged trust among customers wary of SPARC lock-in, and failing to strike a deal with Google in 2002 because Sun insisted on knowing how many servers Google had. Others contrasted Sun's cumbersome sales process with Dell's direct model and noted how Linux's availability in universities limited the pool of Solaris-trained hires.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**Background**: Sun Microsystems was a major American computer company founded in 1982, known for its SPARC workstations, Solaris operating system, Java programming language, and the slogan "the network is the computer." It rose to prominence during the dot-com boom but struggled in the 2000s against cheaper x86-based Linux servers, and was acquired by Oracle in 2010. Bryan Cantrill worked at Sun for 14 years and is known for creating DTrace, a dynamic tracing framework.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill - Wikipedia</a></li>
<li><a href="https://bcantrill.dtrace.org/about/">Bryan Cantrill</a></li>
<li><a href="https://tms-outsource.com/blog/posts/what-happened-to-sun-microsystems/">What Happened to Sun Microsystems: Oracle’s Big Buy</a></li>

</ul>
</details>

**Discussion**: Commenters shared a mix of nostalgia and sharp criticism, with some recalling Sun's painful sales process compared to Dell's efficient direct model, and others listing specific strategic errors like canceling Solaris on x86 and failing to partner with Google. A few noted the broader lesson for today's high-valuation tech stocks, while others praised Sun's hacker-friendly thin clients and tools like pine and vi.

**Tags**: `#Sun Microsystems`, `#technology history`, `#business strategy`, `#Hacker News`, `#systems engineering`

---

<a id="item-4"></a>
## [TypeSafe AI Launches Jev, a 'System One' Decision Model](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI unveiled Jev on September 15, 2026, the first of a new class it calls 'System One models' that accept text input but return typed probabilistic decisions — yes/no confidence scores, choice distributions, and numeric ratings — instead of generated text. The release came alongside a $40 million seed round led by DCVC, and Jev charges only for input at $0.042 per million tokens, with output free. Jev represents a potential paradigm shift by reframing LLM usage around classification and decision tasks rather than text generation, which could eliminate the parsing, validation, and retry overhead that currently plagues AI pipelines. Its extremely low cost and fast parallel question evaluation make it attractive for high-volume use cases like spam detection, labeling, ranking, and search reranking. Jev supports three question types: 'Noul' yes/no questions (named after the Bernoulli distribution) returning a 0–1 confidence, choice questions returning a probability distribution over provided options, and score questions returning a float along a described numeric range. A single 'state' document can be paired with many questions evaluated in parallel, but the model returns only floating-point numbers with no textual justification, making its reasoning opaque and raising bias concerns.

rss · Simon Willison · Sep 21, 23:09

**Background**: Traditional LLMs are priced by input and output tokens, with output typically costing far more, and they generate free-form text that downstream software must parse and validate. TypeSafe AI, a San Francisco company founded in 2024, positions Jev as a 'frontier-intelligence function call' — unstructured state in, typed probabilistic decisions out — aimed at automation rather than conversation. The 'System One' name contrasts with slower, deliberative 'System Two' reasoning, echoing the dual-process theory of cognition.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI ’s System One Model</a></li>

</ul>
</details>

**Discussion**: Commentators such as Maggie Appleton argued that 'decision models' is a better name than 'System One models', a framing Simon Willison endorsed. Discussion also highlighted discomfort with Jev's black-box nature — it returns only a floating-point number with no explanation of which content signals drove a decision — and warned that such scores could conceal bias, for example if used to rank job applicants.

**Tags**: `#LLM`, `#decision-models`, `#AI`, `#TypeSafe`, `#probabilistic-models`

---