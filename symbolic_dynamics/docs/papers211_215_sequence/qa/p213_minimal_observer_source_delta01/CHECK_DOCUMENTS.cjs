"use strict";
// Author document-integrity checks only. No Python parsing or execution.
const fs = require("fs"), crypto = require("crypto");
const root = "docs/papers211_215_sequence/qa/";
const base = root + "p213_minimal_observer_source_delta01/";
const before = root + "p213_minimal_observer_source01/";
const proposed = root + "p213_minimal_observer_binding_preparation01/";
let checks = 0;
const check = (ok, label) => { checks++; if (!ok) throw new Error(label); };
const same = (a,b) => JSON.stringify(a) === JSON.stringify(b);
const sha = b => crypto.createHash("sha256").update(b).digest("hex");
const statFields = ["dev","ino","mode","nlink","uid","gid","rdev","size","mtimeNs","ctimeNs"];
const stat = s => Object.fromEntries(statFields.map(k => [k,String(s[k])]));
const cache = new Map(), keys = [];
function read(path) {
  check(path.startsWith(root) && !path.split("/").includes(".."), "selected_document_path");
  if (cache.has(path)) return cache.get(path);
  const a = fs.lstatSync(path,{bigint:true});
  check(a.isFile() && !a.isSymbolicLink() && a.nlink === 1n,"regular_single_link_document");
  const fd = fs.openSync(path,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
  const b = fs.fstatSync(fd,{bigint:true});
  check(same(stat(a),stat(b)),"document_path_fd");
  const bytes = fs.readFileSync(fd), c = fs.fstatSync(fd,{bigint:true});
  fs.closeSync(fd);
  const d = fs.lstatSync(path,{bigint:true});
  check(same(stat(a),stat(d)) && same(stat(b),stat(c)) && BigInt(bytes.length) === b.size,
        "document_changed_or_incomplete");
  const entry = {path,bytes:bytes.length,sha256:sha(bytes),ten_fields:stat(b)};
  keys.push(entry); cache.set(path,bytes); return bytes;
}
const text = path => read(path).toString("utf8");
const json = path => JSON.parse(text(path));
const pinLines = text(base+"INPUTS.sha256").trimEnd().split("\n");
check(pinLines.length === 17,"exact_input_count");
const pins = new Map();
for (const line of pinLines) {
  const m = /^([0-9a-f]{64})  (docs\/papers211_215_sequence\/qa\/[A-Za-z0-9_/.]+)$/.exec(line);
  check(m && !pins.has(m[2]),"input_pin_grammar_unique");
  pins.set(m[2],m[1]); check(sha(read(m[2])) === m[1],"input_pin_match");
}
const inputKeyObject = json(base+"INPUT_KEYS_NATIVE.json");
check(inputKeyObject.result.exit_code === 0,"input_key_native_exit");
const priorKeys = JSON.parse(inputKeyObject.result.output).keys;
check(priorKeys.length === 17,"prior_key_count");
for (const old of priorKeys) {
  const current = keys.find(x => x.path === old.path);
  check(current && current.sha256 === old.sha256 && current.bytes === old.bytes
        && same(current.ten_fields,old.ten_fields),"input_key_still_unchanged");
}
const oldReads = json(base+"SOURCE_READS_NATIVE.json").records;
check(oldReads.length === 17,"all_original_read_records");
for (const r of oldReads) {
  check(pins.has(r.path) && r.result.exit_code === 0,"original_read_scope_exit");
  check(Buffer.from(r.result.output,"utf8").equals(read(r.path)),"whole_original_native_read_bytes");
}
const ownReads = json(base+"READBACK_NATIVE.json").records;
check(ownReads.length === 9,"all_authored_read_records");
for (const r of ownReads) {
  check(r.path.startsWith(base) && r.result.exit_code === 0,"own_read_scope_exit");
  check(Buffer.from(r.result.output,"utf8").equals(read(r.path)),"whole_own_native_read_bytes");
}
const p = json(proposed+"POLICY.proposed.json"), b = json(base+"BINDING.disabled.json");
check(!b.enabled && !b.operation_authorized && b.id === null,"binding_disabled");
check(b.actual_launch_record === null && b.actual_module_rows === null
      && b.source_pins === null && b.capture_pins === null,"no_fabricated_actual_facts");
check(b.proposal_sha256 === pins.get(proposed+"POLICY.proposed.json"),"proposal_pin");
check(same(b.launch_policy,p.launch_admissibility) && same(b.flag_names,p.launch_admissibility.flag_names),
      "complete_launch_policy_exact");
check(b.flag_names.length === 17 && same(b.bounds,p.bounds),"unchanged_all_flags_bounds");
check(b.observer === p.proposed_paths.observer && b.cwd === p.root_choices.cwd
      && b.env === p.root_choices.env && b.bash === p.root_choices.bash
      && b.capture_mkdir === p.root_choices.mkdir,"root_choices_exact");
for (const phase of ["early","helper","closing"]) {
  check(same(b.module_names[phase],phase === "early" ? p.module_policy.early_allowed_names :
        p.module_policy.helper_and_closing_allowed_names),"finite_phase_names_exact");
  check(same(b.required_module_names[phase],phase === "early" ? p.module_policy.early_required_names :
        p.module_policy.helper_and_closing_required_names),"finite_phase_required_exact");
}
check(same(b.loader_ids,p.loader_permission_records) && same(b.special_maps,p.map_policy.special_names),
      "loader_and_special_map_exact");
check(b.files.length === 69 && new Set(b.files.map(x=>x.lexical)).size === 69,"finite_unique_69");
for (let i=0;i<p.files.length;i++) {
  const q=p.files[i], f=b.files[i];
  check(q.final_policy === "must_equal_lexical" && q.links_policy === "no_leaf_symlink","proposal_no_alias");
  check(f.lexical === q.lexical && f.final === q.lexical && same(f.links,[])
        && f.optional === q.optional && f.earliest_phase === q.earliest_phase
        && same(f.roles,q.roles) && f.absence_required === q.roles.includes("startup_zip_must_be_absent"),
        "exact_candidate_adaptation");
  check(f.observed_presence === null && f.observed_key === null,"no_actual_file_fact");
}
check(same(b.interpreter,b.files.find(x=>x.lexical === p.root_choices.interpreter)),"interpreter_entry_exact");
check(b.files.filter(x=>!x.optional).length === 2 && b.files.filter(x=>x.absence_required).length === 1,
      "two_required_one_zip_absence");
const expectedNames = p.module_policy.helper_and_closing_allowed_names;
check(Object.keys(b.modules).length === 62 && same(Object.keys(b.modules).sort(),[...expectedNames].sort()),
      "no_module_frontier_expansion");
const builtinNames = [...p.module_policy.builtin_early_names,...p.module_policy.builtin_helper_names,
                      ...p.module_policy.builtin_hash_conditional_names];
for (const name of builtinNames) {
  check(b.modules[name].mechanism === "builtin" && b.modules[name].file_roles.length === 0,"builtin_only");
}
for (const [name,nominal] of Object.entries(p.module_policy.frozen_nominal_names)) {
  check(b.modules[name].mechanism === "frozen" && b.modules[name].nominal_file === nominal
        && b.modules[name].file_roles.length === 0,"frozen_nominal_not_read");
}
for (const q of p.module_policy.file_modules) {
  const m=b.modules[q.name];
  check(["mechanism","origin","file","cache","package_path"].every(k=>same(m[k],q[k])),"file_module_fields_exact");
  const roles=q.mechanism === "source_file" ?
    [{path:q.file,role:"source_or_matching_source",content_required:true},
     {path:q.cache,role:"eligible_nonoptimized_cache",content_required:false}] :
    [{path:q.file,role:"extension_origin",content_required:true}];
  check(same(m.file_roles,roles) && m.provenance === q.reason,"file_roles_provenance_exact");
  if (q.mechanism === "source_file") {
    const slash=q.file.lastIndexOf("/"), stem=q.file.slice(slash+1,-3);
    check(q.cache === q.file.slice(0,slash)+"/__pycache__/"+stem+".cpython-310.pyc","exact_static_cache_spelling");
  }
}
check(same(b.modules.__main__.file_roles,[{path:b.observer,role:"direct_script_source",content_required:true}]),
      "own_main_mandatory_source");
for (const m of Object.values(b.modules)) {
  check(m.observed_row === null && !Object.hasOwn(m,"record") && typeof m.provenance === "string"
        && m.provenance.length > 0,"no_expected_row_nonempty_provenance");
  for (const r of m.file_roles) check(b.files.some(f=>f.lexical === r.path && f.roles.includes(r.role)),"role_links");
}
check(b.files.filter(x=>x.roles.includes("source_or_matching_source")).length === 29
      && b.files.filter(x=>x.roles.includes("eligible_nonoptimized_cache")).length === 29,"29_sources_29_caches");
check(same(b.files.filter(x=>x.roles.includes("mapped_file")).map(x=>({path:x.lexical,earliest_phase:x.earliest_phase})),
      p.map_policy.file_names),"nine_native_phase_roles_exact");
const observer=text(base+"observe.py"), oldObserver=text(before+"observe.py");
function region(source,name) {
  const start=source.indexOf("def "+name+"(");
  check(start>=0,"function_present_"+name);
  const end=source.indexOf("\n\n\n",start);
  check(end>=0,"function_region_end_"+name);
  return source.slice(start,end);
}
for (const name of ["module_snapshot","attribute","loader_id","raw_maps","full_stat","key_file"])
  check(region(observer,name) === region(oldObserver,name),"unchanged_function_"+name);
const expectedMap=region(oldObserver,"map_roles").replace(
  '            need(item["inode"] > 0, "file_map_inode")',
  '            need(phase != "early" or entries[path]["earliest_phase"] == "early", "early_map_path")\n'+
  '            need(item["inode"] > 0, "file_map_inode")');
check(region(observer,"map_roles") === expectedMap,"map_parser_only_phase_guard_delta");
const processRegion=region(observer,"process_points");
check(processRegion.indexOf('"cwd_binding"') < processRegion.indexOf('"exe_binding"')
      && processRegion.indexOf('"exe_binding"') < processRegion.indexOf('os.stat("/proc/self/exe")')
      && processRegion.indexOf('os.stat("/proc/self/exe")') < processRegion.indexOf('"exe_file_identity"'),"F01_literal_order");
check((observer.match(/^\s+process_points\(/gm)||[]).length === 3,"three_proc_points_retained");
const failureRegion=region(observer,"failure");
check(!failureRegion.includes(".args") && !failureRegion.includes("__module__") && !failureRegion.includes("__qualname__")
      && failureRegion.includes("kind is ObserverFailure and exc.owner is OWNED_FAILURE")
      && failureRegion.includes('code = "operation_failed"') && failureRegion.includes("exc.code in FAILURE_CODES")
      && failureRegion.includes("kind in ERRNO_TYPES"),"F02_owned_finite_fixed_labels");
const codeList=json(base+"FINITE_FAILURE_CODES.json");
const codeText=observer.slice(observer.indexOf("FAILURE_CODES = (\n")+18,observer.indexOf("\n)\n",observer.indexOf("FAILURE_CODES = (\n")));
const literals=[...codeText.matchAll(/"([a-z_]+)"/g)].map(x=>x[1]);
check(same(literals,codeList.owned_codes) && literals.length === 99 && new Set(literals).size === 99,"99_codes_exact");
check(!observer.includes("raise RuntimeError") && !observer.includes("exc.args") && observer.includes('raise ObserverFailure("unsupported_scalar_type")'),
      "no_dynamic_runtimeerror_text");
const importNames=[...observer.matchAll(/^\s*import ([a-z]+)$/gm)].map(x=>x[1]);
check(same(importNames,["sys","os","hashlib","json"]),"only_four_declared_imports");
check(observer.indexOf('raise SystemExit("P213_OBSERVER_DISABLED_SOURCE_DELTA")') < observer.indexOf("BINDING = None")
      && observer.indexOf("BINDING = None") < observer.indexOf("\nimport sys"),"unconditional_observer_gate");
check(!observer.includes('BINDING["launch_record"]') && !observer.includes('policy["record"]'),"unattainable_expected_rows_removed");
const early=observer.slice(observer.indexOf("\ntry:\n    ENTRIES"));
check(early.indexOf('module_roles(EARLY_MODULES, "early", ENTRIES)') < early.indexOf('raw_maps("early_pre_helpers")')
      && early.indexOf('map_roles(EARLY_MAPS, "early", ENTRIES)') < early.indexOf('module_snapshot("second_prehelper")')
      && early.indexOf('"prehelper_change"') < early.indexOf("    import os"),"early_unknown_checks_before_further_access");
const outer=observer.slice(observer.indexOf("\nRESULT ="));
check(outer.indexOf('module_roles(helper_modules, "helper", entries)') < outer.indexOf('raw_maps("helper")')
      && outer.indexOf('module_roles(closing_modules, "closing", entries, keyed)') < outer.indexOf('raw_maps("closing")'),
      "helper_closing_guards_before_maps");
check(!outer.slice(outer.indexOf('closing_modules = module_snapshot("closing")')).includes("key_file("),"no_key_after_closing");
check(region(observer,"points").includes('need(not entry["absence_required"], "required_absence_not_observed")')
      && region(observer,"path_ok").indexOf("os.") < 0,"zip_gate_and_pure_lexical_path");
const capture=text(base+"capture.sh"), oldCapture=text(before+"capture.disabled.sh"), request=json(base+"CAPTURE_REQUEST.disabled.json");
check(capture.indexOf("\nexit 78\n") < capture.indexOf("\nP213_CAPTURE_ENV="),"unconditional_capture_gate");
check(capture.slice(capture.indexOf("\nfor P213_CAPTURE_VALUE")) === oldCapture.slice(oldCapture.indexOf("\nfor P213_CAPTURE_VALUE")),
      "capture_operational_body_unchanged");
check(request.enabled === false && request.operation_authorized === false && request.request.cmd === null
      && request.source_pins === null && request.output_directory_observed_absence === null,"request_still_disabled_unknown");
for (const [key,value] of Object.entries({ENV:p.root_choices.env,MKDIR:p.root_choices.mkdir,
  PYTHON:p.root_choices.interpreter,OBSERVER:p.proposed_paths.observer,CWD:p.root_choices.cwd,
  DIRECTORY:p.proposed_paths.capture_directory})) check(capture.includes("P213_CAPTURE_"+key+"='"+value+"'"),"capture_literal_choice");
const diffRecords=json(base+"SOURCE_DIFF_NATIVE.json").records;
check(diffRecords.length === 6,"six_complete_native_diffs");
function applyUnified(original,diff) {
  const old=original.split("\n"), out=[], lines=diff.split("\n"); let cursor=0, i=2, hunks=0;
  check(lines[0].startsWith("--- ") && lines[1].startsWith("+++ "),"diff_headers");
  while (i<lines.length && lines[i] !== "") {
    const h=/^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@/.exec(lines[i++]);
    check(h,"unified_hunk_header"); hunks++;
    const start=Number(h[1])-1, wantOld=h[2] === undefined ? 1:Number(h[2]),
          wantNew=h[4] === undefined ? 1:Number(h[4]);
    check(start>=cursor,"ordered_hunks"); out.push(...old.slice(cursor,start)); cursor=start;
    let usedOld=0,usedNew=0;
    while (i<lines.length && !lines[i].startsWith("@@ ") && lines[i] !== "") {
      const line=lines[i++], sign=line[0], value=line.slice(1);
      check(" +-".includes(sign),"unified_line_prefix");
      if (sign === " " || sign === "-") { check(old[cursor] === value,"unified_original_line"); cursor++; usedOld++; }
      if (sign === " " || sign === "+") { out.push(value); usedNew++; }
    }
    check(usedOld === wantOld && usedNew === wantNew,"complete_hunk_counts");
  }
  check(hunks>0 && lines.slice(i).every(x=>x === ""),"complete_native_diff_tail");
  out.push(...old.slice(cursor)); return out.join("\n");
}
for (const d of diffRecords) {
  check(d.result.exit_code === 1 && !d.result.session_id && d.old.startsWith(before) && d.new.startsWith(base),"native_diff_scope_exit");
  check(Buffer.from(applyUnified(text(d.old),d.result.output),"utf8").equals(read(d.new)),"complete_diff_reconstructs_exact_new_bytes");
}
for (const k of keys) check(same(stat(fs.lstatSync(k.path,{bigint:true})),k.ten_fields),"closing_document_stat");
process.stdout.write(JSON.stringify({scope:"AUTHOR_DOCUMENT_INTEGRITY_ONLY",checks,
  original_inputs:17,original_bytes:priorKeys.reduce((n,x)=>n+x.bytes,0),whole_original_reads:17,
  whole_own_reads:ownReads.length,native_diffs_verified:6,module_names:62,early_allowed_names:23,
  files:69,finite_owned_codes:99,python_parsed:false,observer_executed:false,capture_executed:false,
  runtime_accepted:false,source_independently_accepted:false,keys},null,2)+"\n");
