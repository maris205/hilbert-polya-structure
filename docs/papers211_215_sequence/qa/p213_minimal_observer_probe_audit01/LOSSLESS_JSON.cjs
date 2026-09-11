"use strict";
// Independent data grammar only. No filesystem, child process, Python parser or eval.
function parseIntegerJSON(text){
 if(typeof text!=="string"||text.length>16777216)throw Error("unsupported JSON text size/type");
 let i=0,integers=0,unsafeIntegers=0,objects=0,arrays=0,strings=0,booleans=0,nulls=0,maxDepth=0;
 const bad=m=>{throw Error("integer JSON "+m+" at character "+i);};
 const ws=()=>{while(i<text.length&&/[ \t\r\n]/.test(text[i]))i++;};
 function quoted(){
  if(text[i]!=="\"")bad("expected string");const start=i++;
  while(i<text.length){const c=text[i++];if(c==="\""){strings++;return JSON.parse(text.slice(start,i));}
   if(c==="\\"){if(i>=text.length)bad("unfinished escape");const e=text[i++];if(e==="u"){if(!/^[0-9a-fA-F]{4}$/.test(text.slice(i,i+4)))bad("unicode escape");i+=4;}else if(!'\"\\/bfnrt'.includes(e))bad("escape");}
   else if(c.charCodeAt(0)<32)bad("control in string");
  }bad("unterminated string");
 }
 function value(depth){
  if(depth>100)bad("nesting bound");maxDepth=Math.max(maxDepth,depth);ws();const c=text[i];
  if(c==="\"")return quoted();
  if(c==="{"){objects++;i++;const out=Object.create(null),seen=new Set();ws();if(text[i]==="}"){i++;return out;}
   while(true){ws();const k=quoted();if(seen.has(k))bad("duplicate object key");seen.add(k);ws();if(text[i++]!==":")bad("expected colon");out[k]=value(depth+1);ws();const end=text[i++];if(end==="}")return out;if(end!==",")bad("object delimiter");}
  }
  if(c==="["){arrays++;i++;const out=[];ws();if(text[i]==="]"){i++;return out;}
   while(true){out.push(value(depth+1));ws();const end=text[i++];if(end==="]")return out;if(end!==",")bad("array delimiter");}
  }
  for(const [token,out]of[["true",true],["false",false],["null",null]])if(text.startsWith(token,i)){i+=token.length;if(out===null)nulls++;else booleans++;return out;}
  const m=/^-?(?:0|[1-9][0-9]*)/.exec(text.slice(i));if(!m)bad("unsupported value");i+=m[0].length;
  if(i<text.length&&!/[ \t\r\n,}\]]/.test(text[i]))bad("noninteger or malformed number");
  const out=BigInt(m[0]);integers++;if(out>9007199254740991n||out< -9007199254740991n)unsafeIntegers++;return out;
 }
 const data=value(0);ws();if(i!==text.length)bad("trailing data");
 return {data,counts:{integers,unsafeIntegers,objects,arrays,strings,booleans,nulls,maxDepth,characters:text.length}};
}
function typedEqual(a,b){
 if(typeof a!==typeof b)return false;
 if(a===null||b===null)return a===b;
 if(Array.isArray(a)||Array.isArray(b))return Array.isArray(a)&&Array.isArray(b)&&a.length===b.length&&a.every((x,i)=>typedEqual(x,b[i]));
 if(typeof a==="object"){const x=Object.keys(a).sort(),y=Object.keys(b).sort();return x.length===y.length&&x.every((k,i)=>k===y[i]&&typedEqual(a[k],b[k]));}
 return a===b;
}
function canonicalIntegerJSON(x){
 if(x===null)return "null";
 if(typeof x==="bigint")return x.toString();
 if(typeof x==="boolean")return x?"true":"false";
 if(typeof x==="string")return JSON.stringify(x).replace(/[\u007f-\uffff]/g,c=>"\\u"+c.charCodeAt(0).toString(16).padStart(4,"0"));
 if(Array.isArray(x))return "["+x.map(canonicalIntegerJSON).join(",")+"]";
 if(typeof x==="object")return "{"+Object.keys(x).sort().map(k=>canonicalIntegerJSON(k)+":"+canonicalIntegerJSON(x[k])).join(",")+"}";
 throw Error("unsupported output scalar type");
}
module.exports={parseIntegerJSON,typedEqual,canonicalIntegerJSON};
