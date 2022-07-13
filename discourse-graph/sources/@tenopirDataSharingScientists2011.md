---
title: @tenopirDataSharingScientists2011
url: https://roamresearch.com/#/app/megacoglab/page/K2G_GewoV
author: Joel Chan
date: Wed Nov 18 2020 23:11:07 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Data Sharing by Scientists: Practices and Perceptions

    - Meta:

        - Authored by:: [[Carol Tenopir]] [[Suzie Allard]] [[Kimberly Douglass]] [[Arsev Umur Aydinoglu]] [[Lei Wu]] [[Eleanor Read]] [[Maribeth Manoff]] [[Mike Frame]]

        - Year: [[2011]]

        - Publication: PLOS ONE

        - Zotero link: [Zotero Link](zotero://select/items/1_X2NIXCYZ)

        - URL: [Tenopir et al. (2011). Data Sharing by Scientists: Practices and Perceptions. PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0021101)

    - Content

        - Abstract

            - Background Scientific research in the 21st century is more data intensive and collaborative than in the past. It is important to study the data practices of researchers – data accessibility, discovery, re-use, preservation and, particularly, data sharing. Data sharing is a valuable part of the scientific method allowing for verification of results and extending research from prior results. Methodology/Principal Findings A total of 1329 scientists participated in this survey exploring current data sharing practices and perceptions of the barriers and enablers of data sharing. Scientists do not make their data electronically available to others for various reasons, including insufficient time and lack of funding. Most respondents are satisfied with their current processes for the initial and short-term parts of the data or research lifecycle (collecting their research data; searching for, describing or cataloging, analyzing, and short-term storage of their data) but are not satisfied with long-term data preservation. Many organizations do not provide support to their researchers for data management both in the short- and long-term. If certain conditions are met (such as formal citation and sharing reprints) respondents agree they are willing to share their data. There are also significant differences and approaches in data management practices based on primary funding agency, subject discipline, age, work focus, and world region. Conclusions/Significance Barriers to effective data sharing and preservation are deeply rooted in the practices and culture of the research process as well as the researchers themselves. New mandates for data management plans from NSF and other federal agencies and world-wide attention to the need to share and preserve data could lead to changes. Large scale programs, such as the NSF-sponsored DataNET (including projects like DataONE) will both bring attention and resources to the issue and make it easier for scientists to apply sound data management principles.

###### Discourse Context



###### References

[[May 20th, 2020]]

- Reading again the [[CEDAR project]] (led by [[Mark Musen]], met at the [[AAAI TACOS symposium 2019]]): motivation and lessons are similar for [[open data]]: everyone knows science is better for it if data are shared with appropriate metadata, following [[FAIR principles]]. But uptake is low, except when there are extreme incentives. Some stuff I saw at [[iConference]] last year along this vein. See also [[@tenopirDataSharingScientists2011]]

    - The route we are thinking of is similar to what some are doing, like what we saw with the other Stanford folks, and the Netherlands person and [[sys/CodeOcean]]: basically make it so that the work you need to do to make something shareable and reproducible happens as a matter of course. [[[[PTN]] - Organize by using]]! Again, basically the route of [[[[PTN]] - Integrated crowdsourcing]]. To take advantage of this route, we need more than surveys or interviews: we need a deep dive detailed look into actual workflows as they play out, to identify points of friction but also integration. This is the argument for how we might tackle the [[Authorship Bottleneck]].

    - Now again, there is the alternate route of doing it via AI, completely autonomously. I'm not optimistic. We're struggling even for basic [[OpenIE]]. [[sys/Snorkel]] has some nice results in constrained domains for constrained tasks. But.. see also [[Jodi Schneider]]'s stuff on [[Argumentation Mining]] [[@stedeArgumentationMining2018]]

        - [[SOTA]] for extracting claims is quite low (~60ish percent) (p. 76)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_cUM0ccYHH.png?alt=media&token=d818d715-cc1c-4eab-b240-e9dea8eaaf13)

        - Highest performance is for very idiosyncratic domains - models that perform well on these domains do poorly when generalizing to other domains (p. 76)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FilN0nw-mzv.png?alt=media&token=8a5ac151-ed75-4d21-9f43-76ce34ee1416)

    - In general, mandates are not strong enough medicine.

    - The other route that's often considered is individual incentives (rewarding scientists for doing it, counting in publications). This is true to a point. But it's a heavy lift: requires widespread cultural change, and might be chicken and egg.
