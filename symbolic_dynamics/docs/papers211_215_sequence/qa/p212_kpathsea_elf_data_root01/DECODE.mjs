// SOURCE-ONLY proposed root DATA entry. No received executable is invoked.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
assert.equal(process.cwd(),'/root/autodl-tmp/symbolic_dynamics');assert.equal(process.argv.length,2);
const Q='docs/papers211_215_sequence/qa/',P=Q+'p212_kpathsea_elf_data_preparation01/';
const SOURCES=[
 [P+'load_kpathsea.proposed.mjs.txt',6675,'51b42905e783ca4b92219edcfcc4828fa8975d058515b33503c48479b8499fcd'],
 [Q+'p212_elf_cache_data_decoder_source01/decode.v2.proposed.mjs.txt',15863,'24122a0fa7da0e38390bbdb8ba240279c166f1b3116a3c87f9a136c9791b1068'],
 [P+'decoder_append.proposed.mjs.txt',3983,'949264a331a6f843a6cf4a9f9efb88178bc61634382970675e0d389dc40977d5']
];
const F='dev ino mode nlink uid gid rdev size mtimeNs ctimeNs'.split(' '),stat=s=>Object.fromEntries(F.map(k=>[k,String(s[k])])),pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
const sourceKeys=[],sourceBytes=[];
let output=null;
try{
 for(const [path,bytes,sha256]of SOURCES){const k={path,lstat_before:null,fstat_before:null,fstat_after:null,lstat_after:null,reads:[],bytes_read:0,eof:false,close_succeeded:false,content:null};sourceKeys.push(k);let fd=null;const chunks=[];
  try{const first=fs.lstatSync(path,{bigint:true});k.lstat_before=stat(first);assert(first.isFile()&&first.size===BigInt(bytes));fd=fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);k.fstat_before=stat(fs.fstatSync(fd,{bigint:true}));assert.deepEqual(k.fstat_before,k.lstat_before);const block=Buffer.alloc(65536);
   for(;;){const requested=Math.min(block.length,bytes-k.bytes_read+1),returned=fs.readSync(fd,block,0,requested,null);k.reads.push({requested,returned});assert(Number.isSafeInteger(returned)&&returned>=0&&returned<=requested);if(returned===0){k.eof=true;break;}chunks.push(Buffer.from(block.subarray(0,returned)));k.bytes_read+=returned;assert(k.bytes_read<=bytes);}
   k.fstat_after=stat(fs.fstatSync(fd,{bigint:true}));k.lstat_after=stat(fs.lstatSync(path,{bigint:true}));assert.deepEqual(k.fstat_after,k.lstat_before);assert.deepEqual(k.lstat_after,k.lstat_before);assert.equal(k.bytes_read,bytes);
  }finally{let closeFailure=null;if(fd!==null){try{fs.closeSync(fd);k.close_succeeded=true;}catch(e){k.close_error={name:e.name,message:e.message};closeFailure=e;}}const b=Buffer.concat(chunks);k.content=pin(b);k.partial_hex=b.toString('hex');if(closeFailure!==null)throw closeFailure;}
  assert(k.close_succeeded);assert.deepEqual(k.content,{bytes,sha256});sourceBytes.push(Buffer.concat(chunks));delete k.partial_hex;
 }
 // Only exact reviewed workspace source bytes become code. Body bytes do not.
 const adapter=await import('data:text/javascript;base64,'+sourceBytes[0].toString('base64'));
 const data=adapter.loadKpathseaData();
 if(data.status!=='ACCEPTED_KPATHSEA_BUFFER_ADAPTED_NO_ELF_INTERPRETATION'){output={status:'HOLD_ADAPTER',data,source_keys:sourceKeys,operation_permission:false};process.exitCode=1;}
 else{const composed=Buffer.concat([sourceBytes[1],sourceBytes[2]]),decoder=await import('data:text/javascript;base64,'+composed.toString('base64'));
  const result=decoder.decodeAcceptedKpathsea(data.body,data.priorRaw);output={result,authentication:data.authentication,source_keys:sourceKeys,composed_decoder_pin:pin(composed),operation_permission:false,installed_closure:false};
  if(result.status!=='LITERAL_KPATHSEA_SUPPLEMENT_WITH_EXPLICIT_HOLDS')process.exitCode=1;
 }
}catch(e){output={status:'HOLD_ENTRY_OR_SOURCE_FAILURE',error:{name:e.name,message:e.message},source_keys:sourceKeys,operation_permission:false,installed_closure:false};process.exitCode=1;}
process.stdout.write(JSON.stringify(output)+'\n');
