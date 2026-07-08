---
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 63 items, 4 important content pieces were selected

---

1. [MIRA: 5B Parameter Multiplayer World Model for Rocket League](#item-1) ⭐️ 9.0/10
2. [Google Releases Gemma 4 Technical Report](#item-2) ⭐️ 9.0/10
3. [Kokoro TTS: High-Quality, CPU-Friendly Local Text-to-Speech](#item-3) ⭐️ 8.0/10
4. [sqlite-utils 4.0 adds database schema migrations](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MIRA: 5B Parameter Multiplayer World Model for Rocket League](https://www.reddit.com/r/MachineLearning/comments/1upofuw/mira_multiplayer_interactive_world_models_trained/) ⭐️ 9.0/10

MIRA is a 5 billion parameter multiplayer interactive world model trained on 10,000 hours of synthetic Rocket League data, enabling real-time 4-player simulation at 20 FPS on a single NVIDIA B200 GPU. The team has released an open-source codebase, a technical report, a 1,000-hour dataset, and a playable online demo. This is the first multiplayer world model capable of simulating highly dynamic environments with complex physics, conditioning on multiple agents' actions simultaneously. It opens new possibilities for multi-agent reinforcement learning, game AI, and interactive simulation, with open-source resources enabling broader research. The model uses a latent diffusion architecture to generate video frames from four players' actions, maintaining coherence under arbitrary action combinations. It runs at 20 FPS on a single B200 GPU (part of NVIDIA's Blackwell architecture with 180 GB HBM3e memory).

reddit · r/MachineLearning · /u/MasterScrat · Jul 7, 07:59

**Background**: World models are AI systems that learn to simulate the dynamics of an environment, enabling agents to plan and reason without constant real-world interaction. Prior world models have been limited to single-player or simple environments; MIRA extends this to multiplayer settings with complex physics like Rocket League, where multiple agents interact in real-time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mira-wm/mira">MIRA: Multiplayer Interactive World Models with ... - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2607.05352">[2607.05352] Multiplayer Interactive World Models with ...</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/b200.c4210">NVIDIA B200 Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**Tags**: `#world models`, `#reinforcement learning`, `#multiplayer`, `#Rocket League`, `#open source`

---

<a id="item-2"></a>
## [Google Releases Gemma 4 Technical Report](https://x.com/_akhaliq/status/2074589735780016129) ⭐️ 9.0/10

Google has released the Gemma 4 technical report, detailing a new generation of open-weight language models with architectures including 12B, 31B, and 26B A4B variants. This release marks a significant advancement in open-weight LLMs, providing researchers and practitioners with detailed insights into model architecture and training, which could accelerate innovation in the AI community. Gemma 4 models introduce native system prompt support and multi-token prediction with a dedicated draft model for speculative decoding, enabling faster inference without quality loss.

twitter · _akhaliq · Jul 7, 20:21

**Background**: Gemma 4 is Google's latest family of open-weight language models, following the earlier Gemma models. Open-weight models allow developers to access and fine-tune the model weights, promoting transparency and customization. The technical report provides detailed information on architecture, training data, and evaluation results.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Google`, `#Gemma`, `#technical report`

---

<a id="item-3"></a>
## [Kokoro TTS: High-Quality, CPU-Friendly Local Text-to-Speech](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro, an open-source text-to-speech model with 82 million parameters, offers high-quality speech synthesis that runs efficiently on CPUs without requiring a dedicated GPU. It also supports manual IPA pronunciation guides for improved accuracy. This makes high-quality TTS accessible to users without powerful GPUs, such as those with Apple Silicon or older hardware, democratizing voice synthesis for accessibility products, content consumption, and more. Kokoro-82M is particularly efficient on Apple Silicon via the mlx-audio library. Users have noted limitations with single-word utterances and homograph disambiguation, but the IPA override feature helps mitigate these issues.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio. Many high-quality TTS models require powerful GPUs for inference, limiting their use on consumer hardware. Kokoro is an open-source alternative that prioritizes CPU efficiency while maintaining natural-sounding output.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool using the ...</a></li>
<li><a href="https://www.vocabulary.com/resources/ipa-pronunciation/">IPA Pronunciation Guide | Vocabulary.com</a></li>

</ul>
</details>

**Discussion**: Community members praise Kokoro for its accessibility, especially for those without NVIDIA GPUs. Some note limitations with short phrases and homographs, but appreciate the IPA pronunciation guide feature. Others have integrated it into accessibility products and podcast workflows.

**Tags**: `#text-to-speech`, `#open-source`, `#accessibility`, `#machine learning`, `#CPU-friendly`

---

<a id="item-4"></a>
## [sqlite-utils 4.0 adds database schema migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0, released on July 7, 2026, introduces database schema migrations, nested transactions via a new db.atomic() method, and support for compound foreign keys. This is the first major version bump since 3.0 in November 2020. This release significantly enhances sqlite-utils as a tool for managing SQLite databases, providing a built-in migration system that was previously only available as a separate plugin. It simplifies schema evolution for Python developers and data scientists who rely on SQLite for lightweight data storage. Migrations are defined as Python functions using the new Migrations class, leveraging the powerful table.transform() method that implements the SQLite-recommended pattern of creating a new table, copying data, and renaming. The release also includes breaking changes detailed in an upgrade guide.

rss · Simon Willison · Jul 7, 19:32

**Background**: sqlite-utils is a Python library and CLI tool for creating and manipulating SQLite databases. Schema migrations are a way to apply incremental changes to a database schema while tracking which changes have been applied, which is essential for evolving applications. Previously, sqlite-utils users had to use a separate plugin (sqlite-migrate) for migrations.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/migrations.html">Database migrations - sqlite-utils</a></li>
<li><a href="https://simonwillison.net/2026/Jul/7/sqlite-utils-4/">sqlite-utils 4.0, now with database schema migrations</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open-source`

---