---
layout: default
title: "Horizon Summary: 2026-10-27 (ZH)"
date: 2026-10-27
lang: zh
---

> 从 27 条内容中筛选出 3 条重要资讯。

---

1. [OpenAI 预印本声称推翻指数时间假设](#item-1) ⭐️ 10.0/10
2. [OpenAI 宣称推翻指数时间假设](#item-2) ⭐️ 9.0/10
3. [Anthropic 提交 S-1 文件，披露超 5000 亿美元基础设施承诺](#item-3) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [OpenAI 预印本声称推翻指数时间假设](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) ⭐️ 10.0/10

OpenAI 发布了一篇预印本，声称推翻了计算复杂性理论中的基础猜想——指数时间假设（ETH）。该公司正请求学术界验证这项工作，未来审查将与复杂性研究者 Russell Impagliazzo、Ramamohan Paturi 和 Ryan Williams 合作进行。 如果正确，这将是复杂性理论中范式转变的成果，因为 ETH 是比 P ≠ NP 更强的假设，并支撑许多条件下界。它还可能对算法设计以及我们对 SAT 求解等问题的理解产生影响。 该结果并不意味着 NP 问题具有次指数时间，因为形如 2^o(n)的运行时间界在一般多项式时间归约下并不传递。该声明尚未经过同行评审，OpenAI 明确警告在验证之前不应将其视为定论。

hackernews · vok · 10月26日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=50251661)

**背景**: 指数时间假设由 Impagliazzo 和 Paturi 于 1999 年提出，认为 3-SAT 问题不能在次指数时间内求解，具体而言，存在常数 s3 > 0，使得所有算法所需时间至少为 2^(s3 n)。它是一个比 P ≠ NP 更强的假设，并意味着许多已知算法具有最优或接近最优的时间复杂度。推翻它将颠覆算法设计中广泛使用的硬度假设基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://www.scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof/">The inside story behind OpenAI’s million-dollar math proof</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了惊讶和意外，有人澄清该结果并不意味着 NP 问题存在次指数算法。其他人注意到 Anthropic 也发布了一个具有相同边界但方法不同的证明，并讨论了该方法是否可能对 SAT 求解或自注意力机制有实际应用。

**标签**: `#complexity-theory`, `#ETH`, `#SAT-solving`, `#research-breakthrough`, `#computer-science`

---

<a id="item-2"></a>
## [OpenAI 宣称推翻指数时间假设](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 9.0/10

OpenAI 宣布在数学、计算机科学和物理学领域取得三项新发现，其中包括声称推翻了指数时间假设（ETH）。该 ETH 声明于 2026 年 10 月 26 日发布，尚未经过同行评审，OpenAI 正请求学术界对这项工作进行检查。 ETH 是计算复杂性理论中的一个基础性假设，如果被推翻，将使得许多依赖它的硬度结果和算法下界失效。这可能会重塑参数化复杂性等领域的研究，并影响广泛的理论计算机科学工作。 所声称的精确计数 k-CNF 公式满足赋值算法运行时间为 (n+m)^{O_k(1)} 2^{n/(log n)^{1/2+o(1)}}，这是超多项式但亚指数的，与 ETH 矛盾。OpenAI 表示，未来的证明审查将与复杂性研究者 Russell Impagliazzo、Ramamohan Paturi 和 Ryan Williams 合作进行。

hackernews · jonluca · 10月26日 21:35 · [社区讨论](https://news.ycombinator.com/item?id=50251344)

**背景**: 指数时间假设由 Impagliazzo 和 Paturi 于 1999 年提出，认为 3-SAT 无法在亚指数时间内求解，即存在常数 s>0，使得所有算法至少需要 2^{s n} 时间。它是一个比 P≠NP 更强的假设，并意味着许多已知算法具有最优或接近最优的时间复杂度。推翻它将对计算复杂性理论产生重大影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://grokipedia.com/page/Exponential_time_hypothesis">Exponential time hypothesis</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了震惊和难以置信，一些人指出 ETH 被推翻的重要性，另一些人则强调与 Terence Tao 等数学家的合作。还有关于对 P vs NP 问题的影响以及对复杂性理论更广泛影响的讨论。

**标签**: `#complexity-theory`, `#ETH`, `#AI-for-science`, `#OpenAI`, `#research-breakthrough`

---

<a id="item-3"></a>
## [Anthropic 提交 S-1 文件，披露超 5000 亿美元基础设施承诺](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) ⭐️ 9.0/10

Anthropic 于 2026 年 10 月 26 日向美国证券交易委员会提交了 S-1 注册声明，拟在纳斯达克进行首次公开募股，披露了巨额基础设施承诺，包括向谷歌承诺 1140 亿美元、向 AWS 承诺 1100 亿美元、向博通承诺 1610 亿美元以及向 SpaceX 承诺 1200 亿美元，同时收入快速增长。 这份文件是行业重大事件，揭示了支撑 AI 热潮的财务押注规模，并将影响投资者对 AI 基础设施支出以及整个 AI 生态系统需求可持续性的预期。 文件显示，Anthropic 每在计算上花费 1 美元就能产生 2.08 美元的收入，高于 2025 年第一季度的 0.40 美元，这意味着计算投资回收期不到一年；然而，公司也承认了与开源和开放权重模型相关的风险，以及其 AI 模型被滥用可能造成的危害。

hackernews · SiNTEx · 10月26日 13:04 · [社区讨论](https://news.ycombinator.com/item?id=50242939)

**背景**: S-1 是计划上市的公司向美国证券交易委员会提交的注册声明，提供详细的财务和业务信息。Anthropic 是一家 AI 安全与研究公司，以其 Claude 系列大语言模型闻名，其 IPO 将成为 AI 领域最重要的上市之一。披露的承诺反映了为确保前沿 AI 模型训练和推理所需的计算和基础设施而投入的巨额资本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/s1-sec">Anthropic files S-1 with the SEC for proposed initial public ...</a></li>
<li><a href="https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/0001628280-26-067168-index.htm">EDGAR Filing Documents for 0001628280-26-067168 - SEC.gov</a></li>
<li><a href="https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-10-26-2026/card/read-the-full-anthropic-s-1-filing-1Sp1ib6qlFieTq1U5Bxd">Read the Full Anthropic S-1 Filing - The Wall Street Journal</a></li>

</ul>
</details>

**社区讨论**: 评论者关注需求是否真正可持续，一些人指出 AI 编程（如 Claude Code）是推动大部分收入增长的关键应用，但可能无法保持其采用率。其他人则强调了令人印象深刻的计算投资回收期，并质疑来自中国实验室的开源模型是否构成重大竞争风险。

**标签**: `#Anthropic`, `#AI`, `#S-1`, `#business`, `#infrastructure`

---