# Archived JSON collation recipe

SOURCE_ONLY metadata collation in the orchestration context, not a filesystem
helper execution. Inputs were complete native workspace sed-read strings; no
host spelling in those strings was dereferenced by this collation.

The exact lexical integer preservation recipe was:

```javascript
function parseExact(text) {
 let out="", i=0;
 while(i<text.length) {
  if(text[i]==='"') { let j=i+1; for(;j<text.length;j++){if(text[j]==='\\'){j++;continue;}if(text[j]==='"'){j++;break;}} out+=text.slice(i,j);i=j;continue; }
  if(text[i]==='-' || /[0-9]/.test(text[i])) {const m=/^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/.exec(text.slice(i));if(!m)throw Error("number");const n=m[0];out+=/^-?[0-9]+$/.test(n)&&(BigInt(n)>9007199254740991n||BigInt(n)<-9007199254740991n)?JSON.stringify("__EXACT_INTEGER__:"+n):n;i+=n.length;continue;}
  out+=text[i++];
 }
 return JSON.parse(out);
}
```

Raw archived strings remain preserved. Metadata integer tagging is solely for
in-memory comparisons; Python source draft uses Python JSON integers directly.
Four scientific file fields and all scalar configuration states use the
original values, without source/result normalization. Whole key sets, not counts
alone, were compared. Equal overlapping domains do not assert current host
state. This recipe is not an executed checker file, nor independent proof of
operating-system runtime closure.
