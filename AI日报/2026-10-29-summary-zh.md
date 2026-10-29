---
title: "Horizon Summary: 2026-10-29 (ZH)"
date: 2026-10-29
lang: zh
---

> 从 37 条内容中筛选出 3 条重要资讯。

---

1. [Qwenputer：在 Qwen3.5 中模拟出确定性 RISC-V CPU](#item-1) ⭐️ 8.0/10
2. [指纹识别脚本被 LLM 误判为生物武器](#item-2) ⭐️ 8.0/10
3. [Alpine Linux 重新发布 GitLab 镜像以修复 Ruby 正则表达式 RCE 漏洞](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwenputer：在 Qwen3.5 中模拟出确定性 RISC-V CPU](https://divagr.com/blog/qwenputer) ⭐️ 8.0/10

一位开发者发布了名为 Qwenputer 的项目，在 Qwen3.5 大语言模型内部完整实现了一个可运行且确定性的 RISC-V CPU，并在此基础上进一步添加了文件系统。 该项目表明大语言模型能够模拟确定性计算系统，模糊了语言模型与传统模拟器之间的界限，并可能为程序执行、验证和智能体设计带来新的思路。 该 CPU 具有确定性，即相同输入产生相同输出，这一点值得注意，因为 LLM 推理通常是非确定性的；该实现运行在 Qwen3.5 内部，这是 Qwen 近期推出的模型，提供 2B 和 35B-A3B 等规模。

hackernews · csmantle · 10月29日 00:25 · [社区讨论](https://news.ycombinator.com/item?id=50282838)

**背景**: RISC-V 是一种开源指令集架构（ISA），任何人都可以自由设计和实现基于它的 CPU。像 Qwen3.5 这样的大语言模型是在海量文本数据上训练、用于预测下一个 token 的神经网络，通常并不用于执行机器指令。在 LLM 内部模拟 CPU 意味着将 CPU 的状态和指令执行编码为模型处理的文本或 token，这是对大语言模型一种非常规且富有创意的使用方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-2B">Qwen/Qwen3.5-2B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC - V - Wikipedia</a></li>
<li><a href="https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/">Defeating Nondeterminism in LLM Inference - Thinking Machines Lab</a></li>

</ul>
</details>

**社区讨论**: 评论者认为该项目有趣且令人印象深刻，有人开玩笑说智能体会滥用它来最大化回形针，还有人提到 Qwen 中有一个“恶魔邪恶 Qwen”神经元。其他人则指出相关工作，例如在 Transformer 中实现 WASM，并好奇该方法能否在 AdderBoard（一项构建能做大数加法的微型 Transformer 的竞赛）中具有竞争力。

**标签**: `#LLM`, `#RISC-V`, `#emulation`, `#Qwen`, `#creative coding`

---

<a id="item-2"></a>
## [指纹识别脚本被 LLM 误判为生物武器](https://nullpt.rs/fingerprinting-bioweapons) ⭐️ 8.0/10

nullpt.rs 上的一篇博客文章调查了为什么一个浏览器指纹识别脚本会被大型语言模型（LLM）标记为与生物武器相关，引发了关于 LLM 安全过滤器和混淆的讨论。 这凸显了 LLM 安全过滤器中误报的挑战，可能阻碍合法的安全研究和开发，并强调了需要更具上下文感知的审核机制。 指纹识别脚本可能包含触发安全分类器的模式或关键词，社区讨论显示，像 GLM-5.3 这样的模型会遵从，而其他模型则会阻止，表明安全实现存在差异。

hackernews · hazebooth · 10月28日 17:13 · [社区讨论](https://news.ycombinator.com/item?id=50276998)

**背景**: 浏览器指纹识别是一种收集用户浏览器属性以创建唯一标识符进行跟踪的技术，常用于欺诈检测和分析。LLM 越来越多地用于分析代码和日志，但其安全过滤器可能错误地将良性内容标记为恶意，导致误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/fingerprintjs/fingerprintjs">GitHub - fingerprintjs/fingerprintjs: The most advanced free ... FingerprintJS: The Browser ID Tool Every Developer Needs Browser Fingerprinting in JavaScript: A Developer's ... Fingerprintjs2 by eisman Thumbmark — Visitor Identification at Scale Browser Fingerprint Detection and Anti-Tracking - arXiv.org</a></li>
<li><a href="https://community.openai.com/t/recent-safety-filter-update-causing-high-false-positives-on-legitimate-academic-ml-research/1410325">Recent Safety Filter Update Causing High False Positives on ...</a></li>
<li><a href="https://arxiv.org/html/2410.02916v3">LLM Safeguard is a Double-Edged Sword: Exploiting False ...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了关于水印导致电子邮件被隔离的轶事，并指出像 GLM-5.3 这样的 LLM 更为宽松，而其他人则开玩笑说混淆和检测之间正在展开军备竞赛。

**标签**: `#fingerprinting`, `#LLM safety`, `#obfuscation`, `#adversarial ML`, `#web security`

---

<a id="item-3"></a>
## [Alpine Linux 重新发布 GitLab 镜像以修复 Ruby 正则表达式 RCE 漏洞](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html) ⭐️ 8.0/10

Alpine Linux 发布了一份安全事件报告，详细描述了针对 CVE-2026-97229 的未遂利用尝试。该漏洞是 Ruby 的 Onigmo 正则表达式引擎中的整数溢出，可导致远程代码执行。Alpine Linux 于 10 月 27 日重新发布了 alpinelinux/gitlab:19.3.6 容器镜像，其中包含 Ruby 3.3.13 以纳入修复。 该漏洞存在于 Ruby 的正则表达式引擎中，而非 GitLab 自身的代码，因此任何从不可信输入编译正则表达式的程序都会受到影响，而不仅仅是 GitLab；这凸显了语言运行时的广泛供应链风险以及修补从源码构建的容器镜像所面临的挑战。 修复包含在 Ruby 3.3.13（以及 3.4.12 和 4.0.9）中，任何在 10 月 27 日之前拉取的 19.3.6 镜像或更旧的标签仍然存在漏洞；Alpine 在相同的 19.3.6 标签下重新发布了修复后的镜像，而没有提升版本号，这遭到了一些社区成员的批评。

hackernews · sashk · 10月28日 23:45 · [社区讨论](https://news.ycombinator.com/item?id=50282544)

**背景**: CVE-2026-97229 是 Ruby 内置的正则表达式引擎 Onigmo 中的整数溢出漏洞，可通过 GitLab CI/CD 配置中特制的正则表达式触发，实现未认证的远程代码执行。GitLab 在其官方软件包中修复了该问题，但像 Alpine 这样的第三方镜像最初使用的是未打补丁的标准 Ruby。Ruby 于 2026 年 10 月 23 日发布了修复版本（4.0.9、3.4.12、3.3.13），解决了此漏洞及几个相关的 CVE。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/">Regexp compilation fixes related to GitLab's CVE-2026-89078 ...</a></li>
<li><a href="https://thehackernews.com/2026/10/ruby-fixes-three-regex-engine-bugs.html">Ruby Fixes Three Regex Engine Bugs Responsible for Four ...</a></li>
<li><a href="https://www.rapid7.com/blog/post/ra-gitlab-ci-cd-regex-integer-overflow-technical-analysis-cve-2026-97229/">Rapid7 Analysis: GitLab CI/CD Regex Integer Overflow (CVE ...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调该缺陷存在于 Ruby 的正则表达式引擎中，影响任何编译不可信正则表达式的程序，并批评 Alpine 在相同的 19.3.6 标签下重新发布修复镜像，而不是提升版本号。其他人对反复出现的 C 库漏洞和“重新发明轮子”综合征表示不满，同时赞扬事件报告对未知因素和潜在数据泄露的透明度。

**标签**: `#security`, `#vulnerability`, `#GitLab`, `#Ruby`, `#containers`

---