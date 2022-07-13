---
title: @deWaardProteinsFairytalesDirections2010
url: https://roamresearch.com/#/app/megacoglab/page/Slep8P0rL
author: Joel Chan
date: Wed Jun 17 2020 16:30:16 GMT-0400 (Eastern Daylight Time)
---

- #[[references]]

    - Title: From Proteins to Fairytales: Directions in Semantic Publishing

    - Meta:

        - Authored by:: [[Anita de Waard]]

        - Year: [[2010]]

        - Publication: IEEE Intelligent Systems

        - Zotero link: [Zotero Link](zotero://select/items/6_Z9QWKR6E)

        - URL: [de Waard (2010). From Proteins to Fairytales: Directions in Semantic Publishing. IEEE Intelligent Systems](https://ieeexplore.ieee.org/document/5456415)

    - Content

        - Abstract

            - There has been an ongoing discussion about how to improve the delivery of scientific content using online tools, especially by focusing on content reuse and social media. This column explores how semantic technologies and systems could also enhance the scientific communication process. The author discusses some ongoing initiatives in semantic publishing, which aims to improve how scientists communicate using semantic technologies. The column mentions different types of projects, including efforts focusing on entity enrichment and projects that involve triple markup of documents (subject-predicate-object expressions). However, such approaches are not enough. They help us find information, but they don't help us understand it. The author argues that we need to incorporate a better understanding of how language encodes meaning into our systems, so that we can develop a richer scientific knowledge representation.

    - #lit-context

        - Author is key figure in [[semantic publishing]], now at [[Elsevier]]

    - #[[📝 lit-notes]]

        - #> "The column mentions different types of projects, including efforts focusing on entity enrichment and projects that involve triple markup of documents (subject-predicate-object expressions). However, such approaches are not enough. They help us find information, but they don't help us understand it. The author argues that we need to incorporate a better understanding of how language encodes meaning into our systems, so that we can develop a richer scientific knowledge representation"

            - Basically wants to say we need to model [[discourse]], not just [[entities]] and [[RDF triple store]] and [[ontologies]]

        - mentions exemplars of [[discourse]]-modeling efforts (p. 86):

            - [[std/SWAN]] #[[@ciccareseSWANBiomedicalDiscourse2008]]

                - which is a heroic #example-of [[specialized [[curator]] model of semantic publishing]]

                - ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyeTGkZb5eB.png?alt=media&token=7da3494b-0159-4ec4-b93a-52f00f61fcb7)

            - #[[@grozaSALTWeavingClaim2007]]

            - the [[sys/Cohere]] system from the [[Knowledge Media Institute]]

###### Discourse Context

- **Informs::** [[CLM - Scholarly argumentation operates on atomic statements and concepts as fundamental units]]

###### References

[[January 26th, 2021]]

- Significant work across formal conceptual models of scholarly argumentation [[@deWaardProteinsFairytalesDirections2010]], [[@clarkMicropublicationsSemanticModel2014]], sensemaking [[@russellCostStructureSensemaking1993]], and knowledge management [[@ackermanSharingKnowledgeExpertise2013]] suggest that an optimal information model for supporting synthesis is the epistemic model: shareable collections of knowledge __claims__ (e.g., __children are less susceptible to COVID-19 infection, given equivalent exposure__) and their associated __context__ (e.g., \textit{was sampling symptom-based? Where was the study conducted? At what point in the locality's epidemic time course?}), \textit{connected} in a discourse graph (e.g., supporting other hypotheses/claims, corroborated/disputed by other claims).

    - Key hypothesized affordances of [[[[PTN]] - discourse graph]] include the ability to compress complex ideas into granular statements, which affords quicker comparison, comprehension, and composition of ideas, while also retaining links to contextual details to allow for "unpacking" and critical interrogation of ideas as they are interpreted and recombined into more complex arguments/models.

    - These affordances are hypothesized to enable key process-level interactions with scholarly knowledge that are crucial for synthesis, such as a principled dialectic between context-rich observations (data) and creative and formal construction of models and hypotheses (theory).

    - These affordances may also enable more effective reuse and remixing of ideas across boundaries of time, projects, and even collaborators.
[[January 27th, 2021]]

- Significant work across formal conceptual models of scholarly argumentation [[@deWaardProteinsFairytalesDirections2010]], [[@clarkMicropublicationsSemanticModel2014]], sensemaking [[@russellCostStructureSensemaking1993]], and knowledge management [[@ackermanSharingKnowledgeExpertise2013]] suggest that an optimal information model for supporting synthesis is a collection of knowledge **claims** and their associated __context__, __connected__ in a discourse graph.

    - The answers to these questions cannot be found simply in the titles of research papers, in groupings of papers by area, or even in citation or authorship networks (effective though they might be at revealing macro structures in scientific communities). These information structures are not at the desired level of granularity, which is at the level of theoretical concepts/claims and empirical **claims** and evidence: for example, "__game theory predicts that discourse can devolve to an escalating tit-for-tat spiral under X conditions__", or "__banning bad actors from a subreddit in 2012 was somewhat effective at mitigating spread of misinformation on the subreddit__". This level of granularity is crucial not just for finding relevant claims to inform the synthesis, but also for constructing more complex arguments and theories (by connecting statements in logical and discursive relationships).

    - To understand why this information model is hypothesized to augment synthesis, let us return to our motivating example of the researcher who wants to design new interventions to mitigate online harassment. To synthesize a formulation of this problem that can advance the state of the art, she needs material that can help her work through detailed answers to a range of granular questions. For example, what theories of online behavior and antisocial behavior might be most relevant for understanding what is going on here? Which theories have the most empirical support in this particular setting? Are there conflicting theoretical predictions that might signal fruitful areas of inquiry? What are the key phenomena to keep in mind when designing an intervention (e.g., perceptions of human vs. automated action, procedural considerations, noise in judgments of wrongdoing, scale considerations for spread of harm)? What intervention patterns have been proposed that are both a) judged on theoretical and circumstantial grounds as likely to be effective in this setting, and b) lacking in direct evidence for efficacy?

    - Beyond operating at the claim level, however, our researcher will need to work through a range of **contextual details**. For example, to judge which studies and findings/theories are "actually applicable" (e.g.,, studying similar populations, interventions, settings, or outcome measures?) to her setting, she might need to reason over the fact that two studies that concluded limited efficacy of bans had ban interventions that were quite short, on a forum with no identity verification. Or she might reason through the fact that a prominent theory of bad faith and discourse was proposed by a philosopher from the early 2000's (before the rise of modern social media). To judge the validity of past findings (e.g., what has been established with sufficient certainty, where the frontier might be), she would need to know, for example, which findings came from which measures (e.g., self-report, behavioral measures), and the extent to which findings have been replicated cross authors from different labs, and across a variety of settings.

    - Also, contextual details, such as methodology or metadata, are explicitly included in the discourse graph. This should support direct analysis of claims with their evidentiary context. Figure X shows how this might be supported in the specific worked example above.

    - Beyond these direct hypothesized benefits to synthesis, such models could also be used and repurposed over time, across projects, and potentially even across people. For example, imagine collaborators sharing these collections of epistemic models with each other, to speed up the process of working towards shared mental models and identify productive areas of divergence; or PIs and senior students onboarding newer students not with long reading lists, but subsets of epistemic models that they can build on and add to over time. How much time and overhead could be saved if this were a reality?

    - An epistemic model has key affordances that are hypothesized to enable just these sorts of operations. Information is represented primarily at the claim/statement level, and are embedded in a discourse graph. Thus, claims should be able to have many-to-many relationships to support composition of more complex arguments and theories, or "decompression" into component supporting/opposing claims.
[[June 17th, 2020]]

- bit of a critical review by [[Anita de Waard]] about [[semantic publishing]] ca. [[2010]]: #[[@deWaardProteinsFairytalesDirections2010]] #> "The column mentions different types of projects, including efforts focusing on entity enrichment and projects that involve triple markup of documents (subject-predicate-object expressions). However, such approaches are not enough. They help us find information, but they don't help us understand it. The author argues that we need to incorporate a better understanding of how language encodes meaning into our systems, so that we can develop a richer scientific knowledge representation"

    - very similar vision to what we're arguing for, in tandem with [[@kuhnGenuineSemanticPublishing2017]], for moving beyond [[ontologies]] to modeling claims and [[discourse]]
