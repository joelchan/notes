---
title: "Q- What is a decentralized discourse graph"
enableToc: false # do not show a table of contents on this page
---

Authored By:: [[P- Joel Chan]], [[P- Rob Haisfield]], [[P- Brendan Langen]]

Our research draws from a long line of information models, such as the Semantic Web Applications in Neuromedicine (SWAN) ontology [[R- The SWAN biomedical discourse ontology]], the Micropublications model [[R- Micropublications a semantic model]], the ScholOnto ontology for modeling scientific discourse [[R- ScholOnto an ontology-based digital library server for research documents and discourse]], the nanopublication model [[R- The anatomy of a nanopublication]], and the Hypotheses, Evidence, and Relationships (HypER) model [[R- Hypotheses Evidence and Relationships]]. These models share a common underlying model for representing scientific discourse: they distill traditional forms of publication down into more granular, formalized knowledge **claims**, linked to supporting evidence and **context** through a network or **graph** model. 

We use the term **discourse graph** to refer to this information model, to evoke the core concepts of representing and relating knowledge claims (rather than concepts) as the central unit, and emphasizing linking and relating these claims (rather than categorizing or filing them). Standardizing the representation of scientific claims and evidence in a graph model can support machine reasoning ([[R- Genuine semantic publishing]]). We are particularly interested in the [[C- Discourse graphs could significantly accelerate human synthesis work | potential of discourse graphs to accelerate human synthesis work]]. 

So what does it mean for a discourse graph to be decentralized?

As seen in [[R- Towards a comprehensive model of the cognitive process and mechanisms of individual sensemaking|R- Towards a comprehensive model of the cognitive process and mechanisms of individual sensemaking]], we see that there are many component parts to synthesis. Given that, [[C- The responsibilities required to produce synthesis can be split up among many people]]. [[P- Michael Karpeles]] refers to this concept as [human computation](https://twitter.com/mekarpeles/status/1440886235917164546?s=20)
- Some people will contribute primary research. 
- Some will formalize the research contributed by others into frameworks and theories. [[C- Incrementally processing notes is a key user behavior to promote synthesis]]
- Some will help determine what directions are meaningful to explore, ranking the utility of the outputs of others.
- Some will simply read everyone else's outputs and annotate them, all the while meaningfully connecting the conversation between the various fields they explore. [[C- It will be important to capture the potential energy of information consumption]]. 
- Some will rate the contributions of those who annotate to improve the signal to noise ratio. As such, a key question as we go into the interview phase of our research will be: [[Q- What community roles are necessary in a decentralized knowledge graph]]?

Dividing the responsibilities of synthesis is one of the core strengths of decentralizing the process. When we look at prior attempts at building a semantic web, we find that the primary reasons have to do with human behavior and dishonesty.

[[C- People are lazy]] and [[content/garden/LitReview/C- Most people will primarily consume information]], so we can't expect them to do all of the work necessary to index information themselves. While tools like [[Roam Research]] and [[Obsidian|Obsidian]] enable people to develop advanced discourse graphs for themselves, over time they may end up with a system that is so complicated that maintaining it becomes work. Why not split up the effort so the ones who share information aren't responsible for 100% of the processing?

%%And if people can be dishonest, isn't consensus over a shared state of truth one of the key innovations of the blockchain?%%
%%- [ ] Respond to this question. [[Todo List for LitReview]]%%