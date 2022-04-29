---
title: "Q- How might we apply map filter reduce to notes and what other primitives are relevant to this domain"
enableToc: false # do not show a table of contents on this page
---
Authored By:: [[P- Rob Haisfield]]

[[Q- What are powerful primitives for a user of a decentralized knowledge graph]]

Some ideas: Write a query, save the results to a list. Process that list with map, filter, and reduce. Filter it down. Map some function onto each note in the list. Reduce the results into another page, or into the "backlinks" for a page. [[C- Bulk refactors are a necessary primitive to maintaining a decentralized discourse graph]].

As can be seen in [[content/garden/LitReview/I- Search as a part of the primitive design]], search is a powerful way to populate a list. One could map the append function onto a list of the search results in order to append a new tag onto each item. Alternatively, one could map syntax highlighting rules based on the results of a query.

[[P- Conor White-Sullivan]] has an [interesting thread](https://twitter.com/Conaw/status/1134173307878629376?s=20) on this:

> In practice -- for notes Filter your notes for questions Map over your open questions and say -- how could I reframe this question to make it easier to answer -- what smaller or bigger questions help me answer this one -- how will I know I've found an answer
> Filter your notes for beliefs Map over them Ask -- How surprised would I be if this were false ("weight") -- what other beliefs do I think are true because this one is *what does this imply* -- What other beliefs, if I changed my mind about them, would change this one