# Fifth scout source, encoding and replay record

2026-09-05 UTC. Scope: six rejected literals in this directory.
All web reading was read-only. No manuscript, local PDF, source code or
private material was uploaded, and no external specialist was contacted.

## Primary sources actually read

| Source | Actual read scope and relevance | Boundary |
|---|---|---|
| Jesús Leaños, Rutilo Moreno, Luis Manuel Rivera-Martínez, *On the number of mth roots of permutations*, Australasian Journal of Combinatorics 52 (2012), 41–54; [journal PDF](https://ajc.maths.uq.edu.au/pdf/52/ajc_v52_p041.pdf) | Main author read pp.41–43 including Theorem 1; §3 pp.46–47; Proposition 7 and §4.1 pp.47–49. A separate agent independently checked those contexts and author arXiv metadata. | The $m=2$ specialization owns the entire permutation-square-root primitive used by GHD's exact adapter. It is not a theorem on GHD iterates or roots inside arbitrary subgroups. No journal DOI is invented. |
| O. Colón-Reyes, A. S. Jarrah, R. Laubenbacher, B. Sturmfels, *Monomial Dynamical Systems over Finite Fields*, [author preprint math/0605439](https://arxiv.org/pdf/math/0605439), submitted 2006 | First three PDF pages and §2 through Lemma 2.7, Corollary 2.8 and Theorem 2.9 with proof on p.4. The first page also states unique reduced polynomial representations. | The support reduction and logarithmic linearization on the nonzero torus are established mechanisms. XCY's explicit determinant graph is our own adapter; the source does not enumerate its constrained inverse fibres. The inconsistent 2018 typesetting footer is not used as publication metadata. |
| William Carter, *New Examples of Torsion-Free Non-unique Product Groups*, [author preprint arXiv:1302.0049v4](https://arxiv.org/pdf/1302.0049), 2013 | First three PDF pages: definition of unique product and statements of its torsion-free construction results. | This is a direct primary context for ordered unique products and squares of subsets, not an owner of the finite feedback UOP or its iterates. The construction proofs were not read or imported. |

No full-paper reading is asserted beyond these scopes. The source-root
formula in PROOF_BOUNDARIES is a specialization, with an explicitly proved
whole-source adapter; it is not a new theorem credited to this lane.
No claim from the Carter introduction about the present status of group-ring
conjectures is made.

Focused searches included group products with inverse, symmetric-group
square roots, the literal words $g^2h$ and $gh^2$, cyclic cross-product
dynamics, monomial finite-field systems, derivative-composition feedback,
Wronskian/product iteration, logarithmic derivatives and ordered unique
products. Additional arXiv-domain searches supplied primary candidates.
Irrelevant scalar polynomial evaluation dynamics were not treated as
coefficient-state DCP owners. Search misses are neither novelty nor priority
clearance for any of the six rows.

An IACR logarithmic-derivative PDF retrieval returned an internal error;
it was not read and carries no theorem evidence here. The WPP ratio identity
is derived directly in PROOF_BOUNDARIES. No speculative Cartier or
all-characteristic logarithmic-derivative theorem is invoked.
A few initially abbreviated local paths failed to resolve; corrected
paths below were read before any corresponding subtraction was used.

Research-lit's optional Zotero and Obsidian tools were unavailable.
The arxiv_fetch helper was not found, so the documented arXiv web-search
fallback was used. The local library/history was searched first; relevant
old manuscript source and literal maps were read instead of unrelated PDFs.
No external PDF was saved into the workspace.

## Internal collision checks and exact scope

The nine read-only historical inputs are pinned in
[INPUTS.sha256](INPUTS.sha256), relative to the workspace root.

- [P103 source](../../../../papers/103-double-adjugate-matrix-dynamics/main.tex):
  the opening sections, double-adjugate identity and iterate normal form
  were read. Its occupied engine is determinant times a matrix, followed
  by scalar-power recurrence. XCY is not literally P103 and is not claimed
  to be globally conjugate to it; the exact two-step monomial restriction
  is written out separately.
- [P157–P161 replacement geometry](../../../papers157_161_sequence/scouting/replacement_geometry_mechanism/SCOUT.md):
  the PDU subsection on polar projective triangles was read. It identifies
  opposite-side cross products with a three-by-three adjugate. Its
  projective-triangle carrier is not the four-vector XCY carrier.
- [P117–P121 algebra scout](../../../papers117_121_sequence/scouting/ALGEBRAIC_PHASE2B_SCOUT.md):
  B2B-05 and B2B-06 were read, including the class-two central translation
  and involution-pair mutual-sandwich product-cubing formula. These literals
  are excluded, not re-counted or asserted equivalent to TQP.
- [P172–P176 fresh algebra](../../../papers172_176_sequence/scouting/fresh_nonlinear_algebra/SCOUT_AND_KILL_LEDGER.md):
  G02/MCF is exactly mutual conjugation. It is a desk exclusion, not GHD
  or TQP.
- [P162–P166 sixth replacement ledger](../../../papers162_166_sequence/scouting/open_fresh_p166_round6/IDEA_LEDGER.md):
  the XSD row is exactly projective point subsets mapped to dual lines
  containing exactly two source points. It is excluded before pilots.
- [P197 nonlinear fifth scout](../../../papers197_201_sequence/scouting/nonlinear_fifth_20260905/SCOUT_AND_DISPOSITION.md):
  UPR counts unordered distinct XOR pairs; CPA uses canonical $ff'$.
  Both full literal descriptions and their stated failure boundaries were
  read. UOP includes ordered and diagonal pairs, while DCP composes the
  derivative; no full conjugacy to these older literals is asserted.
- [P197 geometry reopening](../../../papers197_201_sequence/scouting/geometry_reopen_20260905/SCOUT_AND_DISPOSITION.md):
  the complete CSP description, norm-factor limitation, XPF/PDU exclusions
  and double-cross monomial desk filter were read. It explicitly records
  the occupied cross-product family and distinguishes genuine nonmonomial
  norm feedback from a monomial reduction.
- [P182–P186 algebra ledger](../../../papers182_186_sequence/scouting/algebra_lane/SCOUT_AND_KILL_LEDGER.md)
  and [P197 late tree ledger](../../../papers197_201_sequence/scouting/final_seat_tree_lane_20260905/LEDGER.md):
  the BHD rows were read. The second explicitly excludes the affine
  binary-quartic Hessian lift, without claiming projective/vector conjugacy.
  Hessian feedback therefore contributes no extra executed row.

The current batch's preceding four lanes were checked during intake.
This list is the narrower pinned subtraction boundary, not a claim to
have read every historical manuscript or proved absolute nonduplication.

## Exact finite encodings and dependency key

Runtime: Python 3.12.3, standard library only. The producer imports
collections.Counter, hashlib.sha256, itertools.permutations/product and
json. It reads no external files or data, uses no random seed, no persistent
cache, no environment-dependent scientific parameters and no network.

Final producer SHA-256:
04ff77b02216c5265c9436d0c349463c84645beb874d411ecfca00550212dc61.

- Symmetric permutations and alternating permutations are lexicographically
  ordered tuples on zero-based labels. Pair coordinates are group indices.
- $D_8$ is $(a,e)\in\mathbb Z_4\times\mathbb Z_2$ in lexicographic order,
  with product $(a+(-1)^e b,e+f)$.
- $Q_8$ index is twice the unit index plus the sign bit; units are
  $1,i,j,k$, and sign bit one is negative.
- Group subsets are integer masks, bit equal to element index.
- Field vectors and polynomial coefficient tuples are lexicographic.
  Coefficients run from constant to highest degree. XCY uses vector
  indices, and WPP uses polynomial indices, not coefficient values as indices.
- DCP composes by evaluation at each field element and looks up the unique
  reduced coefficient tuple. WPP multiplies by truncated convolution.
- Each all-state digest line is JSON containing rule, parameters, source,
  target, tail and period, using sorted keys, compact separators and LF.
  The canonical is the complete pretty-printed producer stdout, not a
  separately edited result table.

## Actual runs and retained failure

1. Initial fixed-box producer completed with exit zero:
   21 boxes, 574,166 states, 1,148,389 assertions; scientific digest
   6224bb188fcc21b11288dda94d342ce809a5d78efede05dba0ad6e7f5698f20f.
   This exploratory output was shown in the execution record but was not
   separately frozen as an initial producer/canonical artifact.
2. Adding the GHD/TQP/XCY mathematical assertions caused one immediate
   syntax failure before checks ran: a missing closing square bracket in
   the TQP target expression, reported at line 183:
   ~~~text
   SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
   ~~~
   The bracket was repaired. No mathematical assertion failure or
   parameter alteration was hidden by that fix.
3. A final-version completion then exited zero with all 1,713,958 assertions.
   Its scientific all-state digest remained unchanged.
4. Two additional fresh final-version processes were launched by the
   exact wrapper below. Both completed successfully, and complete stdout
   was compared in memory as raw bytes, before any decoding or JSON parse.

Working directory for every producer run:
/root/autodl-tmp/symbolic_dynamics.

~~~python
import subprocess, hashlib, json
command = ['python3','docs/papers204_208_sequence/scouting/graph_algebra_fifth/pilot.py']
runs = [subprocess.run(command, capture_output=True) for _ in range(2)]
assert all(run.returncode == 0 and not run.stderr for run in runs)
assert runs[0].stdout == runs[1].stdout
print(json.dumps({'command':command,'returncodes':[r.returncode for r in runs],
                 'stderr_bytes':[len(r.stderr) for r in runs],
                 'stdout_bytes':[len(r.stdout) for r in runs],
                 'raw_byte_equal':runs[0].stdout==runs[1].stdout,
                 'stdout_sha256':hashlib.sha256(runs[0].stdout).hexdigest()}))
print('CANONICAL_STDOUT_BEGIN')
print(runs[0].stdout.decode(),end='')
print('CANONICAL_STDOUT_END')
~~~

Actual wrapper result: exit zero; child exits $[0,0]$; stderr lengths
$[0,0]$; stdout lengths $[14004,14004]$; raw_byte_equal true.
Stdout SHA-256:
3e54cde3514d397e8c90b693f938301be33ad993dbe87f5825e398d44a10ce91.

The complete marked stdout, including the final LF, was saved through
apply_patch as CANONICAL.json. A physical sha256sum and byte-length check
then matched the raw producer receipt. This is the complete output, not
a normalized or regenerated summary. The assertion count includes the
new identity/fibre checks, whereas the state-space and transition digest
are unchanged.

The pair above is two new executions, not two readings of archived data.
An additional saved-canonical comparison was then executed separately;
it is not relabelled as one of that pair. It launched the same command
with subprocess.run(command, capture_output=True), loaded CANONICAL.json
with Path.read_bytes(), and asserted a zero child exit, empty stderr,
and run.stdout == canonical before decoding. Actual result:
~~~json
{"kind":"additional_saved_canonical_check_not_one_of_pair","returncode":0,"stderr_bytes":0,"stdout_bytes":14004,"canonical_raw_byte_equal":true,"stdout_sha256":"3e54cde3514d397e8c90b693f938301be33ad993dbe87f5825e398d44a10ce91"}
~~~
This is the fourth successful final-version process (the initial completion,
the two pair members, and this additional archival check), not a fourth
independent algorithm. All complete scientific stdout bytes are represented
by the raw-equal canonical. No review PASS is inferred from these repeats.

A final optional read-only spot-check of the XCY/WPP proof paragraphs
was requested from the same secondary agent after its completed GHD
source check. That follow-up returned no assessment because the process
reported a model-capacity error. No mathematical check, independent PASS
or required phase gate is claimed for this uncompleted optional request.
The closed NO_PROMOTION disposition rests on the written author proofs,
bounded exact checks and completed source adapter, not that request.

## Package integrity commands

Historical pins are workspace-root-relative:
~~~bash
sha256sum -c docs/papers204_208_sequence/scouting/graph_algebra_fifth/INPUTS.sha256
~~~

The nonself package manifest is directory-relative:
~~~bash
sha256sum -c SHA256SUMS
~~~

Run the second command from this package directory. The manifest excludes
itself and covers every other package file. No frozen historical artifact,
central index, paper directory or Git object is written by this scout.

Actual final read-only audit: all nine historical pin entries passed;
all 15 Markdown local targets existed; the canonical had 21 profiles and
574,166 total states; every cycle histogram's length-weighted sum matched
its recorded recurrent-state count. Package-manifest verification is
reported after the physical manifest is created, not inferred from this text.
