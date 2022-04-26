---
title: "I- Enable composable queries to facilitate structure in hindsight"
enableToc: false # do not show a table of contents on this page
---
- [If a page's related items section is defined through a search term]([I- Populate the related items section through a search term](I-%20Populate%20the%20related%20items%20section%20through%20a%20search%20term.md)), then we can think of the page title and its query as a key-value pair. The data structure would look something like this:
- ```clojure
"structure in hindsight" means 
  (any: "structure in hindsight" 
        (all: (any: "structure" "structuring")
              "hindsight")
"structure in foresight" means 
  (any: "structure in foresight" 
        (all: (any: "structure" "structuring")
              "foresight")
"structuring across time" means
        (any: "structure in hindsight"
              "structure in foresight")
"PCT" means
  (any: "PCT"
        "Perceptual Control Theory")
"SDT" means
  (any: "SDT"
        "Self-Determination Theory")
"Behavioral Science Theories" means
  (any: "Behavioral Science Theories"
        (any: "SDT"
              "PCT"))
"Theories" means
  (any: "Behavioral Science Theories"
        "Political Science Theories"
        "Biology Theories")```
- Over time, composable queries fight entropy. We would frequently see people create multiple pages that mean the same thing simply because their body of notes had grown so large that they didn't remember they had already created other pages to refer to the same concept. 
- This is a huge challenge of adding structure! In our private research notebook, we refer to this problem of entropy from structure in multiple ways (for example, `[Q- How might we prevent workflow entropy](Q-%20How%20might%20we%20prevent%20workflow%20entropy)` and `[[[I- Enable composable queries to reduce system entropy](%5B%5BI-%20Enable%20composable%20queries%20to%20reduce%20system%20entropy)]]`).
- We aim to [work at the speed of thought](work%20at%20the%20speed%20of%20thought), but too much structure creates paralyzing cognitive overhead. [C- An increasing amount of structure leads to entropy](C-%20An%20increasing%20amount%20of%20structure%20leads%20to%20entropy) [*](((Rf-9FlEw9))).
- [Roam](Roam) enables users to merge pages together. This affordance aims to solve issues where users have created multiple pages for similar ideas, but the results are different in practice. When two pages represent conceptually "close" concepts, users consistently link blocks to both pages to ensure linked references show up on each page. Merging is not always appropriate.
- Over time, these duplicate links pile up, and users feel the need to link to a large vocabulary of pages, which brings us back to square one with [Repeat work](Repeat%20work). Their system's surface area has greatly increased in size, and they're reliant on their own memory to recall each new link they add. Ultimately, this leads to system collapse or abandonment.  
- Multiplayer amplifies the problem, [as different people refer to similar concepts with different language]([Q- How do we solve the problem of different people referring to the same concept with different language](../LitReview/Extended%20Universe/Q-%20How%20do%20we%20solve%20the%20problem%20of%20different%20people%20referring%20to%20the%20same%20concept%20with%20different%20language.md)).
- Composable queries enable people to create both aliases and hierarchies. Aided by the full expressiveness of a query language, composable searches empower people to build up their own semantic dictionary and thesaurus over time. As the queries can be adjusted at any point, this is a promising solution to the question: [Q- How might we allow people to adapt their past system and notes to current needs](../LitReview/Extended%20Universe/Q-%20How%20might%20we%20allow%20people%20to%20adapt%20their%20past%20system%20and%20notes%20to%20current%20needs.md)?
