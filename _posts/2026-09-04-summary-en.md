---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
lang: en
---

> From 22 items, 3 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra with Near-Perfect ARC-AGI-3 Score](#item-1) ⭐️ 10.0/10
2. [Verisign Proposes Terminating Third-Level .name Domains](#item-2) ⭐️ 8.0/10
3. [Porting a 1993 Amiga Game to Godot Using an LLM](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra with Near-Perfect ARC-AGI-3 Score](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI has announced GPT-6 Astra, a new flagship model that achieves a 99.9% score on the ARC-AGI-3 benchmark and shows major gains on the Artificial Analysis Coding Agent Index. The model is now rolling out to users. This release marks a significant milestone in AI development, as GPT-6 Astra's near-perfect ARC-AGI-3 performance suggests a leap toward more general reasoning capabilities. The improvements in coding benchmarks could enhance developer productivity and accelerate AI adoption across industries. The ARC-AGI-3 score of 99.9% was achieved using a specific harness configuration, and OpenAI notes that without it, the score would be around 30%. The model also shows major gains on the Artificial Analysis Coding Agent Index, which is a composite of DeepSWE, Terminal-Bench v2.1, and SWE-Atlas-QnA.

hackernews · kibae · Sep 3, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49554643)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark designed to measure human-like intelligence in AI agents by challenging them to explore novel environments and acquire goals on the fly. The Artificial Analysis Coding Agent Index is a composite score built from several coding benchmarks to evaluate AI agents' performance on real-world software engineering tasks. GPT-6 Astra is part of OpenAI's ongoing series of large language models, succeeding GPT-5.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/">How enabling two settings tripled our scores on the ARC-AGI-3 benchmark | OpenAI</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the ARC-AGI-3 scorecard, noting that the 99.9% figure is misleading without the specific harness, and that other benchmarks show only modest improvements. Some users question the emphasis on autonomous purchasing in demos, while others draw parallels to François Chollet's work on measuring intelligence, suggesting that progress may still be skill acquisition rather than true AGI.

**Tags**: `#AI`, `#OpenAI`, `#GPT-6`, `#large language models`, `#ARC-AGI`

---

<a id="item-2"></a>
## [Verisign Proposes Terminating Third-Level .name Domains](https://neil.fraser.name/news/2026/09/03/) ⭐️ 8.0/10

Verisign has proposed terminating all third-level .name domains (e.g., john.smith.name), which would affect existing registrations and release the corresponding second-level domains (smith.name) for new registration. The proposal is currently under consideration by ICANN. This policy change could destabilize existing domain registrations and enable domain squatting, contradicting ICANN's mission to ensure stable and secure operation of the Internet's unique identifier systems. It affects current .name registrants and raises broader concerns about registry accountability and the reliability of domain ownership. The proposal specifically targets third-level .name domains, not second-level domains like dvt.name, which remain unaffected. Verisign has not mentioned whether it will reserve the released second-level domains for a period to prevent squatting, leaving a significant gap in the proposal.

hackernews · pavel_lishin · Sep 3, 14:54 · [Discussion](https://news.ycombinator.com/item?id=49550772)

**Background**: The .name TLD was designed to support personal names, allowing registrations at both the second level (e.g., jane.name) and third level (e.g., jane.doe.name). Third-level registrations were part of the original scheme but have seen low adoption. Verisign operates the .name registry under contract with ICANN, and changes to domain policies require ICANN approval.

<details><summary>References</summary>
<ul>
<li><a href="https://support.opensrs.com/support/solutions/articles/201000063568--name-domain-policies">A Domain Resellers Guide to . NAME Domain Policies : OpenSRS...</a></li>
<li><a href="https://webmasters.stackexchange.com/questions/85024/clarify-terminology-top-level-domain-second-level-domain-and-apex-domain">Clarify terminology: top level domain , second level domain , and apex...</a></li>
<li><a href="https://support.enom.com/support/solutions/articles/201000127176--name-domain-policies">NAME Domain Policies : Enom Customer Support</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about the termination, with some suggesting that Verisign should stop new registrations but honor existing ones. Others noted the contradiction with ICANN's mission and the risk of domain squatting, while some clarified that second-level domains are not affected. A few drew parallels to the inherent risks of leased domain names.

**Tags**: `#ICANN`, `#domain names`, `#policy`, `#internet governance`, `#Verisign`

---

<a id="item-3"></a>
## [Porting a 1993 Amiga Game to Godot Using an LLM](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

The developer successfully ported his 1993 Amiga game, originally written in MC68000 assembly, to the Godot engine using Claude Fable 5, achieving a working game in one evening. The LLM assembled the code with vasm until the binary was byte-identical to the original, except for a 108-byte discrepancy due to the original AsmOne memory snapshot. This demonstrates a practical, high-value use case for LLMs in retrocomputing and legacy code porting, potentially lowering the barrier for preserving and modernizing classic software. It also highlights the capability of LLMs to handle low-level assembly and produce byte-identical output, which could inspire similar projects in game preservation and migration. The original game was built in Baghdad in 1993 using MC68000 assembly and assembled with AsmOne, which assembles into memory; the shipped files were snapshots of the running game, not clean assembler output. The LLM used vasm on the developer's Mac to iterate until the binary matched the original, except for the 108-byte mismatch, which the developer never independently verified.

hackernews · rabahs · Sep 3, 14:28 · [Discussion](https://news.ycombinator.com/item?id=49550375)

**Background**: The Amiga is a classic personal computer from the 1980s-90s, known for its custom hardware and assembly programming. MC68000 assembly is the low-level language for the Motorola 68000 CPU used in the Amiga. vasm is a portable assembler that can target multiple CPUs, while AsmOne is an integrated assembler environment for the Amiga that assembles into memory. Porting such legacy code typically requires manual rewriting, but LLMs can assist in translating assembly to modern languages like GDScript in Godot.

<details><summary>References</summary>
<ul>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>
<li><a href="https://aminet.net/package/dev/asm/ASM-One">Aminet - dev/asm/ASM-One.lha Asm One 1.02 Manual : Rune Gram-Madsen : Free Download ... ASM-One Macro Assembler - HandWiki Commodore Software - ASM-One v1.02 Manual ASM-One Page - theflamearrows.info ASM-One Macro Assembler - EverybodyWiki Bios & Wiki Asm One 1.02 Manual : Free Download, Borrow, and Streaming ...</a></li>
<li><a href="https://en.wikibooks.org/wiki/68000_Assembly">68000 Assembly - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**Discussion**: Commenters expressed admiration for the original assembly work and shared similar experiences using LLMs to port retro games, such as converting a ZX81 game to Go. Some discussed technical details like the use of hardware registers versus system-friendly calls, and others noted the game's resemblance to 'Gods: Into the Wonderful'.

**Tags**: `#LLM`, `#retrocomputing`, `#game development`, `#code porting`, `#Godot`

---