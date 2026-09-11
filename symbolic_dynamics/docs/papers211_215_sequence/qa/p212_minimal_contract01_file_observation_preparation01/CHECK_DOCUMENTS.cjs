const fs = require("node:fs");
const crypto = require("node:crypto");
const FIELD_NAMES = ["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
let checks = 0, totalRead = 0;
const keys = [], buffers = new Map();
function need(test, label) { checks++; if (!test) throw new Error(label); }
function hash(buffer) { return crypto.createHash("sha256").update(buffer).digest("hex"); }
function fullStat(s) { return Object.fromEntries(FIELD_NAMES.map(k => [k, s[k].toString()])); }
function equal(a,b) { return JSON.stringify(a) === JSON.stringify(b); }
function fullRead(path) {
  need(ALLOWED.has(path), "OUTSIDE_FIXED_DOCUMENTARY_INPUT_SET");
  if (buffers.has(path)) return buffers.get(path);
  const record = {path, eof:false, byte_count:0, complete:false, closed:false};
  keys.push(record);
  let fd = null;
  try {
    const first = fs.lstatSync(path,{bigint:true});
    record.lstat_before = fullStat(first);
    need((first.mode & 0o170000n) === 0o100000n, "NONREGULAR_DOCUMENT");
    need(first.size >= 0n && first.size <= 16777216n, "DOCUMENT_SIZE_BOUND");
    fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW|fs.constants.O_NONBLOCK);
    record.fd_before = fullStat(fs.fstatSync(fd,{bigint:true}));
    need(equal(record.lstat_before,record.fd_before), "DOCUMENT_ENDPOINT_FD_BEFORE");
    const chunks = [], block = Buffer.alloc(65536);
    for (;;) {
      const count = fs.readSync(fd,block,0,block.length,null);
      need(Number.isInteger(count) && count >= 0 && count <= block.length, "READ_COUNT");
      if (count === 0) { record.eof = true; record.eof_zero_return = 0; break; }
      record.byte_count += count; totalRead += count;
      chunks.push(Buffer.from(block.subarray(0,count)));
      need(record.byte_count <= 16777216 && totalRead <= 67108864, "DOCUMENT_READ_BOUND");
    }
    record.fd_after = fullStat(fs.fstatSync(fd,{bigint:true}));
    record.lstat_after = fullStat(fs.lstatSync(path,{bigint:true}));
    need(equal(record.fd_before,record.fd_after), "DOCUMENT_SAME_FD_AFTER");
    need(equal(record.lstat_before,record.lstat_after), "DOCUMENT_ENDPOINT_AFTER");
    need(BigInt(record.byte_count) === first.size, "DOCUMENT_COMPLETE_SIZE");
    const buffer = Buffer.concat(chunks);
    need(buffer.length === record.byte_count, "DOCUMENT_CAPTURE_COUNT");
    record.sha256 = hash(buffer);
    fs.closeSync(fd); fd = null; record.closed = true;
    record.complete = true;
    buffers.set(path,buffer);
    return buffer;
  } catch (error) {
    record.failure = {name:error.name,code:error.code || null,message:error.message};
    throw error;
  } finally {
    if (fd !== null) {
      try { fs.closeSync(fd); record.closed = true; }
      catch (error) { record.close_failure = {name:error.name,code:error.code || null,message:error.message}; throw error; }
    }
  }
}
function pin(path) {
  const b = fullRead(path);
  return {path,bytes:b.length,sha256:hash(b)};
}

const INPUT_SPEC=[{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SHA256SUMS","sha256":"523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/ARCHIVAL_DISPOSITIONS.json","sha256":"886c14e841f3c2a7127699637e5d2a7f211d0fd103c1b09641006dfc7dea5f6e"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/BINDING.disabled.json","sha256":"1ee579b56e551dbadcf019a217ab1a194161019723fd4172be26db3b00a3dbd6"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_KEYS.json","sha256":"ec12e41a690ee44b4a5a1dcae3d3a59ba630e3dc2b09d2fb04cace2f93c71a95"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CLOSING_NATIVE.json","sha256":"2a28cb9ce721c2ce496d06dc0f4e2f0b6181e0c1becbf0be04e985c45fa96853"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/CONTRACT.md","sha256":"79393d2248d06859da5e972af8604cf3f356e996e12c4eefa49720da021eb193"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DEPENDENCY_GATE.md","sha256":"83c8083824976a78d87b6c4387fbf781af2779db39934babbbf8a94e3559c910"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DIRECTORY_REQUEST.disabled.json","sha256":"b27e00424c7f670347776e704be4e0e4d83df3b83c0a59ff79b2f1dc2ca68c73"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_CHECK01.json","sha256":"1bca0e8ff95b69acdf2f90ab7c558cac7c946f7ac368e18914c25ba846b772e3"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/DOCUMENTARY_NATIVE.json","sha256":"a6291de898e88cd843569d8569ba8d9be8b12a9075d2c5a968cf84699ad1c0aa"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/FILE_REQUEST.disabled.json","sha256":"c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/HANDOFF.md","sha256":"5646008e7943787cec097104c038959aae291292d6b5c656b53ec04854dd27bc"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/INPUTS.sha256","sha256":"8b272d0277e21d4be04f25fed9fb7635470f822c4b3e9ce96c2c79c64036d4f3"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/OBLIGATION_DELTA.md","sha256":"7ccc470b31a5903af44f6364484b1303284ab438d78c057e7e47176b2350e733"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/PRIMARY_SOURCE_EVIDENCE.json","sha256":"d8b6d4b371683d0429c8dd69b3403287f20b083a5105ac9635a75295b923cd32"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/REQUEST.disabled.json","sha256":"bdd262ecf3029d86c7e811d98f7a5d0bd1bbed9fcd73978e48a47f22b1d539d4"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/SOURCE_ORIGIN.md","sha256":"58ab8a9c8fe3dec8e16c35c3c97d430972549e5db70c61dcfd8d237686a236aa"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/capture.js","sha256":"c0369d9c6d0b623f59620884ef7b6252c9d99c98ff38a73168d0eba9733b8063"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/file_keys.mjs","sha256":"448b7a0c17ddc708fd14a9adb15beef5b5eb8b5081fd7480045b00c80973b896"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/receive.mjs","sha256":"adc0570ff23bece682812c77e69a2e8e7e9e1bcc64cba87c970e97f390202421"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/RECEPTION.md","sha256":"663fcfdaf3d0541acb3199f2bc31f0e55050f75b74480c025df97abbf78ac1f7"},{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/SHA256SUMS","sha256":"e2a1d505ebcaf7685a0e1f89cfe5f971514adb588265aefe0dab4bf3610a1c12"},{"path":"AGENTS.md","sha256":null},{"path":".agents/skills/symbolic-dynamics-research/SKILL.md","sha256":null},{"path":"docs/research_state/WORKFLOW.md","sha256":null}];
const OUTDIR="docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01";
const OWN_NAMES=["file_keys.proposed.mjs.txt","collect_files.proposed.mjs.txt","capture.proposed.sh.txt","FILE_REQUEST.proposed.json","DRAFT_ENTRY01.mjs.txt","ENTRY_REQUEST.proposed.json","SOURCE_DELTA.json","PINSET.json","INPUTS.sha256","CONTRACT.md","SOURCE_ORIGIN.md","HANDOFF.md","CHECK_DOCUMENTS.cjs","CLOSE.cjs","READ_NATIVE.json","CREATION_NATIVE.json"];
const PACK={"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01","lines":["886c14e841f3c2a7127699637e5d2a7f211d0fd103c1b09641006dfc7dea5f6e  ARCHIVAL_DISPOSITIONS.json","1ee579b56e551dbadcf019a217ab1a194161019723fd4172be26db3b00a3dbd6  BINDING.disabled.json","ec12e41a690ee44b4a5a1dcae3d3a59ba630e3dc2b09d2fb04cace2f93c71a95  CLOSING_KEYS.json","2a28cb9ce721c2ce496d06dc0f4e2f0b6181e0c1becbf0be04e985c45fa96853  CLOSING_NATIVE.json","79393d2248d06859da5e972af8604cf3f356e996e12c4eefa49720da021eb193  CONTRACT.md","83c8083824976a78d87b6c4387fbf781af2779db39934babbbf8a94e3559c910  DEPENDENCY_GATE.md","b27e00424c7f670347776e704be4e0e4d83df3b83c0a59ff79b2f1dc2ca68c73  DIRECTORY_REQUEST.disabled.json","1bca0e8ff95b69acdf2f90ab7c558cac7c946f7ac368e18914c25ba846b772e3  DOCUMENTARY_CHECK01.json","a6291de898e88cd843569d8569ba8d9be8b12a9075d2c5a968cf84699ad1c0aa  DOCUMENTARY_NATIVE.json","c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790  FILE_REQUEST.disabled.json","5646008e7943787cec097104c038959aae291292d6b5c656b53ec04854dd27bc  HANDOFF.md","8b272d0277e21d4be04f25fed9fb7635470f822c4b3e9ce96c2c79c64036d4f3  INPUTS.sha256","7ccc470b31a5903af44f6364484b1303284ab438d78c057e7e47176b2350e733  OBLIGATION_DELTA.md","d8b6d4b371683d0429c8dd69b3403287f20b083a5105ac9635a75295b923cd32  PRIMARY_SOURCE_EVIDENCE.json","bdd262ecf3029d86c7e811d98f7a5d0bd1bbed9fcd73978e48a47f22b1d539d4  REQUEST.disabled.json","58ab8a9c8fe3dec8e16c35c3c97d430972549e5db70c61dcfd8d237686a236aa  SOURCE_ORIGIN.md","c0369d9c6d0b623f59620884ef7b6252c9d99c98ff38a73168d0eba9733b8063  capture.js","448b7a0c17ddc708fd14a9adb15beef5b5eb8b5081fd7480045b00c80973b896  file_keys.mjs","adc0570ff23bece682812c77e69a2e8e7e9e1bcc64cba87c970e97f390202421  receive.mjs"],"sha256":"523e5f3c361a41fd36f8e25f16f03a8cdfd6fdcb035df20dd2eabfb9bafdff40"};
const EXPECTED_UPDATE="*** Update File: docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt\n@@\n-  } finally {\n-    record.raw_hex=Buffer.concat(chunks).toString('hex');\n-    record.content={bytes:record.bytes_read,sha256:digest.digest('hex')};\n-    if (fd!==null) {\n-      try { fs.closeSync(fd); record.close_succeeded=true; }\n-      catch(error) { record.close_succeeded=false; record.close_error=errorData(error); throw error; }\n-    }\n-  }\n+  } finally {\n+    let closeFailure=null;\n+    if (fd!==null) {\n+      try { fs.closeSync(fd); record.close_succeeded=true; }\n+      catch(error) { record.close_succeeded=false; record.close_error=errorData(error); closeFailure=error; }\n+    }\n+    record.raw_hex=Buffer.concat(chunks).toString('hex');\n+    record.content={bytes:record.bytes_read,sha256:digest.digest('hex')};\n+    if (closeFailure!==null) throw closeFailure;\n+  }\n@@\n-          need(d&&Object.hasOwn(d,'value'),'ENCODER_NO_ARRAY_ACCESSOR');\n+          need(d&&Object.prototype.hasOwnProperty.call(d,'value'),'ENCODER_NO_ARRAY_ACCESSOR');\n@@\n-          need(d&&Object.hasOwn(d,'value'),'ENCODER_NO_OBJECT_ACCESSOR');\n+          need(d&&Object.prototype.hasOwnProperty.call(d,'value'),'ENCODER_NO_OBJECT_ACCESSOR');\n@@\n-const diagnosticOnly = (label,error) => {\n+const diagnosticOnly = (label,error,priorError=null) => {\n@@\n-      phase,label,error:errorData(error),stdout_bytes_written:output.written,\n+      phase,label,error:errorData(error),prior_error:priorError===null?null:errorData(priorError),stdout_bytes_written:output.written,\n@@\n-    } catch(secondary) { diagnosticOnly('failure_envelope_incomplete',secondary); }\n+    } catch(secondary) { diagnosticOnly('failure_envelope_incomplete',secondary,error); }\n";
const EXPECTED_ENTRY={"schema":"p212-eight-file-prospective-entry-request-v1","status":"SOURCE_ONLY_DOCUMENTARY_PROPOSAL_NOT_SUBMITTED","operation_authorized":false,"request_cmd":null,"operation_request":null,"root_grant":null,"actual_native_request":null,"actual_native_result":null,"actual_session_id":null,"actual_continuations":null,"target_directory":null,"target_directory_key":null,"actual_destination_keys":null,"actual_bound_request":null,"actual_bound_request_key":null,"actual_input_keys":null,"independent_source_acceptance":null,"root_source_acceptance":null,"materialization_receipt":null,"new_observation_grant":null,"new_observation_grant_consumed":false,"actual_stdout":null,"actual_stderr":null,"actual_output_canonical_pin":null,"observation_accepted":false,"installed_closure_accepted":false,"operation_permission":false,"proposed_native_request":{"tool":"exec_command","arguments":{"cmd":"# Prospective eight-file key-tool capture BYTES ONLY; no current grant.\n# A separately received fresh owned 0700 destination must already exist.\numask 077\nset -o noclobber\nexec 3>'/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_raw01/stdout.canonical.json' || exit 78\nexec 4>'/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_raw01/stderr.raw' || exit 78\nexec node '/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/collect_files.mjs' 1>&3 2>&4 3>&- 4>&-\n","workdir":"/root/autodl-tmp/symbolic_dynamics","shell":"/bin/bash","login":false,"tty":false,"yield_time_ms":1000,"max_output_tokens":4000}},"proposed_continuation":{"tool":"write_stdin","arguments":{"session_id":null,"chars":"","yield_time_ms":10000,"max_output_tokens":4000},"may_submit_now":false,"session_binding":"Only the actual session of this exact separately granted key-tool native request; no guessed or borrowed handle.","rule":"Receive every original return to actual final completion. No second launch, stdin command, retry, kill, cleanup, or unsupported settlement inference."},"prospective_sources":[{"documentary_carrier":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/file_keys.proposed.mjs.txt","bytes":13660,"sha256":"957111a4a680f61cc94e89eb220b8c7c10d779e04eabd4734948690ef11b41f8","lines":189},"future_path":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/file_keys.mjs","actual_future_key":null},{"documentary_carrier":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt","bytes":13540,"sha256":"bd9baeb57f2387860a400f4b27e8acf9897da3843482cf856378f9807a2b2b87","lines":304},"future_path":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_enabled01/collect_files.mjs","actual_future_key":null},{"documentary_carrier":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/capture.proposed.sh.txt","bytes":638,"sha256":"11c0ac1540f30fa60cc691e7c42586918d4061d07aaca41d5b66a1329e3d30a4","lines":7},"future_path":null,"delivery":"Exact complete native cmd data; no separate capture-script path loader.","actual_future_key":null}],"proposed_bound_request":{"documentary_template":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/FILE_REQUEST.proposed.json","bytes":1979,"sha256":"c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790","lines":83},"future_path":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_binding01/FILE_REQUEST.json","actual_bytes":null,"actual_pin":null,"actual_nonself_before_key":null,"actual_nonself_after_key":null,"allowed_later_delta":["enabled","status","permission_receipt"],"required_later_values":{"enabled":"literal true only after separate source/materialization and fresh grant reception","status":"ROOT_BOUND_FINITE_FILES_ONLY","permission_receipt":"actual external newly granted eight-file observation receipt reference, not a source-acceptance receipt or an old consumed grant"},"other_fields":"Every other value, eight entry order/spelling/role/optionality/limit/expected-null field, total_byte_limit and settlement_receipt-null remain identical."},"proposed_target_directory":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_raw01","proposed_outputs":{"stdout":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_raw01/stdout.canonical.json","stderr":"/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_raw01/stderr.raw"},"future_path_queried":false,"future_path_materialized":false,"capture_prerequisites":["independent exact derivative/complete entry/serializer/capture/request reception","root original source reception","separately scoped exact enabled-module and actual bound-request materialization; nonself source/request keys outside the request","separately scoped fresh owned 0700 target-directory preparation and actual current preflight; no existing raw leaf may be overwritten","one fresh distinct eight-file observation grant consumed before this exact native submission"],"native_capture_rules":{"control_output":"Separate original native control output, never split into raw stdout/stderr or treated as the complete result; successful candidate requires it empty.","stdout":"Complete canonical JSON envelope in the exclusive named regular leaf, including the unmodified complete returned reader result and all its large hex/partial-failure rows.","stderr":"Separate exact raw file, including bootstrap/import/native diagnostics and bounded entry diagnostics; never merged with stdout.","completion":"Only genuine final completion of this actual native process/session supports closed-raw reception under the adopted ordinary key-tool bootstrap trust.","no_preview_acceptance":true,"no_automatic_retry":true},"exact_eight_candidates":[{"id":"BASH","path":"/bin/bash","role":"executable","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"ENV","path":"/usr/bin/env","role":"executable","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"KPSEWHICH","path":"/usr/bin/kpsewhich","role":"executable","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"LOADER_CANDIDATE","path":"/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2","role":"loader","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"LIBC_CANDIDATE","path":"/usr/lib/x86_64-linux-gnu/libc.so.6","role":"loader","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"TINFO_CANDIDATE","path":"/usr/lib/x86_64-linux-gnu/libtinfo.so.6.3","role":"loader","optional":false,"max_bytes":16777216,"capture_hex":true,"expected":null},{"id":"LOADER_CACHE","path":"/etc/ld.so.cache","role":"configuration","optional":true,"max_bytes":1048576,"capture_hex":true,"expected":null},{"id":"SYSTEM_PRELOAD","path":"/etc/ld.so.preload","role":"configuration","optional":true,"max_bytes":1048576,"capture_hex":true,"expected":null}],"purpose":"source_gate","total_byte_limit":102760448,"bounds":{"root_request_bytes":65536,"canonical_output_bytes":268435456,"entry_diagnostic_bytes":8388608,"value_nodes":8192,"value_depth":32,"string_piece_utf16_units":16384,"candidate_read_bytes_including_one_possible_overflow_sentinel":102760449,"candidate_hex_characters_including_one_possible_overflow_sentinel":205520898,"hard_memory_wall_time_storage_guarantee":false,"native_bootstrap_stderr_globally_capped":false},"later_reception":{"actual_complete_native_originals":null,"closed_stdout_key":null,"closed_stderr_key":null,"complete_canonical_parse_and_raw_bytes_received":false,"complete_reader_rows_received":false,"canonical_reencoding_raw_equal":null,"actual_semantic_receipt":null,"existing_receive_mjs_enabled":false,"old_closed_raw_file_request_compatible":false,"note":"This new up-to-256-MiB capture/envelope is not an old S0 raw result or old 128-MiB-file reader request. Any new DATA-only interpretation/receiver source needs its own gate; none is implemented or activated here."},"unchanged_holds":["B1","B2","B3","B4","remaining B5 enabled/request reception","B6","directory observations","help/version","S1-S6","paper/build/review/terminal"],"old_two_observation_grants":"remain consumed; neither is a new grant","directory_guard_enabled":false,"help_version_capture_enabled":false,"old_receiver_enabled":false,"root_key_tool_bootstrap_trust":"adopted explicitly by the cited root source reception; no recursive runtime observer","source_owner":"/root/round211_functional_surgery_residual/p213_literal_role_analysis","author_self_review":false,"external_status":"HOLD_EXTERNAL"};
const EXPECTED_DELTA={"schema":"p212-eight-file-source-delta-v1","status":"AUTHOR_SOURCE_ONLY_PROPOSAL","operation_authorized":false,"independent_review":null,"root_reception":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_root01/RECEPTION.md","bytes":10139,"sha256":"663fcfdaf3d0541acb3199f2bc31f0e55050f75b74480c025df97abbf78ac1f7","seal":"e2a1d505ebcaf7685a0e1f89cfe5f971514adb588265aefe0dab4bf3610a1c12"},"original_reader":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/file_keys.mjs","bytes":13630,"sha256":"448b7a0c17ddc708fd14a9adb15beef5b5eb8b5081fd7480045b00c80973b896"},"proposed_reader":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/file_keys.proposed.mjs.txt","bytes":13660,"sha256":"957111a4a680f61cc94e89eb220b8c7c10d779e04eabd4734948690ef11b41f8","lines":189},"reader_edits":[{"old_byte_offset":0,"old_text":"// SOURCE PROPOSAL ONLY. No CLI and no automatic call. Import is not authorized.","new_text":"// PROSPECTIVE FILE-ONLY SOURCE. No CLI or automatic call; import/observation still require separate authority."},{"old_byte_offset":277,"old_text":"  const SOURCE_ENABLED = false;","new_text":"  const SOURCE_ENABLED = true;"}],"unchanged_directory_suffix_starts":"// The only directory observations are the query cwd and three new capture\n","directory_guard_still_false":true,"other_original_source_bytes_unchanged":true,"original_file_request":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/FILE_REQUEST.disabled.json","bytes":1979,"sha256":"c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790"},"proposed_file_request":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/FILE_REQUEST.proposed.json","bytes":1979,"sha256":"c81d8d5e3fd5e4305c0871365832dca0256256ffd63a899686c236b0fb3df790","lines":83},"file_request_complete_bytes_unchanged":true,"complete_new_entry_source":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt","bytes":13540,"sha256":"bd9baeb57f2387860a400f4b27e8acf9897da3843482cf856378f9807a2b2b87","lines":304},"complete_new_capture_source":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/capture.proposed.sh.txt","bytes":638,"sha256":"11c0ac1540f30fa60cc691e7c42586918d4061d07aaca41d5b66a1329e3d30a4","lines":7},"entry_source_status":"New, separately reviewable source; not inherited source acceptance or executed code.","unexecuted_entry_draft":{"preserved_carrier":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/DRAFT_ENTRY01.mjs.txt","bytes":13332,"sha256":"df0f338786a9c9dfcbb0abfd84724891a4998d1b05deb57a19932f3b526a2563","lines":302},"current_carrier":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_file_observation_preparation01/collect_files.proposed.mjs.txt","bytes":13540,"sha256":"bd9baeb57f2387860a400f4b27e8acf9897da3843482cf856378f9807a2b2b87","lines":304},"changes":{"old_finally":"  } finally {\n    record.raw_hex=Buffer.concat(chunks).toString('hex');\n    record.content={bytes:record.bytes_read,sha256:digest.digest('hex')};\n    if (fd!==null) {\n      try { fs.closeSync(fd); record.close_succeeded=true; }\n      catch(error) { record.close_succeeded=false; record.close_error=errorData(error); throw error; }\n    }\n  }","new_finally":"  } finally {\n    let closeFailure=null;\n    if (fd!==null) {\n      try { fs.closeSync(fd); record.close_succeeded=true; }\n      catch(error) { record.close_succeeded=false; record.close_error=errorData(error); closeFailure=error; }\n    }\n    record.raw_hex=Buffer.concat(chunks).toString('hex');\n    record.content={bytes:record.bytes_read,sha256:digest.digest('hex')};\n    if (closeFailure!==null) throw closeFailure;\n  }","reason":"Unexecuted author draft only: close request fd before building receipt buffers; retain primary alongside secondary failure; use legacy hasOwnProperty builtin form. No failed runtime/test occurred."},"exact_text_replacements":[["const diagnosticOnly = (label,error) => {","const diagnosticOnly = (label,error,priorError=null) => {"],["phase,label,error:errorData(error),stdout_bytes_written:output.written,","phase,label,error:errorData(error),prior_error:priorError===null?null:errorData(priorError),stdout_bytes_written:output.written,"],["diagnosticOnly('failure_envelope_incomplete',secondary);","diagnosticOnly('failure_envelope_incomplete',secondary,error);"],["Object.hasOwn(d,'value')","Object.prototype.hasOwnProperty.call(d,'value')"]],"source_executed_or_tested":false,"not_an_operational_alternative":true},"canonical_format":"p212-ascii-canonical-json-v1: sorted own enumerable object keys, dense array order, null/boolean/safe integer (no -0), all string UTF-16 units outside printable ASCII excluding quote/backslash encoded as lower-case backslash-u plus four hex digits, one LF. Raw hex strings are retained without decoding or interpretation.","canonical_observation_output":null,"old_capture_source_unchanged":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/capture.js","bytes":8187,"sha256":"c0369d9c6d0b623f59620884ef7b6252c9d99c98ff38a73168d0eba9733b8063"},"old_receiver_source_unchanged":{"path":"docs/papers211_215_sequence/qa/p212_minimal_contract01_source_preparation01/receive.mjs","bytes":26753,"sha256":"adc0570ff23bece682812c77e69a2e8e7e9e1bcc64cba87c970e97f390202421"},"original_grants_and_failures":"All original source, raw failures and two consumed grants remain frozen; none is changed, reused, reopened or re-observed.","operation_or_future_path_action":false};
const ALLOWED=new Set([...INPUT_SPEC.map(x=>x.path),...OWN_NAMES.map(n=>OUTDIR+'/'+n)]);

const report={schema:"p212-eight-file-author-documentary-check-v1",status:"RUNNING",
 operation_authorized:false,independent_review:null,source_import_parse_ast_syntax_or_execution:false,
 host_or_future_observation:false,eight_file_observation_result:null};
function rawText(path) {
 const b=fullRead(path),t=b.toString("utf8");
 need(Buffer.from(t,"utf8").equals(b),"DOCUMENT_UTF8_REVERSIBLE"); return t;
}
function data(name) { return JSON.parse(rawText(OUTDIR+"/"+name)); }
function pinMatch(p) {
 const actual=pin(p.path);
 need(actual.bytes===p.bytes&&actual.sha256===p.sha256,"COMPLETE_DOCUMENT_PIN");
 if("lines" in p) need(rawText(p.path).split("\n").length-1===p.lines,"COMPLETE_SOURCE_LINE_COUNT");
}
function sameKey(old) {
 const now=keys.find(k=>k.path===old.path);
 need(now!==undefined,"PRIOR_KEY_IN_FIXED_SET");
 for(const field of ["eof","eof_zero_return","byte_count","complete","closed","sha256",
  "lstat_before","fd_before","fd_after","lstat_after"])
  need(equal(old[field],now[field]),"PRIOR_COMPLETE_KEY_UNCHANGED:"+field);
}
try {
 for(const expected of INPUT_SPEC) {
  const p=pin(expected.path);
  if(expected.sha256!==null) need(p.sha256===expected.sha256,"FROZEN_SELECTED_INPUT_PIN");
 }
 for(const name of OWN_NAMES) fullRead(OUTDIR+"/"+name);
 const oldManifest=PACK.lines.join("\n")+"\n";
 need(fullRead(PACK.path+"/SHA256SUMS").equals(Buffer.from(oldManifest)),"OLD_COMPLETE_MANIFEST_BYTES");
 need(equal(fs.readdirSync(PACK.path).sort(),["SHA256SUMS",...PACK.lines.map(l=>l.slice(66))].sort()),"OLD_COMPLETE_TWENTY_FILE_LAYOUT");
 need(equal(fs.readdirSync(OUTDIR).sort(),OWN_NAMES.slice().sort()),"PRECHECK_EXACT_SIXTEEN_FILE_LAYOUT");
 need(rawText(OUTDIR+"/INPUTS.sha256")===INPUT_SPEC.map(x=>hash(fullRead(x.path))+"  "+x.path+"\n").join(""),"WHOLE_INPUT_MANIFEST");
 const pins=data("PINSET.json"),entry=data("ENTRY_REQUEST.proposed.json"),delta=data("SOURCE_DELTA.json");
 need(equal(entry,EXPECTED_ENTRY),"COMPLETE_EXPECTED_ENTRY_DOCUMENT");
 need(equal(delta,EXPECTED_DELTA),"COMPLETE_EXPECTED_SOURCE_DELTA_DOCUMENT");
 for(const p of pins.documents) pinMatch(p);
 need(pins.documents.length===7,"SEVEN_CURRENT_CORE_PINS");
 for(const p of [delta.root_reception,delta.original_reader,delta.proposed_reader,
 delta.original_file_request,delta.proposed_file_request,delta.complete_new_entry_source,
 delta.complete_new_capture_source,delta.unexecuted_entry_draft.preserved_carrier,
 delta.unexecuted_entry_draft.current_carrier,delta.old_capture_source_unchanged,
 delta.old_receiver_source_unchanged]) pinMatch(p);
 need(hash(fullRead(INPUT_SPEC[21].path))===delta.root_reception.seal,"WHOLE_ROOT_SEAL_PIN");
 const old=fullRead(delta.original_reader.path),now=fullRead(delta.proposed_reader.path);
 let cursor=0; const pieces=[];
 for(const e of delta.reader_edits) {
  const from=Buffer.from(e.old_text),to=Buffer.from(e.new_text);
  need(Number.isInteger(e.old_byte_offset)&&e.old_byte_offset>=cursor,"ORDERED_EXACT_READER_EDITS");
  need(old.subarray(e.old_byte_offset,e.old_byte_offset+from.length).equals(from),"OLD_READER_EDIT_BYTES");
  pieces.push(old.subarray(cursor,e.old_byte_offset),to);cursor=e.old_byte_offset+from.length;
 }
 pieces.push(old.subarray(cursor));
 need(Buffer.concat(pieces).equals(now),"EXACT_TWO_READER_EDITS_ALL_OTHER_BYTES_UNCHANGED");
 const marker=Buffer.from(delta.unchanged_directory_suffix_starts);
 const oi=old.indexOf(marker),ni=now.indexOf(marker);
 need(oi>=0&&ni>=0&&old.subarray(oi).equals(now.subarray(ni)),"ENTIRE_DIRECTORY_SUFFIX_RAW_IDENTICAL");
 need(now.subarray(ni).includes(Buffer.from("const SOURCE_ENABLED = false;")),"DIRECTORY_GUARD_FALSE");
 const requestRaw=fullRead(delta.proposed_file_request.path);
 need(requestRaw.equals(fullRead(delta.original_file_request.path)),"ENTIRE_FILE_REQUEST_RAW_IDENTICAL");
 const template=JSON.parse(requestRaw.toString("utf8"));
 need(template.enabled===false&&template.permission_receipt===null&&template.settlement_receipt===null,"TEMPLATE_NOT_AUTHORITY");
 need(template.entries.length===8&&equal(template.entries,entry.exact_eight_candidates),"ALL_EIGHT_LITERAL_ROWS_UNCHANGED");
 need(template.entries.every(x=>x.expected===null&&x.capture_hex===true),"NO_EXPECTED_KEY_FABRICATION");
 need(template.total_byte_limit===102760448&&entry.total_byte_limit===template.total_byte_limit,"UNCHANGED_FINITE_TOTAL");
 const source=rawText(delta.complete_new_entry_source.path),draft=rawText(delta.unexecuted_entry_draft.preserved_carrier.path);
 let derived=draft.replace(delta.unexecuted_entry_draft.changes.old_finally,delta.unexecuted_entry_draft.changes.new_finally);
 need(derived!==draft,"DRAFT_FINALLY_PRESENT");
 for(const [a,b] of delta.unexecuted_entry_draft.exact_text_replacements) {
  need(derived.includes(a),"DRAFT_REPLACEMENT_PRESENT");derived=derived.split(a).join(b);
 }
 need(Buffer.from(derived).equals(fullRead(delta.complete_new_entry_source.path)),"WHOLE_DRAFT_TO_CURRENT_SOURCE_BYTES");
 need(source.includes("const TEMPLATE = "+JSON.stringify(template,null,2)+";"),"INLINE_WHOLE_JSON_TEMPLATE_TEXT");
 need(source.includes("const REQUEST_PATH = "+JSON.stringify(entry.proposed_bound_request.future_path)+";"),"LITERAL_REQUEST_SOURCE_PATH_AS_DATA");
 need(source.split("readerResult=collectP212S0Files(request);").length===2,"ONE_TEXTUAL_READER_CALL_SITE");
 const capture=fullRead(delta.complete_new_capture_source.path);
 const command=Buffer.from(entry.proposed_native_request.arguments.cmd);
 need(command.equals(capture),"WHOLE_NATIVE_COMMAND_CAPTURE_BYTES");
 need(equal(pins.complete_native_cmd,{bytes:command.length,sha256:hash(command)}),"WHOLE_NATIVE_COMMAND_PIN");
 need(command.toString("utf8").split("\n").length-1===7,"SEVEN_CAPTURE_LINES");
 for(const line of ["umask 077\n","set -o noclobber\n",
  "exec 3>'"+entry.proposed_outputs.stdout+"' || exit 78\n",
  "exec 4>'"+entry.proposed_outputs.stderr+"' || exit 78\n",
  "exec node '"+entry.prospective_sources[1].future_path+"' 1>&3 2>&4 3>&- 4>&-\n"])
  need(command.includes(Buffer.from(line)),"EXACT_CAPTURE_LITERAL_LINE");
 for(const p of entry.prospective_sources) {
  pinMatch(p.documentary_carrier);need(p.actual_future_key===null,"NO_FUTURE_SOURCE_KEY");
 }
 for(const name of ["request_cmd","operation_request","root_grant","actual_native_request",
 "actual_native_result","actual_session_id","actual_continuations","target_directory",
 "target_directory_key","actual_destination_keys","actual_bound_request","actual_bound_request_key",
 "actual_input_keys","independent_source_acceptance","root_source_acceptance","materialization_receipt",
 "new_observation_grant","actual_stdout","actual_stderr","actual_output_canonical_pin"])
  need(entry[name]===null,"ACTUAL_OPERATION_ROLE_STILL_NULL:"+name);
 for(const name of ["operation_authorized","new_observation_grant_consumed","observation_accepted",
 "installed_closure_accepted","operation_permission","future_path_queried","future_path_materialized",
 "directory_guard_enabled","help_version_capture_enabled","old_receiver_enabled","author_self_review"])
  need(entry[name]===false,"OPERATION_AND_ACCEPTANCE_STILL_FALSE:"+name);
 const clauses=[
 "const REQUEST_BYTE_LIMIT = 65536;","const OUTPUT_BYTE_LIMIT = 268435456;",
 "const DIAGNOSTIC_BYTE_LIMIT = 8388608;","const MAX_VALUE_NODES = 8192;",
 "const MAX_VALUE_DEPTH = 32;","at+=16384","Object.keys(value).sort()",
 "Object.getOwnPropertyDescriptor(value,name)","Object.prototype.hasOwnProperty.call(d,'value')",
 "Number.isSafeInteger(value)&&!Object.is(value,-0)","ENCODER_DATA_ONLY_NO_CYCLE",
 "ENCODER_DENSE_ARRAY","ENCODER_NO_ARRAY_ACCESSOR","ENCODER_NO_OBJECT_ACCESSOR",
 "ENCODER_PLAIN_DATA_OBJECT","OUTPUT_POSITIVE_WRITE_PROGRESS",
 "OUTPUT_BYTE_BOUND_PARTIAL_PRESERVED","OUTPUT_SAME_DESCRIPTOR_IDENTITY",
 "OUTPUT_SIZE_EQUALS_ACTUAL_WRITES","request_input:requestInput","reader_result:readerResult",
 "FAILED_ENTRY_OR_UNRETURNED_READER","failure_envelope_incomplete","prior_error:",
 "fs.closeSync(1)","stdout_close_failure","process.exitCode=exitCode",
 "readerResult.status==='OBSERVED_ROOT_RECEPTION_PENDING'?0:78",
 "const withoutActivation={...request,enabled:false,status:TEMPLATE.status,permission_receipt:null};",
 "EXACT_EIGHT_UNCHANGED_CANDIDATES_AND_LIMITS","REQUEST_OVERFLOW_SENTINEL_PRESERVED"];
 for(const c of clauses) need(source.includes(c),"REQUIRED_DOCUMENTARY_SOURCE_CLAUSE:"+c);
 need(entry.bounds.candidate_hex_characters_including_one_possible_overflow_sentinel===2*(template.total_byte_limit+1),"DOCUMENTED_HEX_BOUND_ARITHMETIC");
 need(entry.bounds.hard_memory_wall_time_storage_guarantee===false&&entry.bounds.native_bootstrap_stderr_globally_capped===false,"NO_UNSUPPORTED_GLOBAL_RESOURCE_GUARANTEE");
 need(entry.later_reception.old_closed_raw_file_request_compatible===false&&entry.later_reception.existing_receive_mjs_enabled===false,"OLD_RECEIVER_REMAINS_DISABLED_INCOMPATIBLE");
 const reads=data("READ_NATIVE.json");
 need(reads.events.length===20&&reads.cutoff_last_chunk_id==="7b6a29","FINITE_NATIVE_READ_CUTOFF");
 for(const event of reads.events) {
  need(event.tool==="exec_command"&&event.result.exit_code===0&&!event.result.session_id,"ACTUAL_COMPLETED_DOCUMENTARY_NATIVE");
  need(typeof event.result.output==="string"&&!event.result.output.includes("Warning: truncated output"),"RETAINED_NATIVE_NOT_RECONSTRUCTED_PREVIEW");
 }
 const textSlices=[
 ["e1b001",INPUT_SPEC[23].path,1,200],["5e3dcb",INPUT_SPEC[24].path,1,160],
 ["3366c6",INPUT_SPEC[20].path,1,260],["713550",INPUT_SPEC[21].path,1,260],
 ["5c8eac",delta.original_reader.path,1,260],["178f5c",delta.original_file_request.path,1,260],
 ["9c404c",PACK.path+"/CONTRACT.md",1,320],["b46ea2",PACK.path+"/OBLIGATION_DELTA.md",1,320],
 ["44b268",PACK.path+"/DEPENDENCY_GATE.md",1,320],["8f8986",PACK.path+"/SHA256SUMS",1,320],
 ["21346f",delta.complete_new_entry_source.path,1,165],["ce0fc7",delta.complete_new_entry_source.path,166,330],
 ["e688e5",delta.complete_new_capture_source.path,1,30],["9924d7",INPUT_SPEC[22].path,1,200]];
 for(const [id,path,start,end] of textSlices) {
  const event=reads.events.find(e=>e.result.chunk_id===id);need(!!event,"ACTUAL_READ_CHUNK_FOUND");
  const lines=rawText(path).match(/[^\n]*\n|[^\n]+$/g)||[];
  need(Buffer.from(event.result.output).equals(Buffer.from(lines.slice(start-1,end).join(""))),"WHOLE_NATIVE_SLICE_RAW_EQUAL:"+id);
 }
 const transferred=JSON.parse(reads.events.find(e=>e.result.chunk_id==="792911").result.output);
 need(transferred.length===2,"WHOLE_ORIGINAL_SOURCE_TRANSFER");
 for(const item of transferred) need(Buffer.from(item.text).equals(fullRead(item.path))&&Buffer.byteLength(item.text)===item.bytes,"WHOLE_SOURCE_TRANSFER_RAW_EQUAL");
 const intake=JSON.parse(reads.events.find(e=>e.result.chunk_id==="7b6a29").result.output);
 need(intake.status==="PASS_DOCUMENTARY_INPUT_BYTES_ONLY"&&intake.key_count===32&&intake.checks===437&&intake.total_read_bytes===1404071,"ACTUAL_PRIOR_INTAKE_ORIGINAL");
 for(const k of intake.keys) sameKey(k);
 const created=data("CREATION_NATIVE.json");
 need(created.events.length===4,"FOUR_ACTUAL_PATCH_EVENTS");
 const addBodies=[],updates=[];
 for(const [index,event] of created.events.entries()) {
  need(event.tool==="apply_patch"&&typeof event.request==="string","WHOLE_ACTUAL_CREATION_REQUEST");
  const lines=event.request.split("\n");
  need(lines[0]==="*** Begin Patch","NATIVE_PATCH_BEGIN");
  let at=1;
  while(at<lines.length&&lines[at]!=="*** End Patch") {
   if(lines[at].startsWith("*** Add File: ")) {
    const path=lines[at].slice(14);at++;const body=[];
    while(at<lines.length&&!lines[at].startsWith("*** ")) { need(lines[at].startsWith("+"),"ADD_BODY_LINES");body.push(lines[at].slice(1));at++; }
    const target=index===0&&path===delta.complete_new_entry_source.path?delta.unexecuted_entry_draft.preserved_carrier.path:path;
    need(ALLOWED.has(target)&&target.startsWith(OUTDIR+"/"),"CREATION_BODY_FIXED_OWN_TARGET");
    need(Buffer.from(body.join("\n")+"\n").equals(fullRead(target)),"WHOLE_ADD_BODY_CURRENT_OR_EXPLICIT_DRAFT_RAW_EQUAL");
    addBodies.push({event_index:index,created_path:path,received_against:target,bytes:Buffer.byteLength(body.join("\n")+"\n")});
   } else if(lines[at].startsWith("*** Update File: ")) {
    const from=at;
    do { at++; } while(at<lines.length&&!lines[at].startsWith("*** "));
    const block=lines.slice(from,at).join("\n")+"\n";
    need(index===1&&block===EXPECTED_UPDATE,"WHOLE_EXACT_DECLARED_NATIVE_UPDATE");
    updates.push({event_index:index,path:delta.complete_new_entry_source.path,complete_update_bytes:Buffer.byteLength(block)});
   } else throw new Error("UNEXPECTED_CREATION_DIRECTIVE");
  }
  need(lines[at]==="*** End Patch","NATIVE_PATCH_END");
 }
 need(addBodies.length===14&&updates.length===1,"COMPLETE_STATIC_ADDITION_AND_ONE_DRAFT_UPDATE_CENSUS");
 const distinct=[...new Set(addBodies.map(x=>x.created_path))].sort();
 need(equal(distinct,OWN_NAMES.filter(x=>!["READ_NATIVE.json","CREATION_NATIVE.json"].includes(x)).map(x=>OUTDIR+"/"+x).sort()),"ALL_FOURTEEN_STATIC_CURRENT_PAYLOAD_BODIES");
 report.original_package={payloads:19,files:20,seal:PACK.sha256};
 report.selected_inputs=INPUT_SPEC.map(x=>pin(x.path));
 report.source_pins=pins.documents;report.command_pin=pins.complete_native_cmd;
 report.source_delta={exact_reader_edits:2,entire_directory_suffix_unchanged:true,unchanged_eight_file_request:true,
  full_entry_and_capture_as_data:true,unexecuted_draft_received:true,complete_new_source_tested:false};
 report.native_evidence={read_events:reads.events.length,complete_source_slices_compared:textSlices.length,
  prior_full_keys_unchanged:intake.keys.length,creation_events:created.events.length,add_bodies:addBodies,updates,
  cutoff_is_nonself:true};
 report.status="PASS_DOCUMENTARY_SOURCE_CONSISTENCY_ONLY";
} catch(error) {
 report.status="FAIL_DOCUMENTARY_SOURCE_CONSISTENCY_ONLY";
 report.failure={name:error.name,code:error.code||null,message:error.message};process.exitCode=1;
}
report.checks=checks;report.key_count=keys.length;report.total_read_bytes=totalRead;report.keys=keys;
process.stdout.write(JSON.stringify(report,null,2)+"\n");
