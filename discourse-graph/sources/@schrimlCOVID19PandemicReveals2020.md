---
title: @schrimlCOVID19PandemicReveals2020
url: https://roamresearch.com/#/app/megacoglab/page/v0JQ-7zCa
author: Joel Chan
date: Tue Jun 23 2020 17:02:47 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: COVID-19 pandemic reveals the peril of ignoring metadata standards

    - Meta:

        - Tags: #ref/Paper

        - Authored by:: [[Lynn M. Schriml]] [[Maria Chuvochina]] [[Neil Davies]] [[Emiley A. Eloe-Fadrosh]] [[Robert D. Finn]] [[Philip Hugenholtz]] [[Christopher I. Hunter]] [[Bonnie L. Hurwitz]] [[Nikos C. Kyrpides]] [[Folker Meyer]] [[Ilene Karsch Mizrachi]] [[Susanna-Assunta Sansone]] [[Granger Sutton]] [[Scott Tighe]] [[Ramona Walls]]

        - Year: [[2020]]

        - Publication: Scientific Data

        - Zotero link: [Zotero Link](zotero://select/items/1_EDJNCZPG)

        - URL: [Schriml et al. (2020). COVID-19 pandemic reveals the peril of ignoring metadata standards. Scientific Data](https://www.nature.com/articles/s41597-020-0524-5)

    - Content

        - Abstract

            - Efficient response to the pandemic through the mobilization of the larger scientific community is challenged by the limited reusability of the available primary genomic data. Here, the Genomic Standards Consortium board highlights the essential need for contextual genomic data FAIRness, for empowering key data-driven biological questions.

        - #quotes

            - in the International Nucleotide Sequence Database Collaboration (INSDC, [www.insdc.org](http://www.insdc.org)) there are 2.1 million Sequence Read Archive (SRA) experiments listed under the taxonomy term “metagenomes”, less than 33% of which are tagged with environment metadata. Although published descriptions of metagenomic datasets are generally associated with enriched metadata describing the environment, source material, and sequencing technology, and in theory it is possible for one to read the manuscripts (including figures, tables and supplementary information) and gather that information, this is an onerous task when dealing with multiple studies. It also means multiple researchers potentially repeating the same work of trawling for metadata, resulting in significant researcher-hours that could be better spent actually interrogating the data.

            - host” is not annotated in 2,416 of the 5,198 SARS-CoV-2 BioSample submissions.

            - Even when researchers use the required metadata packages in INSDC, reporting of critical metadata is often hampered by confusion over the selection of metadata packages and inconsistent value specification for specific metadata terms, leading to the submission of incomplete, mislabeled, or missing metadata. As exemplified by 5,198 SARS-CoV-2 BioSample submissions (as of May 4, 2020), samples are being submitted using primarily the Pathogen: clinical or host-associated package, with a small set of submissions using the Microbe, Virus, or human-associated MIxS packages. The requirements for specific metadata attributes should ensure that sufficient contextual information is included. However, submitters may provide inappropriate information in these fields at the time of submission.

            - the more granular level taxon “viral metagenome” in the INSDC SRA has about 12k experiments (12,105 runs)(as of 5/7/2020). Of those (viewed in SRA Run Selector: [https://www.ncbi.nlm.nih.gov/Traces/study/](https://www.ncbi.nlm.nih.gov/Traces/study/)), 68% (8,225/12,105) have no reported geo\_loc\_name (country/continent) and 9% of runs have an ‘uncalculated’ geo\_loc\_name, as the submitting institution information has been filled in the country/continent field. Perhaps encouragingly, SARS-CoV-2 (txid2697049) in the SRA identifies 3,352 records with (SRA Run Selector) only 25% (887) of the 3,352 runs are reported with no country/continent metadata and only one submission with an ‘uncalculated’ geo\_loc\_name. Regrettably, we simply do not know the geographic origin of many sequenced samples, which is critical for subsequent analysis and data reuse.

            - the variation in submissions for ‘host disease’ complicate further analysis, as human disease has been submitted as (number of samples): COVID-19 (2,243); severe acute respiratory syndrome (119); Acute infection (34); novel coronavirus pneumonia (11); nCoV pneumonia (8); COVID19 (6); pneumonia (5); respiratory infection (2); Covid-2019 (2); Severe acute respiratory syndrome coronavirus 2 (1); pneumonia complicated by diarrhea (1). More than half of the submitted samples do not report any disease (2,766). Standard annotation of the metadata is supported by the usage of the structured controlled vocabularies and ontologies, such as the Environment Ontology[17](/articles/s41597-020-0524-5#ref-CR17 "Buttigieg, P. L. et al. The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation. J. Biomed. Semantics 7, 57 (2016).") and Disease Ontology[18](/articles/s41597-020-0524-5#ref-CR18 "Schriml, L. M. et al. Human Disease Ontology 2018 update: classification, content and workflow expansion. Nucleic Acids Res. 47, D955–D962 (2018)."), as specified in the MIxS standard. Each term in the MIxS standard is defined to clarify the scope of each data descriptor.

###### Discourse Context

- **Informs::** [[CLM - Sustaining authorship for semantic publishing is hard]]
