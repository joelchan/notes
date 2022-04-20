Authored By: [[P- Brendan Langen]]

%%[[Todos for Brendan - DONE]]%%

[[P- Iian Neill]]'s goal with [[Codex OS]] is to build a system for *relation* - the principle of relatedness or [[sensemaking]]. To achieve this, he uses a modified data structure called standoff annotation, which allows information to respect multiple interpretations. 

This concept carries a ton of implications, but namely that an entity can be defined and connected in multiple

Most databases require an entity to carry the same relationship across the entirety of the database. This causes inherent challenges in extending knowledge across domain boundaries, as entities often carry different definitions - and thus, relationships. 

Codex OS is designed to enable users to frame things in multiple ways (or layers) without breaking the structure of their graph. 

Standoff annotation allows users to annotate atop an entity, which is stored separately from the text, yet still retains the relationship to the initial text.
https://github.com/argimenes/standoff-properties-editor

> A standoff property is a property that 'stands off' from the text it refers to, that is stored apart from the text source.
> A property in this context is a data structure that represents a range of characters in the text along with information relevant to the annotation, such as the annotation type. Annotations can be of any type, e.g. stylistic (italics; bold; underline), semantic (line; paragraph; page), or linked entities (database record; URL).

> XML does not cope well with [overlapping annotations](https://en.wikipedia.org/wiki/Overlapping_markup). This is because the tree structure of XML mandates that an overlapping annotation (two or more annotations that overlap the same text sequence) cross one or more branches of that tree structure.
> These problems disappear, however, if the text and its annotation properties are kept entirely separate. The text, then, is stored in a raw or unformatted state, annotated by a collection of discrete standoff properties.

Technical challenges from standoff properties can be mitigated by creating linked-list data structures.

> The technical challenge posed by standoff properties is that they require indexes to link annotations to the words in the text, which suggests that the text cannot be changed without breaking the annotations. However, by using a linked list-style structure composed of SPANs it is possible to create properties that reference characters by pointers, allowing text to be freely inserted or deleted without breaking the annotations. Indexes are only calculated at the end of the session, when the annotated text is to be exported (and presumably saved).

[[P- Iian Neill]] suggests that since machine generated annotations could enable a wealth of annotations, a layering structure can act as a focusing frame. 

> As there is no defined limit on the number or types of annotations that can be added to a text, there is the chance that texts may become visually cluttered with annotations. To address this, there is an option to assign a user-defined 'layer' to an annotation for the purpose of grouping them. Layers can be shown and hidden at will, thus reducing clutter. This is particularly helpful when it comes to computer-generated annotations, such as syntactic or semantic annotations created by an NLP library or other text analysis tools.

Adding a graph database atop standoff properties affords compounding benefits.

> While standoff properties can be stored in any format storing them as LOD entities in a graph database vastly increases their potential. For example, if you were searching for all references to a person you would not only find the texts but the exact character positions in the text. If you expanded your query from a person like Leonardo da Vinci, say, to all artists you could see every instance an artist is mentioned in any text
> Queries could also be combined across annotation types. For example, if you had the syntax tree of a text you could find every occurence of a term within a given syntactical unit. The more annotation types you record, the greater the number of text mining options become available.