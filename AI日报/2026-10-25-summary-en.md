---
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 15 items, 2 important content pieces were selected

---

1. [Goose: A New Programming Language Without a Heap](#item-1) ⭐️ 8.0/10
2. [Brotli RCE dubbed HTTP2Shell affects many HTTP libraries and apps](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Goose: A New Programming Language Without a Heap](https://aardappel.github.io/goose/) ⭐️ 8.0/10

Aardappel (Wouter van Oortmerssen) released Goose, a new systems programming language that eliminates the heap by using compiler-managed data stacks and resizable fields, enabling efficient memory mapping and parsing. The language gained attention after John Carmack endorsed it on Twitter, sparking a Hacker News AMA and 186 substantive comments. Goose challenges conventional memory management by removing the heap entirely, offering memory safety without garbage collection, reference counting, or lifetime annotations. This could significantly impact systems programming by simplifying memory layout and enabling direct memory mapping of data structures, potentially outperforming C++ and Rust in parsing tasks. Each data stack is a large address-space reservation with a bump pointer, and at most one resizable value is live per stack and always on top, so growth never moves data or checks capacity. Memory is freed with a single store when scope ends, but the lack of garbage collection requires careful memory management for long-running programs.

hackernews · bobbydigitales · Oct 24, 19:06 · [Discussion](https://news.ycombinator.com/item?id=50224100)

**Background**: Goose is designed by Aardappel, known for the Wren scripting language and the Lobster programming language. Traditional systems languages like C++ and Rust manage dynamic memory via heap allocations, which can be slow and complex. Goose introduces data stacks and resizable fields as an alternative, aiming to make parsing and memory mapping more efficient by allowing direct use of network data without copying.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/aardappel/goose/tree/master/">GitHub - aardappel/goose: The Goose Programming Language</a></li>
<li><a href="https://news.lavx.hu/article/goose-programming-language-claims-speed-wins-over-c-and-rust-with-zero-heap-allocations">Goose Programming Language Claims Speed Wins Over C++ and ...</a></li>
<li><a href="https://news.lavx.hu/article/goose-is-a-memory-safe-systems-language-without-a-heap">Goose Is a Memory-Safe Systems Language Without a Heap</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was lively, with the author answering questions in an AMA. Commenters praised the practical design, with some suggesting additions like lightweight processes and CSP-style typed communication, while others raised concerns about representing dynamically sized values and the lack of garbage collection requiring careful memory management.

**Tags**: `#programming-languages`, `#memory-management`, `#compilers`, `#systems-programming`, `#hackernews`

---

<a id="item-2"></a>
## [Brotli RCE dubbed HTTP2Shell affects many HTTP libraries and apps](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

A critical remote code execution vulnerability in Brotli decompression, previously known as Node2Shell and now rebranded as HTTP2Shell (CVE-2026-111497), has been found to impact numerous HTTP libraries and applications beyond Node.js and Bun. This vulnerability is significant because Brotli decompression is widely used in HTTP servers and clients, so a single flaw can expose a large attack surface; any application that decompresses attacker-controlled Brotli data is at risk and should patch immediately. The flaw allows unauthenticated remote code execution when an application decompresses malicious Brotli data, and while HTTP is the most common vector, manual Brotli decoding in other contexts is also vulnerable; patched versions of affected libraries have been released.

hackernews · theanonymousone · Oct 24, 08:06 · [Discussion](https://news.ycombinator.com/item?id=50219177)

**Background**: Brotli is a lossless compression algorithm developed by Google, commonly used in HTTP to compress responses and sometimes requests. A vulnerability in its decompression logic can lead to memory corruption and code execution, making it a serious security concern for web infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497">Node2Shell: Node.js Brotli vulnerability allows remote code execution...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brotli">Brotli - Wikipedia</a></li>
<li><a href="https://github.com/google/brotli">GitHub - google/brotli: Brotli compression format · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters criticized the name HTTP2Shell as overly broad and meaningless, preferring alternatives like Brotli2Shell or Broccoli2Shell. Some questioned why the bug wasn't recognized as a security issue when reported earlier, and others noted that Brotli-compressed request bodies are an obscure feature, so the actual impact may be narrower than sensationalized.

**Tags**: `#security`, `#vulnerability`, `#brotli`, `#http`, `#rce`

---