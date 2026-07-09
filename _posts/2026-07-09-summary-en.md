---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 79 items, 3 important content pieces were selected

---

1. [Bun Rewritten from Zig to Rust Using AI](#item-1) ⭐️ 9.0/10
2. [TypeScript 7.0 Rewritten in Go, Up to 11.9x Faster](#item-2) ⭐️ 9.0/10
3. [OpenAI Audit Finds 30% of SWE-Bench Pro Tasks Broken](#item-3) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [Bun Rewritten from Zig to Rust Using AI](https://bun.com/blog/bun-in-rust) ⭐️ 9.0/10

Bun's team used AI to rewrite the entire runtime from Zig to Rust, achieving a 20% smaller binary size, 5% performance improvement, and enhanced memory safety and stability. This demonstrates that AI-assisted rewrites can be cost-effective and produce significant improvements, potentially accelerating the adoption of memory-safe languages like Rust in systems programming. The rewrite was done by one engineer using Fable and Claude Code, which would have taken a team a year manually. The AI-generated code was carefully reviewed and tested.

hackernews · afturner · Jul 8, 21:49 · [Discussion](https://news.ycombinator.com/item?id=48837877)

**Background**: Bun is a fast all-in-one JavaScript runtime that was originally written in Zig, a systems programming language focused on simplicity and performance. Rust is another systems language known for memory safety without garbage collection. AI-assisted code rewriting uses large language models to translate code between languages.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://arstechnica.com/ai/2026/03/ai-can-rewrite-open-source-code-but-can-it-rewrite-the-license-too/">AI can rewrite open source code—but can it rewrite the ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the rewrite reflects poorly on Zig, as a naive AI rewrite fixed memory leaks and improved stability. Some argued that AI-assisted rewrites make it harder to justify hiring expensive engineers for such tasks, while others praised the strong test suite that enabled the AI to succeed.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#AI-assisted rewrite`, `#performance`

---

<a id="item-2"></a>
## [TypeScript 7.0 Rewritten in Go, Up to 11.9x Faster](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft announced TypeScript 7.0, featuring a complete rewrite of the compiler in Go, delivering up to 11.9x faster type-checking on large codebases like VS Code. The release also includes JSDoc syntax improvements and enhanced editor support via the Language Server Protocol. This dramatic performance improvement makes TypeScript significantly more practical for large-scale projects, reducing build and type-checking times from minutes to seconds. The Go rewrite also sets a new precedent for compiler performance in the JavaScript ecosystem, potentially influencing future tooling development. Benchmarks show TypeScript 7.0 reduces type-check time for VS Code from 125.7s to 10.6s (11.9x), Sentry from 139.8s to 15.7s (8.9x), and Playwright from 12.8s to 1.47s (8.7x). The rewrite is a port of the existing TypeScript compiler to Go, preserving type-checking semantics while enabling native multithreading.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, widely used for large-scale web development. The original TypeScript compiler was written in TypeScript itself, which could become a bottleneck on large codebases. By rewriting the compiler in Go, a language known for fast compilation and efficient concurrency, Microsoft achieves significant speedups without altering the language's semantics.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/">Announcing TypeScript 7.0 - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://betterstack.com/community/guides/scaling-nodejs/typescript-7-go-rewrite/">TypeScript 7.0: New Features and the Go-Powered Compiler Rewrite</a></li>
<li><a href="https://www.devbolt.dev/blog/typescript-7-go-rewrite">TypeScript 7.0: What the Go Rewrite Means for Every Developer</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly positive, with many praising the team's engineering feat and the dramatic speed improvements. Some users expressed excitement about the JSDoc improvements and the continued focus on type safety, while others humorously anticipated a future Rust rewrite.

**Tags**: `#TypeScript`, `#performance`, `#programming languages`, `#compiler`, `#Microsoft`

---

<a id="item-3"></a>
## [OpenAI Audit Finds 30% of SWE-Bench Pro Tasks Broken](https://x.com/OpenAI/status/2074972179385720836) ⭐️ 9.0/10

OpenAI audited SWE-Bench Pro, a widely used AI coding benchmark, and found that 30% of its tasks are broken, leading them to retract their previous recommendation for the research community to use it. This finding undermines the reliability of SWE-Bench Pro as a measure of frontier coding capability, potentially affecting how AI coding models are evaluated and compared across the industry. The audit used model-based investigator agents alongside independent reviews from five experienced software engineers to examine tasks at scale while maintaining expert judgment.

twitter · OpenAI · Jul 8, 21:41

**Background**: SWE-Bench Pro is a benchmark designed to evaluate AI agents on realistic software engineering tasks, addressing issues like data contamination. Benchmarks like these are critical for tracking progress in AI coding capabilities, but their validity depends on task quality and relevance.

<details><summary>References</summary>
<ul>
<li><a href="https://labs.scale.com/leaderboard/swe_bench_pro_public">SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale</a></li>
<li><a href="https://arxiv.org/abs/2502.01236">Eliciting Language Model Behaviors with Investigator Agents Eliciting Language Model Behaviors with Investigator Agents Eliciting Language Model Behaviors with Investigator Agents Eliciting Language Model Behaviors with Investigator Agents Automatically Jailbreaking Frontier Language Models with ... Eliciting Language Model Behaviors with Investigator Agents OpenAI on X: "To audit SWE-Bench Pro, we used model-based ...</a></li>

</ul>
</details>

**Tags**: `#AI benchmarks`, `#coding`, `#OpenAI`, `#software engineering`, `#evaluation`

---