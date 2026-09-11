// Root-authorized finite DATA invocation. Never execute observer or host paths.
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const Q='docs/papers211_215_sequence/qa/',O=Q+'p212_eight_file_data_context_root01/',P=Q+'p212_eight_file_data_context_preparation01/',V=Q+'p212_eight_file_data_receiver_source01/',R=Q+'p212_minimal_contract01_file_observation_raw01/';
const read=p=>fs.readFileSync(p),pin=b=>({bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')});
assert.equal(process.cwd(),'/root/autodl-tmp/symbolic_dynamics');assert.equal(process.argv.length,2);
const source=read(V+'receive_data.v2.proposed.mjs.txt');assert.equal(pin(source).sha256,'fc1ece786bb81cf1046e766ec9223272db576ebc284eab0ad45f9d42198ab253');
const context=read(O+'CONTEXT.bound.json'),trustedPin=pin(context);
assert.equal(trustedPin.sha256,'b8dcf95d14b61f36a2a2bfc29f6c881476917e6701ee336d3f633809aec3fd2a');
const prospective=read(P+'CONTEXT.prospective.json');assert.equal(pin(prospective).sha256,'20745f1758ea43cf42841b819e1d638581298ac71f7e95b0cf56bed120600960');
const bound=JSON.parse(context),original=JSON.parse(prospective),receipt=read(O+'RECEPTION.md');
assert.equal(pin(receipt).sha256,'b2c12e6884596662187853885382aa0a7774c30309cffa4dc95cb39d4815710e');
assert.deepEqual(bound.root_original_projection_reception,{path:'/root/autodl-tmp/symbolic_dynamics/'+O+'RECEPTION.md',pin:pin(receipt)});
assert.deepEqual({...bound,root_original_projection_reception:null},original);
const stdout=read(R+'stdout.canonical.json'),stderr=read(R+'stderr.raw');
assert.equal(pin(stdout).sha256,'ecfe71cf8c7665d4e896791ec84f547a4a4ccee80d94ca5bfb6a6a8576f12feb');assert.equal(stderr.length,0);
// The only imported source is the fully source-reviewed pure consumer.
const {receiveData}=await import('data:text/javascript;base64,'+source.toString('base64'));
const result=receiveData(stdout,stderr,context,trustedPin);
const summary={status:result.status,reason:result.reason??null,counts:result.counts??null,request_input_pin:result.request_input_pin??null,source_pin:pin(source),context_pin:trustedPin,stdout_pin:pin(stdout),stderr_pin:pin(stderr),root_receipt_pin:pin(receipt),whole_context_delta_fields:['root_original_projection_reception'],whole_envelope_processed:!!result.envelope,original_raw_retained_in_place:true,full_result_embedding_omitted:'Envelope/evidence/retained Buffers are exact referenced inputs, not duplicated; this report is explicitly a projection.',operation_permission:false,installed_closure:false,host_queries:false,science_execution:false,external_status:'HOLD_EXTERNAL'};
process.stdout.write(JSON.stringify(summary,null,2)+'\n');
if(result.status!=='RECEIVED_EIGHT_FILE_DATA_ONLY')process.exitCode=1;
