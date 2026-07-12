---
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 45 条内容中筛选出 3 条重要资讯。

---

1. [Grok Build CLI 上传整个仓库，包括密钥文件](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 在回答质量上超越医生](#item-2) ⭐️ 9.0/10
3. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Grok Build CLI 上传整个仓库，包括密钥文件](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

安全研究人员发现，xAI 的 Grok Build CLI 会将整个仓库内容（包括 .env 等敏感文件）上传到 xAI 服务器，无论代理读取了什么。 这一隐私缺陷削弱了开发者对 AI 编码工具的信任，因为它未经明确同意就将密钥和专有代码暴露给第三方。 该 CLI 会上传每个跟踪文件的内容以及 git 历史记录，与代理读取的内容无关，并且会逐字、未编辑地传输文件内容。

hackernews · jhoho · 7月12日 01:09 · [社区讨论](https://news.ycombinator.com/item?id=48877371)

**背景**: Grok Build 是一款基于终端的编码代理，由 Grok 4.5 驱动，已面向 SuperGrok 和 X Premium Plus 订阅者发布 Beta 版。许多 AI 编码工具会上传代码到云端模型进行处理，但用户往往不清楚发送数据的范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了震惊和担忧，有些人表示他们已经对 Claude 等其他工具进行沙盒化以防止此类数据泄露。其他人指出，许多编码代理都有类似行为，但缺乏透明度是核心问题。

**标签**: `#privacy`, `#security`, `#AI coding tools`, `#xAI`, `#data leakage`

---

<a id="item-2"></a>
## [GPT-5.6 在回答质量上超越医生](https://x.com/sama/status/2075985056846451123) ⭐️ 9.0/10

Sam Altman 宣布，医生发现 GPT-5.6 的回答比医生自己写的回答缺陷更少。 这表明 GPT-5.6 可能在医学沟通上超越人类专家，有望改变临床决策支持和患者教育。 GPT-5.6 是 OpenAI 于 2026 年 7 月 9 日发布的模型系列，包括 Luna、Terra 和 Sol 三个变体；其中 Sol 变体在编程、科学和网络安全方面达到了最先进水平。

twitter · sama · 7月11日 16:46

**背景**: 像 GPT-5.6 这样的大型语言模型通过大量文本数据训练，能够生成类似人类的回答。在医学 AI 中，评估回答质量通常涉及使用评分标准或专家评审将 AI 输出与人类医生的回答进行比较。Altman 的说法表明，医生自己判断 GPT-5.6 的回答更优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#GPT-5.6`, `#healthcare`, `#medical AI`, `#OpenAI`

---

<a id="item-3"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了旧的 PagedAttention 实现，并引入了新的 Streaming Parser Engine，同时新增了对 LLaVA-OneVision-2 和 GLM-5 等多个新模型的支持。 此版本标志着 vLLM 架构的重大转变，通过标准化 Model Runner V2 提高了性能和模块化，惠及所有稠密模型用户。移除 PagedAttention 简化了代码库，并标志着全面采用更新的注意力后端。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存，以及带有完整 CUDA 图的动态推测解码。Transformers 建模后端已优化至与原生 vLLM 性能相当，此版本包含来自 232 位贡献者的 558 次提交。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个用于大语言模型的高性能推理引擎，最初以其高效管理键值缓存的 PagedAttention 算法而闻名。Model Runner V2 是一个重新设计的执行核心，旨在解决技术债务，提高模块化、性能以及对推测解码和多模态输入等高级功能的支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#model serving`

---