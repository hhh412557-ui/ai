---
title: "Horizon Summary: 2026-11-06 (EN)"
date: 2026-11-06
lang: en
---

> From 29 items, 4 important content pieces were selected

---

1. [OpenSSH on musl libc vulnerable to password auth bypass via '*' hash](#item-1) ⭐️ 9.0/10
2. [Claude Code Reportedly Leaks User Email in User-Agent Headers](#item-2) ⭐️ 8.0/10
3. [MS Paint Remote Code Execution Vulnerability Raises Concerns](#item-3) ⭐️ 8.0/10
4. [SemiAnalysis: Google's TPU Challenges NVIDIA's CUDA Moat in Inference](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenSSH on musl libc vulnerable to password auth bypass via '*' hash](https://sshhole.com/) ⭐️ 9.0/10

A critical OpenSSH password authentication bypass, dubbed "sshole", was disclosed on November 5, 2026, affecting OpenSSH builds on musl libc (such as Alpine Linux) without PAM and with password authentication enabled. The flaw allows attackers to log in to locked accounts (where the shadow password field is '*') by supplying any password of 257 to 1024 bytes, and OpenSSH 10.6p2 fixes it. This vulnerability is significant because it affects widely used container base images like Alpine Linux, potentially allowing unauthorized access to systems that should be locked. It highlights the risks of in-band signaling in security-critical code and underscores the need for careful handling of special values in authentication routines. The bug arises because musl's crypt() returns '*' on error, and OpenSSH compares this directly with the shadow entry, so when the stored hash is '*', a crafted long password causes crypt() to fail and return '*', matching the hash. The vulnerable path in musl is only a little bit vulnerable, and a workaround exists for DES but not for SHA-crypt, and the workaround is also incorrect if the salt is 'x'.

hackernews · josemrb · Nov 5, 12:19 · [Discussion](https://news.ycombinator.com/item?id=50378228)

**Background**: OpenSSH uses the crypt() function to verify passwords by comparing the result of crypt(entered_password, stored_hash) with the stored hash. In /etc/shadow, a password field of '*' or '!' indicates a locked account that should not allow password login. musl is a lightweight C library used by Alpine Linux and many Docker images, and its crypt() implementation returns '*' on error, which conflicts with the use of '*' as a locked account marker. This is an example of in-band signaling, where a special value in the data stream is used to convey control information, leading to ambiguity.

<details><summary>References</summary>
<ul>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh -server password authentication bypass</a></li>
<li><a href="https://hadrian.io/vulnerability-alerts/openssh-on-musl-accepts-any-long-password-for-locked-accounts">From * to Access: How musl’s crypt () Behavior Undermines ...</a></li>
<li><a href="https://sesamedisk.com/openssh-musl-star-password-bypass/">The Star That Opened OpenSSH on musl - Sesame Disk</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that this is another case of in-band signaling causing security issues, with BoppreH noting that '*' should not have been used as a special value and suggesting Result types instead. amluto points out that musl already had a workaround for a similar issue in DES crypt but forgot to apply it to SHA-crypt, and aljgz advocates for avoiding magic strings altogether. Overall, the discussion emphasizes the need for better error handling and design in system programming.

**Tags**: `#security`, `#openssh`, `#crypt`, `#in-band-signaling`, `#vulnerability`

---

<a id="item-2"></a>
## [Claude Code Reportedly Leaks User Email in User-Agent Headers](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

A GitHub issue (#107757) alleges that Claude Code writes the signed-in user's email address into the User-Agent header of its outbound web-search requests, exposing it to every site the agent visits. Anthropic responded by shipping a built-in privacy plugin, cc-plugin-privacy, in version 2.1.317 that blocks the behavior by default. This privacy leak affects anyone using Claude Code for web-enabled tasks, potentially exposing corporate email addresses to third-party sites and increasing spam or phishing risk. It also highlights the broader challenge of preventing AI agents from inadvertently leaking user identity data through standard HTTP headers. The leak appears tied to web-search requests, and community analysis suggests the SEC API's requirement for an email in the User-Agent may be one trigger. Anthropic's fix is a 171-line regex-based plugin that blocks the specific reported pattern, but independent testing found it misses at least 8 other variations of the same leak.

hackernews · motoroco · Nov 5, 22:17 · [Discussion](https://news.ycombinator.com/item?id=50385272)

**Background**: Claude Code is Anthropic's agentic coding tool that runs in the terminal and can perform web searches and other tasks on behalf of the user. The User-Agent header is a standard HTTP field that identifies the client software making a request, and it is sent to every website contacted. Some APIs, such as the U.S. SEC's data API, require a contact email in the User-Agent to identify callers and will reject requests without one.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-code-leaks-your-email-user-agent-header-how-to-stop-it-2026">Claude Code Leaks Your Email in Headers: 5-Min Fix - explainx.ai</a></li>
<li><a href="https://aiweekly.co/alerts/claude-code-bug-report-alleges-email-leak-in-user-agent-header">Claude Code bug report alleges email leak in User-Agent ...</a></li>
<li><a href="https://dev.to/frankchu/8-leaks-pass-anthropics-23-test-email-fix-2e66">8 leaks pass Anthropic's 23-test email fix - DEV Community</a></li>

</ul>
</details>

**Discussion**: Commenters offered a plausible explanation that the SEC API requires an email in the User-Agent, while others linked related past issues about email auto-injection and hidden trackers. Some users blamed Claude for increased spam, but others pushed back, noting spam predates AI and blaming Claude may be far-fetched.

**Tags**: `#privacy`, `#security`, `#AI coding tools`, `#Claude Code`, `#Hacker News`

---

<a id="item-3"></a>
## [MS Paint Remote Code Execution Vulnerability Raises Concerns](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 8.0/10

A newly disclosed CVE (CVE-2026-83844) reveals a remote code execution vulnerability in MS Paint versions 11.0.0.0 to before 11.2605.91.0, exploitable via crafted network packets without user interaction. This is significant because MS Paint is a simple graphics application that typically does not handle network traffic, so a network-facing RCE without user interaction is surprising and could affect many Windows users if exploited. The vulnerability is classified as an out-of-bounds read (CWE-125) in Windows Paint, and Microsoft's advisory confirms the network attack vector and lack of required authentication; the fix is available in version 11.2609.401.0, but some users report that Windows Update does not show the update.

hackernews · kuberwastaken · Nov 5, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50384233)

**Background**: MS Paint is a basic image editor included with Windows. A remote code execution (RCE) vulnerability allows an attacker to run arbitrary code on a victim's machine. Typically, such vulnerabilities require user interaction (e.g., opening a malicious file), but this one is network-based and requires no user action, which is unusual for a simple application like Paint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-83844/">CVE-2026-83844: Windows Paint RCE Vulnerability - SentinelOne</a></li>
<li><a href="https://cybersecuritynews.com/windows-paint-rce-vulnerability/">Microsoft Paint 0-Click Vulnerability Could Allow Hackers to ...</a></li>
<li><a href="https://windowsforum.com/news/cve-2026-83844-windows-11-paint-rce-fix-confusion-and-how-to-check-your-version.451018/">CVE-2026-83844: Windows 11 Paint RCE Fix Confusion and How to ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock and skepticism that Paint has a network-facing attack surface, questioning why a simple image editor would have a remote code execution vulnerability. Some noted that the fix was only available via the Microsoft Store, not Windows Update, and others pointed out that older versions of Paint are likely unaffected.

**Tags**: `#security`, `#vulnerability`, `#windows`, `#remote-code-execution`, `#microsoft`

---

<a id="item-4"></a>
## [SemiAnalysis: Google's TPU Challenges NVIDIA's CUDA Moat in Inference](https://newsletter.semianalysis.com/p/tpu-strikes-the-king) ⭐️ 8.0/10

SemiAnalysis published a deep-dive analysis arguing that Google's TPU is now a viable alternative to NVIDIA's CUDA for inference workloads, highlighting ecosystem tools such as TorchTPU, vLLM, SGLang, and llm-d. This matters because NVIDIA's CUDA software moat has long been a key barrier to competition in AI hardware; if TPUs become a credible inference alternative, it could reshape the AI infrastructure market and pressure NVIDIA's dominance. The analysis covers Google's collaboration with Meta on TorchTPU, a native PyTorch backend for TPUs, as well as support for popular inference engines like vLLM and SGLang, and orchestration via llm-d; however, the excerpt is brief and lacks full technical benchmarks.

rss · Semianalysis · Nov 5, 19:03

**Background**: TPUs (Tensor Processing Units) are Google's custom ASICs designed to accelerate machine learning workloads, available through Google Cloud. CUDA is NVIDIA's proprietary parallel computing platform and programming model, which has become the de facto standard for GPU-accelerated AI, creating a strong ecosystem lock-in. Inference is the phase where a trained AI model makes predictions, and it is increasingly important as AI models are deployed at scale. TorchTPU is an open-source project from Google and Meta that provides a native PyTorch backend for TPUs, aiming to make TPUs more accessible to PyTorch developers.

<details><summary>References</summary>
<ul>
<li><a href="https://pytorch.org/blog/introducing-torchtpu/">Introducing TorchTPU - PyTorch</a></li>
<li><a href="https://cloud.google.com/tpu">Tensor Processing Units ( TPUs ) | Google Cloud</a></li>
<li><a href="https://deepwiki.com/llm-d/llm-d/2.4-model-servers-(vllm-sglang-trt-llm)">Model Servers ( vLLM , SGLang , TRT-LLM) | llm - d / llm - d | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#CUDA`, `#AI inference`, `#hardware`, `#SemiAnalysis`

---