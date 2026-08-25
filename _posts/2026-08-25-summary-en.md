---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 26 items, 4 important content pieces were selected

---

1. [MS Paint and Photos Invisibly Watermark Local AI Images with GUID](#item-1) ⭐️ 8.0/10
2. [San Francisco Recreated as an Interactive 3D Web Game](#item-2) ⭐️ 8.0/10
3. [Oceans Hit Record High Temperatures, Highlighting Climate Crisis](#item-3) ⭐️ 8.0/10
4. [Your Executable Is a SQLite Database: A Clever Linux Hack](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [MS Paint and Photos Invisibly Watermark Local AI Images with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Reverse engineering reveals that Microsoft Paint and Photos embed an invisible watermark containing a server-issued 16-byte GUID into every locally generated AI image, even when using local models. The GUID is obtained from a mandatory remote moderation request to an Azure Front Door endpoint before local generation runs. This raises significant privacy and anonymity concerns, as the invisible watermark could be used to trace images back to individual Microsoft accounts, potentially enabling copyright subpoenas or surveillance. It also highlights a broader trend of embedding tracking mechanisms in widely-used consumer software, affecting all users of these built-in Windows apps. The watermark is invisible and cannot be disabled, and it is added even when using local AI models, not just cloud-based ones. It is unclear whether the watermark applies to all AI-assisted edits, such as background removal, but the GUID is embedded in the image metadata or pixel data.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: Microsoft Paint and Photos have integrated AI features that can generate or edit images locally. To moderate content, these apps send prompts to a remote server, which returns a GUID that is then embedded as an invisible watermark. This is part of Microsoft's broader effort to track AI-generated content, but it has sparked concerns about user privacy and the potential for misuse.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible...</a></li>
<li><a href="https://mangodeveloper.com/articles/microsoft-paint-embeds-invisible-guid-watermarks-in-local-ai-images-via-remote-moderation-server">Microsoft Paint Embeds Invisible GUID Watermarks in Local AI ...</a></li>
<li><a href="https://elsolitario.org/en/2026/08/24/microsoft-paint-invisible-guid-watermark/">Invisible Watermark in Microsoft Paint: How It Works</a></li>

</ul>
</details>

**Discussion**: Community comments express shock and concern, with some noting that the AI aspect is a red herring and the real issue is the secret addition of unique identifiers to every image, which could be used to de-anonymize users. Others point out Microsoft's past sloppy implementations of similar features, leading to distrust and recommendations to avoid using these apps.

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#reverse-engineering`

---

<a id="item-2"></a>
## [San Francisco Recreated as an Interactive 3D Web Game](https://sf.thijs.gg/) ⭐️ 8.0/10

A web-based interactive 3D representation of San Francisco, built from real map data, has been released, allowing users to explore the city in a game-like environment. The project, accessible at sf.thijs.gg, has gained significant community attention with 348 points and 120 comments. This project demonstrates the potential of turning real-world GIS data into immersive, interactive experiences accessible directly in the browser, which could inspire new applications in urban planning, education, and entertainment. It also highlights the growing trend of web-based 3D city visualization and the use of open data for creative projects. The project appears to use real map data, possibly from Apple Maps, as suggested by community comments referencing the 'retroplasma flyover-reverse-engineering code' and the HEIF texture format. The interactive experience includes driving a vehicle and collecting coins, though it lacks other game elements. Users have suggested potential enhancements like street names, landmarks, and address teleportation.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: Web-based 3D city visualization is an emerging field that leverages GIS data and browser technologies to create interactive models of urban environments. Tools like 3DCityDB-Web-Map-Client and platforms like 3DCity.ai enable similar experiences, but this project stands out for its game-like presentation and use of real-world data. The technology often involves 3D tiling, web-based rendering, and handling large datasets efficiently in the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://3dcity.ai/">3DCity.ai — Design AI-Ready Cities in Your Browser</a></li>
<li><a href="https://www.3dcitydb.org/3dcitydb-web-map/1.8.0/3dwebclient/index.html">3DCityDB-Web-Map-Client</a></li>
<li><a href="https://link.springer.com/article/10.1007/s12145-023-01167-5">An interoperable web-based application for 3d city modelling ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly positive, with users expressing awe and emotional connection to the virtual city. Some users discuss technical aspects, such as the data source and reverse-engineering methods, while others suggest improvements like adding street names, landmarks, and multiplayer features. A few users share related projects, like a Seattle map in N64 style.

**Tags**: `#3D mapping`, `#web development`, `#GIS`, `#interactive visualization`, `#San Francisco`

---

<a id="item-3"></a>
## [Oceans Hit Record High Temperatures, Highlighting Climate Crisis](https://www.bbc.com/news/articles/c62m4gpnp78o) ⭐️ 8.0/10

Oceans have reached their highest temperature on record, according to a recent report, underscoring the accelerating pace of climate change. This milestone was reported by BBC News and has sparked widespread discussion. This record is significant because ocean temperatures are a critical indicator of global warming, affecting weather patterns, sea levels, and marine ecosystems. It underscores the inadequacy of current mitigation efforts and the urgent need for stronger climate action. The report highlights that fossil fuels still supply 81.1% of global energy as of 2023, only marginally down from 81.4% in 2000, indicating a negligible decline. Additionally, melting ice reduces the energy required to warm the ocean, as noted by a commenter, amplifying the heating effect.

hackernews · tcp_handshaker · Aug 24, 19:19 · [Discussion](https://news.ycombinator.com/item?id=49424606)

**Background**: Ocean temperatures are a key measure of climate change because oceans absorb over 90% of the excess heat from greenhouse gas emissions. Record high temperatures can lead to more intense storms, coral bleaching, and sea level rise. The ongoing reliance on fossil fuels is a major driver of this warming trend.

**Discussion**: Community comments express concern about the slow decline of fossil fuels, with one user noting that they are not on track to end by 2050. Others criticize government inaction, particularly in the US, and share educational resources. A commenter reflects on the personal realization of the severity of a few degrees of warming.

**Tags**: `#climate change`, `#ocean temperature`, `#environment`, `#fossil fuels`, `#policy`

---

<a id="item-4"></a>
## [Your Executable Is a SQLite Database: A Clever Linux Hack](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 8.0/10

Farid Zakaria has demonstrated a technique to create a single file that is both a valid SQLite database and a directly executable Linux binary. By setting the SQLite application ID to 'SELF' and arranging ELF components into SQLite tables, the file can be executed via a custom interpreter registered with binfmt_misc. This hack opens up creative possibilities for software distribution and introspection, allowing executables to be queried and manipulated as databases. It showcases deep technical insight and could inspire novel approaches in packaging, debugging, or self-modifying programs, though its immediate practical impact may be limited. The technique relies on setting the 4-byte application ID at offset 68 in the SQLite file to 'SELF' (Structured Executable & Linkable Format). The ELF components are stored in multiple SQLite tables according to a schema, and a C interpreter (self-exec) extracts and executes them. binfmt_misc registration can be done via a simple command, as shown in the article.

rss · Simon Willison · Aug 24, 11:38

**Background**: ELF (Executable and Linkable Format) is the standard binary format for executables on Linux and many Unix-like systems. SQLite databases have a header that includes an application ID field, which is intended to identify the application that created the database. binfmt_misc is a Linux kernel feature that allows the kernel to recognize and execute non-native binary formats by invoking a specified interpreter.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>
<li><a href="https://sqlite.org/forum/info/6a768e7dca11a7b2">SQLite User Forum: Usage of application_id and magic.txt</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely praised the cleverness and originality of the hack, with some users discussing potential use cases and limitations. There may be debates about the practicality and security implications of such an approach.

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#executable`, `#hack`

---