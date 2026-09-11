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

function compareTree(actual,expected,label) {
  need(typeof actual === typeof expected,label+":TYPE");
  if (expected === null || typeof expected !== "object") { need(actual === expected,label+":VALUE"); return; }
  need(Array.isArray(actual) === Array.isArray(expected),label+":ARRAY");
  need(equal(Object.keys(actual),Object.keys(expected)),label+":KEYS");
  for (const key of Object.keys(expected)) compareTree(actual[key],expected[key],label+"."+key);
}

const OUTDIR = "docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01";
const INPUTS = [{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/SHA256SUMS","bytes":680,"sha256":"8071e2eaddbe6a01bccca9d0cd63bee96af9b44e8b11d97b43e905eb5ce35cbf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CHECK_NATIVE.json","bytes":35085,"sha256":"516b77a6a153eb8b99f0bb33dfcf8013408bbecfbc78022a9483f1f978198453"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CHECK_ROOT.cjs","bytes":13098,"sha256":"7141eb93c24d58a8a46926b5e326dc596205ad0a77afc235cb082e1f82621617"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CLOSE.cjs","bytes":2582,"sha256":"e5cc40fb24c599c984538ae042be0cb04123be1a33d59eaef66a94a120aa5a57"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/CLOSING_NATIVE.json","bytes":24511,"sha256":"41bbbd0858323ae235e5d2f2c8c4a911a849781ed7b23fd0ab010123d6807c59"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/RECEPTION.md","bytes":7455,"sha256":"de2892a93661d177f78bacbb4c15904a7e33d88d509fe96eb38c3e23ae03b5df"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_AUDIT_READS_NATIVE.json","bytes":45877,"sha256":"cc3dee08b507b49683b07008ae757330c5fac7401dde0744f8caae16502ef4ee"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_READS_NATIVE.json","bytes":281328,"sha256":"533f58d1e7484f39f76b8614a581930618fa95f7e8a16266e2860edd22325f36"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01/ROOT_REPLAY_NATIVE.json","bytes":73429,"sha256":"4b8e1febb3a3b53f90a1e122e1562b228beb9b3aee3b70cacfa76c5f90287177"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SHA256SUMS","bytes":1508,"sha256":"ef1e95d740634c6531706aaa3b4fda0f0f99fbb14f604c80bc24f3d3235a7cdf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/BINDING.proposed.json","bytes":66395,"sha256":"78da1d06c05cd6244e9de9c1565a843823051e98c8702c07c5447e20d1da3ab6"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CHECK_NATIVE.json","bytes":96548,"sha256":"6253a4dc5318adcfde9592fe8fcc7eca6ea9354e0ececea1f3cd70c288f12a52"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/COLLECTOR_REUSE_CHECK.json","bytes":3302,"sha256":"162a054e1f0f3e4ac0cf34f01cfbe214ea6e7fc7c04a637f5aa9879a55a835be"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/CREATION_NATIVE.json","bytes":1252,"sha256":"a0e9a260565255dd231c28a8f092bf1ed4f259e5f745e3a4395b7849bcca4c86"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/DEPENDENCY_CONTRACT.md","bytes":11195,"sha256":"c52d389d4bbcf944905b241a6c8ef14b23082362f9f003848f143b8ef2dbb307"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/EXECUTION_SEQUENCE.md","bytes":5079,"sha256":"3c35cab1996c0207755755323ccc3b508ed4f86e6c9b35e5c4483e6b4b908c11"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/HANDOFF.md","bytes":5367,"sha256":"ac9290b2eb34fc02445dcc42493783a1c4013f9eba0cc30e0c849d41976697db"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/PREPARATION.md","bytes":7820,"sha256":"1268b6f5b2c0da7dca2b460782e7a26637065c63fc0125217612dad3b55b9f3a"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/REQUEST.disabled.json","bytes":5909,"sha256":"d7e01fe79599289d3a05538ffca2b896eff960dff35d5659a58caee5b4f68b17"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_DELTA.md","bytes":4991,"sha256":"0cc248fc9a1e6640cae462ed398aed78a2d1f934168816f93f19158996602b5c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_INPUTS.sha256","bytes":2291,"sha256":"33767cd63ab4c5b7f44669dee5ebdc7f60ec9563536ac4d01b05df0f06fac41d"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/SOURCE_TEXT_READS_NATIVE.json","bytes":226946,"sha256":"51b9e15d5d7e59064d63c99c35994af4d95ff10b9ae3f908558b02a834d3126a"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/WORKSPACE_READS_NATIVE.json","bytes":316289,"sha256":"d395e20dab0f0d0cce5e538ef2b487c7bcc517e9811e0f541b3d2a27a8075bd5"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.initial.disabled.sh","bytes":1759,"sha256":"d16d681d44f95784d15d26929a3fddd5a3775c48a5e032759bef52c61679614c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay01.disabled.sh","bytes":1762,"sha256":"35a9af07787bf526b64aeedee2a67f64959f4e2deab68c800798d1bb557f4500"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay02.disabled.sh","bytes":1762,"sha256":"d3a223d9b73ef0c2813f5fe451320eb50bb31418e7ca52f42cc0cdeab3115888"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/run_science.disabled.py","bytes":108770,"sha256":"2dcc96f6540e3caa5078f7cd9d92b307fea2a62e069415a50e333367e91ca7a9"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/SHA256SUMS","bytes":999,"sha256":"27890badfbebbac1db8ddb4046d98c847555c7cc62995253b1ebf23064c10dcf"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/AUDIT.md","bytes":15311,"sha256":"7d5c2ba9f62a312aeae3f424ba0e0f67df5d1310c602a63bc87a09a9c89a727d"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_FAILURE01_NATIVE.json","bytes":75893,"sha256":"8d13c7e9a9fa75cbded5c522d8c0f1068c219642f39aae8cab66b35b4fbde3f4"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_NATIVE.json","bytes":94152,"sha256":"e9a8bfb78c2e1085b58bac95897c03d496a5dc4825c03e8ba7a7dfcf7acd1961"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_SOURCE.cjs","bytes":16426,"sha256":"590b405446c40e2a62fbfb221812f623b1f79f9a4be11031323a9481bcb02e84"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CHECK_SOURCE_FAILURE01.cjs.txt","bytes":16096,"sha256":"64425b259e98c3a52a3aa9292d9478cb5b4dcc457a28147725a21af4dcfe2697"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CLOSE_DOCUMENTS.cjs","bytes":5944,"sha256":"0da72837e055433d6b71e10a66487282b20a5566a04b59a763b401718ff16d85"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/CLOSURE_NATIVE.json","bytes":21543,"sha256":"ed23eb46ef5a6fdd83252369885dec5537d4fcf4cc3fbdad9a6ab41988c01fb4"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/FINDINGS.json","bytes":2209,"sha256":"737f3dc9824c7a051090f892a4cb0a7639bc27d2b423debcb06fe314a2d29721"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/HANDOFF.md","bytes":2194,"sha256":"2fb72a401702047ec1a71be139da66808fb292ddaabcf84c42c58be5770e4e4c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/INPUTS.sha256","bytes":5064,"sha256":"aa17440c2339ce843b633fc980cfed47066406d75ef777b43ae0792b62032290"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/PLAN.md","bytes":1544,"sha256":"d20c8514bc403dd6e9e4e9ea47afb85adb9e9afdffaaa30673232b5c4db3e804"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01/READ_NATIVE.json","bytes":697287,"sha256":"cb64667cab5767e08d7609443c7bf84753215c70f2afaed5e57009930e211ab7"},{"path":"papers/213-receiver-limited-cyclic-transfer/verify.py","bytes":17539,"sha256":"a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812"},{"path":"papers/213-receiver-limited-cyclic-transfer/VERIFICATION_PARAMETERS.json","bytes":1452,"sha256":"7454c9462903bc305a43438004f362317ae3b2cad514674d72a945519fb338df"},{"path":"papers/213-receiver-limited-cyclic-transfer/OUTPUT_SCHEMA.md","bytes":6947,"sha256":"c0ff52c4705de83f59ca858cb82e21a679da918b906e7d2698b3d7aad92fef6b"},{"path":"papers/213-receiver-limited-cyclic-transfer/SCIENTIFIC_DEPENDENCIES.md","bytes":3340,"sha256":"d4e70a87586e6f09ff126e2bb91b11142f9b89c77169ec63279d990ff5e38984"},{"path":"papers/213-receiver-limited-cyclic-transfer/RUNTIME_PLAN.md","bytes":4430,"sha256":"65751565f6165af8187fe4eb456646b1e82fb8fc12b635902c034b54c2f129d8"},{"path":"papers/213-receiver-limited-cyclic-transfer/REVIEW_INTERFACES.md","bytes":2532,"sha256":"6e9568c69e70229c90769448f5bb4735a992783e91fa9e139a879f4196d0bd52"},{"path":".agents/skills/symbolic-dynamics-research/SKILL.md","bytes":1596,"sha256":"1af30c2095702a0cc722e87389c8d515a4d668b22e85af25edb2fce02c10d22d"},{"path":"docs/research_state/WORKFLOW.md","bytes":6861,"sha256":"dd6c109a695d8774b3dacff5fa9d76d28aa5e72e99b33c4abe0ac7afb1a26324"},{"path":"AGENTS.md","bytes":1618,"sha256":"bbc2d46f26aa43474f9f09fbffd93f6f4faf29982c1ffae2ece18b1fa48fbd35"}];
const GROUPS = [{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_root01","sha256":"8071e2eaddbe6a01bccca9d0cd63bee96af9b44e8b11d97b43e905eb5ce35cbf","lines":["516b77a6a153eb8b99f0bb33dfcf8013408bbecfbc78022a9483f1f978198453  CHECK_NATIVE.json","7141eb93c24d58a8a46926b5e326dc596205ad0a77afc235cb082e1f82621617  CHECK_ROOT.cjs","e5cc40fb24c599c984538ae042be0cb04123be1a33d59eaef66a94a120aa5a57  CLOSE.cjs","41bbbd0858323ae235e5d2f2c8c4a911a849781ed7b23fd0ab010123d6807c59  CLOSING_NATIVE.json","de2892a93661d177f78bacbb4c15904a7e33d88d509fe96eb38c3e23ae03b5df  RECEPTION.md","cc3dee08b507b49683b07008ae757330c5fac7401dde0744f8caae16502ef4ee  ROOT_AUDIT_READS_NATIVE.json","533f58d1e7484f39f76b8614a581930618fa95f7e8a16266e2860edd22325f36  ROOT_READS_NATIVE.json","4b8e1febb3a3b53f90a1e122e1562b228beb9b3aee3b70cacfa76c5f90287177  ROOT_REPLAY_NATIVE.json"]},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01","sha256":"ef1e95d740634c6531706aaa3b4fda0f0f99fbb14f604c80bc24f3d3235a7cdf","lines":["78da1d06c05cd6244e9de9c1565a843823051e98c8702c07c5447e20d1da3ab6  BINDING.proposed.json","6253a4dc5318adcfde9592fe8fcc7eca6ea9354e0ececea1f3cd70c288f12a52  CHECK_NATIVE.json","162a054e1f0f3e4ac0cf34f01cfbe214ea6e7fc7c04a637f5aa9879a55a835be  COLLECTOR_REUSE_CHECK.json","a0e9a260565255dd231c28a8f092bf1ed4f259e5f745e3a4395b7849bcca4c86  CREATION_NATIVE.json","c52d389d4bbcf944905b241a6c8ef14b23082362f9f003848f143b8ef2dbb307  DEPENDENCY_CONTRACT.md","3c35cab1996c0207755755323ccc3b508ed4f86e6c9b35e5c4483e6b4b908c11  EXECUTION_SEQUENCE.md","ac9290b2eb34fc02445dcc42493783a1c4013f9eba0cc30e0c849d41976697db  HANDOFF.md","1268b6f5b2c0da7dca2b460782e7a26637065c63fc0125217612dad3b55b9f3a  PREPARATION.md","d7e01fe79599289d3a05538ffca2b896eff960dff35d5659a58caee5b4f68b17  REQUEST.disabled.json","0cc248fc9a1e6640cae462ed398aed78a2d1f934168816f93f19158996602b5c  SOURCE_DELTA.md","33767cd63ab4c5b7f44669dee5ebdc7f60ec9563536ac4d01b05df0f06fac41d  SOURCE_INPUTS.sha256","51b9e15d5d7e59064d63c99c35994af4d95ff10b9ae3f908558b02a834d3126a  SOURCE_TEXT_READS_NATIVE.json","d395e20dab0f0d0cce5e538ef2b487c7bcc517e9811e0f541b3d2a27a8075bd5  WORKSPACE_READS_NATIVE.json","d16d681d44f95784d15d26929a3fddd5a3775c48a5e032759bef52c61679614c  capture.initial.disabled.sh","35a9af07787bf526b64aeedee2a67f64959f4e2deab68c800798d1bb557f4500  capture.replay01.disabled.sh","d3a223d9b73ef0c2813f5fe451320eb50bb31418e7ca52f42cc0cdeab3115888  capture.replay02.disabled.sh","2dcc96f6540e3caa5078f7cd9d92b307fea2a62e069415a50e333367e91ca7a9  run_science.disabled.py"]},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_source_audit01","sha256":"27890badfbebbac1db8ddb4046d98c847555c7cc62995253b1ebf23064c10dcf","lines":["7d5c2ba9f62a312aeae3f424ba0e0f67df5d1310c602a63bc87a09a9c89a727d  AUDIT.md","8d13c7e9a9fa75cbded5c522d8c0f1068c219642f39aae8cab66b35b4fbde3f4  CHECK_FAILURE01_NATIVE.json","e9a8bfb78c2e1085b58bac95897c03d496a5dc4825c03e8ba7a7dfcf7acd1961  CHECK_NATIVE.json","590b405446c40e2a62fbfb221812f623b1f79f9a4be11031323a9481bcb02e84  CHECK_SOURCE.cjs","64425b259e98c3a52a3aa9292d9478cb5b4dcc457a28147725a21af4dcfe2697  CHECK_SOURCE_FAILURE01.cjs.txt","0da72837e055433d6b71e10a66487282b20a5566a04b59a763b401718ff16d85  CLOSE_DOCUMENTS.cjs","ed23eb46ef5a6fdd83252369885dec5537d4fcf4cc3fbdad9a6ab41988c01fb4  CLOSURE_NATIVE.json","737f3dc9824c7a051090f892a4cb0a7639bc27d2b423debcb06fe314a2d29721  FINDINGS.json","2fb72a401702047ec1a71be139da66808fb292ddaabcf84c42c58be5770e4e4c  HANDOFF.md","aa17440c2339ce843b633fc980cfed47066406d75ef777b43ae0792b62032290  INPUTS.sha256","d20c8514bc403dd6e9e4e9ea47afb85adb9e9afdffaaa30673232b5c4db3e804  PLAN.md","cb64667cab5767e08d7609443c7bf84753215c70f2afaed5e57009930e211ab7  READ_NATIVE.json"]}];

const CORE_NAMES = ["run_science.proposed.py.txt","capture.initial.proposed.sh.txt","capture.replay01.proposed.sh.txt","capture.replay02.proposed.sh.txt","REQUEST.initial.proposed.json","REQUEST.replay01.proposed.json","REQUEST.replay02.proposed.json","SOURCE_DELTA.json","PINSET.json","INPUTS.sha256","CONTRACT.md","HANDOFF.md","CHECK_DOCUMENTS.cjs","READ_NATIVE.json","CREATION_NATIVE.json","CLOSE.cjs"];
const CORE_PINS = [{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/run_science.proposed.py.txt","bytes":108715,"sha256":"87cd4409bf5394792f66318893cc9e187ff43c1419bcfd819f17f874cdb7c121"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.initial.proposed.sh.txt","bytes":1748,"sha256":"c0d5c51be1de58531d897bf97f4c7fc7458aa37858ff6cb005bfce5607f08e25"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay01.proposed.sh.txt","bytes":1751,"sha256":"013144ba4673f7440efe9873ad851b2c1b4f19ecbabd4ce9af2d70a5f0bcd2fa"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay02.proposed.sh.txt","bytes":1751,"sha256":"92ba8b7ae2e57274fafd93be5bd7b3f998b515832eeeb52cad17e263c4d3ffa8"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.initial.proposed.json","bytes":7721,"sha256":"83afb8f6b2d0286048fcb3f84e6bac11e9aed0e1e2808b37e1929dd602d9b27c"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.replay01.proposed.json","bytes":7758,"sha256":"1d70fb92308b5f604334d12b89c8f2d1118d5ea1fece1c63d1874208675557ea"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/REQUEST.replay02.proposed.json","bytes":7758,"sha256":"3814e6984b28b540c80879b52d55e71166157ad8759625f27ee4c9e171e59346"},{"path":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/SOURCE_DELTA.json","bytes":6982,"sha256":"8ebfe4921b6a4aad93a7d02a62d565907ab4c25ebe94fb92f1a7d9c06a30d652"}];
const PREFIXES = [{"old":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/run_science.disabled.py","new":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/run_science.proposed.py.txt","before":"# This preparation is disabled before binding/imports/observation/science.\nraise SystemExit(\"P213_SCIENCE_PREPARATION_DISABLED_NO_AUTHORITY\")\n","after":"# Prospective enabled bytes; materialization and execution require separate authority.\n"},{"old":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.initial.disabled.sh","new":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.initial.proposed.sh.txt","before":"# Disabled preparation: no cwd/allocation/interpreter operation is authorized.\nexit 78\n# Removal of the gate and exact enabled-copy pins require separate review.\n","after":"# Prospective enabled capture bytes; this document grants no operation.\n# Exact derivative/request reception and a separate run grant remain required.\n"},{"old":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay01.disabled.sh","new":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay01.proposed.sh.txt","before":"# Disabled preparation: no cwd/allocation/interpreter operation is authorized.\nexit 78\n# Removal of the gate and exact enabled-copy pins require separate review.\n","after":"# Prospective enabled capture bytes; this document grants no operation.\n# Exact derivative/request reception and a separate run grant remain required.\n"},{"old":"docs/papers211_215_sequence/qa/p213_initial_science_preparation01/capture.replay02.disabled.sh","new":"docs/papers211_215_sequence/qa/p213_initial_science_enabled_preparation01/capture.replay02.proposed.sh.txt","before":"# Disabled preparation: no cwd/allocation/interpreter operation is authorized.\nexit 78\n# Removal of the gate and exact enabled-copy pins require separate review.\n","after":"# Prospective enabled capture bytes; this document grants no operation.\n# Exact derivative/request reception and a separate run grant remain required.\n"}];
const PREP = "docs/papers211_215_sequence/qa/p213_initial_science_preparation01";
const ROOT_RECEPTION = "docs/papers211_215_sequence/qa/p213_initial_science_source_root01/RECEPTION.md";
const WORKSPACE = "/root/autodl-tmp/symbolic_dynamics";
const OWNER = "/root/round211_functional_surgery_residual/p213_literal_role_analysis";
const REVIEWER = "/root/round211_finite_matching_scout";
const ALLOWED = new Set([...INPUTS.map(x=>x.path),...CORE_NAMES.map(n=>OUTDIR+"/"+n)]);

const report = {schema:"P213_EXACT_ENABLED_DERIVATIVE_DOCUMENTARY_CHECK_V1",status:"RUNNING",
  operation_authorized:false,independent_review:null,science_executed:false};
try {
  need(process.argv.length === 2,"NO_CHECKER_ARGUMENTS");
  for (const expected of INPUTS) compareTree(pin(expected.path),expected,"FIXED_INPUT_PIN");
  for (const group of GROUPS) {
    need(hash(fullRead(group.path+"/SHA256SUMS")) === group.sha256,"FROZEN_SEAL");
    need(fullRead(group.path+"/SHA256SUMS").equals(Buffer.from(group.lines.join("\n")+"\n")),"COMPLETE_SEAL_TEXT");
    const names = ["SHA256SUMS",...group.lines.map(line=>line.slice(66))].sort();
    need(equal(fs.readdirSync(group.path).sort(),names),"COMPLETE_OLD_INVENTORY");
  }
  for (const name of CORE_NAMES) fullRead(OUTDIR+"/"+name);
  for (const expected of CORE_PINS) compareTree(pin(expected.path),expected,"INITIAL_CORE_DOCUMENT_PIN");
  const inputText = INPUTS.map(x=>x.sha256+"  "+x.path).join("\n")+"\n";
  need(fullRead(OUTDIR+"/INPUTS.sha256").equals(Buffer.from(inputText)),"FULL_INPUT_PIN_LIST");
  const pinset = JSON.parse(fullRead(OUTDIR+"/PINSET.json").toString("utf8"));
  compareTree(pinset.source_documents,CORE_PINS.slice(0,4),"ALL_FOUR_SOURCE_PINS");
  compareTree(pinset.request_documents,CORE_PINS.slice(4,7),"ALL_THREE_REQUEST_FILE_PINS");
  compareTree(pinset.source_delta_document,CORE_PINS[7],"FULL_DELTA_PIN");
  need(pinset.operation_authorized === false && pinset.root_grant === null,"PINSET_NO_GRANT");
  need(pinset.actual_future_wrapper_key === null && pinset.actual_destination_keys === null &&
       pinset.actual_results === null,"PINSET_NO_ACTUAL_OBSERVATION");
  const delta = JSON.parse(fullRead(OUTDIR+"/SOURCE_DELTA.json").toString("utf8"));
  need(delta.changes.length === 4 && delta.operation_authorized === false,"DELTA_SCOPE");
  report.suffix_comparisons = [];
  for (let i=0;i<4;i++) {
    const s = PREFIXES[i], old = fullRead(s.old), proposed = fullRead(s.new);
    const before = Buffer.from(s.before), after = Buffer.from(s.after);
    need(old.subarray(0,before.length).equals(before),"EXACT_OLD_PREFIX");
    need(proposed.subarray(0,after.length).equals(after),"EXACT_NEW_PREFIX");
    need(old.subarray(before.length).equals(proposed.subarray(after.length)),"COMPLETE_RAW_SUFFIX_EQUAL");
    const d = delta.changes[i];
    compareTree(d.old,pin(s.old),"DELTA_OLD_PIN");
    compareTree(d.proposed,{...pin(s.new),lines:proposed.toString("utf8").split("\n").length-1},"DELTA_PROPOSED_PIN");
    need(d.old_prefix === s.before && d.new_prefix === s.after,"DELTA_LITERAL_PREFIXES");
    need(d.old_prefix_bytes === before.length && d.new_prefix_bytes === after.length,"DELTA_PREFIX_BYTE_COUNTS");
    need(d.unchanged_suffix_bytes === old.length-before.length,"DELTA_SUFFIX_BYTE_COUNT");
    need(d.unchanged_suffix_sha256 === hash(old.subarray(before.length)) && d.raw_suffix_equal === true,"DELTA_SUFFIX_PIN");
    need(d.old_prefix_lines === (i===0?2:3) && d.new_prefix_lines === (i===0?1:2),"DELTA_PREFIX_LINES");
    need(d.old_unchanged_suffix_starts_line === (i===0?3:4) &&
         d.new_unchanged_suffix_starts_line === (i===0?2:3),"DELTA_EXACT_LINE_OFFSET");
    need((BigInt(keys.find(k=>k.path===s.new).fd_before.mode)&0o111n) === 0n,"CARRIER_NOT_EXECUTABLE_MODE");
    report.suffix_comparisons.push({source:s.new,bytes:d.unchanged_suffix_bytes,sha256:d.unchanged_suffix_sha256,raw_equal:true});
  }
  const original = JSON.parse(fullRead(PREP+"/REQUEST.disabled.json").toString("utf8"));
  compareTree(delta.unchanged_scientific_source,original.science_source,"DELTA_UNCHANGED_SCIENCE");
  for (const key of ["inline_binding_unchanged","old_actual_observations_unchanged","parameters_unchanged","controls_paths_body_unchanged"]) need(delta[key] === true,"DECLARED_UNCHANGED:"+key);
  for (const key of ["canonical_target_queried","sources_executed","sources_parsed_or_syntax_checked","author_self_review"]) need(delta[key] === false,"DELTA_FALSE:"+key);
  need(delta.new_canonical_implementation === null,"NO_CANONICAL_IMPLEMENTATION");
  need(delta.baseline_root_reception.sha256 === hash(fullRead(ROOT_RECEPTION)),"ACTUAL_ROOT_RECEPTION_PIN");
  need(delta.baseline_root_reception.seal === GROUPS[0].sha256,"ROOT_SEAL_REFERENCE");
  report.complete_requests = [];
  for (let i=0;i<3;i++) {
    const stage = original.stages[i], requestPath = OUTDIR+"/REQUEST."+stage.id+".proposed.json";
    const r = JSON.parse(fullRead(requestPath).toString("utf8"));
    need(r.schema === "P213_PROSPECTIVE_NATIVE_SCIENCE_REQUEST_V1" &&
         r.status === "SOURCE_ONLY_DATA_NOT_SUBMITTED" && r.stage === stage.id,"REQUEST_IDENTITY");
    for (const key of ["operation_authorized","materialization_accepted","derivative_independently_accepted","derivative_root_accepted","science_accepted","accepted","future_path_queried"]) need(r[key] === false,"NO_REQUEST_AUTHORITY:"+key);
    for (const key of ["request_cmd","root_grant","actual_native_request","actual_native_result","actual_session_id","actual_continuations","actual_destination_keys","actual_wrapper_key","expected_actual_stdout","expected_native_result","independent_review"]) need(r[key] === null,"NO_ACTUAL_REQUEST_VALUE:"+key);
    need(r.proposed_native_request.tool === "exec_command","EXACT_NATIVE_TOOL");
    const capture = fullRead(OUTDIR+"/capture."+stage.id+".proposed.sh.txt");
    const command = Buffer.from(r.proposed_native_request.arguments.cmd,"utf8");
    need(command.equals(capture),"COMPLETE_COMMAND_CAPTURE_RAW_EQUAL");
    compareTree(r.proposed_native_request.arguments,{
      cmd:capture.toString("utf8"),workdir:original.proposed_launch.cwd,
      shell:"/bin/bash",login:false,tty:false,yield_time_ms:1000,max_output_tokens:4096
    },"COMPLETE_NATIVE_ARGUMENT_OBJECT");
    need(r.proposed_continuation.tool === "write_stdin" && r.proposed_continuation.may_submit_now === false,"CONTINUATION_DISABLED");
    compareTree(r.proposed_continuation.arguments,{session_id:null,chars:"",yield_time_ms:10000,max_output_tokens:4096},"CONTINUATION_ACTUAL_SESSION_ONLY");
    compareTree(r.documentary_wrapper_carrier,delta.changes[0].proposed,"REQUEST_WRAPPER_PIN");
    compareTree(r.documentary_capture_carrier,delta.changes[i+1].proposed,"REQUEST_CAPTURE_PIN");
    need(r.proposed_wrapper_path === original.enabled_wrapper.proposed_path,"UNCHANGED_WRAPPER_PATH");
    need(r.proposed_output_directory === stage.proposed_output_directory,"UNCHANGED_CAPTURE_DIRECTORY");
    compareTree(r.output_files,stage.files,"UNCHANGED_RAW_FILE_NAMES");
    compareTree(r.inherited_stage_prerequisites,stage.prerequisites,"UNCHANGED_STAGE_PREREQUISITES");
    for (const key of ["science_source","proposed_launch","canonical_adoption","strict_pair","limits"]) compareTree(r[key],original[key],"UNCHANGED_REQUEST_SUBTREE:"+key);
    need(r.owner === OWNER && r.designated_independent_reviewer === REVIEWER && r.external_status === "HOLD_EXTERNAL","REQUEST_ROLE_BOUNDARY");
    need(r.derivative_prerequisites.length === 4,"FOUR_SEPARATE_DERIVATIVE_PREREQUISITES");
    const commandPin = {stage:stage.id,request_path:requestPath,command_bytes:command.length,command_sha256:hash(command)};
    compareTree(pinset.full_native_command_strings[i],commandPin,"FULL_COMMAND_PIN");
    report.complete_requests.push({...pin(requestPath),...commandPin});
  }
  need(original.operation_authorized === false && original.request_cmd === null && original.root_grant === null,"OLD_DISABLED_REQUEST_UNCHANGED");
  const binding = fullRead(PREP+"/BINDING.proposed.json");
  need(hash(binding) === "78da1d06c05cd6244e9de9c1565a843823051e98c8702c07c5447e20d1da3ab6","UNCHANGED_FULL_BINDING_DOCUMENT");
  const readArchive = JSON.parse(fullRead(OUTDIR+"/READ_NATIVE.json").toString("utf8"));
  need(readArchive.capture_cutoff.first_exec_chunk === "4c1eb7" && readArchive.capture_cutoff.last_exec_chunk === "19ce5d","EXPLICIT_NATIVE_CAPTURE_CUTOFF");
  let sliceCount = 0, sliceBytes = 0;
  for (const entry of readArchive.entries) {
    need(entry.tool === "exec_command" && entry.request.workdir === WORKSPACE,"DOCUMENTARY_NATIVE_TOOL_CWD");
    const m = /^sed -n '([0-9]+),([0-9]+)p' (.+)$/.exec(entry.request.cmd);
    if (!m) continue;
    const paths = m[3].split(" ");
    if (!paths.every(p=>ALLOWED.has(p))) continue; // explicitly excluded mutable navigation only
    need(entry.result.exit_code === 0,"SOURCE_TEXT_READ_NATIVE_ZERO");
    const raw = Buffer.concat(paths.map(fullRead));
    need(Buffer.from(raw.toString("utf8"),"utf8").equals(raw),"READ_UTF8_REVERSIBLE");
    const lines = raw.toString("utf8").split("\n");
    need(lines.pop() === "","SOURCE_TEXT_FINAL_LF");
    const selected = lines.slice(Number(m[1])-1,Number(m[2]));
    const expected = Buffer.from(selected.length?selected.join("\n")+"\n":"");
    const actual = Buffer.from(entry.result.output,"utf8");
    need(actual.equals(expected),"ORIGINAL_SED_SLICE_RAW_EQUAL");
    sliceCount++; sliceBytes += actual.length;
  }
  const sourceEvent = readArchive.entries.find(e=>e.result.chunk_id === "ff9d10");
  need(sourceEvent && sourceEvent.result.exit_code === 0,"WHOLE_SOURCE_TEXT_NATIVE");
  const sourceTexts = JSON.parse(sourceEvent.result.output);
  need(sourceTexts.length === 5,"WHOLE_SOURCE_TEXT_COUNT");
  for (const item of sourceTexts) {
    need(ALLOWED.has(item.path),"SOURCE_TEXT_FIXED_DOCUMENT_PATH");
    const raw = fullRead(item.path);
    need(raw.length === item.bytes && Buffer.from(item.text,"utf8").equals(raw),"WHOLE_ORIGINAL_SOURCE_TEXT_RAW_EQUAL");
  }
  const intakeEvent = readArchive.entries.find(e=>e.result.chunk_id === "19ce5d");
  need(intakeEvent && intakeEvent.result.exit_code === 0,"ACTUAL_INTAKE_NATIVE");
  const old = JSON.parse(intakeEvent.result.output);
  need(old.status === "PASS_DOCUMENTARY_BYTES_ONLY" && old.checks === 799 &&
       old.key_count === 57 && old.keys.length === 57,"ORIGINAL_INTAKE_CENSUS");
  compareTree(old.inputs,INPUTS,"INTAKE_INPUT_PIN_ORIGINAL");
  compareTree(old.documents,CORE_PINS,"INTAKE_CORE_PINS_ORIGINAL");
  for (const oldKey of old.keys) {
    fullRead(oldKey.path);
    compareTree(keys.find(k=>k.path===oldKey.path),oldKey,"WHOLE_INTAKE_KEY_UNCHANGED");
  }
  const creation = JSON.parse(fullRead(OUTDIR+"/CREATION_NATIVE.json").toString("utf8"));
  let creationBodies = 0, creationBytes = 0;
  const createdPaths = [];
  for (const event of creation.entries) {
    need(event.tool === "apply_patch" && typeof event.request === "string","ORIGINAL_PATCH_REQUEST");
    const lines = event.request.split("\n");
    need(lines.shift() === "*** Begin Patch" && lines.pop() === "*** End Patch","PATCH_FRAME");
    let path = null, text = "";
    function finish() {
      if (path === null) return;
      need(ALLOWED.has(path) && path.startsWith(OUTDIR+"/"),"PATCH_EXACT_OWNERSHIP");
      const raw = Buffer.from(text,"utf8");
      need(raw.equals(fullRead(path)),"COMPLETE_ORIGINAL_PATCH_BODY_RAW_EQUAL");
      createdPaths.push(path); creationBodies++; creationBytes += raw.length;
    }
    for (const line of lines) {
      if (line.startsWith("*** Add File: ")) { finish(); path=line.slice(14); text=""; }
      else { need(path!==null && line.startsWith("+"),"ADDITION_ONLY_PATCH_BODY"); text += line.slice(1)+"\n"; }
    }
    finish();
  }
  need(creationBodies === 14 && new Set(createdPaths).size === 14,"ALL_FOURTEEN_STATIC_CREATIONS");
  const expectedCreated = CORE_NAMES.filter(n=>!["READ_NATIVE.json","CREATION_NATIVE.json"].includes(n)).map(n=>OUTDIR+"/"+n).sort();
  need(equal(createdPaths.sort(),expectedCreated),"COMPLETE_STATIC_CREATION_SET");
  report.read_comparisons = {sed_slices:sliceCount,sed_raw_bytes:sliceBytes,whole_source_texts:5,
    prior_complete_keys:57,creation_bodies:creationBodies,creation_raw_bytes:creationBytes};
  report.input_count = INPUTS.length; report.core_documents = CORE_NAMES.length;
  report.old_packages = GROUPS.map(g=>({path:g.path,payloads:g.lines.length,files:g.lines.length+1,seal:g.sha256}));
  report.status = "PASS_AUTHOR_DOCUMENTARY_CONSISTENCY_ONLY";
} catch (error) {
  report.status = "FAIL_AUTHOR_DOCUMENTARY_CONSISTENCY_ONLY";
  report.failure = {name:error.name,code:error.code||null,message:error.message};
  process.exitCode = 1;
}
report.checks = checks; report.key_count = keys.length; report.total_read_bytes = totalRead;
report.keys = keys;
process.stdout.write(JSON.stringify(report,null,2)+"\n");
