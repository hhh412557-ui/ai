---
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 24 条内容中筛选出 2 条重要资讯。

---

1. [OpenAI 撤回三项数学成果，引发 AI 证明可靠性质疑](#item-1) ⭐️ 8.0/10
2. [ThinkingBox-Bench 以最终数据库状态评估智能体可靠性](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 撤回三项数学成果，引发 AI 证明可靠性质疑](https://twitter.com/danintheory/status/2108065033070789090) ⭐️ 8.0/10

OpenAI 从其公开数学仓库中撤回了三项数学成果，相关记录出现在 openai/math 项目的 history.md 文件中。该撤回事件由@danintheory 在 X 上披露，随后在 Hacker News 上引发 559 条评论的热烈讨论，聚焦于 AI 生成证明的可靠性问题。 这对 AI 数学领域是一个重大事件，因为它直接挑战了大语言模型能够产出可信数学突破的说法。它提出了紧迫的问题：AI 生成的证明应如何验证，以及是否应在发布任何成果前强制使用 Lean 等形式化工具。 被撤回的成果似乎是 OpenAI 发布的大量 AI 生成数学手稿中的一部分，社区成员指出并非所有成果都附有 Lean 证书。即便是经过 Lean 验证的证明也可能存在问题，因为证明可以通过编译，但形式化的命题却可能与原本意图不同。

hackernews · sashank_1509 · 10月8日 07:05 · [社区讨论](https://news.ycombinator.com/item?id=50002650)

**背景**: Lean 是一种开源证明助手和函数式编程语言，自 2013 年起由微软开发，允许数学家以计算机可机械检查的形式编写证明。OpenAI 已发布数百份 AI 生成的数学手稿，其中部分附有 Lean 证书，这引发了数学家的批评，他们认为这种做法绕过了既有的同行评审规范。OpenAI 随后成立了一个独立的数学与 AI 咨询小组来监督这项研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://eonsr.com/en/formal-verification-of-ai-generated-proofs-ensuring-logical-integrity-and-trustworthiness-in-complex-mathematical-problem-solving/">Formal verification of AI generated proofs ensuring logical... - EONSR</a></li>
<li><a href="https://www.nytimes.com/2026/10/06/science/openai-math-problems.html">OpenAI Releases Findings on 377 Math Problems, Further Roiling Field</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑这三项被撤回的证明是否正是缺少 Lean 验证的那些，以及 OpenAI 为何要将形式化验证的证明与自然语言证明混在一起。一些人认为，许多完全由 AI 生成的证明最终会站不住脚，因为即便在 Lean 中，也可以构建出能编译但所陈述内容与原本意图不同的理论，而且产出量之大意味着错误可能要数年才会暴露。还有人将此次撤回形容为软件工程实践与数学的碰撞，并建议所有此类成果都应被形式化。

**标签**: `#AI for mathematics`, `#proof verification`, `#Lean`, `#OpenAI`, `#research integrity`

---

<a id="item-2"></a>
## [ThinkingBox-Bench 以最终数据库状态评估智能体可靠性](https://www.reddit.com/r/MachineLearning/comments/1x17shf/thinkingbox_solving_an_agent_task_once_vs_solving/) ⭐️ 8.0/10

微软研究人员发布了 ThinkingBox-Bench，这是一个包含 507 个有状态业务工作流的基准测试，覆盖零售、旅行/酒店、汽车保险、数字银行内部 IT、咨询 IT/HR 五个领域；每个任务都在完全相同的干净后端上运行 20 次，每个模型共 10,140 次试验。评分将最终后端状态和副作用与要求的最终状态进行比对，论文报告了 pass@1、pass@20 和 all-20 三个指标，显示发现能力与可重复性对模型的排名差异极大。 大多数智能体基准只报告单一成功率，把偶尔发现与可靠执行混为一谈；ThinkingBox 显示 Kimi-K3 至少成功一次的任务占 93.89%，但 20 次全部成功的仅 13.41%，而 Claude Opus 5 发现率较低（79.09%）却重复成功率更高（47.53%）。这对在企业工作流中部署智能体的人很重要，因为以“完成”为标准的代理指标会把 67.24% 干净终止但数据库状态错误的失败判为成功。 507 个任务中有 477 个仅按状态评分，另有 30 个还会检查最终回复的某一狭窄属性；在对 12 个模型、121,680 次有效试验的回溯消融中，79,853 次未通过可执行检查，其中 67.24% 仍然干净终止、调用了改变状态的工具且没有最终工具错误。作者提醒：任务是对企业模式的合成重建，20/20 是在固定试验预算下的观测计数而非未来可靠性的保证，模拟用户是固定 LLM，因此也是方差来源。

reddit · r/MachineLearning · /u/tuhin_k · 10月9日 00:50

**背景**: 人们越来越期望 AI 智能体通过调用数据库、API 等工具来完成多轮业务任务，但评估它们很困难，因为看似合理的最终回答并不能证明后端被留在了正确状态。ThinkingBox 提供了一个沙箱，包含隔离的 MCP 兼容工具会话、持有私有上下文的模拟用户，以及对最终状态、副作用和对话的可执行检查。它随代码、基准数据和 Hugging Face OpenEnv 环境一同发布，方便他人用这 507 个任务测试自己的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19741">[2608.19741] One Success Isn't Reliability: Thinkingbox, a ...</a></li>
<li><a href="https://commandline.microsoft.com/thinkingbox-bench-agent-benchmarking/">ThinkingBox: Measuring whether agents finish the job</a></li>
<li><a href="https://huggingface.co/blog/openenv">Building the Open Agent Ecosystem Together: Introducing OpenEnv</a></li>

</ul>
</details>

**标签**: `#agent evaluation`, `#benchmark`, `#stateful workflows`, `#reliability`, `#AI agents`

---