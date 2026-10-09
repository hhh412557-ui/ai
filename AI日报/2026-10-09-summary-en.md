---
title: "Horizon Summary: 2026-10-09 (EN)"
date: 2026-10-09
lang: en
---

> From 24 items, 2 important content pieces were selected

---

1. [OpenAI withdraws three mathematical results, raising AI proof reliability questions](#item-1) ⭐️ 8.0/10
2. [ThinkingBox-Bench grades agent reliability on terminal database state](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI withdraws three mathematical results, raising AI proof reliability questions](https://twitter.com/danintheory/status/2108065033070789090) ⭐️ 8.0/10

OpenAI has withdrawn three mathematical results from its public math repository, as documented in the history.md file of the openai/math GitHub project. The retraction was surfaced on X by @danintheory and quickly became a high-engagement Hacker News discussion with 559 comments about the reliability of AI-generated proofs. This is a significant event for AI-for-mathematics because it directly challenges claims that large language models can produce trustworthy mathematical breakthroughs. It raises urgent questions about how AI-generated proofs should be verified, and whether formal tools like Lean should be mandatory before any result is published. The withdrawn results appear to be among the hundreds of AI-generated mathematical manuscripts OpenAI has released, and community members note that not all of those results carried Lean certificates. Even Lean-verified proofs can be problematic, since a proof can compile while formalizing a statement different from the one intended.

hackernews · sashank_1509 · Oct 8, 07:05 · [Discussion](https://news.ycombinator.com/item?id=50002650)

**Background**: Lean is an open-source proof assistant and functional programming language, developed by Microsoft since 2013, that lets mathematicians write proofs in a form a computer can mechanically check. OpenAI has released hundreds of AI-generated mathematical manuscripts, some accompanied by Lean certificates, which has drawn criticism from mathematicians who argue this bypasses established peer-review norms. OpenAI has since added an independent Mathematics and AI Advisory Group to oversee this research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://eonsr.com/en/formal-verification-of-ai-generated-proofs-ensuring-logical-integrity-and-trustworthiness-in-complex-mathematical-problem-solving/">Formal verification of AI generated proofs ensuring logical... - EONSR</a></li>
<li><a href="https://www.nytimes.com/2026/10/06/science/openai-math-problems.html">OpenAI Releases Findings on 377 Math Problems, Further Roiling Field</a></li>

</ul>
</details>

**Discussion**: Commenters questioned whether the three withdrawn proofs were the ones lacking Lean verification, and why OpenAI mixed formally verified and natural-language proofs at all. Several argued that many fully AI-generated proofs will eventually fall apart, since even Lean can compile theories that state something different from what was intended, and that the sheer volume of output means errors may take years to surface. Others described the retraction as software engineering practices meeting mathematics, and one commenter suggested all such results should be formalized.

**Tags**: `#AI for mathematics`, `#proof verification`, `#Lean`, `#OpenAI`, `#research integrity`

---

<a id="item-2"></a>
## [ThinkingBox-Bench grades agent reliability on terminal database state](https://www.reddit.com/r/MachineLearning/comments/1x17shf/thinkingbox_solving_an_agent_task_once_vs_solving/) ⭐️ 8.0/10

Microsoft researchers released ThinkingBox-Bench, a benchmark of 507 stateful business workflows across five domains (retail, travel/hospitality, auto insurance, neobank IT, consulting IT/HR), where each task is run 20 times from an identical clean backend, yielding 10,140 trials per model. Grading compares the terminal backend state and side effects against the required end state, and the paper reports three metrics — pass@1, pass@20, and all-20 — showing that discovery and repeatability rank models very differently. Most agent benchmarks report a single success rate, which conflates occasional discovery with reliable execution; ThinkingBox shows that models like Kimi-K3 solve 93.89% of tasks at least once but only 13.41% on all 20 attempts, while Claude Opus 5 discovers fewer (79.09%) yet repeats far more (47.53%). This matters for anyone deploying agents in enterprise workflows, because a completion-style proxy would have scored 67.24% of clean-terminating failures as successful even though the database ended up wrong. 477 of the 507 tasks are graded on state alone, while 30 also check a narrow property of the final response; in a retrospective ablation over 121,680 valid trials across 12 models, 79,853 failed executable checks, and 67.24% of those still terminated cleanly with a state-changing tool call and no final tool error. The authors caution that tasks are synthetic reconstructions of enterprise patterns, that 20/20 is an observed count on a fixed trial budget rather than a guarantee, and that the simulated user is a fixed LLM and thus a source of variance.

reddit · r/MachineLearning · /u/tuhin_k · Oct 9, 00:50

**Background**: AI agents are increasingly expected to carry out multi-turn business tasks by calling tools such as databases and APIs, but evaluating them is hard because a plausible final answer does not prove the backend was left in the correct state. ThinkingBox provides a sandbox with isolated MCP-compatible tool sessions, a simulated user holding private context, and executable checks over final state, side effects, and dialogue. It is released alongside code, benchmark data, and a Hugging Face OpenEnv environment so others can run the 507 tasks against their own models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19741">[2608.19741] One Success Isn't Reliability: Thinkingbox, a ...</a></li>
<li><a href="https://commandline.microsoft.com/thinkingbox-bench-agent-benchmarking/">ThinkingBox: Measuring whether agents finish the job</a></li>
<li><a href="https://huggingface.co/blog/openenv">Building the Open Agent Ecosystem Together: Introducing OpenEnv</a></li>

</ul>
</details>

**Tags**: `#agent evaluation`, `#benchmark`, `#stateful workflows`, `#reliability`, `#AI agents`

---