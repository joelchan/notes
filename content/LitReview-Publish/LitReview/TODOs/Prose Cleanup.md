This will show any links that have LitReview at the beginning. 

LitReview
```query
--path:(litreview) line:("LitReview") 
```

Drafts
```query
--path:(litreview) line:("Drafts") 
```

Zettels
```query
--path:(litreview) line:("Z- ") 
```

```dataview
table length(file.inlinks) as references 
from "LitReview"
where regexmatch("^Z-", file.name)
sort author desc
```
