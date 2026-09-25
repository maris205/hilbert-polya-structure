# Five-round mechanical verification

Batch `RCF01-BATCH-20260921-A`. Run from the arithmetic_symplectic_flow
directory with Node22.22.2. These checks verify artifacts and preservation,
not mathematical truth or review calibration. No scientific numerics ran.

## Checks and exact method

The following read-only command checks every new Markdown link, paired
code fence, trailing newline and the four identity/status surfaces.
It checks target existence only, not Markdown anchor resolution or websites.

```sh
node <<'JS'
const fs=require('fs'),p=require('path');
const rows=[
 ['350-transverse-graded-trace','ANG-AUDIT-20260921-TGT01','SIGNED GRADED FLAT IDENTITY ESTABLISHED; COHOMOLOGICAL OWNER OPEN'],
 ['351-contact-differential-complex','ANG-AUDIT-20260921-CDC01','CONTACT COMPLEX ESTABLISHED; ORDINARY SUPERTRACE ZERO'],
 ['352-contact-order-cohomology','ANG-AUDIT-20260921-COG01','ORDER-WEIGHTED FLAT SQUARE; COHOMOLOGICAL TRACE STOP'],
 ['353-arithmetic-clock-rigidity','ANG-AUDIT-20260921-CRG01','CLOCK NONUNIQUENESS ESTABLISHED; CONDITIONAL LOG RIGIDITY'],
 ['354-local-factor-refinement','ANG-20260921-LFR01','FULL LOCAL EXECUTOR AND PRIME PACKETS ESTABLISHED; NATURALNESS OPEN']
];
let total=0,links=0;
for(const [slug,id,status] of rows){
 const base='papers/'+slug;
 const files=fs.readdirSync(base,{recursive:true}).filter(x=>x.endsWith('.md'));
 let local=0;
 for(const f of files){
  const file=p.join(base,f),s=fs.readFileSync(file,'utf8');
  if(!s.endsWith('\n')||(s.match(/^```/gm)||[]).length%2)throw Error(file);
  for(const m of s.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){
   const v=m[1].split('#')[0];
   if(!v||/^https?:/.test(v))continue;
   if(!fs.existsSync(p.resolve(p.dirname(file),v)))throw Error(file+' '+v);
   local++;
  }
 }
 for(const f of ['candidate-card.md','paper.md','README.md','claim-ledger.md']){
  const s=fs.readFileSync(p.join(base,f),'utf8');
  if(!s.includes(id)||!s.includes(status))throw Error('surface '+base+'/'+f);
 }
 total+=files.length;links+=local;
 console.log(slug,files.length,'Markdown files',local,'relative links PASS');
}
console.log('TOTAL',total,'files',links,'relative links PASS');
JS
```

The original-card prefix is the first N newline-terminated lines, SHA-256
of their unchanged UTF-8 bytes. Prefix lengths/hashes are recorded in the
batch log and scope reports:350/100,351/101,352/88,353/88,354/146.
Paper changes in351/352 preserve their analysis prefixes; the final
check is exact prefix hashing, not another scientific re-audit.

## Historical preservation measured before final surface integration

For each old package recursively list ALL files, sort relative paths,
form each line `relativePath TAB sha256(fileBytes) LF`, and SHA-256 the
concatenated manifest. This yielded the exact opening anchors:

| Package | Files | Unchanged bundle SHA-256 |
| --- | --- | --- |
| 348 | 11 | `5255ca400be05283270cc95553d041004469a866853a26e260f25a3f0d9cc0d6` |
| 349 | 10 | `7607376f515dd6bc628e4c326baae68fe772d086ca14102e5a5256d686a4988f` |

Removing only the added batch overview block and restoring349's original
current-heading wording reproduces the exact original overview hashes:
root readme `2a80edb628002321cd76f414208dac25157c71bd17963521f1b9af96467e41ea`;
registry `c8502ba344347d6e2858c23ee37aafb8bb5b2769148247b9a9e9c67f277850ab`.
Neither old scientific package is edited after this measurement. Existing
dirty/untracked unrelated work is untouched; no Git reference, stage,
commit, external upload, LaTeX or PDF was created by this batch.

## Results

Before the final CP3 append, the exact command above returned:

```text
350-transverse-graded-trace 9 Markdown files 31 relative links PASS
351-contact-differential-complex 8 Markdown files 25 relative links PASS
352-contact-order-cohomology 7 Markdown files 22 relative links PASS
353-arithmetic-clock-rigidity 7 Markdown files 16 relative links PASS
354-local-factor-refinement 7 Markdown files 11 relative links PASS
TOTAL 38 files 105 relative links PASS
```

All17 then-existing Markdown tables passed a separate consistent-row-width
scan outside code fences. The five original card prefixes and analysis
proof prefixes350/221,351/232,352/265,353/228,354/304 matched their
recorded SHA-256 locks. This checks preservation, not the proofs again.

Untouched guidance/input hashes also matched the opening anchors:
AGENTS `86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d`;
plan `9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0`;
prior-work README `d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd`;
paper template `ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b`.

Final changed-review and overview surfaces are checked separately after
integration; unchanged scientific inputs do not require another re-audit.

Final integration check:354 review,350 batch log, Chinese summary and this
record passed link-existence, paired-fence, trailing-newline and table-width
checks; together they contain14 relative links. Both changed root/registry
overview blocks passed new-link and5/5-state checks, and removing just
those blocks again reproduced BOTH original overview SHA-256 anchors.
No old scientific input was changed or mathematically re-audited.

All five CP1/CP2/CP3 checkpoints are complete. Final354 review is167 lines,
SHA `6f02b1dc008c8effb5e7a1047b246517b1757a7b4ae6c844923002fba90f902c`.
Its CP3 inspected the scientific summary at SHA163adaa6abf973e8ef6a5c9a5c7249a43005e2976e18c16564fc0a836a9d49a3.
The subsequent summary change was workflow completion plus this verification
link ONLY; final63-line summary SHA
`f9120a0c5a1e11f00ec2374fa279c8542c7f70864568921a7c7998a718ea0d63`.
The batch now awaits user confirmation; no sixth round was started.
