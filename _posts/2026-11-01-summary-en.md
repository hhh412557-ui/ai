---
layout: default
title: "Horizon Summary: 2026-11-01 (EN)"
date: 2026-11-01
lang: en
---

> From 17 items, 3 important content pieces were selected

---

1. [Critical Linux TCP Use-After-Free CVE-2026-98432 (CVSS 9.8) Lacks Distro Patches](#item-1) ⭐️ 9.0/10
2. [HackerTube: A YouTube-style Interface Built from Hacker News Video Recommendations](#item-2) ⭐️ 8.0/10
3. [Jepsen finds severe transactional anomalies in ParticleDB 1.1.4](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Critical Linux TCP Use-After-Free CVE-2026-98432 (CVSS 9.8) Lacks Distro Patches](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf) ⭐️ 9.0/10

A critical use-after-free vulnerability in the Linux kernel's IPv4 TCP handshake path, tracked as CVE-2026-98432 with a CVSS score of 9.8, has been publicly detailed. The flaw was fixed upstream on October 15, 2026, but major distributions like Ubuntu and Red Hat Enterprise Linux have not yet released patches. This vulnerability affects a core networking component of Linux, potentially allowing remote code execution or denial of service, and its high severity score underscores the risk. The delay in patching by major enterprise distributions leaves many servers exposed and raises concerns about distribution response times. Exploitation requires multiple CPU cores to process packets concurrently, so single-core systems or those with packet processing pinned to one core are immune. Internet-based exploitation is unlikely because most ISP routers drop packets with IP options, and dropping such packets locally helps but is not a complete mitigation according to Red Hat.

hackernews · oger · Oct 31, 19:16 · [Discussion](https://news.ycombinator.com/item?id=50319143)

**Background**: A use-after-free vulnerability occurs when a program continues to use a pointer after freeing the memory it points to, which can lead to arbitrary code execution or crashes. CVE-2026-98432 specifically affects the Linux kernel's handling of IPv4 TCP handshakes, where a race condition between processors can cause a shared IP options object to be freed prematurely. CVSS is a standardized scoring system for assessing the severity of security vulnerabilities, with scores of 9.0 and above considered critical.

<details><summary>References</summary>
<ul>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux 's October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>
<li><a href="https://www.penligent.ai/hackinglabs/cve-2026-98432/">CVE - 2026 - 98432 Linux TCP Flaw, Ubuntu Patch and Mitigation Status</a></li>
<li><a href="https://getrff.com/blog/cve-2026-98432-linux-tcp-ip-options-block/">CVE - 2026 - 98432 : how to block the Linux TCP bug until Ubuntu and...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the vulnerability is Linux-specific and does not affect BSD, macOS, or Windows. They also noted that MPTCP is not required, exploitation over the internet is unlikely due to IP options filtering, and multi-core systems are necessary for exploitation. There was sharp criticism of Ubuntu and RHEL for not yet providing patches, with some questioning their suitability for servers.

**Tags**: `#linux`, `#security`, `#vulnerability`, `#tcp`, `#cve`

---

<a id="item-2"></a>
## [HackerTube: A YouTube-style Interface Built from Hacker News Video Recommendations](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 8.0/10

Andrej Karpathy launched HackerTube, a YouTube-style interface that aggregates 6,454 videos recommended across 39,834 Hacker News comments since 2007, offering a curated, non-algorithmic alternative to mainstream video feeds. This project demonstrates the value of community-driven curation over engagement-optimized algorithms, resonating with users who seek serendipitous and high-quality content. It highlights a growing demand for alternative content discovery systems that prioritize user interests over addictive design. The site uses a YouTube-like UI but sources videos solely from HN comments, resulting in a collection of 6,454 videos. Community feedback suggests adding a sort by new-to-old, and the project is noted as a novel, high-engagement tool with 1013 points and 312 comments on HN.

hackernews · karpathy · Oct 31, 19:56 · [Discussion](https://news.ycombinator.com/item?id=50319510)

**Background**: Hacker News (HN) is a social news website focusing on computer science and entrepreneurship, where users submit and vote on content. Algorithmic curation refers to the use of recommender systems to select and personalize content based on user data, often optimizing for engagement. HackerTube bypasses such algorithms by relying on explicit recommendations from the HN community.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/?ref=dtf.ru">Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Algorithmic_curation">Algorithmic curation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters appreciate the refreshing lack of clickbait and influencer content, with some expressing a desire for more serendipitous discovery beyond personalized feeds. There is also a suggestion to add sorting options, and overall sentiment is highly positive.

**Tags**: `#content-curation`, `#hacker-news`, `#recommendation-systems`, `#youtube`, `#community`

---

<a id="item-3"></a>
## [Jepsen finds severe transactional anomalies in ParticleDB 1.1.4](https://jepsen.io/analyses/particledb-1.1.4) ⭐️ 8.0/10

Jepsen analyzed ParticleDB versions 1.1.4 through 1.1.18.11.rc-22 and found frequent, profound transactional anomalies, including lost writes, internal consistency violations, G1a (Aborted Read), G1b (Intermediate Read), and P4 (Lost Update), despite the database claiming Postgres compatibility and full ACID compliance. Jepsen recommends halting deployment and migrating to other databases. This analysis exposes critical reliability flaws in a database marketed for AI workloads, potentially affecting users who rely on its ACID guarantees. It underscores the importance of rigorous testing and the risks of deploying systems with unverified correctness claims. Jepsen reported 96 issues, ranging from crashes and deadlocks to bizarre behaviors like partially-invisible rows, WHERE 4 = 5, dropped tables re-emerging, and strings turning into integers. ParticleDB's home page advertised a TLA+ formal proof, but no specification was available during testing.

hackernews · aphyr · Oct 31, 13:39 · [Discussion](https://news.ycombinator.com/item?id=50316100)

**Background**: Jepsen is an open-source framework for testing distributed systems' consistency and partition tolerance by simulating network failures and other faults. ParticleDB is a multi-model database designed for AI workloads, claiming Postgres compatibility and full ACID compliance. ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee reliable transaction processing in databases.

<details><summary>References</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://jepsen.io/">Jepsen - Distributed Systems Safety Research</a></li>
<li><a href="https://particledb.ai/">ParticleDB | The database for AI agents</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock at the severity of the issues, with some attributing them to 'vibecoding' (AI-generated code) and discussing the dichotomy between correct-by-construction and incorrect-by-construction software. Others noted the absence of the promised TLA+ proof and the bizarre bugs like 'WHERE 4 = 5'.

**Tags**: `#databases`, `#distributed-systems`, `#correctness`, `#jepsen`, `#transactional-consistency`

---