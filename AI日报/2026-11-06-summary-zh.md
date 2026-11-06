---
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06
lang: zh
---

> 从 29 条内容中筛选出 4 条重要资讯。

---

1. [musl libc 上的 OpenSSH 因 '*' 哈希存在密码认证绕过漏洞](#item-1) ⭐️ 9.0/10
2. [Claude Code 被曝在 User-Agent 中泄露用户邮箱](#item-2) ⭐️ 8.0/10
3. [MS Paint 远程代码执行漏洞引发担忧](#item-3) ⭐️ 8.0/10
4. [SemiAnalysis：谷歌 TPU 在推理领域挑战英伟达 CUDA 护城河](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [musl libc 上的 OpenSSH 因 '*' 哈希存在密码认证绕过漏洞](https://sshhole.com/) ⭐️ 9.0/10

2026 年 11 月 5 日，一个名为“sshole”的严重 OpenSSH 密码认证绕过漏洞被披露，影响在 musl libc（如 Alpine Linux）上构建、未使用 PAM 且启用了密码认证的 OpenSSH。该漏洞允许攻击者通过提供任意 257 到 1024 字节的密码登录到锁定账户（其 shadow 密码字段为 '*'），OpenSSH 10.6p2 已修复此问题。 该漏洞影响广泛使用的容器基础镜像（如 Alpine Linux），可能使本应锁定的系统被未授权访问，因此意义重大。它凸显了安全关键代码中带内信令的风险，并强调了在认证例程中谨慎处理特殊值的必要性。 该漏洞源于 musl 的 crypt() 在出错时返回 '*'，而 OpenSSH 直接将其与 shadow 条目比较，因此当存储的哈希为 '*' 时，精心构造的长密码会导致 crypt() 失败并返回 '*'，从而与哈希匹配。musl 中的易受攻击路径仅稍微脆弱，DES 已有变通方法但 SHA-crypt 没有，且如果盐为 'x'，该变通方法也是错误的。

hackernews · josemrb · 11月5日 12:19 · [社区讨论](https://news.ycombinator.com/item?id=50378228)

**背景**: OpenSSH 使用 crypt() 函数验证密码，通过比较 crypt(输入的密码, 存储的哈希) 的结果与存储的哈希是否一致。在 /etc/shadow 中，密码字段为 '*' 或 '!' 表示账户已锁定，不应允许密码登录。musl 是 Alpine Linux 和许多 Docker 镜像使用的轻量级 C 库，其 crypt() 实现在出错时返回 '*'，这与使用 '*' 作为锁定账户标记相冲突。这是带内信令的一个例子，即在数据流中使用特殊值来传达控制信息，从而导致歧义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh -server password authentication bypass</a></li>
<li><a href="https://hadrian.io/vulnerability-alerts/openssh-on-musl-accepts-any-long-password-for-locked-accounts">From * to Access: How musl’s crypt () Behavior Undermines ...</a></li>
<li><a href="https://sesamedisk.com/openssh-musl-star-password-bypass/">The Star That Opened OpenSSH on musl - Sesame Disk</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调这是带内信令导致安全问题的又一案例，BoppreH 指出不应将 '*' 用作特殊值，并建议使用 Result 类型。amluto 指出 musl 在 DES crypt 中已有针对类似问题的变通方法，但忘记将其应用于 SHA-crypt，aljgz 则主张完全避免魔术字符串。总体而言，讨论强调系统编程中需要更好的错误处理和设计。

**标签**: `#security`, `#openssh`, `#crypt`, `#in-band-signaling`, `#vulnerability`

---

<a id="item-2"></a>
## [Claude Code 被曝在 User-Agent 中泄露用户邮箱](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

GitHub 议题（#107757）指控 Claude Code 将登录用户的邮箱地址写入其对外网页搜索请求的 User-Agent 头中，从而暴露给代理访问的每个网站。Anthropic 随后在 2.1.317 版本中内置了隐私插件 cc-plugin-privacy，默认阻止该行为。 这一隐私泄露影响所有使用 Claude Code 进行联网任务的用户，可能将企业邮箱暴露给第三方网站，增加垃圾邮件或钓鱼风险。它也凸显了防止 AI 代理通过标准 HTTP 头无意泄露用户身份数据这一更广泛的挑战。 该泄露似乎与网页搜索请求有关，社区分析认为 SEC API 要求在 User-Agent 中提供邮箱可能是触发因素之一。Anthropic 的修复是一个基于正则表达式的 171 行插件，仅阻止了报告中提到的特定模式，但独立测试发现它至少漏掉了同一泄露的 8 种其他变体。

hackernews · motoroco · 11月5日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=50385272)

**背景**: Claude Code 是 Anthropic 的代理式编程工具，运行在终端中，可以代表用户执行网页搜索等任务。User-Agent 头是标识发起请求的客户端软件的标准 HTTP 字段，会发送给每个被访问的网站。某些 API（如美国 SEC 的数据 API）要求在 User-Agent 中提供联系邮箱以识别调用者，否则会拒绝请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-code-leaks-your-email-user-agent-header-how-to-stop-it-2026">Claude Code Leaks Your Email in Headers: 5-Min Fix - explainx.ai</a></li>
<li><a href="https://aiweekly.co/alerts/claude-code-bug-report-alleges-email-leak-in-user-agent-header">Claude Code bug report alleges email leak in User-Agent ...</a></li>
<li><a href="https://dev.to/frankchu/8-leaks-pass-anthropics-23-test-email-fix-2e66">8 leaks pass Anthropic's 23-test email fix - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了一个合理的解释：SEC API 要求在 User-Agent 中提供邮箱，同时其他人链接了此前关于邮箱自动注入和隐藏追踪器的相关议题。一些用户将垃圾邮件增多归咎于 Claude，但其他人反驳称垃圾邮件早在 AI 之前就存在，归咎于 Claude 可能牵强。

**标签**: `#privacy`, `#security`, `#AI coding tools`, `#Claude Code`, `#Hacker News`

---

<a id="item-3"></a>
## [MS Paint 远程代码执行漏洞引发担忧](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 8.0/10

新披露的 CVE（CVE-2026-83844）显示，MS Paint 版本 11.0.0.0 至 11.2605.91.0 之前存在远程代码执行漏洞，可通过特制网络数据包在无需用户交互的情况下利用。 这一点很重要，因为 MS Paint 是一个简单的图形应用程序，通常不处理网络流量，因此无需用户交互的面向网络的 RCE 令人惊讶，如果被利用可能影响许多 Windows 用户。 该漏洞被归类为 Windows Paint 中的越界读取（CWE-125），微软的公告确认了网络攻击向量和无需身份验证；修复版本为 11.2609.401.0，但一些用户报告 Windows Update 未显示该更新。

hackernews · kuberwastaken · 11月5日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50384233)

**背景**: MS Paint 是 Windows 自带的基本图像编辑器。远程代码执行（RCE）漏洞允许攻击者在受害者机器上运行任意代码。通常，此类漏洞需要用户交互（例如打开恶意文件），但此漏洞基于网络且无需用户操作，这对于像 Paint 这样的简单应用程序来说很不寻常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-83844/">CVE-2026-83844: Windows Paint RCE Vulnerability - SentinelOne</a></li>
<li><a href="https://cybersecuritynews.com/windows-paint-rce-vulnerability/">Microsoft Paint 0-Click Vulnerability Could Allow Hackers to ...</a></li>
<li><a href="https://windowsforum.com/news/cve-2026-83844-windows-11-paint-rce-fix-confusion-and-how-to-check-your-version.451018/">CVE-2026-83844: Windows 11 Paint RCE Fix Confusion and How to ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Paint 具有面向网络的攻击面表示震惊和怀疑，质疑为什么一个简单的图像编辑器会有远程代码执行漏洞。一些人指出修复仅通过 Microsoft Store 提供，而非 Windows Update，另一些人指出旧版 Paint 可能不受影响。

**标签**: `#security`, `#vulnerability`, `#windows`, `#remote-code-execution`, `#microsoft`

---

<a id="item-4"></a>
## [SemiAnalysis：谷歌 TPU 在推理领域挑战英伟达 CUDA 护城河](https://newsletter.semianalysis.com/p/tpu-strikes-the-king) ⭐️ 8.0/10

SemiAnalysis 发布深度分析文章，认为谷歌 TPU 已成为英伟达 CUDA 在推理工作负载方面的可行替代方案，并重点介绍了 TorchTPU、vLLM、SGLang 和 llm-d 等生态工具。 这一点很重要，因为英伟达的 CUDA 软件护城河长期以来是 AI 硬件竞争的关键壁垒；如果 TPU 成为可信的推理替代方案，可能重塑 AI 基础设施市场并对英伟达的主导地位构成压力。 分析涵盖了谷歌与 Meta 合作开发的 TorchTPU（TPU 的原生 PyTorch 后端），以及对 vLLM 和 SGLang 等流行推理引擎的支持，还有通过 llm-d 进行编排；不过摘录内容简短，缺少完整的技术基准测试。

rss · Semianalysis · 11月5日 19:03

**背景**: TPU（张量处理单元）是谷歌设计的定制 ASIC 芯片，旨在加速机器学习工作负载，可通过谷歌云使用。CUDA 是英伟达专有的并行计算平台和编程模型，已成为 GPU 加速 AI 的事实标准，形成了强大的生态锁定。推理是训练好的 AI 模型进行预测的阶段，随着 AI 模型大规模部署而日益重要。TorchTPU 是谷歌和 Meta 合作的开源项目，为 TPU 提供原生 PyTorch 后端，旨在让 PyTorch 开发者更容易使用 TPU。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pytorch.org/blog/introducing-torchtpu/">Introducing TorchTPU - PyTorch</a></li>
<li><a href="https://cloud.google.com/tpu">Tensor Processing Units ( TPUs ) | Google Cloud</a></li>
<li><a href="https://deepwiki.com/llm-d/llm-d/2.4-model-servers-(vllm-sglang-trt-llm)">Model Servers ( vLLM , SGLang , TRT-LLM) | llm - d / llm - d | DeepWiki</a></li>

</ul>
</details>

**标签**: `#TPU`, `#CUDA`, `#AI inference`, `#hardware`, `#SemiAnalysis`

---