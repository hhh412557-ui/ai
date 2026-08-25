---
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 26 条内容中筛选出 4 条重要资讯。

---

1. [MS Paint 和照片应用为本地 AI 图像添加隐形 GUID 水印](#item-1) ⭐️ 8.0/10
2. [旧金山被重制为交互式 3D 网页游戏](#item-2) ⭐️ 8.0/10
3. [海洋温度创历史新高，凸显气候危机](#item-3) ⭐️ 8.0/10
4. [你的可执行文件是 SQLite 数据库：一个巧妙的 Linux 技巧](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MS Paint 和照片应用为本地 AI 图像添加隐形 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

逆向工程揭示，微软画图（MS Paint）和照片（Photos）应用会在每张本地生成的 AI 图像中嵌入包含服务器颁发的 16 字节 GUID 的隐形水印，即使使用本地模型也是如此。该 GUID 是在本地生成之前，通过向 Azure Front Door 端点发送强制远程审核请求而获得的。 这引发了重大的隐私和匿名性担忧，因为隐形水印可能被用来将图像追溯到个人微软账户，从而可能支持版权传票或监控。这也凸显了在广泛使用的消费软件中嵌入追踪机制的趋势，影响所有使用这些内置 Windows 应用的用户。 该水印是隐形的，无法禁用，并且即使使用本地 AI 模型（而不仅仅是基于云的模型）也会添加。目前尚不清楚该水印是否适用于所有 AI 辅助编辑（如背景移除），但 GUID 被嵌入到图像元数据或像素数据中。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 微软画图和照片应用集成了 AI 功能，可以在本地生成或编辑图像。为了进行内容审核，这些应用会将提示词发送到远程服务器，服务器返回一个 GUID，然后将其作为隐形水印嵌入。这是微软追踪 AI 生成内容的更广泛努力的一部分，但引发了关于用户隐私和潜在滥用的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible...</a></li>
<li><a href="https://mangodeveloper.com/articles/microsoft-paint-embeds-invisible-guid-watermarks-in-local-ai-images-via-remote-moderation-server">Microsoft Paint Embeds Invisible GUID Watermarks in Local AI ...</a></li>
<li><a href="https://elsolitario.org/en/2026/08/24/microsoft-paint-invisible-guid-watermark/">Invisible Watermark in Microsoft Paint: How It Works</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了震惊和担忧，一些人指出 AI 方面是转移视线，真正的问题是在每张图像中秘密添加唯一标识符，这可能导致用户去匿名化。其他人则指出微软过去在类似功能上的草率实施，导致不信任，并建议避免使用这些应用。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#reverse-engineering`

---

<a id="item-2"></a>
## [旧金山被重制为交互式 3D 网页游戏](https://sf.thijs.gg/) ⭐️ 8.0/10

一个基于网页的交互式 3D 旧金山城市模型已发布，它利用真实地图数据构建，让用户能以游戏般的方式探索城市。该项目可在 sf.thijs.gg 访问，已获得社区广泛关注，获得 348 个点赞和 120 条评论。 该项目展示了将真实 GIS 数据转化为浏览器中可直接访问的沉浸式交互体验的潜力，可能激发城市规划、教育和娱乐领域的新应用。它也凸显了基于网页的 3D 城市可视化以及利用开放数据进行创意项目的日益增长趋势。 该项目似乎使用了真实地图数据，可能来自苹果地图，社区评论中提到的“retroplasma flyover 逆向工程代码”和 HEIF 纹理格式暗示了这一点。交互体验包括驾驶车辆和收集硬币，但缺乏其他游戏元素。用户建议增加街道名称、地标和地址传送等功能。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**背景**: 基于网页的 3D 城市可视化是一个新兴领域，利用 GIS 数据和浏览器技术创建城市环境的交互式模型。像 3DCityDB-Web-Map-Client 和 3DCity.ai 等工具也能实现类似体验，但该项目因其游戏化的呈现方式和对真实数据的使用而脱颖而出。相关技术通常涉及 3D 分块、基于网页的渲染以及高效处理浏览器中的大型数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://3dcity.ai/">3DCity.ai — Design AI-Ready Cities in Your Browser</a></li>
<li><a href="https://www.3dcitydb.org/3dcitydb-web-map/1.8.0/3dwebclient/index.html">3DCityDB-Web-Map-Client</a></li>
<li><a href="https://link.springer.com/article/10.1007/s12145-023-01167-5">An interoperable web-based application for 3d city modelling ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪非常积极，用户对虚拟城市表示惊叹并产生情感共鸣。一些用户讨论技术细节，如数据来源和逆向工程方法，而另一些则建议改进，如添加街道名称、地标和多人游戏功能。还有用户分享了相关项目，如西雅图的 N64 风格地图。

**标签**: `#3D mapping`, `#web development`, `#GIS`, `#interactive visualization`, `#San Francisco`

---

<a id="item-3"></a>
## [海洋温度创历史新高，凸显气候危机](https://www.bbc.com/news/articles/c62m4gpnp78o) ⭐️ 8.0/10

根据最近的一份报告，海洋温度达到了有记录以来的最高水平，凸显了气候变化加速的态势。这一里程碑事件由 BBC 新闻报道，并引发了广泛讨论。 这一纪录意义重大，因为海洋温度是全球变暖的关键指标，影响天气模式、海平面和海洋生态系统。它凸显了当前减缓措施不足，以及采取更强有力气候行动的紧迫性。 报告指出，截至 2023 年，化石燃料仍占全球能源供应的 81.1%，仅比 2000 年的 81.4%略有下降，表明下降幅度微乎其微。此外，正如一位评论者所指出的，冰融化减少了海洋升温所需的能量，从而放大了升温效应。

hackernews · tcp_handshaker · 8月24日 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49424606)

**背景**: 海洋温度是气候变化的关键指标，因为海洋吸收了温室气体排放产生的 90%以上的多余热量。创纪录的高温可能导致更强烈的风暴、珊瑚白化和海平面上升。对化石燃料的持续依赖是这一变暖趋势的主要驱动因素。

**社区讨论**: 社区评论对化石燃料的缓慢下降表示担忧，一位用户指出，化石燃料不太可能在 2050 年前终结。其他人批评政府的不作为，尤其是美国，并分享教育资源。一位评论者反思了个人对几度升温严重性的认识。

**标签**: `#climate change`, `#ocean temperature`, `#environment`, `#fossil fuels`, `#policy`

---

<a id="item-4"></a>
## [你的可执行文件是 SQLite 数据库：一个巧妙的 Linux 技巧](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 8.0/10

Farid Zakaria 展示了一种技术，可以创建既是有效 SQLite 数据库又是可直接执行的 Linux 二进制的单一文件。通过将 SQLite 应用程序 ID 设置为“SELF”，并将 ELF 组件组织到 SQLite 表中，该文件可以通过注册到 binfmt_misc 的自定义解释器来执行。 这个技巧为软件分发和自省开辟了创造性的可能性，使可执行文件可以作为数据库进行查询和操作。它展示了深厚的技术洞察力，并可能激发打包、调试或自修改程序的新方法，尽管其直接的实际影响可能有限。 该技术依赖于将 SQLite 文件中偏移量 68 处的 4 字节应用程序 ID 设置为“SELF”（结构化可执行与可链接格式）。ELF 组件按照模式存储在多个 SQLite 表中，一个 C 解释器（self-exec）提取并执行它们。可以通过简单的命令进行 binfmt_misc 注册，如文章所示。

rss · Simon Willison · 8月24日 11:38

**背景**: ELF（可执行与可链接格式）是 Linux 和许多类 Unix 系统上可执行文件的标准二进制格式。SQLite 数据库的头部包含一个应用程序 ID 字段，用于标识创建数据库的应用程序。binfmt_misc 是 Linux 内核的一个特性，允许内核通过调用指定的解释器来识别和执行非本机二进制格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>
<li><a href="https://sqlite.org/forum/info/6a768e7dca11a7b2">SQLite User Forum: Usage of application_id and magic.txt</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论可能赞扬了该技巧的巧妙性和原创性，一些用户讨论了潜在的使用案例和局限性。关于这种方法的实用性和安全影响可能存在争论。

**标签**: `#SQLite`, `#ELF`, `#Linux`, `#executable`, `#hack`

---