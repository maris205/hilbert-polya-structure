"use strict";
// Read/decode existing authorized raw data only. Never execute captured requests or Python.
const io=require("./DOCUMENTARY_IO.cjs"),{parseIntegerJSON,canonicalIntegerJSON}=require("./LOSSLESS_JSON.cjs");
const input=io.openDocument(io.rawFiles[0]);
if(input.key.bytes!==322982||input.key.sha256!=="6b4aa5f0ab3c8f0a67bb4ab179c29dae38cb8703598a620fa408a6b1c95c59d5")throw Error("wrong original raw stdout");
if(input.bytes.some(b=>b>127))throw Error("not ASCII JSON stream");
const parsed=parseIntegerJSON(input.bytes.toString("ascii")),x=parsed.data;
if(canonicalIntegerJSON(x)+"\n"!==input.bytes.toString("ascii"))throw Error("noncanonical or lost original data");
function shape(v){return v===null?"null":Array.isArray(v)?{array:v.length}:typeof v==="object"?{object:Object.keys(v)}:typeof v;}
const summary={scope:"LOSSLESS_ARCHIVED_DATA_STRUCTURE_NOT_RUNTIME_VERDICT",raw_key:input.key,parser:parsed.counts,top:Object.fromEntries(Object.entries(x).map(([k,v])=>[k,shape(v)])),status:x.status,runtime_accepted:x.runtime_accepted,snapshots:x.module_snapshots?.map(s=>({phase:s.phase,rows:s.rows.length,complete:s.complete})),maps:x.maps?.map(m=>({phase:m.phase,byte_count:m.byte_count,eof:m.eof,parsed:m.parsed.length})),file_schema_counts:{},launch:x.early_launch,first_file:x.files?.[0],absent_files:x.files?.filter(f=>f.absent),process:x.process_begin,deltas:{helper:x.helper_module_delta,closing:x.closing_module_delta,helper_maps:x.helper_observed_map_additions,closing_maps:x.closing_observed_map_additions},environment:x.environment,total_file_read_bytes:x.total_file_read_bytes};
for(const f of x.files||[]){const k=Object.keys(f).sort().join(",");summary.file_schema_counts[k]=(summary.file_schema_counts[k]||0)+1;}
process.stdout.write(JSON.stringify(summary,(_,v)=>typeof v==="bigint"?{integer:v.toString()}:v,2)+"\n");
