import json,gzip,re,hashlib,collections
from pathlib import Path
R=Path('/root/autodl-tmp/symbolic_dynamics'); Q=R/'docs/papers204_208_sequence/qa'; H=Q/'five_paper_terminal_gate_revision_01'
def A(p):
 p=Path(p);return p if p.is_absolute() else R/p
def J(p):return json.loads(A(p).read_bytes())
C=J(H/'FOUR_INPUTS.json'); aliases={(str(A(r['original'])),r['sha256'],c):A(r['physical'])for r in C['aliases']for c in r['cases']}
names=set(); rich={}; partial={}; stages=[]; manifests={}; metadata=set()
def add(p,e=None,case=False):
 p=A(p); d=e if isinstance(e,str) else e.get('sha256')if e else None
 p=aliases.get((str(p),d,case),p)
 n=str(p);names.add(n)
 if isinstance(e,dict)and'sha256'in e:
  v={k:e[k]for k in('sha256','bytes')if k in e};partial.setdefault(n,[]).append(v)
  if 'resolved'in e and p==A(n):
   row={k:e[k]for k in('sha256','bytes','resolved')};row['symlink']=e.get('link') if type(e.get('symlink'))is bool else e.get('symlink')
   if not case or (str(A(n)),d,case)not in aliases:rich.setdefault(n,row)
 return p
def obj(p):
 add(p);metadata.add(str(A(p)));return J(p)
def stage(k):stages.append((k,len(names)))
def mf(spec,case=False):
 seal=A(spec['path']);base=A(spec.get('base',seal.parent));physical=add(seal,spec['sha256'],case)
 rows={}
 for line in physical.read_text().splitlines():
  d,n=line.split('  ',1);rows[n]=d;add(base/n,d,case)
 assert len(rows)==spec['payload_rows']
 manifests[str(base)]=set(str(base/n)for n in rows)|{str(seal)}
 return rows
def pkg(p):return mf({'path':str(Path(p['root'])/'SHA256SUMS'),'sha256':p['manifest']['sha256'],'payload_rows':p['payloads']})
def interval(b,a,case=False):
 x=obj(b);y=obj(a);assert x==y
 for n,v in x.items():add(n,v,case)
def states(d):
 for n,v in d.items():
  if v.get('is_file')or'sha256'in v:add(n,v)
mf({'path':str(H/'SHA256SUMS'),'sha256':'3863616519c14cc2f70d92deced93d745978a34f7e90f78aed5f00dd12ca8238','payload_rows':14})
for n,v in obj(H/'REVISION_PROVENANCE.json')['inputs'].items():add(n,v)
binding=obj(H/'ROOT_REUSE_BINDING.json')
for n,v in C['fixed_inputs'].items():add(n,v)
for row in C['aliases']:add(row['physical'],row['sha256'])
add(C['current_index'])
pr=obj(H/'KEY_SELECTOR_PROVENANCE.json')
for n,v in obj(H/'LINK_PARSER_PROVENANCE.json')['sources'].items():add(n,v)
for n,v in pr.items():add(v['source'],v['source_sha256'])
stage('preparation_fixed_alias_selector')
for p in C['papers']:
 base=A(p['paper']);mf(p['completion_key']['whole_paper'])
 if'package'in p['completion_key']:mf(p['completion_key']['package'])
 for f in p['physical_freezes']:
  mf(f['manifest'])
  for n,v in p['scientific_pins'].items():add(base/('frozen_round'+str(f['round']))/n,v);add(base/n,v)
 for row in p['accepted_reviews']:
  mf(row['final_manifest']);rv=A(row['accepted_delta']).parent
  for n in('REPORT.md','SOURCE_AND_PROOF.md','REPLAY_LOG.md','BUILD_REPORT.md','verify.py','CANONICAL.json','INPUT_PINS.sha256','DELTA.md'):add(rv/n)
  for line in (rv/'INPUT_PINS.sha256').read_text().splitlines():
   d,n=line.split('  ',1);add(n,d)
  add(row['current_census'],row['current_census_pin']);add(row['accepted_delta'],row['accepted_delta_pin'])
for row in C['rejected_preservation']:
 for n,v in row['pins'].items():add(n,v)
stage('completion_manifests_reviews')
obj(C['strict_root_completion'])
for role,p in C['supplemental_pairs'].items():
 b=A(p['directory']);mf(p['manifest']);obj(b/'RESULT.json');interval(b/'INPUTS_BEFORE.json',b/'INPUTS_AFTER.json')
 obj(b/'RESOURCE_NAMES_BEFORE.json');obj(b/'RESOURCE_NAMES_AFTER.json')
 states(obj(b/'CONFIGURATION_BEFORE.json'));obj(b/'CONFIGURATION_AFTER.json')
 add(p['producer'],p['producer_pin']);add(p['canonical'],p['canonical_pin'])
 for n in('01','02'):add(b/('commands/03_verify_'+n+'/stdout.raw'))
stage('strict_six')
obj(C['four_build_root_completion']);b=A(C['supplemental_builds']['directory']);mf(C['supplemental_builds']['manifest'])
for phase in('BEFORE','AFTER'):
 z=b/('KNOWN_INPUTS_'+phase+'.json.gz');add(z);g=json.loads(gzip.decompress(z.read_bytes()));obj(str(z)+'.meta.json')
 if phase=='BEFORE':
  for rows in g.values():states(rows)
for stem in('ORIGINALS','LIBRARIES','CONSUMED_TEX'):interval(b/(stem+'_BEFORE.json'),b/(stem+'_AFTER.json'))
views=obj(C['four_build_views'])
for v in views['papers']:
 p=C['supplemental_builds']['papers'][v['paper']]
 for num in(1,2):
  cold=b/(v['paper']+'_cold_build_'+str(num));initial=obj(b/(cold.name+'_SOURCE_ONLY_INITIAL.json'))
  for n,e in initial.items():add(cold/n,e)
  add(cold/'main.pdf',p['pdf']);add(p['paper']+'/main.pdf')
 for page in v['pages']:add(page['path'],{'sha256':page['sha256'],'bytes':page['bytes']})
add('/usr/bin/ldd')
stage('four_builds')
fixed=obj(C['reuse_inputs']);pkg(C['reuse_output_package']);obj(C['reuse_native']);result=obj(C['reuse_result'])
for k in('native','report'):add(binding[k],binding[k+'_pin'])
for spec in fixed['accepted_packages']:pkg(spec)
for n,v in fixed['fixed_inputs'].items():add(n,v)
for row in result['original_ledger_references']:
 cases=[]
 for case,p in {**fixed['pairs'],**fixed['builds']}.items():
  roots=[p['package']['root']]+([p['launcher']['root']]if'launcher'in p else[])
  if any(Path(row['before']).is_relative_to(Path(t))for t in roots):cases.append(case)
 assert len(cases)==1
 interval(row['before'],row['after'],cases[0])
for p in fixed['pairs'].values():
 b=A(p['package']['root']);pkg(p['package']);conf=obj(b/'CONFIGURATION_BEFORE.json');obj(b/'CONFIGURATION_AFTER.json')
 if p['paper_number']==208:states(conf);obj(b/'RUNTIME_INVENTORY_BEFORE.json')
 else:states(conf['optional']);obj(b/'INTERPRETER_CONFIGURATION.json');obj(b/'PARENT_BEFORE.json');obj(b/'RUNTIME_BEFORE.json')
for p in fixed['builds'].values():
 b=A(p['package']['root']);pkg(p['package']);states(obj(b/'CONFIGURATION_BEFORE.json'));obj(b/'CONFIGURATION_AFTER.json')
 for n in('RUNTIME_BEFORE.json','TEX_INVENTORY_BEFORE.json','USER_ROOTS_AFTER.json'):obj(b/n)
 v=obj(p['view_record'])
 for row in v['pages']:add(row['path'],row['sha256'])
 for num in(1,2):
  cold=b/('cold_build_'+str(num))
  for n,e in p['source_pins'].items():add(cold/n,e)
  add(cold/'main.pdf',p['pdf']);add(A(p['paper'])/'main.pdf')
stage('reuse_intervals_packages')
def local(data,modern):
 s=data.decode()
 if modern:
  s=re.sub(r'(?ms)^[ ]{0,3}(' + chr(96)+r'{3,}|~{3,})[^\n]*\n.*?^[ ]{0,3}\1[ \t]*$','\n\n',s)
  s=re.sub(r'(?:\A|\n\n)(?:(?: {4}|\t)[^\n]*(?:\n|$))+','\n\n',s)
  s=re.sub(r'('+chr(96)+r'+)(?:(?!\1)[\s\S])*?\1',' ',s)
 return [t for v in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s) if(t:=(v.strip()if modern else v).strip('<>').split('#',1)[0])and not re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',t)]
def links(doc,origin,expected=None,case=False,modern=False):
 physical=add(doc,expected,case); targets=local(physical.read_bytes(),modern)
 for href in targets:
  if isinstance(origin,dict):t=origin[href]['physical_target'];e=origin[href]['sha256']
  else:t=(A(origin).parent/href).resolve();e=None
  if Path(t).is_file():add(t,e)
for p in C['papers']:
 ident=p['id'];base=A(p['paper']);modern=ident in('P208','P209');origins={}
 for role in p['artifact_keys']:
  result=obj(role['output']);ledger=result.get(role.get('ledger_field'),{})
  for n,v in ledger.items():add(n,v,role['case'])
  for row in result.get('validated_manifests',result.get('complete_manifests_validated',[])):
   if not row['complete_nonself']:continue
   seal=A(row['path'])if'path'in row else A(row['base'])/row['name'];dig=row.get('sha256')
   if dig is None:dig=ledger[str(seal)if str(seal)in ledger else str(seal.relative_to(R))]['sha256']
   mf({'path':str(seal),'base':row['base'],'sha256':dig,'payload_rows':row['entries']},role['case'])
  rows=result
  for k in role.get('links_selector',[]):rows=rows[k]
  if not role.get('links_selector'):rows=[]
  frozen={}
  if ident=='P209'and role['case']=='artifact_p209_initial':
   for num in(0,1,2):
    f=base/('frozen_round'+str(num));m=obj(f/('FROZEN_LINK_MAP.json'if num==0 else 'ROUND'+str(num)+'_PROVENANCE.json'))
    rr=m['links']if num==0 else m['round1_core_link_map'if num==1 else'round2_historical_link_map']+m['acceptance_and_historical_anchor_link_map']
    for row in rr:
     original=str(A(row['physical_target']));d=row['sha256'];t=result['explicit_historical_aliases_used'].get(original+' @ '+d,original)
     frozen.setdefault(str(f/row['document']),{})[row['href']]={'physical_target':str(A(t)),'sha256':d}
  for row in rows:
   doc=str(A(row['document']));origin=frozen[doc]if row.get('semantic_origin')=='explicit-frozen-link-map'else A(row.get('semantic_origin',row['document']));origins[doc]=origin
  for doc in {A(r['document'])for r in rows}:
   e=ledger.get(str(doc),ledger.get(str(doc.relative_to(R))))if doc.is_relative_to(R)else ledger.get(str(doc))
   links(doc,origins[str(doc)],e,role['case']if e is not None else False,modern)
 for folder in(base,*(A(r['accepted_delta']).parent for r in p['accepted_reviews'])):
  docs=[Path(n)for n in manifests[str(folder)]if n.endswith('.md')]
  for doc in docs:
   origin=Path(re.sub(r'/frozen_round[012]/','/',str(doc)))if ident=='P205'else origins.get(str(doc),doc)
   links(doc,origin,modern=modern)
 stage('artifact_and_links_'+ident)
print(json.dumps({'status':'DATA_ONLY_SOURCE_SELECTION_NO_OLD_PROGRAM_OR_HOST_SCAN','stages':stages,'selected_keys':len(names),'expected':142784,'rich_original_rows_selected':len(set(rich)&names),'partial_original_rows_selected':len(set(partial)&names),'metadata_read_count':len(metadata),'manifest_bases':len(manifests)},sort_keys=True))
