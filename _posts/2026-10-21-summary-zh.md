---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21
lang: zh
---

> 从 23 条内容中筛选出 3 条重要资讯。

---

1. [eMudhra 中间 CA 遭入侵，暴露弱密钥问题](#item-1) ⭐️ 9.0/10
2. [PHP 严重远程代码执行漏洞利用扩散，紧急补丁即将发布](#item-2) ⭐️ 9.0/10
3. [DeepSeek 开源 DeepInfer 推理框架，支持自家模型](#item-3) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [eMudhra 中间 CA 遭入侵，暴露弱密钥问题](https://emudhra.we-have-a-problem.com/) ⭐️ 9.0/10

2026 年 10 月 20 日，Mozilla 和 Google Chrome 根计划确认，eMudhra 的八个中间证书颁发机构（CA）证书的私钥遭到泄露，其中一个私钥仅为单字节“4”。Mozilla 通过 OneCRL 迅速吊销了这些证书，Chrome、Apple 和 Microsoft 也在几天内将其屏蔽。 该事件凸显了 PKI 生态系统中的系统性信任失败，因为被入侵的中间 CA 可用于为任何域名签发有效证书，从而助长广泛的冒充攻击。它还暴露了不同软件在证书吊销支持上的不均衡，导致许多系统长期处于 vulnerable 状态。 弱密钥源于 eMudhra 在特定日期使用的密钥生成仪式（KGC）脚本中的缺陷，尽管主要浏览器已屏蔽这些证书，但许多软件中嵌入的 CA 存储仍未修补。Cloudflare 正在部署缓解措施和客户端更新以应对影响。

hackernews · galadran · 10月20日 13:58 · [社区讨论](https://news.ycombinator.com/item?id=50166579)

**背景**: 中间 CA 是受信任的实体，为网站签发证书，形成从根 CA 到叶子证书的信任链。证书吊销是在证书到期前使其失效的过程，但在浏览器、操作系统和应用程序的多样化生态系统中高效且安全地分发吊销信息具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html">Eight eMudhra CA Keys Compromised, Triggering Emergency Fixes ...</a></li>
<li><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=2083449">2083449 - Private key compromise of eMudhra Intermediate ...</a></li>
<li><a href="https://blog.cloudflare.com/emudhra-certificate-compromise">8 eMudhra certificates are compromised. Here's what you need ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对私钥如此薄弱感到震惊，有人指出密钥字面上就是“4”。Mozilla 的代表强调，得益于 OneCRL，Firefox 用户数小时内就得到了保护，但批评生态系统其他部分缺乏对吊销机制的投资。其他人指出，许多软件供应商自带 CA 存储，使得修补困难，系统仍易受攻击。

**标签**: `#security`, `#PKI`, `#certificate-authority`, `#TLS`, `#incident-response`

---

<a id="item-2"></a>
## [PHP 严重远程代码执行漏洞利用扩散，紧急补丁即将发布](https://news-web.php.net/php.announce/509) ⭐️ 9.0/10

PHP 核心的两个严重远程代码执行漏洞 CVE-2026-109618 和 CVE-2026-109619 在协调披露前被泄露，且可用的漏洞利用正在迅速传播。PHP 安全团队正紧急赶制补丁，预计于 2026 年 10 月 22 日发布，并警告所有 PHP 用户做好立即升级的准备。 该漏洞 CVSS 评分高达 9.2，且利用代码已在流传，可能成为有史以来最严重的 PHP 漏洞之一，影响运行 PHP 5 至 8 的无数网站。漏洞利用的快速武器化（可能因 LLM 而加速）意味着未打补丁的服务器可能在数小时内被攻陷，使大量基于 LAMP 的站点和 VPS 托管商面临风险。 这两个漏洞被 PHP 安全团队评为 CVSS 9.2，影响 PHP 5、6、7 和 8 版本。该漏洞利用允许攻击者将精心构造的载荷粘贴到 URL 中，从而在服务器上获得 shell，演示视频已在 Twitter 上流传，概念验证代码也在私下分享。

hackernews · xd · 10月20日 20:15 · [社区讨论](https://news.ycombinator.com/item?id=50172041)

**背景**: PHP 是一种广泛使用的开源脚本语言，支撑着包括 WordPress、Drupal 和许多自定义应用在内的大量网站。远程代码执行（RCE）是一类允许攻击者在服务器上运行任意命令的漏洞，通常会导致整个系统被攻陷。协调披露是让供应商在细节公开前有时间修补的标准做法；而在此次事件中，这一流程因泄露而被打破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://watchtowr.com/intelligence/php-cve-2026-109618-faq/">PHP Remote Code Execution FAQ: CVE-2026-109618 | watchTowr</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/php-warns-admins-of-two-critical-flaws-emergency-patches-coming-tomorrow/">PHP warns admins of two critical flaws, emergency patches coming...</a></li>
<li><a href="https://arstechnica.com/security/2026/10/php-maintainers-tell-web-devs-to-prepare-themselves-for-critical-security-patches/">PHP warns it plans to release 2 emergency patches ... - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 评论者感到震惊，有人报告成功导出了整个数据库并立即关闭了网站。许多人批评补丁发布缓慢，指出负责的维护者当时在睡觉，并警告由 LLM 驱动的代理可能以前所未有的规模自动化攻击。共识建议是在补丁可用之前关闭服务器。

**标签**: `#PHP`, `#security`, `#vulnerability`, `#exploit`, `#web-development`

---

<a id="item-3"></a>
## [DeepSeek 开源 DeepInfer 推理框架，支持自家模型](https://github.com/deepseek-ai/DeepInfer) ⭐️ 9.0/10

DeepSeek 发布了 DeepInfer，这是支撑其大规模生产服务（包括 DeepSeek-V4.1-Flash）的高性能推理框架。此次开源版本提供了离线推理及大规模服务所需的核心功能，社区报告称单集群日吞吐量达到 155 万亿 tokens。 此次发布让开发者和较小实验室能够使用 DeepSeek 生产级推理栈，可能降低成本，并通过支持华为昇腾 NPU 等替代硬件来挑战英伟达的主导地位。它还加剧了围绕开放权重 AI 模型和中美 AI 基础设施竞争的讨论。 DeepInfer 被描述为 DeepSeek 实际用于生产推理的内部框架，而非精简演示版，并且包含对华为昇腾 950 NPU 的支持。声称的日吞吐量 155 万亿 tokens 和每卡每小时 38 美元（非高峰定价）的收入来自社区报告，而非官方基准测试。

hackernews · ggcr · 10月20日 09:08 · [社区讨论](https://news.ycombinator.com/item?id=50163277)

**背景**: DeepSeek 是一家中国 AI 公司，以发布开放权重的大语言模型而闻名。推理框架是优化已训练模型服务运行的软件栈，处理批处理、内存管理和硬件加速等任务。开放权重模型允许用户自行下载和运行模型，与仅提供 API 的封闭服务形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek-ai/DeepInfer: DeepInfer: High-performance ...</a></li>
<li><a href="https://tech-insider.org/deepseek-deepinfer-open-source-inference-framework-2026/">DeepSeek Open-Sources DeepInfer Inference Engine</a></li>
<li><a href="https://deepwiki.com/deepseek-ai/DeepInfer">deepseek-ai/DeepInfer | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: Hacker News 讨论（2186 分，848 条评论）非常热烈，观点从战略时机（在 DHS 排除令发布数小时后发布）到地缘政治影响，以及对支持华为昇腾 NPU 的赞扬。一些人认为这是对美国前沿实验室估值的打击，而另一些人则强调中国通过开源战略促进经济增长。

**标签**: `#AI inference`, `#DeepSeek`, `#open-source`, `#LLM serving`, `#geopolitics`

---