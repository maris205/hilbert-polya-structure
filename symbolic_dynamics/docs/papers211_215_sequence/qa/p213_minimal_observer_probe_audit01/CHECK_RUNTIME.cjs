"use strict";
// DATA-ONLY receiver. Never runs Python/capture and never opens observed system paths.
const io=require("./DOCUMENTARY_IO.cjs");
const {parseIntegerJSON,canonicalIntegerJSON}=require("./LOSSLESS_JSON.cjs");
const check=require("./RUNTIME_DATA_CHECK.cjs");
const raw=io.openDocument(io.rawFiles[0]),stderr=io.openDocument(io.rawFiles[1]);
if(raw.key.bytes!==322982||raw.key.sha256!=="6b4aa5f0ab3c8f0a67bb4ab179c29dae38cb8703598a620fa408a6b1c95c59d5"||stderr.key.bytes!==0||stderr.key.sha256!=="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")throw Error("wrong original streams");
if(raw.bytes.some(b=>b>127))throw Error("nonASCII original stream");
const parsed=parseIntegerJSON(raw.bytes.toString("ascii"));
if(canonicalIntegerJSON(parsed.data)+"\n"!==raw.bytes.toString("ascii"))throw Error("lossless canonical raw mismatch");
const binding=io.openDocument("docs/papers211_215_sequence/qa/p213_minimal_observer_enabled_preparation01/BINDING.runtime_literal.json");
const bound=parseIntegerJSON(binding.bytes.toString("utf8")).data;
const source=io.openDocument("docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01/observe.py");
const result=check(parsed.data,bound,source.key);
process.stdout.write(JSON.stringify({verdict:"RUNTIME_DATA_PREDICATES_PASS_DOCUMENTARY_RECEPTION_PENDING",parser:parsed.counts,raw_key:raw.key,stderr_key:stderr.key,binding_key:binding.key,source_key:source.key,result},null,2)+"\n");
