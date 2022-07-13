---
title: [[QUE]] - TemplateQuestion
url: https://roamresearch.com/#/app/megacoglab/page/pj2QxzxTR
author: Joel Chan
date: Thu Jun 24 2021 10:38:35 GMT-0400 (Eastern Daylight Time)
---



###### References

[[roamcss]]

- [[[[QUE]] - TemplateQuestion]]

    - ```css
/* change font color and weight */
span[data-link-title^="[[QUE]] - "] > span {
  font-weight: 500; 
  color: #99890E !important; 
}

/* add icon before page ref */
span[data-link-title^="[[QUE]] - "]:before {
    content: '🔎  ' 
}

/* span[data-link-title^="Q - "] > span {
  color: #fff !important;
  font-weight: 500;
  color: var(--cl-black) !important;
}*/

/*span[data-link-title^="Q - "] {
  color: #fff !important;
  background: var(--cl-green-yel-100);
  background:  #F9F0AB;;
}*/

span[data-link-title="QUE"] > span {
   /*color: #fff !important; */
  font-weight: 500; 
  color: #99890E !important; 
}

/*span[data-link-title^="QUE"] {
  color: #fff !important;
  background: var(--cl-green-yel-100); 
  background:  #F9F0AB; 
}*/



/* also support old notation with : for now */
span[data-link-title^="Q: "] > span {
   /*color: #fff !important;
  font-weight: 500;*/
  color: var(--cl-black) !important;
}

span[data-link-title^="Q: "] {
  /* color: #fff !important;*/
  /* background: var(--cl-green-yel-100); */
  background:  #F9F0AB;;
}```
