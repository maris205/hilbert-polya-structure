"use strict";
// In-memory DATA mutation controls. Originals are read-only and never written or executed.
const io=require("./DOCUMENTARY_IO.cjs"),j=require("./LOSSLESS_JSON.cjs"),receive=require("./RUNTIME_DATA_CHECK.cjs");
const Q="docs/papers211_215_sequence/qa/";
const raw=io.openDocument(io.rawFiles[0]).bytes.toString("ascii"),binding=j.parseIntegerJSON(io.openDocument(Q+"p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json").bytes.toString("utf8")).data,source=io.openDocument(Q+"p213_minimal_observer_enabled01/observe.py").key;
const controls=[];
function reject(name,f){let error=null;try{f()}catch(e){error=String(e.message)}if(error===null)throw Error("negative control erroneously accepted: "+name);controls.push({name,rejected:true,error})}
for(const [name,s]of[["duplicate object key",'{"x":1,"x":2}'],["noninteger float",'{"x":1.5}'],["noninteger exponent",'{"x":1e3}'],["trailing text",'{}x'],["leading zero",'{"x":01}'],["malformed string",'{"x":"\\q"}']])reject(name,()=>j.parseIntegerJSON(s));
const high=j.parseIntegerJSON('{"i":1789050904365560948,"b":false,"z":0}').data;
if(high.i!==1789050904365560948n||j.typedEqual(high.b,high.z)||j.canonicalIntegerJSON(high)!=='{"b":false,"i":1789050904365560948,"z":0}')throw Error("lossless positive scalar controls failed");
function mutate(name,f){reject(name,()=>{const data=j.parseIntegerJSON(raw).data;f(data);receive(data,binding,source)})}
mutate("unknown top-level field",x=>{x.extra=true});
mutate("false boolean replaced by zero integer flag",x=>{x.early_launch[1].find(r=>r[0]==="dev_mode")[1]=["value",0n]});
mutate("fourth launch immutable maxsize altered",x=>{x.closing_launch[0].find(r=>r[0]==="maxsize")[1][1]+=1n});
mutate("helper module spec origin altered",x=>{x.module_snapshots[2].rows.find(r=>r[0]==="json")[3][1]=["value","/unpermitted/origin.py"]});
mutate("module loader identity altered",x=>{x.module_snapshots[0].rows.find(r=>r[0]==="sys")[4]=["instance","unknown","UnknownLoader"]});
mutate("five-phase snapshot completeness false",x=>{x.module_snapshots[4].complete=false});
mutate("helper module delta removed entry",x=>{x.helper_module_delta.added.pop()});
mutate("complete role array loses row",x=>{x.closing_roles.pop()});
mutate("map parsed inode +1",x=>{x.maps[0].parsed.find(r=>r.path.startsWith("/")).inode+=1n});
mutate("map raw hex corrupted",x=>{x.maps[1].raw_hex="00"+x.maps[1].raw_hex.slice(2)});
mutate("map EOF false",x=>{x.maps[2].eof=false});
mutate("map observed additions altered",x=>{x.helper_observed_map_additions.pop()});
mutate("file full byte count +1",x=>{x.files.find(f=>f.complete).byte_count+=1n});
mutate("file one exact nanosecond endpoint +1",x=>{x.files.find(f=>f.complete).closing.final_lstat.st_mtime_ns+=1n});
mutate("file extra stat field",x=>{x.files.find(f=>f.complete).fd_before.birthtime=0n});
mutate("absence relabelled complete empty content",x=>{x.files.find(f=>f.absent).complete=true});
mutate("closing absence errno altered",x=>{x.files.find(f=>f.absent).closing.absence.errno=13n});
mutate("total content accounting altered",x=>{x.total_file_read_bytes+=1n});
mutate("source reported digest altered",x=>{x.files.find(f=>f.lexical===binding.observer).sha256_of_read_bytes="0".repeat(64)});
mutate("closing process identity altered",x=>{x.process_closing.exe_stat.st_ino+=1n});
mutate("cached environment promoted to actual environ",x=>{x.environment.scope="complete_live_environment"});
process.stdout.write(JSON.stringify({scope:"RECIPIENT_IN_MEMORY_DATA_NEGATIVE_CONTROLS_NOT_OBSERVER_RETRY",parserPositiveControls:3,negativeControls:controls.length,controls,originalStreamNeverWritten:true,observedRuntimeTargetNeverOpened:true},null,2)+"\n");
