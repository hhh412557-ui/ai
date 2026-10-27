---
layout: default
title: "Horizon Summary: 2026-10-27 (EN)"
date: 2026-10-27
lang: en
---

> From 27 items, 3 important content pieces were selected

---

1. [OpenAI preprint claims to disprove the Exponential Time Hypothesis](#item-1) ⭐️ 10.0/10
2. [OpenAI claims disproof of Exponential Time Hypothesis](#item-2) ⭐️ 9.0/10
3. [Anthropic Files S-1 Disclosing $500B+ in Infrastructure Commitments](#item-3) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [OpenAI preprint claims to disprove the Exponential Time Hypothesis](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) ⭐️ 10.0/10

OpenAI has published a preprint claiming to disprove the Exponential Time Hypothesis (ETH), a foundational conjecture in computational complexity theory. The company is asking academics to verify the work, with future review to be done in collaboration with complexity researchers Russell Impagliazzo, Ramamohan Paturi, and Ryan Williams. If correct, this would be a paradigm-shifting result in complexity theory, as ETH is a stronger assumption than P ≠ NP and underpins many conditional lower bounds. It could also have implications for algorithm design and our understanding of problems like SAT solving. The result does not imply that NP is subexponential, because runtime bounds of the form 2^o(n) do not transfer under general polynomial-time reductions. The claim has not yet been peer reviewed, and OpenAI explicitly cautions that it should not be treated as settled until verified.

hackernews · vok · Oct 26, 21:59 · [Discussion](https://news.ycombinator.com/item?id=50251661)

**Background**: The Exponential Time Hypothesis, formulated by Impagliazzo and Paturi in 1999, posits that 3-SAT cannot be solved in subexponential time, specifically that there exists a constant s3 > 0 such that all algorithms require time at least 2^(s3 n). It is a stronger assumption than P ≠ NP and implies that many known algorithms have optimal or near-optimal time complexity. Disproving it would overturn a widely used basis for hardness assumptions in algorithm design.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://www.scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof/">The inside story behind OpenAI’s million-dollar math proof</a></li>

</ul>
</details>

**Discussion**: Commenters expressed amazement and surprise, with one clarifying that the result does not imply subexponential algorithms for NP. Others noted a parallel proof from Anthropic with the same bounds but a different approach, and discussed whether the method could have practical applications for SAT solving or self-attention mechanisms.

**Tags**: `#complexity-theory`, `#ETH`, `#SAT-solving`, `#research-breakthrough`, `#computer-science`

---

<a id="item-2"></a>
## [OpenAI claims disproof of Exponential Time Hypothesis](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 9.0/10

OpenAI announced three new discoveries in mathematics, computer science, and physics, including a claimed disproof of the Exponential Time Hypothesis (ETH). The ETH claim, posted on October 26, 2026, has not yet been peer reviewed, and OpenAI is asking academics to check the work. The ETH is a foundational assumption in computational complexity theory, and if disproved, it would invalidate many hardness results and algorithmic lower bounds that rely on it. This could reshape research in parameterized complexity and beyond, affecting a wide range of theoretical computer science work. The claimed algorithm for exactly counting satisfying assignments of a k-CNF formula runs in time (n+m)^{O_k(1)} 2^{n/(log n)^{1/2+o(1)}}, which is superpolynomial but subexponential, contradicting ETH. OpenAI stated that future review of the proof would be done in collaboration with complexity researchers Russell Impagliazzo, Ramamohan Paturi, and Ryan Williams.

hackernews · jonluca · Oct 26, 21:35 · [Discussion](https://news.ycombinator.com/item?id=50251344)

**Background**: The Exponential Time Hypothesis, formulated by Impagliazzo and Paturi in 1999, posits that 3-SAT cannot be solved in subexponential time, meaning there exists a constant s>0 such that all algorithms require at least 2^{s n} time. It is a stronger assumption than P≠NP and implies that many known algorithms have optimal or near-optimal time complexity. Disproving it would have major implications for computational complexity theory.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://grokipedia.com/page/Exponential_time_hypothesis">Exponential time hypothesis</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock and disbelief, with some noting the significance of ETH being false and others highlighting the collaboration with mathematicians like Terence Tao. There was also discussion about the implications for P vs NP and the broader impact on complexity theory.

**Tags**: `#complexity-theory`, `#ETH`, `#AI-for-science`, `#OpenAI`, `#research-breakthrough`

---

<a id="item-3"></a>
## [Anthropic Files S-1 Disclosing $500B+ in Infrastructure Commitments](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) ⭐️ 9.0/10

Anthropic filed its S-1 registration statement with the SEC on October 26, 2026, for a proposed IPO on Nasdaq, disclosing massive infrastructure commitments including $114B to Google, $110B to AWS, $161B to Broadcom, and $120B to SpaceX, alongside rapid revenue growth. This filing is a major industry event that reveals the scale of financial bets underpinning the AI boom, and it will shape investor expectations for AI infrastructure spending and the sustainability of demand across the entire AI ecosystem. The filing shows Anthropic generating $2.08 in revenue for every $1 spent on compute, up from $0.40 in Q1 2025, implying a compute payback period of less than a year; however, the company acknowledges risks related to open-source and open-weight models, as well as potential harm from misuse of its AI models.

hackernews · SiNTEx · Oct 26, 13:04 · [Discussion](https://news.ycombinator.com/item?id=50242939)

**Background**: An S-1 is a registration statement filed with the SEC by companies planning to go public, providing detailed financial and business information. Anthropic is an AI safety and research company known for its Claude family of large language models, and its IPO would be one of the most significant in the AI sector. The disclosed commitments reflect the enormous capital required to secure compute and infrastructure for training and serving frontier AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/s1-sec">Anthropic files S-1 with the SEC for proposed initial public ...</a></li>
<li><a href="https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/0001628280-26-067168-index.htm">EDGAR Filing Documents for 0001628280-26-067168 - SEC.gov</a></li>
<li><a href="https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-10-26-2026/card/read-the-full-anthropic-s-1-filing-1Sp1ib6qlFieTq1U5Bxd">Read the Full Anthropic S-1 Filing - The Wall Street Journal</a></li>

</ul>
</details>

**Discussion**: Commenters focused on whether the demand is truly sustainable, with some noting that AI coding (e.g., Claude Code) is the killer app driving most revenue growth but may not maintain its adoption rate. Others highlighted the impressive compute payback period and questioned whether open-source models from Chinese labs pose a significant competitive risk.

**Tags**: `#Anthropic`, `#AI`, `#S-1`, `#business`, `#infrastructure`

---