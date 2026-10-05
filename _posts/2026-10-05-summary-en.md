---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 16 items, 3 important content pieces were selected

---

1. [Strata runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100+ tokens/sec](#item-1) ⭐️ 8.0/10
2. [Stockfish distilled into ResNet/ViT on 1B positions, 3.9B dataset released](#item-2) ⭐️ 8.0/10
3. [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100+ tokens/sec](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

A GitHub project called Strata now lets users run the 125B-parameter Qwen3.8-Flash-Next model on consumer hardware such as an RTX 4090, achieving over 100 tokens per second. Community members report concrete results, including 124 tokens/sec on a 4090 with 128GB DDR5 and about 60 tokens/sec on an AMD R9700 32GB combined with 96GB DDR4. This is significant because a 125B-parameter model normally requires server-class hardware, so running it locally at high speed brings powerful AI capabilities to ordinary PCs without sending data to the cloud. It could reshape local AI workflows for developers, privacy-conscious users, and anyone who wants capable coding and vision assistance on their own machine. Qwen3.8-Flash-Next is a sparse mixture-of-experts model with 125B total parameters, only 6B activated per token, plus 51B additional n-gram embedding parameters held off the accelerator. A critical benchmark comparison found Strata's vision performance notably worse than llama.cpp on the same GGUF and vision adapter weights, with a median error of 154.8 pixels versus 46.5 pixels.

hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Large language models are typically measured in parameters, and a 125B model would normally need multiple high-end GPUs to run. Quantization reduces the precision of model weights, shrinking memory use and speeding up inference at some cost to accuracy, while mixture-of-experts architectures activate only a small subset of parameters per token to save compute. Strata is an open-source project that packages these techniques so a single consumer GPU plus system RAM can serve a large model locally.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/Strata: Qwen3.8-Flash-Next on any consumer ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>

</ul>
</details>

**Discussion**: Sentiment is largely positive, with users reporting strong real-world speeds on RTX 4090, AMD R9700, and even a Ryzen 6600H iGPU at 10 tokens/sec. However, a detailed benchmark showed Strata's vision accuracy is much worse than llama.cpp on identical weights, and one commenter expressed skepticism about going below 4-bit quantization due to quality degradation.

**Tags**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#local AI`

---

<a id="item-2"></a>
## [Stockfish distilled into ResNet/ViT on 1B positions, 3.9B dataset released](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/) ⭐️ 8.0/10

A developer distilled Stockfish's value function into a combined ResNet/ViT neural network using 1 billion positions from the Gigafish dataset, and released the full 3.9 billion position dataset on Hugging Face. The dataset is built from 37 months of Lichess games and is intended to approximate Stockfish's depth-limited search faster than the engine itself. This project shows that knowledge distillation can compress a strong chess engine's evaluation into a neural network that may be competitive with Stockfish's NNUE, while the public 3.9B-position dataset provides a large-scale resource for chess AI and distillation research. It also offers practical insights into combining CNNs and vision transformers for board-game representation learning. The author held search depth constant because the value function at a fixed depth approximates the subtree beneath it, and found that a pure vision transformer was slow to understand the board while a CNN benefited early from geometric inductive biases, with the best results coming from combining both architectures. The released dataset, gigafish-3.8b-d10, is available on Hugging Face and is derived from 37 months of Lichess games.

reddit · r/MachineLearning · /u/microscope1024 · Oct 5, 04:11

**Background**: Stockfish is a free, open-source chess engine that has been among the strongest in the world for years, and since 2020 it has used an efficiently updatable neural network (NNUE) for evaluation, fully replacing its hand-crafted evaluation in 2023. Knowledge distillation is a machine learning technique that transfers knowledge from a large teacher model to a smaller student model by training the student to match the teacher's outputs. In this project, Stockfish acts as the teacher whose value function is distilled into a ResNet/ViT student network.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stockfish_NNUE">Stockfish NNUE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://huggingface.co/datasets/lukesalamone/gigafish-3.8b-d10">lukesalamone/ gigafish -3.8b-d10 · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#knowledge-distillation`, `#chess-ai`, `#deep-learning`, `#dataset`, `#vision-transformer`

---

<a id="item-3"></a>
## [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

Over the past 30 days, top scores on the ARC-AGI-3 Kaggle leaderboard surged from roughly 7% to 56%, achieved by small local models running inside a harness. This means these compact models now surpass average human performance on a benchmark explicitly designed to test human-like reasoning. This rapid improvement suggests that AI reasoning on interactive, novel-environment tasks is advancing much faster than previously expected, potentially reshaping how the community views progress toward AGI. It also highlights that small, locally runnable models can be competitive on benchmarks once thought to require frontier-scale systems. Kaggle competition rules restrict participants to small local models, so the 56% score reflects a harness-and-model combination rather than a single large frontier model. The benchmark is interactive, requiring agents to explore novel environments, acquire goals on the fly, and build adaptable world models.

reddit · r/MachineLearning · /u/we_are_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark from the ARC Prize organization, designed to challenge AI agents to explore unfamiliar environments, infer goals on the fly, and learn continuously. Unlike static benchmarks, it emphasizes learning efficiency and adaptability, with the philosophy that true AGI will arrive only when AI matches human learning efficiency. Kaggle hosts related competitions where participants are limited to small local models, making leaderboard gains a real-time pulse check on progress toward AGI.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://benchlm.ai/benchmarks/arcAgi3">ARC - AGI - 3 Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>
<li><a href="https://arcprize.org/competitions/2026">ARC Prize 2026 — $2M in prizes, 3 tracks, advancing open-source...</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#AI benchmarks`, `#reasoning`, `#Kaggle`, `#machine learning`

---