"use strict";
// Source/doc/raw output reads only; the fixed capability module never opens decoded targets.
const io=require("./DOCUMENTARY_IO.cjs");
const capture_before=io.captureDirectory();
const keys=[...io.documents,...io.rawFiles].map(path=>io.openDocument(path).key);
const capture_after=io.captureDirectory();
if(JSON.stringify(capture_before)!==JSON.stringify(capture_after))throw Error("capture directory changed across finite input reads");
for(const key of keys.filter(k=>io.rawFiles.includes(k.path)))if(key.metadata.mode!=="33152"||key.metadata.uid!=="0"||key.metadata.gid!=="0"||key.metadata.nlink!=="1")throw Error("raw stream owner/mode/link count");
process.stdout.write(JSON.stringify({scope:"P213_INDEPENDENT_POSTREAD_DOCUMENTARY_AND_TWO_AUTHORIZED_RAW_KEYS_NOT_TARGET_RECRAWL",capture_before,capture_after,keys},null,2)+"\n");
