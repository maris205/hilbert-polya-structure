#!/usr/bin/python3.10
"""SOURCE-ONLY DRAFT: bounded stdout-only scientific-key reconciliation.

Not executed, imported, compiled or syntax-tested by the preparing desk.
Root must separately receive these source/spec originals, pin this exact
source and authorize/capture one invocation. The command-line phrase below
is an anti-accidental-invocation guard, NOT root approval by itself.

Disclosed documentary reuse: four-field rich/state semantics from the fully
read accepted final A/B and Round2 refresh02 receivers; no such helper is
imported or called. No scientific program, shell, subprocess, probe, build,
file write, directory creation, recursive host traversal or /proc read.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT/'docs/papers211_215_sequence/qa/p211_lifecycle_scientific_key_desk01'
SPEC_PATH = HERE/'SCIENTIFIC_REUSE_SPEC_v2.json'
SPEC_SHA256 = 'a1c9fd87629b9a175a53fe5fd60680def880d81796018c8ea87eda8b227ea50c'
ENV4 = {'PATH':'/usr/bin:/bin','LANG':'C.UTF-8','LC_ALL':'C.UTF-8','TZ':'UTC'}
FIELDS = {'bytes','sha256','resolved','symlink'}
READS = {}
CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def identity(body):
    return {'bytes':len(body),'sha256':sha256(body).hexdigest()}


def rich(path):
    p = Path(path)
    need(p.is_absolute(), 'literal absolute file spelling')
    body = p.read_bytes()
    now = {**identity(body),'resolved':str(p.resolve(strict=True)),
           'symlink':os.readlink(p) if p.is_symlink() else None}
    need(p.is_file(), ('ordinary resolved file',str(p)))
    need(str(p) not in READS or READS[str(p)] == now,
         ('same whole file key on every read',str(p)))
    READS[str(p)] = now
    return body, now


def unique(pairs):
    value = {}
    for k,v in pairs:
        need(k not in value, ('duplicate JSON key',k))
        value[k] = v
    return value


def parse(body):
    return json.loads(body, object_pairs_hook=unique)


def pinned_json(path, digest):
    body,key = rich(path)
    need(key['sha256'] == digest, ('exact immutable basis bytes',str(path)))
    return parse(body)


def four(value):
    need(FIELDS <= set(value), 'all four original scientific file-key fields')
    return {k:value[k] for k in FIELDS}


def state(path, content=True):
    p = Path(path)
    row = {'lexists':os.path.lexists(p),'exists':p.exists(),
           'is_file':p.is_file(),'is_dir':p.is_dir(),
           'is_character_device':p.is_char_device(),
           'resolved':str(p.resolve()),
           'symlink':os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        s = p.stat()
        row['character_device'] = {
            'major':os.major(s.st_rdev),'minor':os.minor(s.st_rdev),'mode':s.st_mode}
    if content and p.is_file():
        body,key = rich(p)
        row.update({k:key[k] for k in ('bytes','sha256')})
    return row


def sampled_domain(spec, lock):
    files = {}
    for p,expected in sorted(spec['files'].items()):
        body,actual = rich(p)
        need(actual == expected, ('entire current scientific file key',p))
        files[p] = actual
    paths = {p:state(p) for p in sorted(lock['configuration']['paths'])}
    need(paths == lock['configuration']['paths'], 'all69 exact current configuration states')
    memberships = {}
    for directory,expected in sorted(lock['configuration']['memberships'].items()):
        p = Path(directory)
        row = {'directory':state(p,False),'members':{}}
        if p.is_dir():
            # Exactly the existing five direct membership roots, never recurse.
            row['members'] = {x.name:state(x,False) for x in sorted(p.iterdir())}
        need(row == expected, ('complete direct directory and every member state',directory))
        memberships[directory] = row
    loader = {p:state(p,False) for p in sorted(lock['loader_search_directory_states'])}
    need(loader == lock['loader_search_directory_states'], 'all9 exact loader-directory states')
    caches = {p:os.path.lexists(p) for p in spec['absent_cache_paths']}
    need(len(caches) == 15 and not any(caches.values()), 'all15 original scientific caches absent')
    capsules = {}
    for role,record in spec['roles'].items():
        p = Path(record['attempt'])/'recorder/capsule'
        names = sorted(x.name for x in p.iterdir())
        need(names == ['parameters.json','verify.py'], ('unchanged two-file capsule inventory',role))
        capsules[str(p)] = names
    return {'scientific_files':files,'configuration_paths':paths,
            'memberships':memberships,'loader_states':loader,
            'cache_lexists':caches,'capsule_member_names':capsules}


def main():
    need(sys.argv == [str(HERE/'check_scientific_reuse_v2.py'),'--root-authorized-read-only'],
         'source-only draft refuses all other command forms; this flag is not approval')
    need(Path.cwd() == ROOT and Path(__file__).absolute() == HERE/'check_scientific_reuse_v2.py',
         'exact separately authorized source path and cwd')
    need(dict(os.environ) == ENV4 and sys.flags.isolated == 1 and
         sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode,
         'exact documentary ENV4 and I/S/B/unoptimized invocation')
    rich(__file__)  # This actual key must match root's separately pinned source.
    spec = pinned_json(SPEC_PATH,SPEC_SHA256)
    need(spec['schema'] == 'p211-scientific-reuse-source-only-spec-v1' and
         spec['status'] == 'DRAFT_NOT_EXECUTED_REQUIRES_SEPARATE_ROOT_SOURCE_RECEPTION_AND_EXACT_RUN_AUTHORITY',
         'immutable preparation status is not an execution receipt')
    need(spec['workspace'] == str(ROOT) and set(spec['roles']) == {'author','a','b'},
         'exact original workspace and three scientific roles')
    basis = {}
    for p,key in spec['basis_inputs'].items():
        need(Path(p).is_relative_to(ROOT) and set(key) == {'sha256'},
             'only ten exact workspace basis documents')
        basis[p] = pinned_json(p,key['sha256'])
    need(len(basis) == 10, 'one original runtime lock plus3 bindings plus6 input ledgers')
    lock = basis[spec['lock']]
    need(lock['format'] == 'p211-bounded-runtime-lock-v1' and
         lock['configuration'] == spec['configuration'] and
         lock['loader_search_directory_states'] == spec['loader_search_directory_states'],
         'complete original scientific settings, without build-schema substitution')
    union = {}
    for role,record in spec['roles'].items():
        binding,outer,child = [basis[record[k]] for k in ('binding','outer_key','child_key')]
        need(len(outer) == record['outer_entries'] and len(child) == record['child_entries'],
             ('complete original role-key cardinalities',role))
        need(binding['attempt'] == record['attempt'] and binding['mode'] == 'pair' and
             binding['argv_template'] == record['argv_template'] == ['$ENTRY','--parameters','$PARAMETERS']
             and binding['declared_imports'] == ['itertools','json','math','sys']
             and binding['local_helper_imports'] == [],
             ('unchanged accepted role, explicit parameters and import closure',role))
        need(len(binding['provenance_inputs']) == record['provenance_rows'] and
             binding['canonical'] == record['canonical'] and
             binding['capsule_files'] == record['capsule_sources'],
             ('entire accepted capsule/canonical/provenance roles',role))
        expected = dict(lock['files'])
        expected.update(binding['adapter_sources'])
        expected[record['binding']] = outer[record['binding']]
        expected[spec['lock']] = binding['runtime_lock']
        for row in binding['capsule_files'] + binding['provenance_inputs']:
            expected[row['path']] = row
        expected[binding['canonical']['path']] = binding['canonical']
        names = set()
        for p,pin in expected.items():
            need(p in outer and all(outer[p][k] == v for k,v in pin.items() if k in FIELDS),
                 ('original frozen-input schema and pin reconstruction',role,p))
            names.add(p)
            names.add(outer[p]['resolved'])
        need(names == set(outer), ('whole resolved-alias-expanded original outer closure',role))
        augmented = dict(outer)
        for row in binding['capsule_files']:
            p = record['attempt']+'/recorder/capsule/'+row['name']
            need(child[p] == {**four(row),'resolved':p,'symlink':None},
                 ('exact original physical child capsule key',role,p))
            augmented[p] = child[p]
        need(augmented == child, ('entire original child closure, exactly two additions',role))
        for p,key in child.items():
            need(set(key) == FIELDS and (p not in union or union[p] == key),
                 ('all original full-key schemas and role overlaps',p))
            union[p] = key
    need(union == spec['files'] and len(union) == 427, 'entire original427 scientific key, not selected hashes')
    need(sum(not Path(p).is_relative_to(ROOT) for p in union) == 122, 'exact122 host file spellings')
    need(all(p in union and union[p] == k for p,k in lock['files'].items()) and
         len(lock['files']) == 122 and len(lock['configuration']['paths']) == 69 and
         len(lock['configuration']['memberships']) == 5 and
         sum(len(v['members']) for v in lock['configuration']['memberships'].values()) == 292 and
         len(lock['loader_search_directory_states']) == 9, 'whole122/69/5/292/9 domain')
    caches = [r['attempt']+'/never_created_'+s+'_cache'
              for r in spec['roles'].values()
              for s in ('outer','launcher','recorder','child01','child02')]
    need(spec['absent_cache_paths'] == caches, 'exact original15 cache spellings')
    before = sampled_domain(spec,lock)
    after = sampled_domain(spec,lock)
    need(before == after, 'whole scientific dependency endpoints unchanged')
    for p,expected in dict(READS).items():
        need(rich(p)[1] == expected, ('all documentary/scientific read inputs close',p))
    return {'status':'PASS_BOUNDED_SCIENTIFIC_REUSE_KEY_RECONCILIATION_PENDING_ROOT_ACCEPTANCE',
            'checks':CHECKS,'scientific_file_keys':427,'scientific_host_file_spellings':122,
            'runtime_file_keys':122,'configuration_paths':69,'membership_directories':5,
            'membership_direct_entries':292,'loader_states':9,'cache_absences':15,
            'domain_passes':2,'DOMAIN_BEFORE':before,'DOMAIN_AFTER':after,
            'READ_INPUTS':READS,'read_paths':len(READS),
            'new_scientific_runs':0,'new_probes':0,'new_builds':0,'new_page_views':0,
            'new_subprocesses':0,'file_writes':0,'root_acceptance':False,'paper_complete':False,
            'limits':spec['limits'],
            'scope':'Exact scientific four-field key and full original settings only; not a fresh scientific runtime trace or replacement for full historical artifact/lifecycle rich keys.'}


if __name__ == '__main__':
    try:
        result = main()
    except Exception as exc:
        print(json.dumps({'status':'FAIL_READONLY_SCIENTIFIC_KEY_RECONCILIATION_PRESERVE_ATTEMPT',
                          'checks':CHECKS,'exception_type':type(exc).__name__,'exception':str(exc),
                          'READ_INPUTS_PARTIAL':READS},sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result,sort_keys=True))
