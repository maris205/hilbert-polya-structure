'use strict';
// Parse the complete captured JSON as data; integer tokens never pass through Number.
const fs=require('fs'),crypto=require('crypto');
const Q='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/';
const raw=fs.readFileSync(Q+'p213_minimal_observer_probe01/stdout.bin');
const text=raw.toString('ascii');let at=0,integerTokens=0,unsafeMagnitudeTokens=0,objects=0;
function ws(){while(at<text.length&&/[\x20\t\r\n]/.test(text[at]))at++;}
function string(){const begin=at++;for(;;){if(at>=text.length)throw Error('unterminated string');const c=text[at++];if(c==='"')return JSON.parse(text.slice(begin,at));if(c==='\\')at++;}}
function value(){
 ws();const c=text[at];
 if(c==='"')return string();
 if(c==='['){at++;const a=[];ws();if(text[at]===']'){at++;return a;}for(;;){a.push(value());ws();const t=text[at++];if(t===']')return a;if(t!==',')throw Error('array delimiter');}}
 if(c==='{'){at++;objects++;const a=Object.create(null);ws();if(text[at]==='}'){at++;return a;}for(;;){ws();if(text[at]!=='"')throw Error('object key');const k=string();if(Object.hasOwn(a,k))throw Error('duplicate key');ws();if(text[at++]!==':')throw Error('colon');a[k]=value();ws();const t=text[at++];if(t==='}')return a;if(t!==',')throw Error('object delimiter');}}
 for(const [word,v]of [['null',null],['true',true],['false',false]])if(text.startsWith(word,at)){at+=word.length;return v;}
 const m=/^-?(?:0|[1-9][0-9]*)/.exec(text.slice(at));if(!m)throw Error('not integer-only JSON token');
 at+=m[0].length;integerTokens++;const n=BigInt(m[0]);if(n>9007199254740991n||n< -9007199254740991n)unsafeMagnitudeTokens++;return n;
}
if(!raw.every(x=>x<=127))throw Error('not ASCII');
const j=value();ws();if(at!==text.length)throw Error('unparsed tail');
const materialized=JSON.parse(JSON.parse(fs.readFileSync(Q+'p213_minimal_observer_materialization01/BYTE_MATCH_NATIVE.json','utf8')).result.output);
const source=j.files.find(f=>f.lexical===Q+'p213_minimal_observer_enabled01/observe.py');
const key=materialized.keys.find(k=>k.path===source.lexical);
const mapping={st_dev:'dev',st_ino:'ino',st_mode:'mode',st_nlink:'nlink',st_uid:'uid',st_gid:'gid',st_rdev:'rdev',st_size:'size',st_mtime_ns:'mtimeNs',st_ctime_ns:'ctimeNs'};
const comparisons=[];
for(const [field,meta]of Object.entries(mapping)){
 const expected=key.metadata[meta];const stages=[source.begin.final_lstat,source.fd_before,source.fd_after,source.after_read.final_lstat,source.closing.final_lstat];
 if(!stages.every(s=>typeof s[field]==='bigint'&&s[field].toString()===expected))throw Error('exact source-key mismatch '+field);
 comparisons.push({field,rawInteger:source.fd_before[field].toString(),documentaryField:meta,documentaryInteger:expected,stages:stages.length});
}
if(source.byte_count!==98365n||source.sha256_of_read_bytes!==key.sha256||!source.complete||!source.eof)throw Error('source key content mismatch');
console.log(JSON.stringify({scope:'LOSSLESS_CAPTURE_DATA_PARSE_AND_EXACT_SOURCE_KEY_ONLY_NOT_INDEPENDENT_RUNTIME_RECEPTION',rawBytes:raw.length,rawSha256:crypto.createHash('sha256').update(raw).digest('hex'),integerTokens,unsafeMagnitudeTokens,objects,duplicateKeysRejected:true,allInputConsumed:at===text.length,sourceComplete:true,sourceHash:source.sha256_of_read_bytes,sourceKeyComparisons:comparisons,preciseTotalFileReadBytes:j.total_file_read_bytes.toString(),precisionWarningPreserved:'INITIAL_RAW_RECEIVE_NATIVE convenience projection is not an exact-large-integer runtime key.'},null,2));
