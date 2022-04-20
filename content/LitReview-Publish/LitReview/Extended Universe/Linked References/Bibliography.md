
```dataview
table title, author, year, length(file.inlinks) as references
from "LitReview"
where regexmatch("^R-", file.name)
sort author desc
```