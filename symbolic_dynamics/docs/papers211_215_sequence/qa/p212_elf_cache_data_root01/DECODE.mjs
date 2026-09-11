// One root-authorized pure literal decoding of already received DATA.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
assert.equal(process.cwd(),'/root/autodl-tmp/symbolic_dynamics');
assert.equal(process.argv.length,2);
const Q='docs/papers211_215_sequence/qa/';
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
async function fixedModule(path,expected){const b=fs.readFileSync(path);assert.equal(pin(b).sha256,expected);return import('data:text/javascript;base64,'+b.toString('base64'));}
const {loadDecoderInputs}=await fixedModule(Q+'p212_elf_cache_data_adapter_preparation01/load_inputs.proposed.mjs.txt','13ed33fcc3299c7b96bb427664cd7a48266a4235b50b107ea8d7b777e772ee52');
const d=loadDecoderInputs();
assert.equal(d.status,'SEVEN_ACCEPTED_BUFFERS_ADAPTED_NO_INTERPRETATION',d.reason);
const trusted={bytes:4601,sha256:'648cf5dd0cb4a7883b0bff07a8cb8bd629bea17b1d683553288ef3c7ff3bf536'};
assert.deepEqual(pin(d.manifestRaw),trusted);assert.deepEqual(d.manifestPin,trusted);
const {decodeCapturedBodies}=await fixedModule(Q+'p212_elf_cache_data_decoder_source01/decode.v2.proposed.mjs.txt','24122a0fa7da0e38390bbdb8ba240279c166f1b3116a3c87f9a136c9791b1068');
const result=decodeCapturedBodies(d.buffers,d.manifestRaw,trusted);
process.stdout.write(JSON.stringify({result,manifest_pin:trusted,authentication:d.authentication,operation_permission:false,installed_closure:false})+'\n');
if(result.status!=='LITERAL_DATA_TABLE_WITH_EXPLICIT_HOLDS')process.exitCode=1;
