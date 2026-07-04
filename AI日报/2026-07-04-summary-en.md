---
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 55 items, 4 important content pieces were selected

---

1. [Mistral Releases Leanstral 1.5 for Lean Theorem Proving](#item-1) ⭐️ 8.0/10
2. [Current AI Launches Open Source AI Gap Map](#item-2) ⭐️ 8.0/10
3. [BaryGraph: Knowledge Graph with Embedded Relationships as Documents](#item-3) ⭐️ 8.0/10
4. [CDD recovers finetuning data from logits alone](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mistral Releases Leanstral 1.5 for Lean Theorem Proving](https://mistral.ai/news/leanstral-1-5/) ⭐️ 8.0/10

Mistral AI has released Leanstral 1.5, a fine-tuned language model specialized for the Lean theorem prover, enabling automated proof generation and bug finding in formal verification. This model makes formal verification more accessible by automating proof generation, potentially reducing the manual effort required to verify software correctness and find subtle bugs. Leanstral 1.5 is based on Mistral's Mixture-of-Experts architecture with 119B total parameters and 6.5B activated per token, supporting a 256K token context window.

hackernews · programLyrique · Jul 3, 22:33 · [Discussion](https://news.ycombinator.com/item?id=48780801)

**Background**: Lean is an interactive theorem prover that allows users to write mathematical proofs and verify software correctness. Formal verification uses mathematical methods to prove that a system meets its specification, which is critical for high-assurance software. Leanstral 1.5 aims to assist users by generating proof steps or identifying counterexamples.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**Discussion**: Some commenters questioned the bug-finding example, arguing that the overflow bug described would be easily caught by standard testing. Others praised Mistral's strategy of creating small, specialized models for niche tasks, noting cost-effectiveness for specific use cases.

**Tags**: `#AI`, `#formal verification`, `#theorem proving`, `#Mistral`, `#Lean`

---

<a id="item-2"></a>
## [Current AI Launches Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, has launched the Open Source AI Gap Map v0.1, which indexes 421 products and 24,400 artifacts across the open-source AI ecosystem. This comprehensive mapping provides a structured overview of the open-source AI landscape, helping researchers and practitioners identify gaps and opportunities. The underlying data, released under an MIT license, enables further analysis and community contributions. The map details 421 products: 266 software tools/libraries, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across 3 stack layers. The remaining 24,400 artifacts are uncategorized and unscored until researched.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership backed by $400 million in committed capital, aiming to build a public option for AI. The Gap Map builds on work from Columbia Convening, MOF, Hugging Face, and others to map the open-source AI stack and identify missing components.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`

---

<a id="item-3"></a>
## [BaryGraph: Knowledge Graph with Embedded Relationships as Documents](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph introduces BaryEdges, where every relationship in a knowledge graph is embedded as a first-class document with its own vector, enabling recursive MetaBary triads that surface structural bridges between distant concepts. The system runs locally on MongoDB Community with nomic-embed-text over the full English Wiktionary (6.6M documents). This approach addresses a fundamental limitation of flat vector search, which treats relationships as mere byproducts of point proximity, missing cross-domain connections. By embedding relationships as retrievable documents, BaryGraph could significantly improve retrieval-augmented generation (RAG) and graph-based retrieval for tasks requiring analogical or structural reasoning. The BaryEdge vector is computed as normalize(q·v(CM1) + q·v(CM2) + (1−q)·v(type)), where q is connection quality and v(type) is a contextual embedding of the relationship type. The system uses nomic-embed-text (768-dim) and builds a full graph in 8–14 hours on a single workstation with 8–16GB VRAM.

reddit · r/MachineLearning · /u/adseipsum · Jul 4, 08:24

**Background**: Traditional knowledge graph embeddings represent entities and relations as vectors, but relations are typically treated as transformations between entity vectors, not as standalone retrievable objects. Flat vector search retrieves documents based on cosine similarity, which fails to capture structural or relational analogies. BaryGraph reifies each relationship as its own document, enabling recursive abstraction through MetaBary triads that can bridge concepts with no direct embedding similarity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_graph_embedding">Knowledge graph embedding - Wikipedia</a></li>
<li><a href="https://www.ontotext.com/knowledgehub/fundamentals/what-are-knowledge-graph-embeddings/">What Are Knowledge Graph Embeddings? | Ontotext</a></li>

</ul>
</details>

**Tags**: `#knowledge graph`, `#embedding`, `#RAG`, `#vector search`, `#graph neural network`

---

<a id="item-4"></a>
## [CDD recovers finetuning data from logits alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 8.0/10

Contrastive Decoding Diffing (CDD) recovers verbatim finetuning data from large language models using only logit access, without needing model weights or activations. It achieves a verbatim recovery score of 4+/5 on 19 out of 20 model pairs across four model families, outperforming the prior white-box method Activation Difference Lens (ADL). CDD enables model diffing and data recovery with minimal access requirements, which is significant for model interpretability, security auditing, and detecting unauthorized finetuning. It also reveals that synthetic data generated by LLMs can leave identifiable fingerprints in finetuned models, raising privacy and provenance concerns. CDD uses a single default configuration without per-model calibration or layer selection, contrasting base and finetuned model logits directly. An unexpected finding was that the fictional persona 'Dr. Elena Rodriguez' appeared across semantically unrelated finetuning domains, traced back to Claude Sonnet 3.6's bias in synthetic data generation.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to surface behavioral differences between language models, often to detect finetuning or misalignment. Prior work, Activation Difference Lens (ADL), required full weight access and only recovered vague domain descriptions. Contrastive decoding is a technique that contrasts log probabilities of a strong and weak model to improve generation quality; CDD adapts this idea for model diffing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2309.09117">[2309.09117] Contrastive Decoding Improves Reasoning in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2602.10371">[2602.10371] Simple LLM Baselines are Competitive for Model Diffing</a></li>
<li><a href="https://arxiv.org/html/2510.13900">Narrow Finetuning Leaves Clearly Readable Traces in Activation ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#model diffing`, `#interpretability`, `#finetuning`, `#security`

---