---
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 16 条内容中筛选出 3 条重要资讯。

---

1. [Strata 让 125B 的 Qwen 3.8 Flash Next 在 RTX 4090 上以每秒 100+ token 运行](#item-1) ⭐️ 8.0/10
2. [Stockfish 被蒸馏为 ResNet/ViT 模型，3.9B 数据集已发布](#item-2) ⭐️ 8.0/10
3. [ARC-AGI-3 Kaggle 得分 30 天内从 7%跃升至 56%](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata 让 125B 的 Qwen 3.8 Flash Next 在 RTX 4090 上以每秒 100+ token 运行](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata 的 GitHub 项目现在可以让用户在 RTX 4090 等消费级硬件上运行 125B 参数的 Qwen3.8-Flash-Next 模型，速度超过每秒 100 个 token。社区成员报告了具体结果，包括在配备 128GB DDR5 的 4090 上达到每秒 124 个 token，以及在 AMD R9700 32GB 搭配 96GB DDR4 时达到约每秒 60 个 token。 这意义重大，因为 125B 参数的模型通常需要服务器级硬件，而能在本地高速运行意味着普通 PC 也能获得强大的 AI 能力，且无需将数据发送到云端。这可能重塑本地 AI 工作流，惠及开发者、注重隐私的用户，以及希望在自己机器上获得强大编码和视觉辅助的任何人。 Qwen3.8-Flash-Next 是一个稀疏混合专家模型，总参数 125B，但每个 token 仅激活 6B，另有 51B 的 n-gram 嵌入参数存放在加速器之外。一项关键基准对比发现，在相同的 GGUF 和视觉适配器权重下，Strata 的视觉性能明显差于 llama.cpp，中位误差为 154.8 像素，而 llama.cpp 为 46.5 像素。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 大语言模型通常以参数规模衡量，125B 的模型一般需要多块高端 GPU 才能运行。量化通过降低模型权重的精度来减少内存占用并加速推理，但会牺牲一定的准确度；而混合专家架构每个 token 只激活一小部分参数以节省计算。Strata 是一个开源项目，将这些技术打包起来，使单块消费级 GPU 加上系统内存就能在本地服务一个大模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/Strata: Qwen3.8-Flash-Next on any consumer ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏正面，用户报告了在 RTX 4090、AMD R9700 甚至 Ryzen 6600H 核显上每秒 10 个 token 的真实速度。不过，一项详细基准显示，在相同权重下 Strata 的视觉准确度远差于 llama.cpp，还有评论者对低于 4-bit 的量化表示怀疑，认为会导致质量明显下降。

**标签**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#local AI`

---

<a id="item-2"></a>
## [Stockfish 被蒸馏为 ResNet/ViT 模型，3.9B 数据集已发布](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

一位开发者利用 Gigafish 数据集中的 10 亿个棋局位置，将 Stockfish 的价值函数蒸馏到一个 ResNet/ViT 组合神经网络中，并在 Hugging Face 上发布了完整的 39 亿位置数据集。该数据集基于 37 个月的 Lichess 对局构建，目标是比 Stockfish 引擎本身更快地近似其深度受限搜索。 该项目表明，知识蒸馏可以将强大国际象棋引擎的评估能力压缩到一个可能与 Stockfish 的 NNUE 相竞争的神经网络中，同时公开的 39 亿位置数据集为国际象棋 AI 和蒸馏研究提供了大规模资源。它还提供了将 CNN 与视觉 Transformer 结合用于棋类表示学习的实用经验。 作者保持搜索深度不变，因为固定深度下的价值函数近似其下方的子树；他发现纯视觉 Transformer 理解棋盘较慢，而 CNN 由于固有的几何归纳偏置在训练初期更有效，最终将两者结合取得了最佳结果。发布的数据集 gigafish-3.8b-d10 可在 Hugging Face 上获取，来源于 37 个月的 Lichess 对局。

reddit · r/MachineLearning · /u/microscope1024 · 10月5日 04:11

**背景**: Stockfish 是一款免费开源的国际象棋引擎，多年来一直是世界上最强的引擎之一；自 2020 年起它使用可高效更新的神经网络（NNUE）进行评估，并在 2023 年完全取代了手工设计的评估函数。知识蒸馏是一种机器学习技术，通过训练学生模型匹配教师模型的输出来将知识从大型教师模型迁移到较小的学生模型。在本项目中，Stockfish 充当教师，其价值函数被蒸馏到 ResNet/ViT 学生网络中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stockfish_NNUE">Stockfish NNUE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://huggingface.co/datasets/lukesalamone/gigafish-3.8b-d10">lukesalamone/ gigafish -3.8b-d10 · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#knowledge-distillation`, `#chess-ai`, `#deep-learning`, `#dataset`, `#vision-transformer`

---

<a id="item-3"></a>
## [ARC-AGI-3 Kaggle 得分 30 天内从 7%跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

在过去 30 天里，ARC-AGI-3 Kaggle 排行榜的最高得分从约 7%飙升到 56%，这些成绩由运行在特定框架（harness）中的小型本地模型取得。这意味着这些紧凑型模型在一个专门为测试类人推理能力而设计的基准上，已经超过了普通人类的平均水平。 这一快速进步表明，AI 在交互式、新颖环境任务上的推理能力提升速度远超此前预期，可能改变业界对 AGI 进展的看法。同时它也说明，小型、可在本地运行的模型在曾被认为需要前沿规模系统的基准上也能具备竞争力。 Kaggle 比赛规则限制参赛者只能使用小型本地模型，因此 56%的成绩反映的是框架与模型的组合效果，而非单个大型前沿模型。该基准是交互式的，要求智能体探索新颖环境、即时获取目标并构建可适应的世界模型。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI-3 是 ARC Prize 组织推出的交互式推理基准，旨在挑战 AI 智能体探索陌生环境、即时推断目标并持续学习的能力。与静态基准不同，它强调学习效率和适应性，其核心理念是只有当 AI 达到人类的学习效率时，真正的 AGI 才会到来。Kaggle 上举办的相关比赛限制参赛者只能使用小型本地模型，因此排行榜上的进步被视为衡量 AGI 进展的实时脉搏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://benchlm.ai/benchmarks/arcAgi3">ARC - AGI - 3 Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>
<li><a href="https://arcprize.org/competitions/2026">ARC Prize 2026 — $2M in prizes, 3 tracks, advancing open-source...</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#AI benchmarks`, `#reasoning`, `#Kaggle`, `#machine learning`

---