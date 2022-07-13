---
title: [[PTN]] - TemplatePattern
url: https://roamresearch.com/#/app/megacoglab/page/umOQ5m1IC
author: Joel Chan
date: Sat Oct 23 2021 12:05:34 GMT-0400 (Eastern Daylight Time)
---



###### Discourse Context



###### References

[[roamcss]]

- [[[[PTN]] - TemplatePattern]]

    - 🔨

    - ```css
span[data-link-title^="C - "] > span {
   color: var(--col-black) !important;
  /*font-weight: 500;*/
}

span[data-link-title^="C - "] {
  background: var(--cl-green-100);
}

span[data-link-title="PTN"] > span {
   color: #7DA13E; !important;
   font-weight: 500;
}

span[data-link-title="PTN"] {
  /* background: var(--cl-green-100); */
}


span[data-link-title^="[[PTN]]"] > span {
   color: #7DA13E; !important;
   font-weight: 500;
}


span[data-link-title^="[[PTN]] "]:before {
    content: '🔨  ' 
}```
