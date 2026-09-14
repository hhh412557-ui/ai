---
layout: default
title: "Horizon Summary: 2026-09-14 (EN)"
date: 2026-09-14
lang: en
---

> From 27 items, 4 important content pieces were selected

---

1. [Fable 5.1 Solves 370-Year-Old Cyphral Distich Cipher](#item-1) ⭐️ 8.0/10
2. [Google's Persistent Scam Ad Problem Sparks Accountability Debate](#item-2) ⭐️ 8.0/10
3. [Signal to Enable Phone-Number-Free Registration Using Zero-Knowledge Proofs](#item-3) ⭐️ 8.0/10
4. [SemiAnalysis: 4-hi HBM Stacks Cut Inference Costs](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Fable 5.1 Solves 370-Year-Old Cyphral Distich Cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 8.0/10

Anthropic's Claude Fable 5.1, an LLM, successfully solved the Cyphral Distich, a cipher created by Scottish writer Sir Thomas Urquhart that had remained unsolved for over 370 years. The solution was published by vals.ai, which noted the answer was 'quite embarrassing for humans in hindsight.' This demonstrates that LLMs can tackle long-standing problems in historical cryptanalysis, potentially accelerating research in fields bottlenecked by human attention. It also fuels the broader debate about AI's growing role in knowledge work and whether such breakthroughs reflect genuine capability or simply unexplored low-hanging fruit. The cipher is attributed to Sir Thomas Urquhart, a 17th-century Scottish writer, and had remained unsolved for roughly 370 years. Fable 5.1 is Anthropic's newer model, estimated to cost about 25% less than Fable 5 for typical token-billed workloads, with improvements in agentic coding and long-running workflows.

hackernews · u1hcw9nx · Sep 13, 21:06 · [Discussion](https://news.ycombinator.com/item?id=49688695)

**Background**: The Cyphral Distich is a historical cipher created by Sir Thomas Urquhart, a Scottish writer and translator best known for his English translation of Rabelais. Historical ciphers like this are typically solved through manual cryptanalysis, requiring deep knowledge of the era's language and conventions. LLMs have recently been applied to such puzzles, raising questions about how much of their success comes from pattern recognition versus genuine reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html">Claude Fable Solves a Historical Cipher - Schneier on Security</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the cipher was well-known or studied before, with some suggesting the LLM's success may reflect unexplored low-hanging fruit rather than superior capability. Others shared anecdotes of LLMs cracking personal ciphers, while some expressed broader ambivalence about AI's rapid progress and its implications for humanity.

**Tags**: `#AI`, `#cryptography`, `#LLM`, `#historical-cipher`, `#problem-solving`

---

<a id="item-2"></a>
## [Google's Persistent Scam Ad Problem Sparks Accountability Debate](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 8.0/10

An article on atomic14.com examines why Google continues to serve fraudulent ads, sparking a 692-point Hacker News discussion with 321 comments. Commenters shared firsthand experiences with AdSense scam ads on their own sites and debated Google's revenue incentives and lack of accountability. Google's ad network reaches billions of users, so its failure to block scam ads erodes trust in the entire digital advertising ecosystem and harms publishers, advertisers, and consumers alike. The discussion highlights growing calls for strict liability and regulatory action against Google's dominant ad business. Commenters noted that scammers rotate through free hosting domains like azurestaticapps.net, herokuapp.com, and netlify.app, which Google reportedly refuses to block because it treats them as TLDs. One commenter claimed someone who spent over $100M on Google Ads said Google is aggressively juicing revenue in unprecedented ways.

hackernews · iamflimflam1 · Sep 13, 17:37 · [Discussion](https://news.ycombinator.com/item?id=49686445)

**Background**: Google Ads and AdSense place advertisements across search results, websites, and YouTube, generating the vast majority of Google's revenue. Ad fraud, including fake popups and deceptive product pitches, has long plagued the platform, and Google uses AI models to detect and block fraudulent practices. Trust and safety in advertising is a growing industry concern, with advertisers worried about funding fraud and disinformation through programmatic buys.

<details><summary>References</summary>
<ul>
<li><a href="https://bluepear.net/blog/prevent-google-ad-fraud">Google Ads Fraud Detection : Reports, Scams & Prevention</a></li>
<li><a href="https://www.timesofai.com/industry-insights/google-ai-ad-fraud-detection/">Google AI Ad Fraud Detection for Click Fraud Protection</a></li>
<li><a href="https://www.advertiserperceptions.com/trust-in-advertising-have-advertisers-moved-the-needle-on-supporting-brand-safety-news-integrity-and-quality-publishers/">Trust in Advertising: Have Advertisers Moved the Needle on Supporting Brand Safety, News Integrity and Quality Publishers? - Advertiser Perceptions</a></li>

</ul>
</details>

**Discussion**: Commenters were largely critical of Google: one described AdSense as a nightmare that placed thousands of scam ads on their site, another called for strict liability and labeled Google complicit, and a third said every YouTube ad now seems to be an AI-generated scam. Others pointed to Google's incentives, arguing it is maximizing ad revenue while its core business faces AI disruption.

**Tags**: `#advertising`, `#google`, `#fraud`, `#trust-and-safety`, `#hacker-news`

---

<a id="item-3"></a>
## [Signal to Enable Phone-Number-Free Registration Using Zero-Knowledge Proofs](https://community.signalusers.org/t/registration-without-a-phone-number/2222?page=10) ⭐️ 8.0/10

Signal is planning to allow account registration without a phone number by using zero-knowledge proofs (ZKPs), according to community discussions and code commits. The implementation will reportedly require a purchase via Google Play Billing to mitigate spam, while keeping the existing SMS verification option. This marks a significant privacy and cryptography milestone for Signal, as it could let users register without revealing a phone number, a major source of metadata. It may influence other messaging platforms to adopt similar privacy-preserving registration methods. The zero-knowledge proofs would allow Signal to verify that a user is not a bot or spammer without learning their phone number. The use of Google Play Billing for spam mitigation suggests a paid registration option, and the change also enables Android tablets without SIM cards to become first-class adjunct devices.

hackernews · Cider9986 · Sep 13, 21:47 · [Discussion](https://news.ycombinator.com/item?id=49689048)

**Background**: Zero-knowledge proofs are cryptographic protocols that let one party prove a statement is true without revealing any information beyond the statement's validity. Signal has historically required a phone number for registration, which has been a barrier for privacy-conscious users. The community has long requested a phone-number-free option, and this move aligns with Signal's broader efforts to enhance privacy, such as the recent introduction of usernames.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://signal.org/blog/phone-number-privacy-usernames/">Signal >> Blog >> Keep your phone number private with Signal usernames</a></li>
<li><a href="https://theintercept.com/2024/07/16/signal-app-privacy-phone-number/">How I Got a Truly Anonymous Signal Account</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment: some praise the move for enabling tablet use without SIM cards, while others criticize the lack of technical depth and demand transparency about backend infrastructure. Concerns were raised about the reliance on Google Play Billing and the need for more detailed ZKP documentation.

**Tags**: `#privacy`, `#zero-knowledge-proofs`, `#Signal`, `#cryptography`, `#messaging`

---

<a id="item-4"></a>
## [SemiAnalysis: 4-hi HBM Stacks Cut Inference Costs](https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi) ⭐️ 8.0/10

SemiAnalysis published an analysis arguing that 4-hi HBM stacks can deliver the same bandwidth as taller stacks while using fewer DRAM dies, thereby cutting inference costs and stretching scarce DRAM supply further. The piece points out that 4-hi is the lowest stack height capable of accessing all 2048 data I/Os per cube, since each die provides 512 I/Os. If 4-hi HBM can match the bandwidth of taller stacks, AI accelerator makers could reduce the number of DRAM dies per GPU, lowering bill-of-materials costs and easing the DRAM supply crunch that has constrained AI hardware. This could meaningfully reduce the cost of running large-model inference at scale. The argument hinges on HBM's I/O architecture: each cube exposes 2048 data I/Os, and since each die contributes 512 I/Os, a 4-hi stack is the minimum height needed to reach the full 2048 I/Os and maximize bandwidth. Taller stacks (8-hi, 12-hi, 16-hi) add capacity but not necessarily bandwidth, so 4-hi can be more die-efficient for bandwidth-bound inference workloads.

rss · Semianalysis · Sep 13, 18:19

**Background**: HBM (High Bandwidth Memory) is a 3D-stacked DRAM technology used in AI GPUs and HPC accelerators, where multiple DRAM dies are stacked vertically and connected through a wide bus to deliver far higher bandwidth than DDR or GDDR. Stack height (e.g., 4-hi, 8-hi, 12-hi) traditionally determines both capacity and, up to a point, bandwidth. As AI inference demand grows, HBM has become a scarce and expensive component, prompting interest in designs that maximize bandwidth per die.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi">Long Live the Short King: Why 4-hi HBM Wins</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm">Scaling the Memory Wall: The Rise and Roadmap of HBM</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#AI hardware`, `#inference`, `#DRAM`, `#semiconductor`

---