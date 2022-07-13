---
title: @brushSEPIOSemanticModel2016
url: https://roamresearch.com/#/app/megacoglab/page/ahPALW3zI
author: Joel Chan
date: Sat Jun 27 2020 10:43:35 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: SEPIO: A Semantic Model for the Integration and Analysis of Scientific Evidence

    - Meta:

        - Authored by:: [[Matthew H Brush]] [[Kent Shefchek]] [[Melissa Haendel]]

        - Year: [[2016]]

        - Publication: CEUR Workshop Proceedings

        - Zotero link: [Zotero Link](zotero://select/items/1_88XYTD3K)

        - URL: [Brush et al. (2016). SEPIO: A Semantic Model for the Integration and Analysis of Scientific Evidence. CEUR Workshop Proceedings](undefined)

    - Content

        - Abstract

            - The Scientific Evidence and Provenance Information Ontology (SEPIO) was developed to support the description of evidence and provenance information for scientific claims. The core model represents the relationships between claims, their lines of evidence, and the data items that comprise this evidence, as well as the methods, tools, and agents involved in the creation of these artifacts. SEPIO was initially developed to support the data integration and analysis efforts of the Monarch Initiative, where it provides a unified and computable representation of evidence and provenance metadata for genotype-phenotype associations aggregated across diverse model organism and clinical genetics databases. However, additional requirements were collected from diverse community partners in an effort to provide a shared community standard, with a core model that is domain independent and extensible to represent any type of claim and its associated evidence. In this report we describe the structure and principles behind the SEPIO model, and review its applications in support of data integration, curation, knowledge discovery, and manual and computational evaluation of scientific claims. The SEPIO ontology can be found at http://github.com/monarchinitiative/SEPIO-ontology/blob/master/src/ontology/sepio.owl.
- #references

    - Title: SEPIO: A Semantic Model for the Integration and Analysis of Scientific Evidence

    - Meta:

        - Tags: #ref/Paper #provenance

        - Authored by::  Matthew H Brush ,  Kent Shefchek ,  Melissa Haendel

        - Year: [[2016]]

        - Publication: CEUR Workshop Proceedings

        - URL:

        - Citekey: brushSEPIOSemanticModel2016

        - Zotero link:: [Zotero Link](zotero://select/items/1_88XYTD3K)

    - Content

        - Placeholder

        - Abstract

            - The Scientific Evidence and Provenance Information Ontology (SEPIO) was developed to support the description of evidence and provenance information for scientific claims. The core model represents the relationships between claims, their lines of evidence, and the data items that comprise this evidence, as well as the methods, tools, and agents involved in the creation of these artifacts. SEPIO was initially developed to support the data integration and analysis efforts of the Monarch Initiative, where it provides a unified and computable representation of evidence and provenance metadata for genotype-phenotype associations aggregated across diverse model organism and clinical genetics databases. However, additional requirements were collected from diverse community partners in an effort to provide a shared community standard, with a core model that is domain independent and extensible to represent any type of claim and its associated evidence. In this report we describe the structure and principles behind the [[std/SEPIO]] model, and review its applications in support of data integration, curation, knowledge discovery, and manual and computational evaluation of scientific claims. The SEPIO ontology can be found at http://github.com/monarchinitiative/SEPIO-ontology/blob/master/src/ontology/sepio.owl.

    - #[[📝 lit-notes]]

        - introduces the [[std/SEPIO]] conceptual model

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FqX6J3L1DL6.png?alt=media&token=63416388-3cc0-4941-aec7-85bec30c7ac9)

            - example with content:

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F_867Jyfnb7.png?alt=media&token=320443d1-bd51-47af-b503-3f0165c1a757)

###### Discourse Context

- **Informs::** [[CLM - Scholarly argumentation operates on atomic statements and concepts as fundamental units]]
- **Informs::** [[QUE - Do scholarly synthesis infrastructures already exist]]
- **Informs::** [[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]
- **Informs::** [[PTN - discourse graph]]

###### References

[[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]

- ON the flip side, a more qualitative approach (e.g., [[evidence lines]]), as exemplified by [[@clarkMicropublicationsSemanticModel2014]] and [[@brushSEPIOSemanticModel2016]], is less readily quantifiable in a sophisticated sense, but possibly more useful for the early stages of [[synthesis]], particularly where there is [[interdisciplinarity]]

    - One challenge maybe is that not all subdomains have a nice ontology of evidence types, although it's
[[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]

- [[@brushSEPIOSemanticModel2016]]'s [[std/SEPIO]] feels similar to [[@clarkMicropublicationsSemanticModel2014]], in that it doesn't really care about assigning numbers, and is more about making sure that there is direct documentation of "lines of evidence" - what *kind* of support is there for each claim?

    - They support connecting to the [[std/Evidence and Conclusion (ECO)]] ontology, which describes types of scientific evidence (but NOT strength!) in bio
