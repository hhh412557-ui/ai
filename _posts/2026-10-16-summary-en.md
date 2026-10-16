---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 30 items, 5 important content pieces were selected

---

1. [Citizen Lab Exposes AdFection: Targeted Ads Used to Deliver Zero-Click Spyware](#item-1) ⭐️ 9.0/10
2. [Meta Releases Muse Spark Open, an 816B Open-Weight Model for Mac Studio](#item-2) ⭐️ 8.0/10
3. [Meta's New Commercial Terms Require Business Accounts to Consent to Website Scraping](#item-3) ⭐️ 8.0/10
4. [Anthropic Tells Investors Quarterly Revenue Up Nearly 50% to $16.8bn Ahead of IPO](#item-4) ⭐️ 8.0/10
5. [ASML Reportedly Developing Hybrid Bonding Tool for Advanced Packaging](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Citizen Lab Exposes AdFection: Targeted Ads Used to Deliver Zero-Click Spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 9.0/10

Citizen Lab published research revealing that an Israeli firm called Discover Tech operated a malicious ad-targeting platform, dubbed Controlium, which served targeted advertisements to silently install zero-click mercenary spyware on victims' phones and computers. The report, covered by The Guardian, The Verge, Wired, and TechCrunch, provides the first technical evidence that commercial spyware is being distributed through the global online advertising ecosystem. This is significant because it demonstrates a novel attack vector that weaponizes the ubiquitous adtech infrastructure trusted by billions of users, potentially affecting anyone who sees an online ad. It raises urgent questions about accountability across the advertising supply chain and could reshape how governments and platforms regulate both ad delivery and the mercenary spyware industry. Discover Tech presents itself as a legitimate advertising firm but functions as a bridge between ad vendors and the mercenary spyware ecosystem, with links to ADINT and mass surveillance vendors. An AdTech engineer commenting on the report noted that it remains vague about the exact mechanism that activates the malware in a zero-click fashion, and that the term 'ad provider' oversimplifies a complex ecosystem.

hackernews · jcomp · Oct 15, 10:43 · [Discussion](https://news.ycombinator.com/item?id=50101813)

**Background**: Citizen Lab is an interdisciplinary research laboratory at the University of Toronto's Munk School that studies digital threats to civil society and has played a major role in exposing spyware attacks against journalists, politicians, and human rights advocates. Zero-click spyware refers to malware that infects a device without any user interaction, such as tapping a link, making it especially dangerous and hard to detect. The adtech ecosystem involves numerous intermediaries—ad exchanges, demand-side platforms, and real-time bidding networks—that make it difficult to trace who ultimately serves a given ad.

<details><summary>References</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection: How Discover - Tech Turned... - The Citizen Lab</a></li>
<li><a href="https://www.wired.com/story/nightmare-scenario-zero-click-spyware-is-infecting-phones-via-targeted-ads/">‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones ...</a></li>
<li><a href="https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/">Governments are hacking people with 'zero-click' spyware by ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong concern, with some arguing that Israeli cybersecurity firms should be considered beholden to the Israeli government and therefore untrustworthy, while others debated why Israel has become a leading cyber power. An AdTech engineer pushed back on the report's sensationalism and the oversimplified notion of an 'ad provider,' and several users shared the original Citizen Lab report and historical context such as the Download Valley.

**Tags**: `#cybersecurity`, `#spyware`, `#adtech`, `#privacy`, `#surveillance`

---

<a id="item-2"></a>
## [Meta Releases Muse Spark Open, an 816B Open-Weight Model for Mac Studio](https://research.meta.ai/blog/muse-spark-open) ⭐️ 8.0/10

Meta Superintelligence Labs released Muse Spark Open, an 816B total / 42B active parameter open-weight MoE model with a 1M-token context window, natively multimodal and optimized to run on Mac Studio hardware. The release quickly drew 692 points and 374 comments, with debate centering on its restrictive licensing, performance versus DeepSeek, Qwen, and GLM, and Meta's standing in the open-weight race. Muse Spark Open is one of the largest open-weight models ever released by a US lab, and its ability to run on two Mac Studios could shift local inference from hobbyist territory toward serious desktop deployment. However, its custom Muse Model License and reported performance gaps against Chinese open-weight rivals raise questions about whether Meta can maintain its influence in the open-weight ecosystem. The model uses a Mixture-of-Experts architecture with 816B total parameters but only 42B active, a 1M-token context window, and native multimodality, with additional safety post-training applied to the open-weight version. The Muse Model License permits general use but restricts third parties from offering the model as a service via API if their aggregate gross revenue exceeds $20 million, which critics argue makes it not truly open-weight.

hackernews · bigwheels · Oct 15, 17:47 · [Discussion](https://news.ycombinator.com/item?id=50107379)

**Background**: Open-weight models are AI models whose trained parameters are publicly released, allowing anyone to download and run them locally, though the license determines whether users may modify, fine-tune, or redistribute them. Chinese labs such as DeepSeek, Alibaba Cloud (Qwen), Moonshot AI, and Z.ai have led recent open-weight releases under permissive licenses like Apache or MIT, while US labs including Meta have favored more restrictive terms. Running large models locally on Apple Silicon has become increasingly practical, with tools like MLX and Unsloth enabling desktop inference on high-memory Mac Studio configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B">meta-models/Muse-Spark-Open-816B-A42B · Hugging Face</a></li>
<li><a href="https://www.unite.ai/metas-816b-parameter-muse-spark-open-weights-are-now-public/">Meta’s 816B-Parameter Muse Spark Open Weights Are Now Public</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical: keyle noted the model costs about 10x more than DeepSeek v4.1 Flash on OpenRouter while performing worse, and a11r cited Artificial Analysis showing it underperforms Qwen3.8 Flash Next and GLM 5.3 Flash, both runnable on a single B300. seizethecheese examined the license and confirmed it restricts Model-as-a-Service use above $20M revenue, while swalsh argued Meta's strategy is to build a sticky ecosystem moat rather than charge for frontier intelligence, and armcat praised Meta's effort to support nearly every model runner from Unsloth to MLX.

**Tags**: `#AI/ML`, `#open-weight models`, `#Meta`, `#model licensing`, `#LLM`

---

<a id="item-3"></a>
## [Meta's New Commercial Terms Require Business Accounts to Consent to Website Scraping](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/) ⭐️ 8.0/10

Meta's updated commercial terms, effective October 30, will require business account holders to consent to Meta scraping their websites and licensing the content to the platform. Legal experts say the change effectively grants Meta broad scraping rights over any site tied to a business account, sparking concern among publishers and technologists. The change could reshape the balance of power between platforms and publishers, letting Meta legally harvest news and business content without individual licensing deals. It also raises unresolved questions about whether account holders even own or can sublicense the content they publish, potentially exposing them to liability. The terms apply to business account holders rather than ordinary users, and consent is framed as a condition of maintaining the account. Critics note that many publishers license third-party content under terms that may not permit this kind of sublicensing, and Meta has previously sued scrapers for violating its own terms.

hackernews · 0in · Oct 15, 23:37 · [Discussion](https://news.ycombinator.com/item?id=50111852)

**Background**: Web scraping—automatically extracting data from websites—sits in a legally gray area, governed by terms of service, copyright, and court rulings that often hinge on whether a user is logged in. Meta has historically fought scrapers in court, including a California case where a judge ruled its terms only bound logged-in users. By embedding scraping consent into commercial terms, Meta shifts from litigation to contractual permission.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zyte.com/blog/california-court-meta-ruling/">Court Rules Meta 's Terms Do Not Prohibit Scraping of Public Data</a></li>
<li><a href="https://levelup.gitconnected.com/can-data-scraping-get-you-sued-d65b097f5a87">Can data scraping get you sued?. This week, Meta ... | Level Up Coding</a></li>
<li><a href="https://infomineo.com/services/data-analytics/is-web-scraping-legal-laws-compliance-best-practices/">Is Web Scraping Legal? Laws, Risks & Compliance Checklist</a></li>

</ul>
</details>

**Discussion**: Commenters questioned the legal theory behind the terms, noting that publishers often license content they cannot sublicense, and speculated Meta may already be scraping and simply wants legal cover. Others described the move as aggressive 'legal judo' and pointed to Meta's bot as the most active crawler on their sites.

**Tags**: `#Meta`, `#web scraping`, `#terms of service`, `#content licensing`, `#legal`

---

<a id="item-4"></a>
## [Anthropic Tells Investors Quarterly Revenue Up Nearly 50% to $16.8bn Ahead of IPO](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

Anthropic disclosed to investors on Wednesday that its quarterly revenue grew nearly 50% to $16.8bn in Q3, up from $11.5bn in Q2 and about $4.8bn in Q1, according to an FT report. The company also revealed that adjusted operating margins (excluding stock-based compensation) were 11%, and that it earned $1.70 in revenue for every $1 spent on computing power. This is rare financial transparency from a leading AI lab ahead of its IPO, offering a window into the economics of frontier model development. The revenue trajectory and margin data will shape how investors and competitors assess the sustainability of the AI industry's massive compute spending. Anthropic said distillation — rivals training on its model outputs — accounted for 5% to 7% of revenue and that it had cut this back 'materially' in Q3; napkin math suggests unnamed labs spent over half a billion dollars distilling Anthropic's models in Q2 alone. Notably, Anthropic appears to have stopped leaning on 'annualized run-rate revenue' in its investor communications.

rss · Simon Willison · Oct 15, 13:04

**Background**: Knowledge distillation is a technique where a smaller or rival model is trained on the outputs of a more advanced model to approximate its capabilities, and it is difficult to prevent because it only requires API access. Adjusted operating margin is a non-GAAP metric that excludes items like stock-based compensation to show core profitability. Anthropic is a leading AI lab preparing for an IPO, and its disclosures are closely watched as a bellwether for the economics of large language model companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop/">What is AI model distillation, and why is it so hard to stop?</a></li>
<li><a href="https://fastercapital.com/content/Adjusted-Operating-Margin--Optimizing-for-Success--Adjusted-Operating-Margin-and-Non-GAAP-Earnings.html">Adjusted Operating Margin: Optimizing for Success: Adjusted ...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI industry`, `#IPO`, `#revenue`, `#business`

---

<a id="item-5"></a>
## [ASML Reportedly Developing Hybrid Bonding Tool for Advanced Packaging](https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding) ⭐️ 8.0/10

According to SemiAnalysis, ASML is developing a hybrid bonding tool, as suggested by its patent filings, a news report, and its own roadmap, though the company has not made an official announcement. Reports from TheElec and TrendForce in March 2026 indicate ASML is preparing to enter the semiconductor back-end equipment market with a hybrid bonding system. This move would mark ASML's expansion from front-end lithography into the back-end advanced packaging market, a critical area for AI and high-performance computing chips. It could reshape the advanced packaging landscape, where hybrid bonding is becoming essential for next-generation chip stacking and interconnect density. Hybrid bonding directly connects copper surfaces between chips without micro-bumps, enabling higher interconnect density and lower resistance compared to traditional thermocompression bonding. ASML's entry would leverage its precision alignment expertise, though the tool is still in development and no official specifications or timeline have been released.

rss · Semianalysis · Oct 15, 19:27

**Background**: Hybrid bonding is an advanced packaging technique that bonds two chips or wafers directly at the copper pad level, eliminating solder bumps and allowing much finer pitch interconnects. It is increasingly used in 3D stacked ICs and 2.5D packaging to improve performance, reduce latency, and enhance thermal characteristics. ASML is best known for its extreme ultraviolet (EUV) lithography systems used in front-end chip manufacturing, and this would be its first major foray into back-end packaging equipment.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding">ASML Is Building a Hybrid Bonding Tool!ASML is building a ...</a></li>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=5864">ASML Moves Into Advanced Packaging With Hybrid Bonding Tool ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/03/23/news-asml-reportedly-eyes-hybrid-bonding-equipment-precision-edge-may-reshape-advanced-packaging-landscape/">[News] ASML Reportedly Eyes Hybrid Bonding Equipment ...</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#ASML`, `#hybrid bonding`, `#advanced packaging`, `#hardware`

---