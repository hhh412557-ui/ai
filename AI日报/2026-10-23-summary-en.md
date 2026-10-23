---
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 24 items, 4 important content pieces were selected

---

1. [Anthropic: LLMs Make Formal Verification Feasible at Larger Scale](#item-1) ⭐️ 8.0/10
2. [Quad9 to Exit France After Court Fines It for Not Blocking Pirated Content](#item-2) ⭐️ 8.0/10
3. [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agents](#item-3) ⭐️ 8.0/10
4. [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic: LLMs Make Formal Verification Feasible at Larger Scale](https://www.anthropic.com/research/formal-verification) ⭐️ 8.0/10

Anthropic published research arguing that large language models (LLMs) now make formal software verification feasible at a much larger scale than before. The work highlights how LLMs can assist in generating proofs and finding bugs in mature software, and it sparked a substantial Hacker News discussion with 218 points and 121 comments. Formal verification has traditionally been expensive and limited to small, critical codebases, so making it scalable with LLMs could significantly improve software security and reliability. This matters for developers of safety-critical systems and could reshape how proofs are integrated into everyday software engineering. The research acknowledges that while agent-generated proofs are as valid as any other proof of the same theorem, it remains uncertain whether agents can scale their verbose proof style to more complex programs; experience from projects like MachCSL suggests they may hit a complexity wall. A practitioner in the discussion reported using LLMs to prove equivalence between Rust and C code in Lean for about 12% of a Postgres rewrite (~70k lines of C), finding only minor behavioral differences.

hackernews · johnbender · Oct 22, 22:54 · [Discussion](https://news.ycombinator.com/item?id=50202217)

**Background**: Formal verification is the process of using mathematical methods to prove that a program satisfies a formal specification of its behavior, ensuring correctness beyond testing. Lean is a proof assistant and functional programming language based on dependent type theory, often used for formalizing mathematics and verifying software. LLMs are AI models trained on vast text that can generate code and proofs from natural language instructions, making them promising tools for automating tedious verification tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://www.anthropic.com/research/formal-verification">LLMs are making formal software verification feasible at a ...</a></li>

</ul>
</details>

**Discussion**: The discussion was rich and varied: one commenter predicted LLMs will push development toward deterministic declarative languages rather than verifying imperative code, while another highlighted the appendix's caveat about agents hitting a complexity wall with verbose proofs. A practitioner shared concrete success using LLMs to prove Rust-C equivalence in Lean, and another commenter expressed anxiety about AI displacing programming careers.

**Tags**: `#formal-verification`, `#LLMs`, `#software-engineering`, `#Lean`, `#programming-languages`

---

<a id="item-2"></a>
## [Quad9 to Exit France After Court Fines It for Not Blocking Pirated Content](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 8.0/10

Quad9, a major public DNS resolver, announced it will exit France after a French court fined it for contempt of court for failing to block pirated content. The plaintiff, Sony Music Entertainment GmbH, used a VPN to circumvent Quad9's geoIP blocking and then successfully argued noncompliance, leading to the fine. This case highlights the growing conflict between DNS resolvers and content-blocking mandates, raising concerns about legal overreach and the feasibility of geo-blocking. It could set a precedent for how DNS providers are held liable for content they do not control, affecting internet governance and privacy globally. Quad9 plans to use geoIP filters to block French users after November 24, but acknowledges that geoIP blocking is insufficient for selectively denying resolution for certain names. The fine was for contempt of court after Sony circumvented the blocking via VPN from Germany.

hackernews · farrokhi · Oct 22, 14:32 · [Discussion](https://news.ycombinator.com/item?id=50195959)

**Background**: Quad9 is a free, non-profit DNS resolver launched in 2017 that focuses on security and privacy by blocking malicious domains. DNS resolvers translate human-readable domain names into IP addresses, and content-blocking mandates require them to block access to certain sites, such as those hosting pirated material. France has been active in ordering DNS providers to block piracy sites, previously targeting Google, Cloudflare, and Cisco.

<details><summary>References</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/what-is-dns/">What is DNS ? | Learning Center - Cloudflare</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_Name_System">Domain Name System - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion includes comments from Quad9's CTO, who explains the dilemma of geo-blocking and notes they will likely use geoIP filters to block French users. Commenters express frustration with the legal outcome, comparing DNS resolvers to phone books and criticizing the plaintiff for circumventing protections and then suing. Some suggest that DNS resolvers should stop resolving domains of companies that sue them.

**Tags**: `#DNS`, `#privacy`, `#internet governance`, `#legal`, `#content blocking`

---

<a id="item-3"></a>
## [NVIDIA OpenShell: Secure Runtime for Autonomous AI Agents](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA has released OpenShell, an open-source runtime designed to safely run fleets of autonomous AI agents with controlled access to files, packages, APIs, and credentials. The project quickly gained attention on Hacker News, sparking a substantial discussion (343 points, 181 comments) about balancing agent capabilities with security and data exfiltration risks. As AI agents become more autonomous and are deployed in production, providing them with necessary access while preventing data breaches and unintended actions is a critical challenge. OpenShell addresses this by offering a sandboxed environment, which could accelerate enterprise adoption of agentic AI by mitigating security concerns. OpenShell uses container-based isolation to restrict network access by domain, swap credentials, and limit file system access, but it does not completely eliminate data exfiltration risks if agents are granted access to sensitive data. The project is positioned as a batteries-included solution for managing agent containers, though users may need additional layers for team policies and secure git usage.

hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

**Background**: AI agent sandboxing involves isolating code execution in secure environments to prevent unauthorized access, data breaches, and system compromise. As agents are given more autonomy to read files, install packages, and call APIs, the risk of prompt injection and data exfiltration increases, making runtime security controls essential for safe deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor... — Northflank</a></li>
<li><a href="https://callsphere.ai/blog/ai-agent-sandboxing-security-best-practices">AI Agent Sandboxing and Security : Best Practices... | CallSphere Blog</a></li>
<li><a href="https://securetom.com/blog/ai-agent-sandboxing-enterprise-security-guide">AI Agent Sandboxing : Enterprise Security Guide 2026 | SecureTom</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that running agents in containers is essential, but some question whether OpenShell can truly balance capability and security, calling the marketing an 'oxymoron.' Others share practical experiences, noting that preventing data exfiltration remains an unsolved problem and that additional layers for policy management are needed.

**Tags**: `#AI agents`, `#security`, `#sandboxing`, `#NVIDIA`, `#runtime`

---

<a id="item-4"></a>
## [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 8.0/10

Anthropic announced that it is donating its Agent Skills standard to the Agentic AI Foundation (AAIF) under the Linux Foundation, following its earlier donation of the Model Context Protocol (MCP). The AAIF was co-founded by Anthropic, Block, and OpenAI last year. This move transfers control of a key agent interoperability standard to a vendor-neutral body, which could accelerate adoption and ensure that agent skills remain open and cross-platform. It signals a broader trend of standardizing agentic AI tooling under open governance, benefiting developers and the wider ecosystem. Agent Skills was originally released by Anthropic as an open standard on December 18, 2025, and has since been adopted by multiple agent products. The donation means the standard will now be developed under the AAIF's community-driven, vendor-neutral process.

rss · Simon Willison · Oct 22, 18:09

**Background**: Agent Skills is a format for packaging specialized capabilities and expertise that AI agents can load from files and folders, enabling cross-platform portability. MCP is an open standard for connecting AI applications to external data sources and tools. The Linux Foundation is a nonprofit that hosts open-source projects with neutral governance, and the AAIF was created to steward agentic AI standards like MCP and AGENTS.md.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation">Donating Agent Skills to the Agentic AI Foundation \ Anthropic</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#agentic-ai`, `#standards`, `#anthropic`, `#open-source-governance`, `#ai-agents`

---