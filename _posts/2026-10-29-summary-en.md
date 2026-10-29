---
layout: default
title: "Horizon Summary: 2026-10-29 (EN)"
date: 2026-10-29
lang: en
---

> From 37 items, 3 important content pieces were selected

---

1. [Qwenputer: A Deterministic RISC-V CPU Emulated Inside Qwen3.5](#item-1) ⭐️ 8.0/10
2. [Fingerprinting Script Mistakenly Flagged as Bioweapon by LLMs](#item-2) ⭐️ 8.0/10
3. [Alpine Linux Re-releases GitLab Image to Patch Ruby Regex RCE](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwenputer: A Deterministic RISC-V CPU Emulated Inside Qwen3.5](https://divagr.com/blog/qwenputer) ⭐️ 8.0/10

A developer published a project called Qwenputer that implements a functioning, deterministic RISC-V CPU entirely inside the Qwen3.5 large language model, and even added a filesystem on top of it. This project demonstrates that LLMs can emulate deterministic computing systems, blurring the line between language models and traditional emulators, and could inspire new approaches to program execution, verification, and agent design. The CPU is deterministic, meaning identical inputs produce identical outputs, which is notable because LLM inference is often nondeterministic; the implementation runs inside Qwen3.5, a recent Qwen model available in sizes like 2B and 35B-A3B.

hackernews · csmantle · Oct 29, 00:25 · [Discussion](https://news.ycombinator.com/item?id=50282838)

**Background**: RISC-V is an open-source instruction set architecture (ISA) that is freely available for anyone to design and implement CPUs. Large language models like Qwen3.5 are neural networks trained on vast text data to predict the next token, and they are not normally used to execute machine instructions. Emulating a CPU inside an LLM means encoding the CPU's state and instruction execution as text or tokens that the model processes, which is an unconventional and creative use of LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen/Qwen3.5-2B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC - V - Wikipedia</a></li>
<li><a href="https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/">Defeating Nondeterminism in LLM Inference - Thinking Machines Lab</a></li>

</ul>
</details>

**Discussion**: Commenters found the project fun and impressive, with jokes about an agent misusing it for paper-clip maximization and references to a 'demonic evil Qwen' neuron. Others pointed to related work like implementing WASM in a transformer and wondered if the approach could compete in AdderBoard, a challenge to build tiny transformers that add large numbers.

**Tags**: `#LLM`, `#RISC-V`, `#emulation`, `#Qwen`, `#creative coding`

---

<a id="item-2"></a>
## [Fingerprinting Script Mistakenly Flagged as Bioweapon by LLMs](https://nullpt.rs/fingerprinting-bioweapons) ⭐️ 8.0/10

A blog post on nullpt.rs investigates why a browser fingerprinting script is being flagged as bioweapon-related by large language models (LLMs), sparking a discussion on LLM safety filters and obfuscation. This highlights the challenge of false positives in LLM safety filters, which can hinder legitimate security research and development, and underscores the need for more context-aware moderation. The fingerprinting script likely contains patterns or keywords that trigger safety classifiers, and the community discussion reveals that some models like GLM-5.3 comply while others block, indicating variability in safety implementations.

hackernews · hazebooth · Oct 28, 17:13 · [Discussion](https://news.ycombinator.com/item?id=50276998)

**Background**: Browser fingerprinting is a technique that collects attributes from a user's browser to create a unique identifier for tracking, often used for fraud detection and analytics. LLMs are increasingly used to analyze code and logs, but their safety filters can mistakenly flag benign content as malicious, causing false positives.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/fingerprintjs/fingerprintjs">GitHub - fingerprintjs/fingerprintjs: The most advanced free ... FingerprintJS: The Browser ID Tool Every Developer Needs Browser Fingerprinting in JavaScript: A Developer's ... Fingerprintjs2 by eisman Thumbmark — Visitor Identification at Scale Browser Fingerprint Detection and Anti-Tracking - arXiv.org</a></li>
<li><a href="https://community.openai.com/t/recent-safety-filter-update-causing-high-false-positives-on-legitimate-academic-ml-research/1410325">Recent Safety Filter Update Causing High False Positives on ...</a></li>
<li><a href="https://arxiv.org/html/2410.02916v3">LLM Safeguard is a Double-Edged Sword: Exploiting False ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared anecdotes about watermarks causing email quarantine and noted that some LLMs like GLM-5.3 are more permissive, while others joked about an arms race between obfuscation and detection.

**Tags**: `#fingerprinting`, `#LLM safety`, `#obfuscation`, `#adversarial ML`, `#web security`

---

<a id="item-3"></a>
## [Alpine Linux Re-releases GitLab Image to Patch Ruby Regex RCE](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html) ⭐️ 8.0/10

Alpine Linux published a security incident write-up detailing an attempted exploitation of CVE-2026-97229, an integer overflow in Ruby's Onigmo regex engine that enables remote code execution, and re-released its alpinelinux/gitlab:19.3.6 container image on October 27 with Ruby 3.3.13 to include the fix. The vulnerability resides in Ruby's regex engine rather than GitLab's own code, so any program that compiles regular expressions from untrusted input is exposed, not just GitLab; this highlights the broad supply-chain risk of language runtimes and the challenges of patching container images built from source. The fix is in Ruby 3.3.13 (also 3.4.12 and 4.0.9), and any 19.3.6 image pulled before October 27 or older tags remain vulnerable; Alpine re-released the fixed image under the same 19.3.6 tag rather than bumping the version, which some community members criticized.

hackernews · sashk · Oct 28, 23:45 · [Discussion](https://news.ycombinator.com/item?id=50282544)

**Background**: CVE-2026-97229 is an integer overflow in Onigmo, the regular expression engine built into Ruby, which can be triggered by a specially crafted regex in GitLab CI/CD configurations to achieve unauthenticated remote code execution. GitLab patched the issue in its own packages, but third-party images like Alpine's initially used standard Ruby without the patch. Ruby released fixed versions (4.0.9, 3.4.12, 3.3.13) on October 23, 2026, addressing this and several related CVEs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/">Regexp compilation fixes related to GitLab's CVE-2026-89078 ...</a></li>
<li><a href="https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html">Ruby Fixes Three Regex Engine Bugs Responsible for Four ...</a></li>
<li><a href="https://www.rapid7.com/blog/post/ra-gitlab-ci-cd-regex-integer-overflow-technical-analysis-cve-2026-97229/">Rapid7 Analysis: GitLab CI/CD Regex Integer Overflow (CVE ...</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the flaw is in Ruby's regex engine, affecting any program compiling untrusted regexes, and criticized Alpine for re-releasing a fixed image under the same 19.3.6 tag instead of bumping the version. Others expressed frustration with recurring C library vulnerabilities and 'not invented here' syndrome, while praising the incident write-up for its transparency about unknowns and potential data leakage.

**Tags**: `#security`, `#vulnerability`, `#GitLab`, `#Ruby`, `#containers`

---