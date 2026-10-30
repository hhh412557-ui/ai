---
title: "Horizon Summary: 2026-10-30 (ZH)"
date: 2026-10-30
lang: zh
---

> 从 22 条内容中筛选出 3 条重要资讯。

---

1. [Mistral 开源 1 万亿参数 Mistral Large 4 模型权重](#item-1) ⭐️ 9.0/10
2. [范德瓦尔登数 w(2;3,21)=416 获 Lean 4 机器验证证明](#item-2) ⭐️ 9.0/10
3. [币安遭黑客攻击：被盗 56 亿美元，已冻结 24 亿美元](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mistral 开源 1 万亿参数 Mistral Large 4 模型权重](https://mistral.ai/news/mistral-large-4-oss/) ⭐️ 9.0/10

Mistral 发布了 Mistral Large 4（代号“Le Chonk”）的开放权重，这是一个 1 万亿参数的多模态混合专家模型，同时大幅下调了 API 价格。新价格几乎是预览版的一半：输入每百万 token 0.7 美元，输出每百万 token 2.1 美元，此前分别为 1.36 美元和 4.18 美元。 开源一个前沿规模的 1 万亿参数模型是开源 AI 的重大里程碑，使研究者和企业能够检查、微调并在自己的基础设施上部署该模型。大幅降价也使 Mistral 在与其他 API 提供商的竞争中更具优势，可能惠及对成本敏感的企业和寻求本地替代方案的欧洲用户。 Mistral Large 4 采用细粒度混合专家设计，在 1.05 万亿总参数中激活 520 亿参数，并配备 1.6B 视觉编码器处理图像输入，提供三种推理模式以权衡成本与性能。它在编码和防御性安全方面领先开放权重基准，对恶意网络请求的平均拒绝率达到 96.6%，但社区成员指出缺乏非恶意请求处理的数据。

hackernews · kuberwastaken · 10月29日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=50289418)

**背景**: 开放权重是训练好的 AI 模型公开释放的学习参数，允许任何人下载并运行该模型。1 万亿参数模型处于规模前沿，通常需要云基础设施来服务，而混合专家（MoE）架构每次输入只激活部分参数以降低推理成本。法国 AI 公司 Mistral 一直在扩展其 offerings，引入第三方模型和 Responses API 等功能，将自己定位为对欧盟友好的提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/mistral-large-4-oss/">Mistral Large 4 (Le Chonk) is now open weight | Mistral</a></li>
<li><a href="https://ollama.com/library/mistral-large-4">mistral - large - 4</a></li>
<li><a href="https://huggingface.co/blog/mistral-large4">Welcome Le Chonk: Mistral Large 4 on Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎此次发布和降价，有人指出新价格值得对该模型的竞争力进行重大重新评估。其他人赞扬 Mistral 增加了竞争并成为可靠的欧盟提供商，但一位批评者质疑网络安全基准未报告对非恶意请求的拒绝率。

**标签**: `#LLM`, `#open-weights`, `#Mistral`, `#AI`, `#model-release`

---

<a id="item-2"></a>
## [范德瓦尔登数 w(2;3,21)=416 获 Lean 4 机器验证证明](https://www.reddit.com/r/MachineLearning/comments/1xivpue/w2321_416_a_van_der_waerden_number_conjectured_by/) ⭐️ 9.0/10

2010 年由 Kullmann 提出、且今年仍被 DeepMind 形式化猜想列表列为未解决的范德瓦尔登数 w(2;3,21)=416，现已获得 Lean 4 内核检查的证明。该证明由 Hupyy 的神经符号系统 LPM 生成，涵盖 209 个情形和 38,661,140 个叶公式，每个叶公式均由经过验证的 LRAT 检查器 cake_pr 反驳。 这以一个完全机器验证的证明解决了一个长期未决的组合猜想，标志着形式数学与 AI 辅助定理证明的重大里程碑。它表明神经符号系统能够生成不仅正确而且可被可信内核验证的证明，有望加速开放问题的形式化进程。 该证明是一个 Lean 4 定理，涵盖 209 个情形和 38,661,140 个叶公式，每个反驳均由 cake_pr（在 CakeML 中验证的 LRAT 检查器）检查，并通过摘要与其 Lean 项绑定。提供了 13.6 GB 的证据包，包括 Lean 源代码、检查器记录和重放工具包；只有 Lean 内核或 cake_pr 接受的内容才被计入。

reddit · r/MachineLearning · /u/Rodriguez909 · 10月29日 20:46

**背景**: 范德瓦尔登定理指出，对于任意正整数 r 和 k，存在最小的 N，使得 {1,...,N} 的任意 r 着色都包含长度为 k 的单色等差数列；这个 N 就是范德瓦尔登数 W(r,k)。Lean 4 是一个基于依赖类型论的证明助手和函数式编程语言，用于形式化和验证数学证明。LRAT 是 SAT 求解器的一种证明格式，而 cake_pr 是在 CakeML（一个经过形式化验证的编译器和运行时系统）中实现的经过验证的 LRAT 检查器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Van_der_Waerden_number">Van der Waerden number</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7984575/">cake_lpr: Verified Propagation Redundancy Checking in CakeML</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#lean4`, `#automated-theorem-proving`, `#combinatorics`, `#neuro-symbolic-ai`

---

<a id="item-3"></a>
## [币安遭黑客攻击：被盗 56 亿美元，已冻结 24 亿美元](https://arkm.com/explorer/entity/21a94755-f604-45e5-9501-6542e23005e8) ⭐️ 8.0/10

一名黑客据称从全球最大加密货币交易所币安窃取了 56 亿美元，其中约 24 亿美元已被稳定币发行商 Circle 和 Tether 冻结。币安确认正在调查此事件，其创始人表示“看起来确实是币安遭到了黑客攻击”。 如果得到证实，这将是史上最大的加密货币黑客事件，规模可能超过 Mt. Gox 崩盘，并动摇人们对中心化交易所的信心。稳定币的快速冻结凸显了 Circle 和 Tether 等发行商干预链上资产的日益增强的权力，引发了关于加密货币中心化问题的质疑。 根据链上数据，被冻结的资金包括以太坊上的 9.7115 亿 USDT 和 8.23 亿 USDC、波场上的 3.1273 亿 USDT 以及以太坊上的 1.75 亿 USDT。该事件在 Hacker News 上引发了广泛讨论，获得超过 1000 个点赞和 600 条评论，Molly White 等知名人士也表示报道可信。

hackernews · Tiberium · 10月29日 21:38 · [社区讨论](https://news.ycombinator.com/item?id=50296470)

**背景**: USDT（Tether）和 USDC（Circle）等稳定币是与美元挂钩的加密货币，广泛用于交易和结算。其发行商可以在链上冻结资金，这一功能此前曾被用于追回被盗资产，但也引发了对控制权的担忧。币安是按交易量计算全球最大的加密货币交易所，因此任何安全漏洞都会对整个市场产生重大影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/business/2026/oct/29/binance-crypto-exchange-hack">Crypto firms freeze more than $2.5bn in funds as Binance investigates...</a></li>
<li><a href="https://www.independent.co.uk/tech/security/bitcoin-binance-hack-price-market-cryptocurrency-b3076092.html">Bitcoin market in chaos amid fears Binance crypto exchange has...</a></li>
<li><a href="https://cryptoslate.com/coins/tether/">Tether price today, USDT to USD chart, marketcap and... | CryptoSlate</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了 Circle 和 Tether 已冻结的 24 亿美元，并附上了具体交易链接，还将其与历史上的 Mt. Gox 讨论帖相提并论。有人指出 Molly White 认为该事件是真实的，还有人讨论了数字资产可能出现的“避险趋优”现象，并开玩笑说要把 AI 代理关在沙盒里。

**标签**: `#cryptocurrency`, `#security`, `#binance`, `#hack`, `#stablecoins`

---