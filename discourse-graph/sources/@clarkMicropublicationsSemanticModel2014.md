---
title: @clarkMicropublicationsSemanticModel2014
url: https://roamresearch.com/#/app/megacoglab/page/az66HiREz
author: Joel Chan
date: Wed Jan 22 2020 11:06:57 GMT-0500 (Eastern Standard Time)
---

- #[[references]]

    - Title: Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications

    - Meta:

        - Tags: #context #Atomicity #Atomicity #compositionality #[[D/Synthesis Infrastructure]] #std/Micropublication

        - Authored by:: [[Tim Clark]] [[Paolo Ciccarese]] [[Carole A. Goble]]

        - Year: [[2014]]

        - Publication: Journal of Biomedical Semantics

        - Zotero link: [Zotero Link](zotero://select/items/1_CU3KDQGR)

        - URL: [Clark et al. (2014). Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications. Journal of Biomedical Semantics](https://doi.org/10.1186/2041-1480-5-28)

    - Content

        - Abstract

            - Scientific publications are documentary representations of defeasible arguments, supported by data and repeatable methods. They are the essential mediating artifacts in the ecosystem of scientific communications. The institutional “goal” of science is publishing results. The linear document publication format, dating from 1665, has survived transition to the Web.

    - #[[📝 lit-notes]]

        - Minimal form of a [[std/Micropublication]] (p. 10)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F4RD5nUsFD2?alt=media&token=f31624d5-1637-4859-adb5-b205701ac24e)

        - Better form of [[std/Micropublication]]

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FXEIzMIbGby.png?alt=media&token=52de2ef7-02d6-4154-bc9e-4c322bdd5071)

        - Example [[std/Micropublication]] with a real scientific claim (p.15)

            - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FhIBZKnpISn?alt=media&token=056ff6ca-ed18-4166-8b61-fec4e142dc99)

        - Introduced an interface for authoring of micropublications, integrating into [[sys/DOMEO]] - however, I'm not sure where it is now :( - last commit to [their github](https://github.com/domeo/domeo) was like 5 years ago, and I can't find any digital footprints anywhere else...

###### Discourse Context

- **Informs::** [[CLM - Scholarly argumentation operates on atomic statements and concepts as fundamental units]]
- **Informs::** [[QUE - Do scholarly synthesis infrastructures already exist]]
- **Informs::** [[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]
- **Informs::** [[QUE - What (existing) systems facilitate individual synthesis]]
- **Informs::** [[PTN - discourse graph]]

###### References

[[January 26th, 2021]]

- Significant work across formal conceptual models of scholarly argumentation [[@deWaardProteinsFairytalesDirections2010]], [[@clarkMicropublicationsSemanticModel2014]], sensemaking [[@russellCostStructureSensemaking1993]], and knowledge management [[@ackermanSharingKnowledgeExpertise2013]] suggest that an optimal information model for supporting synthesis is the epistemic model: shareable collections of knowledge __claims__ (e.g., __children are less susceptible to COVID-19 infection, given equivalent exposure__) and their associated __context__ (e.g., \textit{was sampling symptom-based? Where was the study conducted? At what point in the locality's epidemic time course?}), \textit{connected} in a discourse graph (e.g., supporting other hypotheses/claims, corroborated/disputed by other claims).

    - Key hypothesized affordances of [[[[PTN]] - discourse graph]] include the ability to compress complex ideas into granular statements, which affords quicker comparison, comprehension, and composition of ideas, while also retaining links to contextual details to allow for "unpacking" and critical interrogation of ideas as they are interpreted and recombined into more complex arguments/models.

    - These affordances are hypothesized to enable key process-level interactions with scholarly knowledge that are crucial for synthesis, such as a principled dialectic between context-rich observations (data) and creative and formal construction of models and hypotheses (theory).

    - These affordances may also enable more effective reuse and remixing of ideas across boundaries of time, projects, and even collaborators.
[[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]

- ON the flip side, a more qualitative approach (e.g., [[evidence lines]]), as exemplified by [[@clarkMicropublicationsSemanticModel2014]] and [[@brushSEPIOSemanticModel2016]], is less readily quantifiable in a sophisticated sense, but possibly more useful for the early stages of [[synthesis]], particularly where there is [[interdisciplinarity]]

    - One challenge maybe is that not all subdomains have a nice ontology of evidence types, although it's
[[January 27th, 2021]]

- Significant work across formal conceptual models of scholarly argumentation [[@deWaardProteinsFairytalesDirections2010]], [[@clarkMicropublicationsSemanticModel2014]], sensemaking [[@russellCostStructureSensemaking1993]], and knowledge management [[@ackermanSharingKnowledgeExpertise2013]] suggest that an optimal information model for supporting synthesis is a collection of knowledge **claims** and their associated __context__, __connected__ in a discourse graph.

    - The answers to these questions cannot be found simply in the titles of research papers, in groupings of papers by area, or even in citation or authorship networks (effective though they might be at revealing macro structures in scientific communities). These information structures are not at the desired level of granularity, which is at the level of theoretical concepts/claims and empirical **claims** and evidence: for example, "__game theory predicts that discourse can devolve to an escalating tit-for-tat spiral under X conditions__", or "__banning bad actors from a subreddit in 2012 was somewhat effective at mitigating spread of misinformation on the subreddit__". This level of granularity is crucial not just for finding relevant claims to inform the synthesis, but also for constructing more complex arguments and theories (by connecting statements in logical and discursive relationships).

    - To understand why this information model is hypothesized to augment synthesis, let us return to our motivating example of the researcher who wants to design new interventions to mitigate online harassment. To synthesize a formulation of this problem that can advance the state of the art, she needs material that can help her work through detailed answers to a range of granular questions. For example, what theories of online behavior and antisocial behavior might be most relevant for understanding what is going on here? Which theories have the most empirical support in this particular setting? Are there conflicting theoretical predictions that might signal fruitful areas of inquiry? What are the key phenomena to keep in mind when designing an intervention (e.g., perceptions of human vs. automated action, procedural considerations, noise in judgments of wrongdoing, scale considerations for spread of harm)? What intervention patterns have been proposed that are both a) judged on theoretical and circumstantial grounds as likely to be effective in this setting, and b) lacking in direct evidence for efficacy?

    - Beyond operating at the claim level, however, our researcher will need to work through a range of **contextual details**. For example, to judge which studies and findings/theories are "actually applicable" (e.g.,, studying similar populations, interventions, settings, or outcome measures?) to her setting, she might need to reason over the fact that two studies that concluded limited efficacy of bans had ban interventions that were quite short, on a forum with no identity verification. Or she might reason through the fact that a prominent theory of bad faith and discourse was proposed by a philosopher from the early 2000's (before the rise of modern social media). To judge the validity of past findings (e.g., what has been established with sufficient certainty, where the frontier might be), she would need to know, for example, which findings came from which measures (e.g., self-report, behavioral measures), and the extent to which findings have been replicated cross authors from different labs, and across a variety of settings.

    - Also, contextual details, such as methodology or metadata, are explicitly included in the discourse graph. This should support direct analysis of claims with their evidentiary context. Figure X shows how this might be supported in the specific worked example above.

    - Beyond these direct hypothesized benefits to synthesis, such models could also be used and repurposed over time, across projects, and potentially even across people. For example, imagine collaborators sharing these collections of epistemic models with each other, to speed up the process of working towards shared mental models and identify productive areas of divergence; or PIs and senior students onboarding newer students not with long reading lists, but subsets of epistemic models that they can build on and add to over time. How much time and overhead could be saved if this were a reality?

    - An epistemic model has key affordances that are hypothesized to enable just these sorts of operations. Information is represented primarily at the claim/statement level, and are embedded in a discourse graph. Thus, claims should be able to have many-to-many relationships to support composition of more complex arguments and theories, or "decompression" into component supporting/opposing claims.
[[February 6th, 2021]]

- [[std/Micropublication]]s from [[@clarkMicropublicationsSemanticModel2014]] comes immediately to mind as the clearest example

    - articulates the addition of richer [[context]] (through direct representation of empirical evidence), and [[composability]] (through the representation of claim networks) as a key advance over [[std/SWAN]], [[std/Nanopublications]], and [[std/BEL]] (the latter two in addition are limited by their requirements that statements be in formal language, although [[@kuhnBroadeningScopeNanopublications2013]] did modify the standard to support natural-language statements)

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F5vRbtoadZU.png?alt=media&token=75c0d383-7499-4afd-aa57-6e2bea5f4aec) (p. 3)

    - note their strong grounding in argument theory, building on [[@toulminUsesArgument2003]], but going beyond it to think more deeply about [[context]], which, like what we [have been saying]([[[[QUE]] - What is context for the purposes of scholarly synthesis?]]), can be roughly divided into "data" (the thing we nest under the `observation note`: a figure/table/quote, etc.), the `context snippets` (typically methodological details that help us understand how the data was produced), and the discourse context of the claim

        - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2F__UTLi_BlT.png?alt=media&token=f4559a05-ab2a-473d-b9a7-5f8d3dfdc48e)

    - [[std/Micropublication]]s [[@clarkMicropublicationsSemanticModel2014]] seems like the right model with an explicit emphasis on grounding in "lower-level" evidence and grounding in [[Stephen E. Toulmin]]'s model of [[defeasible argumentation]] [[@toulminUsesArgument2003]] and [[@verheijEvaluatingArgumentsBased2005]]
[[QUE - How can we support explicit contention with evidence when synthesizing knowledge claims]]

- [[@brushSEPIOSemanticModel2016]]'s [[std/SEPIO]] feels similar to [[@clarkMicropublicationsSemanticModel2014]], in that it doesn't really care about assigning numbers, and is more about making sure that there is direct documentation of "lines of evidence" - what *kind* of support is there for each claim?

    - They support connecting to the [[std/Evidence and Conclusion (ECO)]] ontology, which describes types of scientific evidence (but NOT strength!) in bio
[[August 9th, 2020]]

- [[std/Micropublication]]s [[@clarkMicropublicationsSemanticModel2014]] seems like the right model with an explicit emphasis on grounding in "lower-level" evidence and grounding in [[Stephen E. Toulmin]]'s model of [[defeasible argumentation]] [[@toulminUsesArgument2003]] and [[@verheijEvaluatingArgumentsBased2005]]

    - but there isn't really a repo yet for them; [[std/Nanopublications]] have "repos", but they're mostly self-hosted I think?

    - plus [[Jodi Schneider]] and her students have been playing with it)
[[August 9th, 2020]]

- speaking of [[@clarkMicropublicationsSemanticModel2014]]:

    - cite [[@simkinStochasticModelingCitation2005]] and [[@simkinMathematicalTheoryCiting2007]] to claim that "scientific authors only read approximately 10%-20% of the papers they cite, and many of the rest are evidently copied from reference lists": [[[[CLM]] - Scientists frequently cite papers they haven't read]]

        - definitely cc [[[[CLM]] - Citation practices in science are far from optimal]]

        - FWIW, these findings are consistent with a couple other later papers, [per scite](https://scite.ai/reports/stochastic-modeling-of-citation-slips-Odndy8?contradicting=false&mentioning=false&page=1&utm_campaign=badge_generic&utm_medium=plugin&utm_source=generic)

            - [[@goldbergModellingCitationNetworks2015]]

                - #quotes

                    - "In particular our model and data suggest that around 70% to 80% of papers cited are 'subsidiary papers', that is papers which are also cited by the other papers in the bibliography, the 'core papers'. Similar results have been seen by [[@simkinStochasticModelingCitation2005]] who use a similar model but different data and methods to arrive at this result. From a different perspective, [[@cloughTransitiveReductionCitation2015]] have also shown that around 80% of citations are removed from arXiv citation networks through the process of transitive reduction (an extended version of the declustering algorithm used here).…”
[[#AnnotatedBib for Synthesis Infrastructures]]

- [[@clarkMicropublicationsSemanticModel2014]]

    - idea of claim
