---
title: @beelResearchPaperRecommender2013
url: https://roamresearch.com/#/app/megacoglab/page/7iiLOYRZ9
author: Joel Chan
date: Wed Jan 13 2021 12:31:18 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Research paper recommender system evaluation: a quantitative literature survey

    - Meta:

        - Authored by:: [[Joeran Beel]] [[Stefan Langer]] [[Marcel Genzmehr]] [[Bela Gipp]] [[Corinna Breitinger]] [[Andreas Nürnberger]]

        - Year: [[2013]]

        - Publication: Proceedings of the International Workshop on Reproducibility and Replication in Recommender Systems Evaluation

        - Zotero link: [Zotero Link](zotero://select/items/1_N2IFHIP7)

        - URL: [Beel et al. (2013). Research paper recommender system evaluation: a quantitative literature survey. Proceedings of the International Workshop on Reproducibility and Replication in Recommender Systems Evaluation](https://doi.org/10.1145/2532508.2532512)

    - Content

        - Abstract

            - Over 80 approaches for academic literature recommendation exist today. The approaches were introduced and evaluated in more than 170 research articles, as well as patents, presentations and blogs. We reviewed these approaches and found most evaluations to contain major shortcomings. Of the approaches proposed, 21% were not evaluated. Among the evaluated approaches, 19% were not evaluated against a baseline. Of the user studies performed, 60% had 15 or fewer participants or did not report on the number of participants. Information on runtime and coverage was rarely provided. Due to these and several other shortcomings described in this paper, we conclude that it is currently not possible to determine which recommendation approaches for academic literature are the most promising. However, there is little value in the existence of more than 80 approaches if the best performing approaches are unknown.

    - #lit-context

        - [[workshop paper]], [[superseded-by]] [[@beelResearchpaperRecommenderSystems2016]]

        - setting: 176 papers on 89 recommendation approaches as of ~2012-2013, retrieved from ACM DL, Springer Link, and Google Scholar, using the search term `[paper | article | citation] [recommender | recommendation] [system | systems]`

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F--nQgsG2Gf.png?alt=media&token=0f266c6d-ad37-4f3d-9f2a-bcc2f8995b78) (p. 17)

            - as far as [[systematic review]] goes, not necessarily exhaustive - screening was done manually too, first by title, so there's risk of false negatives if it's not in the title. Not sure if Google Scholar did query expansion or soft matching at the time, maybe that might help.

                - known false negatives:

                    - [[@chauApoloMakingSense2011]] (doesn't have keywords in the title, but i suppose it's not formally a recommendation system: more of a [[🧱 sensemaking]])

                        - ditto [[@dunneRapidUnderstandingScientific2012]], which is notable bc it includes a 17-month study of 3 users, in addition to other user studies

        - measure: type of evaluation was collated across all papers that address the same approach: e.g., if approach A was evaluated with offline in paper 1, online in paper 2, then approach A is marked as yes to offline and online

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F--nQgsG2Gf.png?alt=media&token=0f266c6d-ad37-4f3d-9f2a-bcc2f8995b78) (p. 17)

            - would have loved to see some stats on judgment reliability: offline vs. online vs. user study seems obvious, but there might be edge cases. don't think this is a huge deal

    - #[[📝 lit-notes]]

        - #[[observation-notes]]

            - ~20% of [sample of 89 recommendation approaches](setting: 176 papers on 89 recommendation approaches as of ~2012-2013, retrieved from ACM DL, Springer Link, and Google Scholar, using the search term `[paper | article | citation] [recommender | recommendation] [system | systems]`) as of [[2013]] did not use a known offline/online/user-study [evaluation approach](((fWZDjZut-)))

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F1HyFLrkmBE.png?alt=media&token=daba5707-b54c-43fe-a78c-2eaded72916d) (p. 17)

            - the majority of a [sample of 70 recommendation approaches](setting: 176 papers on 89 recommendation approaches as of ~2012-2013, retrieved from ACM DL, Springer Link, and Google Scholar, using the search term `[paper | article | citation] [recommender | recommendation] [system | systems]`) as of [[2013]] were [evaluated](((fWZDjZut-))) with offline approaches (~70%) and user studies (~30%): a small minority had been evaluated in realistic deployments in online evaluations (N=5,  ~7% of the sample) and qualitative user studies (N=2)

                ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FVaMtJyxcOj.png?alt=media&token=0e0a9e5a-bfd2-40f7-a2c4-877ed9759071) (p. 17)

                ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FxHjkSHjCrP.png?alt=media&token=e626fd19-d490-49ca-bc11-16cbcb3730f5) (p. 17)

###### Discourse Context



###### References

[[January 13th, 2021]]

- [[@beelResearchPaperRecommender2013]] reported that the majority of a [sample of 70 recommendation approaches](((-9iTZhMJF))) as of [[2013]] were [evaluated](((fWZDjZut-))) with offline approaches (~70%) and user studies (~30%): a small minority had been evaluated in realistic deployments in online evaluations (N=5,  ~7% of the sample) and qualitative user studies (N=2)

    - Note: cite [[@beelResearchpaperRecommenderSystems2016]] instead, since it's the more battle-tested full paper version of [[@beelResearchPaperRecommender2013]]
[[January 13th, 2021]]

- [[@beelResearchPaperRecommender2013]] notes 7 research paper recommendation approaches that might be worth looking at, since they ran online evaluations or qual studies #[[➰ breadcrumbs]]

    - online

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FfK3fRUC5cH.png?alt=media&token=a7c37093-c4ba-4f62-9933-862deb8924f6)

            - [[@beelIntroducingDocearResearch2013]]

                - #[[references]]

                    - Title: Introducing Docear's research paper recommender system

                    - Meta:

                        - Authored by:: [[Joeran Beel]] [[Stefan Langer]] [[Marcel Genzmehr]] [[Andreas Nürnberger]]

                        - Year: [[2013]]

                        - Publication: Proceedings of the 13th ACM/IEEE-CS joint conference on Digital libraries

                        - Zotero link: [Zotero Link](zotero://select/items/1_J5JKLP4Y)

                        - URL: [Beel et al. (2013). Introducing Docear's research paper recommender system. Proceedings of the 13th ACM/IEEE-CS joint conference on Digital libraries](https://doi.org/10.1145/2467696.2467786)

                    - Content

                        - Abstract

                            - In this demo paper we present Docear's research paper recommender system. Docear is an academic literature suite to search, organize, and create research articles. The users' data (papers, references, annotations, etc.) is managed in mind maps and these mind maps are utilized for the recommendations. Using content-based filtering methods, Docear's recommender achieves click-through rates around 6%, in some scenarios even over 10%.

            - [[@bogersRecommendingScientificArticles2008]]

                - #[[references]]

                    - Title: Recommending scientific articles using citeulike

                    - Meta:

                        - Authored by:: [[Toine Bogers]] [[Antal van den Bosch]]

                        - Year: [[2008]]

                        - Publication: Proceedings of the 2008 ACM conference on Recommender systems

                        - Zotero link: [Zotero Link](zotero://select/items/1_KKR629GK)

                        - URL: [Bogers & van den Bosch (2008). Recommending scientific articles using citeulike. Proceedings of the 2008 ACM conference on Recommender systems](https://doi.org/10.1145/1454008.1454053)

                    - Content

                        - Abstract

                            - We describe the use of the social reference management website CiteULike for recommending scientific articles to users, based on their reference library. We test three different collaborative filtering algorithms, and find that user-based filtering performs best. A temporal analysis of the data indexed by CiteULike shows that it takes about two years for the cold-start problem to disappear and recommendation performance to improve.

            - [[@monnichAddingValueLibrary2008]]

                - #[[references]]

                    - Title: Adding Value to the Library Catalog by Implementing a Recommendation System

                    - Meta:

                        - Authored by:: [[Michael Mönnich]] [[Marcus Spiering]]

                        - Year: [[2008]]

                        - Publication: D-Lib Magazine

                        - Zotero link: [Zotero Link](zotero://select/items/1_8A4GRI2A)

                        - URL: [Mönnich & Spiering (2008). Adding Value to the Library Catalog by Implementing a Recommendation System. D-Lib Magazine](http://www.dlib.org/dlib/may08/monnich/05monnich.html)

                    - Content

                        - Abstract

                            - undefined

            - [[@middletonOntologicalUserProfiling2004]] is real-world deployment, but as far as i can tell, there is no efficacy data????

                - #[[references]]

                    - Title: Ontological user profiling in recommender systems

                    - Meta:

                        - Authored by:: [[Stuart E. Middleton]] [[Nigel R. Shadbolt]] [[David C. De Roure]]

                        - Year: [[2004]]

                        - Publication: ACM Transactions on Information Systems

                        - Zotero link: [Zotero Link](zotero://select/items/1_SGW9NH7T)

                        - URL: [Middleton et al. (2004). Ontological user profiling in recommender systems. ACM Transactions on Information Systems](https://doi.org/10.1145/963770.963773)

                    - Content

                        - Abstract

                            - We explore a novel ontological approach to user profiling within recommender systems, working on the problem of recommending on-line academic research papers. Our two experimental systems, Quickstep and Foxtrot, create user profiles from unobtrusively monitored behaviour and relevance feedback, representing the profiles in terms of a research paper topic ontology. A novel profile visualization approach is taken to acquire profile feedback. Research papers are classified using ontological classes and collaborative recommendation algorithms used to recommend papers seen by similar people on their current topics of interest. Two small-scale experiments, with 24 subjects over 3 months, and a large-scale experiment, with 260 subjects over an academic year, are conducted to evaluate different aspects of our approach. Ontological inference is shown to improve user profiling, external ontological knowledge used to successfully bootstrap a recommender system and profile visualization employed to improve profiling accuracy. The overall performance of our ontological recommender systems are also presented and favourably compared to other systems in the literature.

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCLQ8zbwVjk.png?alt=media&token=8eda4790-a06a-425c-8d4b-7db8293c69a4)

            - [[@sompelArchitectureAggregationAnalysis2006]]

                - #[[references]]

                    - Title: An architecture for the aggregation and analysis of scholarly usage data

                    - Meta:

                        - Authored by:: [[H. Van de Sompel]] [[J. Bollen]]

                        - Year: [[2006]]

                        - Publication: Proceedings of the 6th ACM/IEEE-CS Joint Conference on Digital Libraries (JCDL '06)

                        - Zotero link: [Zotero Link](zotero://select/items/1_ACJLWK8P)

                        - URL: [Sompel & Bollen (2006). An architecture for the aggregation and analysis of scholarly usage data. Proceedings of the 6th ACM/IEEE-CS Joint Conference on Digital Libraries (JCDL '06)](undefined)

                    - Content

                        - Abstract

                            - Although recording of usage data is common in scholarly information services, its exploitation for the creation of value-added services remains limited due to concerns regarding, among others, user privacy, data validity, and the lack of accepted standards for the representation, sharing and aggregation of usage data. This paper presents a technical, standards-based architecture for sharing usage information, which we have designed and implemented. In this architecture, OpenURL-compliant linking servers aggregate usage information of a specific user community as it navigates the distributed information environment that it has access to. This usage information is made OAI-PMH harvestable so that usage information exposed by many linking servers can be aggregated to facilitate the creation of value-added services with a reach beyond that of a single community or a single information service. This paper also discusses issues that were encountered when implementing the proposed approach, and it presents preliminary results obtained from analyzing a usage data set containing about 3,500,000 requests aggregated by a federation of linking servers at the California State University system over a 20 month period

    - qual

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FCXovMq7eOL.png?alt=media&token=dbb853ae-f883-4f92-b370-647fa80a9dc4)

            - [[@stockFindingScienceScience2013]]

                - #[[references]]

                    - Title: Finding Science with Science: Evaluating a Domain and Scientific Ontology User Interface for the Discovery of Scientific Resources

                    - Meta:

                        - Authored by:: [[Kristin Stock]] [[Vera Karasova]] [[Anne Robertson]] [[Guillaume Roger]] [[Mark Small]] [[Mohamed Bishr]] [[Jens Ortmann]] [[Tim Stojanovic]] [[Femke Reitsma]] [[Lukasz Korczynski]] [[Boyan Brodaric]] [[Zoe Gardner]]

                        - Year: [[2013]]

                        - Publication: Transactions in GIS

                        - Zotero link: [Zotero Link](zotero://select/items/1_6TF6DAWJ)

                        - URL: [Stock et al. (2013). Finding Science with Science: Evaluating a Domain and Scientific Ontology User Interface for the Discovery of Scientific Resources. Transactions in GIS](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9671.2012.01370.x)

                    - Content

                        - Abstract

                            - Current approaches to the discovery of scientific resources (publications, data sets and web services) are dominated by keyword search. These approaches do not allow scientists to search on the deeper semantics of scientific resources, or to discover resources on the basis of the scientific approaches taken. This article evaluates a user interface that allows users to discover scientific resources through structured knowledge in the form of ontologies describing the domain and the scientific knowledge inherent within the scientific resource, and also through informal user tags. These combined capabilities provide scientists with new and powerful options for resource discovery. A qualitative user evaluation explored how scientists felt about the approach for resource discovery in the context of their scientific work. The study showed that marine scientists were enthusiastic about the capabilities of such an approach and appreciated the ability to browse the visual structure of the knowledge and query on scientific method but, overall, preferred the use of tags over ontologies. The exploratory nature of the user study was used to identify future directions for such improvements.

            - [[@stockEScienceSeaScience2009]]

                - #[[references]]

                    - Title: eScience for Sea Science: A Semantic Scientific Knowledge Infrastructure for Marine Scientists

                    - Meta:

                        - Authored by:: [[K. Stock]] [[A. Robertson]] [[F. Reitsma]] [[T. Stojanovic]] [[M. Bishr]] [[D. Medyckyj-Scott]] [[J. Ortmann]]

                        - Year: [[2009]]

                        - Publication: 2009 Fifth IEEE International Conference on e-Science

                        - Zotero link: [Zotero Link](zotero://select/items/1_8Y98945I)

                        - URL: [Stock et al. (2009). eScience for Sea Science: A Semantic Scientific Knowledge Infrastructure for Marine Scientists. 2009 Fifth IEEE International Conference on e-Science](undefined)

                    - Content

                        - Abstract

                            - The COastal and Marine Perception Application for Scientific Scholarship (COMPASS) is a knowledge infrastructure that supports enhanced discovery of scientific resources, including publications, data sets and web services. It provides users with the ability to discover resources on the basis of domain knowledge using ontologies, and scientific knowledge, including the scientific models, theories and methods that were used to conduct the research described by the resource. The application includes an architecture that adopts standards from the geospatial information community to ensure interoperability between repositories and allow interaction with content from digital libraries. The architecture shows how ontologies can be used as a registry for an interoperable infrastructure. A prototype was successfully implemented and evaluated with users, finding enthusiasm and support for the approach, with some suggestions for improvements of the prototype implementation.

                - both of these studies are "reaction-based" evals, not necessarily in real usage, but we can see if there's deeper analysis of the reactions and how this might fit

    - edit: quick skim after adding, feeling a little *more* depressed actually - i haven't seen any really strong studies that stood out that could give real deep insight into real-world efficacy... :(
