```dataview
table context, twitter, length(file.inlinks) as references
from "LitReview"
where regexmatch("^P-", file.name)
sort length(file.inlinks) desc
```