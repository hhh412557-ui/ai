---
title: "Horizon Summary: 2026-09-27 (EN)"
date: 2026-09-27
lang: en
---

> From 16 items, 2 important content pieces were selected

---

1. [DeepSeek's DSec Runs 380,000 Concurrent Sandboxes on 160 Servers](#item-1) ⭐️ 8.0/10
2. [SemiAnalysis Publishes Free Teardown of Intel Panther Lake and 18A](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek's DSec Runs 380,000 Concurrent Sandboxes on 160 Servers](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek published a paper introducing DeepSeek Elastic Compute (DSec), a production sandbox platform that exposes FnCall, container, microVM, and full-VM backends through a unified SDK. The system reportedly sustains 380,000 concurrent sandboxes across 160 Epyc-based server nodes, a scale the community calls 'crazy stuff.' Large-scale sandboxing is a prerequisite for agentic training and evaluation, where each agent needs an isolated environment to execute code safely. If DSec's numbers hold up, it lowers the infrastructure barrier for running hundreds of thousands of parallel agent rollouts, which could accelerate RL-style training and evaluation of LLM agents. DSec unifies four isolation levels — FnCall, container, microVM, and full-VM — behind a single SDK, letting workloads pick the trade-off between startup latency and isolation strength. The headline figure of 380,000 concurrent sandboxes was achieved on 160 Epyc-based nodes, though the paper's exact density and latency numbers are not detailed in the summary.

hackernews · shenli3514 · Sep 26, 18:22 · [Discussion](https://news.ycombinator.com/item?id=49859112)

**Background**: A sandbox is a security mechanism that isolates running programs so failures or vulnerabilities cannot spread to the rest of the system. Elastic computing means resources are provisioned and released dynamically in response to real-time demand, which is exactly what a platform hosting hundreds of thousands of short-lived agent environments needs. DeepSeek, the Chinese AI lab behind the R1 and V3 models, is publishing this work as it expands from model training into agent infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22978">[2609.22978] DeepSeek Elastic Compute ( DSec ): A Sandbox...</a></li>
<li><a href="https://www.emergentmind.com/papers/2609.22978">DeepSeek Elastic Compute ( DSec ): A Sandbox Infrastructure for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sandbox_(computer_security)">Sandbox (computer security) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the scale, with one calling 380,000 concurrent sandboxes on 160 Epyc nodes 'crazy stuff,' and another noting the system resembles Google's AX project. A recurring theme was the paper's unusually long author list — 131 authors with 31 more not shown — which some speculated is a talent-retention strategy to keep competitors from identifying who to poach. Others asked whether DSec functions as an 'agent substrate.'

**Tags**: `#distributed-systems`, `#cloud-computing`, `#sandboxing`, `#DeepSeek`, `#elastic-compute`

---

<a id="item-2"></a>
## [SemiAnalysis Publishes Free Teardown of Intel Panther Lake and 18A](https://newsletter.semianalysis.com/p/intel-panther-lake-teardown) ⭐️ 8.0/10

SemiAnalysis has released a free STEEL teardown of Intel's Panther Lake processor, offering a detailed physical analysis of the chip built on Intel's 18A process technology. The teardown examines Intel's most advanced manufacturing node, which combines RibbonFET gate-all-around transistors with PowerVia backside power delivery. Panther Lake is the first product to ship on Intel 18A, making this teardown a rare independent look at whether Intel's most advanced process can compete with TSMC and Samsung. The findings matter for engineers, analysts, and investors assessing Intel Foundry's credibility and the broader shift toward gate-all-around and backside power in the semiconductor industry. Intel 18A is Intel's first production node to use RibbonFET gate-all-around transistors and industry-first PowerVia backside power delivery, and Panther Lake is branded as Core Ultra Series 3 mobile processors launched at CES 2026. The free teardown is a condensed version of SemiAnalysis's paid STEEL analysis, so it may omit some of the deeper structural and electrical measurements.

rss · Semianalysis · Sep 26, 13:36

**Background**: Intel 18A is Intel's most advanced chipmaking process, designed to restore the company's manufacturing leadership after years of delays at 10nm and 7nm. RibbonFET is Intel's name for gate-all-around transistors, which wrap the gate around the channel to reduce leakage, while PowerVia moves power delivery to the backside of the wafer to free up routing space and improve efficiency. Panther Lake is the codename for Intel's Core Ultra Series 3 mobile processors, the first commercial product family built on 18A. SemiAnalysis's STEEL lab is a dedicated teardown facility in Oregon that physically analyzes advanced datacenter and AI hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/intel-panther-lake-teardown">Intel Panther Lake Teardown, 18A, BSPD, GAAFET, SemiAnalysis STEEL</a></li>
<li><a href="https://www.intel.com/content/www/us/en/foundry/process/18a.html">Intel 18A | See Our Biggest Process Innovation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Panther_Lake_(microprocessor)">Panther Lake (microprocessor) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#semiconductor`, `#teardown`, `#18A`, `#Panther Lake`

---