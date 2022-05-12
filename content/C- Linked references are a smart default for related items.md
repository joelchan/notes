---
title: "C- Linked references are a smart default for related items"
enableToc: false # do not show a table of contents on this page
---

Authored By:: [[P- Rob Haisfield]]

- Assuming you're not using aliases, a plain text search in [Obsidian](Obsidian.md) for `"[page](page)"` within quotations is functionally indistinguishable from the backlinks for that page. Linked references can then be thought of as a search for related items, where all the app knows is that backlinks have a high likelihood of being related because the user explicitly linked the items together.
- Unlinked references can be thought of as a search for `"page" -"[page](page)`. These have a lower likelihood of relatedness, as the connections were not explicitly made by the author while writing, but may represent latent connections in imported text or [quick capture](quick%20capture) thoughts. Linking unlinked references is tool for [structure in hindsight](../LitReview/structure%20in%20hindsight.md)
- If we [I- Populate the related items section through a search term](I-%20Populate%20the%20related%20items%20section%20through%20a%20search%20term.md), there needs to be a smart default term, as requiring the user to manually specify a search to represent related items for each page would be too much work. As wikilink matches are high signal, `[page](page)` should be the default term. That will often be enough. However, if it isn't, the user should be able to adjust the search term to more accurately express what they consider to be related.
- [P- Gordon Brander](P-%20Gordon%20Brander.md) made a similar point, taking inspiration from [Notational Velocity](Notational%20Velocity.md). As he phrases it in [Search reveals useful dimensions in latent idea space](https://subconscious.substack.com/p/search-reveals-useful-dimensions):
- > **Any sufficiently advanced search is indistinguishable from a hyperlink**. A search query is kind of like a hyperlink that can be constructed on the fly. Our question forges a link between notes, just-in-time. When a search becomes extremely specific, it functions like a coordinate to a specific point in latent idea space.