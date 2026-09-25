---
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 24 items, 3 important content pieces were selected

---

1. [F-Droid 2.0 Launches Major Redesign, Phases Out Privileged Extension](#item-1) ⭐️ 8.0/10
2. [Google's Project Suncatcher to put ML infrastructure in space](#item-2) ⭐️ 8.0/10
3. [UK Two-Tier Encryption and Apple's ADP Withdrawal](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [F-Droid 2.0 Launches Major Redesign, Phases Out Privileged Extension](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

F-Droid released version 2.0 on September 24, 2026, introducing a major UI/UX redesign of its open-source Android app repository and beginning to phase out the F-Droid Privileged Extension (FPE). The release marks what the project calls a new chapter for Android freedom, drawing over 1,000 upvotes and 281 comments on Hacker News. F-Droid is one of the most widely used alternatives to Google Play for free and open-source Android apps, so a major redesign affects a large community of privacy-conscious and FOSS-focused users. The timing is significant because Google is expected to tighten Android sideloading and app distribution policies, raising questions about F-Droid's long-term viability. The redesign has drawn criticism for lacking visual separation between UI sections and unclear tappable affordances, with one commenter noting a text-wrapping glitch in the first screenshot. The phase-out of the Privileged Extension, which previously enabled seamless background app installs on rooted or custom ROM devices, is welcomed by users who found it difficult to configure.

hackernews · daveoc64 · Sep 24, 15:26 · [Discussion](https://news.ycombinator.com/item?id=49831968)

**Background**: F-Droid is a catalog and client for libre Android apps, distributing free and open-source software outside of Google Play. The F-Droid Privileged Extension was a system component that allowed the F-Droid client to install and update apps automatically without user confirmation on devices where it was installed as a privileged system app. Google's Android policies have increasingly restricted sideloading and alternative app distribution, which threatens repositories like F-Droid.

<details><summary>References</summary>
<ul>
<li><a href="https://f-droid.org/">F - Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://f-droid.org/packages/">F - Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://developer.android.com/distribute/play-policies">Google Play Policies | Android Developers</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed the overhaul and the removal of the Privileged Extension, with some saying they had switched to alternatives like Droid-ify on GrapheneOS due to F-Droid's poor UI. Others criticized the new design ethos for lacking visual hierarchy and clear affordances, while several raised concerns about F-Droid's future once Google tightens Android lockdown next year.

**Tags**: `#F-Droid`, `#Android`, `#Open Source`, `#App Store`, `#UI/UX`

---

<a id="item-2"></a>
## [Google's Project Suncatcher to put ML infrastructure in space](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) ⭐️ 8.0/10

Google has announced Project Suncatcher, a research moonshot that aims to equip solar-powered satellite constellations with TPUs and free-space optical links to build scalable AI compute infrastructure in orbit. The company published a feasibility study on space-based data centers in November 2025, and the initiative has sparked widespread debate about its physics, economics, and implications. If feasible, space-based AI data centers could offer cleaner, faster, and more scalable computing beyond Earth, potentially reshaping how the AI industry addresses its skyrocketing energy demands. The initiative also raises questions about launch economics, heat dissipation, and possible military applications, drawing attention from both the tech community and policymakers. Google's concept involves compact constellations of solar-powered satellites carrying TPUs and using free-space optical links for communication, with launch costs potentially falling below $200/kg by the mid-2030s according to the feasibility study. Key technical challenges include heat dissipation in the vacuum of space and the economic viability of maintaining and upgrading hardware in orbit.

hackernews · xnx · Sep 24, 13:53 · [Discussion](https://news.ycombinator.com/item?id=49830606)

**Background**: Space-based data centers, also called orbital AI infrastructure, are proposed systems that place data processing and storage for AI and other computing needs into satellites. Google's Project Suncatcher is a research moonshot exploring this frontier, similar to efforts by startups like Starcloud, as AI energy demands continue to grow on Earth.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">Exploring a space-based, scalable AI infrastructure system design</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center - Wikipedia</a></li>
<li><a href="https://www.gao.gov/products/gao-26-109012">Science & Tech Spotlight: Data Centers in Space | U.S. GAO</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the physics and economics of space-based data centers, with one noting the advantage of being out of range of public unrest, while another pointed to startup Starcloud's existing proof of concept and whitepaper. Others raised concerns about heat dissipation, speculated about military SIGINT applications, and highlighted Alphabet's significant stake in SpaceX.

**Tags**: `#Google`, `#ML infrastructure`, `#space computing`, `#data centers`, `#Project Suncatcher`

---

<a id="item-3"></a>
## [UK Two-Tier Encryption and Apple's ADP Withdrawal](https://macanorak.com/two-tier-encryption-in-the-uk/) ⭐️ 8.0/10

The article analyzes the UK's emerging two-tier encryption regime and Apple's decision to disable Advanced Data Protection (ADP) for UK iCloud users rather than comply with a legal order to weaken its security architecture. Affected UK iCloud data reverts from end-to-end encryption to Standard Data Protection, where Apple holds the keys and can respond to lawful requests. This sets a precedent for how governments can pressure technology companies to weaken encryption without formally banning it, potentially encouraging other countries to adopt similar regimes. It directly affects UK users' privacy and raises broader questions about corporate accountability and whether companies will resist or quietly comply with surveillance demands. Withdrawing ADP in the UK did not affect the 14 iCloud categories already end-to-end encrypted by default, such as iCloud Keychain and Health; ADP would have expanded that to 23 categories, so iCloud Backup, Photos, Notes, and iCloud Drive revert to Standard Data Protection. Community members note that even the baseline categories can have their end-to-end encryption secrets exposed under common usage patterns, and that the public disclosure of such legal orders is itself illegal under the Investigatory Powers Act 2016.

hackernews · ReturnoftheHack · Sep 24, 10:39 · [Discussion](https://news.ycombinator.com/item?id=49828731)

**Background**: Advanced Data Protection (ADP) is an optional Apple setting that extends end-to-end encryption to most iCloud data, meaning only the user's devices hold the keys. The UK's Investigatory Powers Act 2016 allows the government to issue secret technical capability notices compelling companies to help law enforcement access encrypted data. A two-tier encryption regime would mean different levels of protection or access for authorities versus ordinary users, effectively creating a lawful backdoor.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-us/108756">How to turn on Advanced Data Protection for iCloud - Apple Support</a></li>
<li><a href="https://en.wikipedia.org/wiki/Investigatory_Powers_Act_2016">Investigatory Powers Act 2016 - Wikipedia</a></li>
<li><a href="https://supremespy.com/spy-tech-tools-2/two-tier-encryption-in-the-uk/">Two - tier Encryption In The UK - Supreme Spy</a></li>

</ul>
</details>

**Discussion**: Commenters are sharply divided but largely critical: some argue Apple has lost the courage it showed in 2015 against the FBI and now quietly complies, pointing to mandatory age-confirmation and KYC screens as evidence of eroding principles. Others defend Apple's third-option strategy of withdrawing ADP as a way to satisfy the legal requirement without building a backdoor, while several call for Apple to exit the UK market or refuse to sell to the UK government. A recurring concern is that once such surveillance powers are accepted, they will never be rolled back.

**Tags**: `#encryption`, `#privacy`, `#UK policy`, `#Apple`, `#security`

---