---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 31 items, 2 important content pieces were selected

---

1. [Researcher Demonstrates Unlocking Any Car from Major Automaker Worldwide](#item-1) ⭐️ 8.0/10
2. [Herb Sutter analyzes Stroustrup vs. committee conflict over C++ contracts](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Researcher Demonstrates Unlocking Any Car from Major Automaker Worldwide](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/) ⭐️ 8.0/10

A security researcher published a demonstration showing a method to unlock cars from a major automaker (likely Toyota/Lexus) in most parts of the world, as detailed in a blog post on shubs.io. The post includes a video demo and has sparked significant discussion on automotive security and connected-car privacy. This disclosure highlights serious security weaknesses in modern connected cars, potentially affecting millions of vehicles and raising concerns about unauthorized access and privacy. It underscores the growing need for robust cybersecurity in the automotive industry as cars become more software-dependent. The exact technical method is not detailed in the provided content, but community comments suggest the attack may target specific models like the fifth-generation RAV4, and older models such as the 2009 Camry may not be affected. The claim of 'any car' is likely an overstatement, and the linked follow-up article by Sam Curry provides additional context on the worldwide scope.

hackernews · infosecau · Nov 9, 00:10 · [Discussion](https://news.ycombinator.com/item?id=50419215)

**Background**: Modern vehicles rely on electronic systems such as CAN bus for internal communication, which often lack strong authentication and can be vulnerable to injection attacks. Keyless entry systems, while convenient, expand the attack surface through relay attacks and other exploits. Connected cars also raise privacy concerns as they collect and transmit data, sometimes without clear user control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/76114830/An_Extended_Survey_on_Vehicle_Security">(PDF) An Extended Survey on Vehicle Security</a></li>
<li><a href="https://www.securityscientist.net/blog/12-questions-and-answers-about-keyless-entry-relay/">12 Questions and Answers About Keyless Entry Relay</a></li>
<li><a href="https://blog.usro.net/2024/10/how-to-permanently-disable-telematics-on-your-bmw-make-your-car-forget-its-a-spy/">How to Permanently Disable Telematics on Your BMW: Make Your...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about the growing control automakers have over connected cars, comparing them to smartphones that are always tracked and hard to repair. Some questioned the 'any car' claim, noting that older models like the 2009 Camry likely aren't affected, while others appreciated the linked follow-up article on the worldwide scope. One user warned about loud bleeps in the video.

**Tags**: `#automotive-security`, `#vulnerability-disclosure`, `#privacy`, `#connected-cars`, `#infosec`

---

<a id="item-2"></a>
## [Herb Sutter analyzes Stroustrup vs. committee conflict over C++ contracts](https://isocpp.org/files/papers/P4454R0.pdf) ⭐️ 8.0/10

Herb Sutter published a PDF paper (P4454R0) summarizing the conflict between C++ creator Bjarne Stroustrup and the ISO C++ committee over the proposed contracts feature for C++26, and outlining possible paths forward. The paper is described as a diplomatic summary that lists six options for C++26, including skipping the standard, removing contracts, or negotiating a compromise. This dispute highlights a governance tension in the C++ standardization process, where the language's creator can strongly influence the direction of major features. The outcome will affect whether contracts ship in C++26 and how future large features are designed and approved, impacting all C++ developers and implementers. The paper reportedly lists six possible paths forward for C++26, such as skipping an official C++26 standard and rolling features into C++29, removing contracts from C++26, or negotiating a compromise. Stroustrup's objections are detailed in a separate document titled 'Contracts_fundamental_flaws.pdf'.

hackernews · acossta · Nov 8, 23:28 · [Discussion](https://news.ycombinator.com/item?id=50418818)

**Background**: C++ is standardized by the ISO C++ committee (WG21), which develops features through study groups and consensus votes. Contracts are a proposed feature that would allow programmers to specify preconditions, postconditions, and assertions directly in code, with various runtime checking modes. Bjarne Stroustrup, the creator of C++, remains an active committee member and has raised concerns about the current contracts design.

<details><summary>References</summary>
<ul>
<li><a href="https://isocpp.org/files/papers/P2900R4.pdf">Contracts for C++</a></li>
<li><a href="https://en.wikipedia.org/wiki/C++26">C++26 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that Stroustrup's objections are sensible and that Sutter's summary is diplomatic and well-written. Some argue that the vote failure reflects broader weariness with large, half-baked features like modules, not just Stroustrup's opposition, while others question whether contracts offer enough benefit over plain assertions.

**Tags**: `#C++`, `#language-design`, `#contracts`, `#standards`, `#programming-languages`

---