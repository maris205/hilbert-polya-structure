// Root source-accepted DATA adaptation only. No ELF/cache decoder import.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const P='docs/papers211_215_sequence/qa/p212_elf_cache_data_adapter_preparation01/load_inputs.proposed.mjs.txt';
assert.equal(process.cwd(),'/root/autodl-tmp/symbolic_dynamics');
assert.equal(process.argv.length,2);
const source=fs.readFileSync(P);
const pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
assert.equal(pin(source).sha256,'13ed33fcc3299c7b96bb427664cd7a48266a4235b50b107ea8d7b777e772ee52');
const {loadDecoderInputs}=await import('data:text/javascript;base64,'+source.toString('base64'));
const r=loadDecoderInputs();
const out={status:r.status,reason:r.reason??null,source_pin:pin(source),manifest_raw:r.manifestRaw?.toString('utf8')??null,manifest_pin:r.manifestPin??null,body_pins:(r.buffers??r.partial_buffers??[]).map(pin),authentication:r.authentication??null,failure_keys:r.fixed_input_keys??null,failure_read_counts:r.read_counts??null,original_full_buffers_retained_at_fixed_inputs:true,decoder_imported:false,elf_cache_interpreted:false,operation_permission:false,installed_closure:false};
process.stdout.write(JSON.stringify(out,null,2)+'\n');
if(r.status!=='SEVEN_ACCEPTED_BUFFERS_ADAPTED_NO_INTERPRETATION')process.exitCode=1;
