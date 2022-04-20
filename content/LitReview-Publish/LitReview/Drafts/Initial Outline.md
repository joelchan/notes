## Outline

### The goal of this research

The goal of this research project is to find data structures and interfaces that support synthesis and innovation in a decentralized discourse graph. *See: [[Q- What is a decentralized discourse graph]]*

[[Q- What is synthesis|What is synthesis]]? 

Synthesis is a creative act. It involves creating a new whole out of component parts. This can come in many forms:
- Generalizing a principle over many instances
- Abstracting a new theory to frame many concepts
- Exaptation

- Some examples of interdisciplinary synthesis include:
	- Daniel Kahneman and Amos Tversky recognized a claim made by economists that people behaved rationally and questioned it. The rational actor model had long been assumed to be true in economics. They then studied the question through the lens of judgment and decision. Amos Tversky, always the militant debater, would challenge economists to rationalize their findings. This led to the beginning of a new field: **Behavioral Economics**
		- Much of the discourse in DisciplineA rests on AssumptionA. Participants in the discourse graph for DisciplineB call AssumptionA into question through the evidence and claims of GraphDisciplineB. 
		- In the effort of refuting AssumptionA, they found the areas where DisciplineA and DisciplineB were [[Q- How do we solve the problem of different people referring to the same concept with different language|discussing the same questions with different language.]]
		- If you picture a venn diagram, behavioral economics is the intersection between economic and behavioral science theory / evidence 
- [[P- Vitalik Buterin]] et al. recognizing that the blockchain could support full programmability and innovating smart contracts through Ethereum. There were further acts of synthesis when specific futures were envisioned, like an alternative to DNS. 
- The scaling solutions in the plan for Ethereum 2.0, with Proof of Stake, Sharding, and Layer 2, is an act of synthesis. They combined many sources of information to solve a problem, emphasizing only the most important bits, where the solutions work together synergistically.
- Cryptoeconomics is the combination of cryptography and economics for the goal of social coordination towards desirable outcomes. 

Example Problems
- SEC is making hands on decisions on a case by case basis with specific companies. The discourse is not made clear to stakeholders. 
	- One process is combative research. Where you agree to research a question together, and you both get to ask each other questions. Right now it's an interrogation. How do conflicting viewpoints come together and combine to form a new set of beliefs and decisions?

How do you push discourse forward such that it can be brought together easily when synthesis is required or desired?

### Core questions:

#### [[Q- What workflows and behaviors facilitate synthesis]]

#pipeline/develop Once we know what workflows and behaviors facilitate synthesis, we can figure out the data structure for a graph built to facilitate decentralized knowledge synthesis. This is the goal of the next 3-4 months. However, there are some initial components that appear to be a clear part of the discourse graph. [[Q- What user behaviors are people doing already that specifies structure that are not being instantiated into a structure]] These include: ^iMEpNj
- Questions
	- Ability to qualify them
	- Ability to promote them
	- **Ability to answer them**
	- Ability to provide resource material
- Concepts
- Claims
	- confidence scores
	- salience
	- Ability to qualify them
	- Evidence
- Boundary conditions
- Conditionals
- Relationships
	- Symmetrical relationships: 
	- Asymmetrical relationships: ^bRrPWV
	- Grouping
	- Encapsulation
		- [[Tools for Thought Examples/Wikum]]
			- [[C- Wikum allows you to summarize groups of comments on a Hacker News style forum]] #pipeline/develop 
	- Fuzzy relationships:
	- Contextual relationships
- Search
	- Basic logical primitives:
		- And
		- Or
		- Not
		- If
	- Nesting
		- [[Linked References/Q- How do you allow people to query nth degree and fuzzy connections without overwhelming the signal to noise ratio]]
- Inline coding
	- Logic blocks
		- let me write sentences and indicate logical relationships between items. Equals, greater than, follows from, also, is a subcomponent of, etc. Maybe provide a logic for people to define their own relationships through a [parser](app://obsidian.md/parser) like [Instaparse](app://obsidian.md/Instaparse)
- Standoff annotation
	- To research
- Triplets
	- x operator y
		- x/y can be subbed in with any search term, and there is some operator describing the relationship between the two sets of things
			- [[Main/I- Search as a part of the primitive design]] isn't sufficient for the whole thing - we'd also need to have the ability to manually add or remove items from the set when a search term is too loose / coarse of a definition. 
- [[C- End-user scripting enables creative workarounds]] and for people to create their own workflows

##### Some initial inklings:
- [[C- Incrementally processing notes is a key user behavior to promote synthesis]]
	- [[Extended Universe/Q- How do we increase the frequency of social review]]
	- [[C- Reviewing past notes in the process of creating new notes is a key user behavior to promote synthesis]]
	- [[C- Compression is necessary for synthesis]]
- [[Migrated/I- Search as a part of the primitive design]]
- [[C- There is a trend of platforms that support user-generated content winning]]

###### Brendan Comments
Research suggests: 
- [[C- Compression is necessary for synthesis]]
- [[Z- Composability is necessary for synthesis]]
- [[C- Contextualizability is necessary for synthesis]]
- [[C- Multiplicity is necessary for synthesis]]

Additionally, 
- [[C- Synthesis is supported by Active Reading]], but there are challenges listed here - [[R- Active reading and its discontents]]. 
- [[Z- Compressing complex ideas into more manageable chunks facilitates more complex thought]], but [[C- Compression and contextualizability are in tension]]. 

#### [[LitReview/Main/Q- What is the data structure of a graph built to facilitate decentralized knowledge synthesis]]

[[Q- What is synthesis]]? [[Q- What workflows and behaviors facilitate synthesis]]? **How could that labor be divided up?**

**[[Q- Should social knowledge management be thought of as social networks with really solid defaults, conventions, and incentives]]?**

At the end of the day, there are many people who will play a role here. Some people will need to fact check, or otherwise indicate their confidence in the credibility of information. Other people will figure out which questions are important to address. Some will primarily contribute new content, whereas others will simply annotate and form bridges between the content of multiple people. One of the main questions we will be asking during interviews will be how people go through the process of synthesis, both on their own and with others, so we can figure out how the responsibility can be distributed.

People need to be a part of the data structure in some way. [[Rob/C- An ideal decentralized knowledge graph would map a social graph and a knowledge graph]]. However, when people cite the research of others in academia, researchers cite the authors and the year of publication of a paper that makes a claim the researchers want to cite somewhere within it. This is convoluted and requires a lot of extra work from the reader. This is especially bizarre when you consider the point of our research... we want to help people better synthesize information! [[Rob/Q- How do we solve the problem of different people referring to the same concept with different language]]? If a claim is supported by many papers, why would we just privilege one set of authors? [[Q- How might we include contributors into the data structure for any block of information]]? **Why not just cite the claim or question directly, knowing that the claim will be connected directly to the resources and authors that researched it?**

Reference: [[R- A Short Introduction to the Underlay]]

[[P- Joel Chan]] has research on how academia and papers organizes information in weird ways. ^Z1MLSI
- Lots in [[R- Where the semantic publishing rubber meets the scholarly practice road]] 
- [[Z- Sensemaking models partially model scholarly synthesis as of April 21st 2020]]
- [[Q- Do scholarly synthesis infrastructures already exist]]
- [[Q- What is context for the purposes of scholarly synthesis]]

[[R- Polysemy and thought - Toward a generative theory of concepts]]

###### Brendan Comments
[[I- Embed metadata in citations to enable ongoing discovery]]
[[Q- Can neural networks answer queries from natural language without a predefined schema]]? If performance is strong enough, can NeuralDB be used?
[[Q- What would a discourse graph without a predefined schema look like]]?

### [[Q- What are powerful primitives for a user of a decentralized knowledge graph]]

Before figuring out [[Q- What are powerful interfaces for entering information into a discourse graph]], we need to figure out what primitives to include anyway.

[[Rob/Q- What user behaviors are people doing already that specify structure that are not being instantiated into a structure]]? Uncovering this will be a main goal for our [[User interview questions]]. 

[[Q- What user behavior is required to maintain a decentralized knowledge graph]]? This will enable us to determine key workflows that we need to enable. For example, we [[C- Bulk refactors are a necessary primitive to maintaining a decentralized discourse graph]] because of the sheer quantity of stuff. 

[[I- A DSL for a discourse graph with information entry, visualization, and retrieval]]. **A Domain-Specific Language will give us an ideal [way to prototype the data structures](https://weblog.jamisbuck.org/2006/4/20/writing-domain-specific-languages.html) and build up our understanding of the problem.** [[C- Yaniv Tal predicts that a GUI will be the most powerful direction for an interface|graphical user interfaces]], and in exploring the hypothetical DSL, we'll be able to identify what GUIs could be built. One possible outcome is using a GUI as an onboarding to full DSL capabilities. [[C- A structural editor can make a DSL approachable to end-users]]. See [here](https://www.figma.com/file/kHLDEecCMvZAIDnfe95tmp/graph-research-visual-inspo?node-id=0%3A1) for prior art to draw on. 

The idea of doing it in a DSL does not exclude us from doing it through a block based system. I'm less tied to text files at this point. I would be curious how to create a more rich data structure on the backend, like an [[EDN]]. However, DSLs have some key advantages.
1. [[C- A DSL speeds up the author]]. Given a simple and concise DSL, your only limiting factor for speed will be how fast you can type. This doesn't exclude us from using a GUI as an optional onramp. With a GUI onramp, then the user can go from doing something slow for the first few times before speeding up to the text version that they can copy / paste around.
2. [[C- A DSL allows for abstraction]]. Not only can you reuse functions that you create, you can also use creative workarounds from more advanced users.  
3. [[C- A DSL allows people to expand their use cases far beyond the imagination of the designer]]. End users can develop features to solve their own problems, which expands platform usability and places less load on the development team to keep up with feature requests. 

A very important idea: Blocks can have different types, and those types can have different schema associated with them. They could come with open metadata [similar to how email does it](https://subconscious.substack.com/p/if-headers-did-not-exist-it-would), where there are certain key-value pair fields that are guaranteed to be included in the metadata, but people are able to create their own fields and they can also write in an open space. 

My opinion differs from [[P- Gordon Brander]]'s insofar as I believe [[C- Inline metadata is more expressive than header metadata]] and [[C- Inline metadata is more satisfying to users than header metadata]]. Other than it not having to be in the header, I believe we're largely on the same page.

**Strong inkling:** Search should be semantic enough for people [[C- Search terms express intentions|to express what they mean]], for cutting through large quantities of information, and seamlessly pulling in live information as needed. [[I- A structural editor for a DSL for inline coding]].

I predict that a DSL for a discourse graph that is plugged into [[The Graph]] and allows for inline queries / inline coding would really allow people to leverage the connection with The Graph.

![[Migrated/I- Search as a part of the primitive design#^Z8qxpB]]
 
One of the core factors that drives the big questions around primitives here has to do with [[Q- What changes in a discourse graph as quantity of content increases]]. When people are solving a difficult problem, they don't always know how to articulate exactly what they are looking for. [[Q- What is a powerful interface for exploratory browsing]]? [[Q- What is a powerful interface for exploratory search]]? [[C- Current search engines are effective for specific informational searches]]. [[C- Newsfeeds are a poor intervention for distributing and discovering relevant information]]. Fuzzy searches don't solve the problem because that just increases the amount of information the exploratory researcher is presented with without improving the signal to noise ratio. *See- [[Extended Universe/Linked References/Q- How do you allow people to query nth degree and fuzzy connections without overwhelming the signal to noise ratio]]?* 

They need to reduce the amount of research necessary to find the right answer because there is a ton of high quality information! If they knew exactly what they were looking for, this wouldn't be a problem. [[C- People need a way of promoting and demoting knowledge in a decentralized knowledge graph]], and of leaving clues for other people to follow. One way that this could happen is through using [[C- Highlighted and lowlighted search results map to how well results map to intentions]] along with [[Migrated/I- Search as a part of the primitive design]].

[[Z- Composability is necessary for synthesis]]

#### Initial hypotheses:
- [[I- I should be able to leave a hole to fill in the blanks for an idea or domain]]
- [[Migrated/I- Search as a part of the primitive design]]
- Syntax
- "Functional programming"
	- [[Q- How might we apply map filter reduce to notes and what other primitives are relevant to this domain]]
		- [[C- There needs to be an excellent workflow for refactoring in a tool for thought]]
- [[C- I want to map arguments more than I want to outline them]]
- [[I- Question and subquestion relationships could be encoded into the logic]]
- Claims
- Questions
- Evidence
- Source of claims/questions/etc.
- [[I- Salience scores as a primitive]]
- [[I- Workspaces as a primitive]]
- [[I- I should be able to leave a hole to fill in the blanks for an idea or domain]]


###### Brendan Comments 
This seems like an opportunity to discuss interactive intent modeling. 
Adding to your words:  #pipeline/develop 

When people are solving a difficult problem, they don't always know how to articulate exactly what they are looking for. Further, as time goes on, the more we learn. [[Q- How do we design search systems that evolve with user knowledge of a topic]]? [[C- An exploratory search system should help the reader cumulatively gain information]]. 

[[C- Updating search results via interactive intent modeling improves user comprehension during exploratory searches]]. This suggests [[I- A search engine with interactive intent modeling can update based on user understanding and aid comprehension]] in an ongoing manner.

Interactive intent modeling can help users see the big picture behind their exploratory search, but [[Q- How can we retroactively provide users with new information related to their past searches]]? 

If subscription is a [[primitive design]], [[I- New findings can be pushed to a user based on their search history]]. This would allow users to "catch up" on new insights even if they aren't actively searching, with notifications by user, tag, updates, etc. 

related: [[Z: People need information about history of changes to reuse information]] [[C- Specifying context for future reuse is costly]] and [[C- Specifying context for future reuse requires predicting trajectories of future reuse]], and [[C- Predicting trajectories of future reuse of information objects is hard]].

Another [[primitive design]] is an interactive visual graph. [[C- Visualizing the intent model improves task performance and comprehension without increasing effort]] and [[C- Interacting with visualizations improves task performance in exploratory searches]]. 


### [[Q- What are powerful interfaces for entering information into a discourse graph]]


#### Initial strong inklings

#### [[I- A DSL for a discourse graph with information entry, visualization, and retrieval]]

This goes with [[I- A structural editor for a DSL for inline coding]]. [[C- Power users want to directly interface with the data structure of the app]]. A DSL would give users a way to do this, and I also bet that a [[I- A structural editor for composing relationships between files or blocks]] and [[I- A structural editor for data structures]] would be valuable to go with it, because [[C- A structural editor can make a DSL approachable to end-users]] since [[C- Programming syntax can be abstracted through the interface of a structural editor]].

Lately I've been grappling with how to create a DSL for thought that technically willing end-users could get into... I think it might be as simple as a [[structural editor]] for creating data structures where every part of the data structure is [[content addressable]], and high level functions for transforming, querying, and visualizing the data. Then people would have [[functional programming]] for creating new functions for themselves. [[C- A DSL allows for abstraction]]!

##### Why a DSL instead of a GUI?

A [[GUI]] can be created on top of the data structures created in a [[DSL]] https://flowchart.fun/ [[example]]
![[Pasted image 20210902175554.png]]       

##### [[example]]
- [[Extended Universe/Linked References/R- Roam can loosely be considered a DSL with a structural editor]]
- [[Hode]]


#### [[C- An ideal decentralized discourse graph would enable people to view information at different levels of granularity through a ZUI]]

#### [[Rob/C- An ideal decentralized knowledge graph would map a social graph and a knowledge graph]]

###### Brendan Comments - #pipeline/develop 
Much of the discussion around [[I- A DSL for a discourse graph with information entry, visualization, and retrieval]] and [[I- A structural editor for composing relationships between files or blocks]] seem to pertain here, because: 
- [[C- A structural editor could allow people to make and edit data structures]], 
- [[C- A DSL would let people write in a certain syntax and notation that gets transformed by functions into a data structure that can be manipulated by pre-built or custom-built functions]], and
- [[C- A DSL enables semantic self-expression]].

This implies [[C- Search terms should have smart defaults so people don't have to always use semantic self-expression]]. Search should play a large role in interface design, as noted - [[Migrated/I- Search as a part of the primitive design]]. 

Entering information into the graph is only one part of the challenge, as information will constantly be updated. Maintaining and improving quality of the graph implies [[C- There needs to be an excellent workflow for refactoring in a tool for thought]]. For example, overlap in context may occur. [[Extended Universe/Q- How do we solve the problem of different people referring to the same concept with different language]]? 

Thus, [[C- Bulk refactors are a necessary primitive to maintaining a decentralized discourse graph]].

Question for [[Rob Haisfield]] - Should this act as the gist of this section? If so, do we need to reformat prior sections? 

## [[User interview questions]] and goals

[[Rob/Q- What user behaviors are people doing already that specify structure that are not being instantiated into a structure]]


# Pipeline queries

## Premises
```query
--path:(litreview) line:("pipeline/premise")
```

## Develop

```query
--path:(litreview) line:("pipeline/develop")
```

# Other queries

## Query for low hanging fruit related to this project

```query
("low-hanging fruit" OR "low hanging fruit") --(discourse OR graph OR decentralized)
```