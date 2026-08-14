# Paper 8 Phase-2 current-literature / novelty-exclusion audit

**Search executed:** 2026-08-14 (Asia/Shanghai)  
**Literature cutoff:** 2026-08-14  
**Verdict:** **PASS — no direct prior bridge was located within the documented search**  
**Novelty classification:** `SUPPORTED_WITHIN_SEARCH`, never “globally verified” or
“first.”

This is a bounded Phase-2 retrieval and exclusion audit.  It does not prove any
P8 target, define a packet trace, upgrade a source topology, or award Route A/B
credit.

## 1. Exact precedent test

A record counted as a **direct precedent** only if its primary text did both of
the following:

1. work with Deninger's rational-Witt finite-kernel subsystem `E_f` and its
   actual prime packets/orbits (not merely cite Deninger, use another meaning of
   “finite kernel,” or study a Bost--Connes / `ax+b` number-field system); and
2. attach that same object to at least one of:
   - the locally compact transformation groupoid for the continuous
     `R`-action and its `C*`-completion;
   - an isotropy-character / Floquet / Plancherel decomposition with a
     distinguished trivial-character trace; or
   - the same completion-level obstruction comparing that point fibre with a
     **normal** functional on the Haar-regular von Neumann completion.

Generic groupoid imprimitivity, generic Plancherel theory, generic singularity
of point evaluation in a diffuse `L-infinity` algebra, and generic trace
classification are prior mathematics; none of those facts is claimed as novel.
The question here is whether the literature already makes the **Deninger-packet
bridge** or the same fixed-object normality comparison.

## 2. Search strategy and execution log

### 2.1 Surfaces and bounds

- arXiv API metadata search (`all:` fields), all dates through the cutoff;
- OpenAlex work, author, and citation-graph metadata;
- Crossref DOI/title metadata verification (used to verify manifestations, not
  as negative-proof evidence because bag-of-words result sets were noisy);
- exact-phrase web search across publisher, author, repository, and journal
  pages;
- full-text screening of the retained primary PDFs and the already retained
  Deninger/Morishita source corpus.

English terms and mathematical notation variants were used.  The principal
families were `Deninger`, `rational Witt`, `E_f`, `finite kernel`, `prime
packet`, `Gamma_x0`, `transformation groupoid`, `C*-algebra`, `crossed
product`, `isotropy character`, `trivial character`, `Plancherel`, `normal
trace`, `normal extension`, and `point evaluation`.

### 2.2 High-precision arXiv queries

The following are exact API results observed on the search date.  A zero is a
zero for that recorded metadata query, not a universal absence statement.

| Query | Hits | Screening result |
|---|---:|---|
| `all:Deninger AND all:groupoid` | 2 | `1106.5912v3` is the unrelated Cuntz--Deninger--Laca `ax+b` false positive; `0706.0925v1` concerns a p-adic fundamental groupoid and Deninger--Werner parallel transport |
| `all:Deninger AND all:Plancherel` | 0 | no candidate |
| `all:Deninger AND all:isotropy` | 2 | `1106.5912v3` as above; `1801.07802v1` is a discrete number-field `C*` phase-transition system |
| `all:Deninger AND all:"normal trace"` | 0 | no candidate |
| `all:Deninger AND all:"rational Witt" AND all:groupoid` | 0 | no candidate |
| `all:"Dynamical systems for arithmetic schemes" AND all:groupoid` | 0 | no candidate |
| `all:"finite kernel" AND all:Witt AND all:groupoid` | 0 | no candidate |
| `all:Deninger AND all:"transformation groupoid"` | 1 | only `1106.5912v3`, the `ax+b` false positive |
| `all:"rational Witt" AND all:C*-algebra` | 0 | no candidate |
| `all:"prime packets" AND all:trace` | 0 | no candidate |
| `all:"compact packets" AND all:C*-algebra` | 0 | no candidate |

The broader query `all:Deninger AND all:trace` returned 12 records.  Eight are
dynamical/Lefschetz/foliated-flow trace or determinant papers
(`0204192`, `0204110`, `0709.2801`, `1307.3851`, `0603576`, `2402.06671`,
`2410.20758`, `2112.03191`); four are groupoid/semigroup or congruence-monoid
KMS records (`1106.5912`, `1902.03521`, `1801.07802`, `1911.00793`).  None
uses the rational-Witt finite-kernel packet as its groupoid/trace object.

The obstruction-synonym queries

```text
all:"isotropy character" AND all:Plancherel AND all:trace
all:"trivial character" AND all:groupoid AND all:trace
all:"point evaluation" AND all:groupoid AND all:normal
all:"normal extension" AND all:groupoid AND all:trace
all:"isotropy groups" AND all:"Plancherel weight"
```

each returned zero.  The broader
`all:groupoid AND all:Plancherel AND all:isotropy` returned one record,
`0308260v1`, on Fourier transform for compact groupoids; it neither concerns
Deninger's system nor the locked continuous-time transformation groupoid.

### 2.3 Citation and author graph checks

OpenAlex resolves Deninger's source as work `W2884984338`, DOI
`10.1016/j.indag.2024.05.007`.  Its citation edge query returned two indexed
citing works on the search date:

1. Deninger, *There is no “Weil-”cohomology theory with real coefficients for
   arithmetic curves*; and
2. Álvarez López--Kordyukov--Leichtnam, *Introduction* (Lecture Notes in
   Mathematics, 2026).

Neither is a packet-to-groupoid/trace bridge.  The OpenAlex author record
`A5111506881` returned 107 works through the cutoff.  Operator-algebra-bearing
hits belong to older semigroup/KMS or Fuglede--Kadison determinant programs;
the rational-Witt dynamical-system records do not acquire the proposed packet
groupoid/Plancherel trace.  The OpenAlex search `Deninger Plancherel isotropy
trace` returned zero; `Deninger rational Witt transformation groupoid`
returned ten low-relevance records, all excluded on object identity.

Semantic Scholar's API returned HTTP 429 during this audit.  That index was
therefore recorded as `API_DEGRADED`, not silently treated as a zero result.
Exact-title web searches and primary arXiv/publisher records supplied the
fallback.

## 3. Retained primary texts and disposition

### 3.1 Source side of the proposed bridge

**Christopher Deninger, “Dynamical systems for arithmetic schemes.”**  The
retained arXiv v4 is the primary locator manifestation; the journal record is
*Indagationes Mathematicae* **37**(1) (2026), 25--136,
doi:10.1016/j.indag.2024.05.007.  Section 6 and Theorem 6.1 (physical
pp. 38--39) supply the packet, period, flow, and common isotropy data.  A
full-text term screen found no `groupoid`, `C*-algebra`, `crossed product`,
`Plancherel`, `von Neumann`, `normal trace`, `semifinite`, or `isotropy
character` occurrence.  This is negative screening evidence only: Deninger
owns the source packet/clock, not the proposed analytic bridge.

The already retained Morishita v5 source was also screened.  Its sole relevant
“crossed product noncommutative algebras” occurrence describes the separate
Connes--Consani adelic quotient in Section 1.1, not a transformation-groupoid
completion or trace on Deninger's `E_f` packets.  It therefore supplies no
direct precedent.

### 3.2 Closest operator-algebra neighbours

| Primary paper | What it actually establishes | Why it is not direct precedent |
|---|---|---|
| Sergey Neshveyev, “KMS states on the C*-algebras of non-principal groupoids,” *J. Operator Theory* **70**(2) (2013), 513--530, doi:10.7900/JOT.2011SEP20.1915; retained corrected arXiv v3 | Measurable isotropy-trace fields for locally compact second-countable **étale** groupoids; Section 2 (PDF p. 6) specializes to a **countable group** acting on a space | Every `Deninger` occurrence points to Cuntz--Deninger--Laca's Toeplitz algebra of the discrete `ax+b` semigroup over a number ring, not to rational-Witt `E_f`; no Plancherel/point-evaluation normality comparison |
| Johannes Christensen and Sergey Neshveyev, “The primitive spectrum of C*-algebras of etale groupoids with abelian isotropy,” arXiv:`2405.02025v3` | Induction of one-dimensional representations of amenable isotropy groups for étale groupoids; Section 3.1 (PDF p. 12) explicitly assumes a **discrete group** action | Closest “isotropy character” neighbour, but wrong groupoid category and no Deninger/Witt, trace selection, Plancherel averaging, or normal-extension result |
| Alistair Miller and Eduardo Scarparo, “Invariant measures and traces on groupoid C*-algebras,” arXiv:`2603.04020v2`, accepted in *Bulletin of the London Mathematical Society* as of 2026-08-10 | Current trace-extension and uniqueness results for possibly non-Hausdorff **étale** groupoids and essential/full `C*`-algebras | Concerns `C*`-trace extension from invariant unit measures; it does not study a Haar-regular von Neumann completion, point-fibre normality, Deninger, or rational Witt packets |
| Jean Renault, “Continuity of the dual Haar measure,” *C. R. Math.* **359**(4) (2021), 415--419, doi:10.5802/crmath.183 | Lower-semicontinuous Plancherel weights for continuous fields of locally compact groups and continuity of dual Haar systems for abelian group bundles | Closest continuous locally compact / Plancherel neighbour, but it is a general **group-bundle** theorem, not a Deninger packet transformation groupoid and not a trivial-character versus regular-normal comparison |

The tempting primary false positive is Cuntz--Deninger--Laca,
“C*-algebras of Toeplitz type associated with algebraic number fields,”
arXiv:`1105.5352v3`, later *Math. Ann.* **355** (2013), 1383--1423,
doi:10.1007/s00208-012-0826-9.  Its object is the left-regular Toeplitz algebra
of the discrete `ax+b` semigroup `R rtimes R^x`; it predates and is not built
from the rational-Witt packet source.  It was screened and excluded rather
than retained as a load-bearing full text.

## 4. Continuous-`R` versus étale/discrete exclusion

This type distinction is decisive, not terminological.

| Literature track | Groupoid/action type | What may be reused later | What this audit withholds |
|---|---|---|---|
| Deninger packet candidate | continuous action of non-discrete `R` on an actual packet/orbit | source flow, period, isotropy only | no source-authored groupoid `C*`- or trace theorem |
| Green/MRW/Williams one-orbit baseline already audited in `phase2_groupoid_source_audit.md` | locally compact transformation groupoid for `R/(LZ) rtimes R` | general one-orbit imprimitivity/completion after hypotheses are checked | no packet bridge, packet measure, Plancherel trace, or normality result |
| Renault 2021 | continuous locally compact **group bundle** | general Plancherel/dual-Haar machinery | not itself the transformation groupoid and no source selection |
| Neshveyev; Christensen--Neshveyev; Miller--Scarparo | **étale** groupoids; transformation examples use discrete/countable groups | nearest conceptual comparisons for isotropy traces/characters and `C*` trace extensions | their étale hypotheses do not turn `Gamma_p rtimes R` into an étale groupoid and do not prove a P8 target |

Accordingly, an étale theorem is recorded as a neighbouring result, not as a
direct prior realization and not as transferable proof credit for the
continuous-`R` candidate.

## 5. Normality-obstruction exclusion verdict

No retained or screened primary paper was found that places the following
three records in one fixed comparison:

```text
Deninger E_f orbit/packet
  -> trivial isotropy-character C*-fibre functional
  -> extension along the Haar-regular von Neumann representation.
```

The retained étale papers discuss `C*` states/traces, induced characters, or
extension from invariant unit measures.  Renault discusses regular
Plancherel weights for group bundles.  None asks whether the trivial-character
point fibre is normal in the corresponding regular, diffuse dual completion,
and none applies that question to Deninger's packets.  This finding supports
the **nonredundancy of the proposed application and fixed-map comparison within
this search**.  It does not make the underlying atomless-measure/normality
lemma novel, and it does not establish the obstruction itself.

## 6. Retained artifacts, integrity preflight, and hashes

All files were downloaded from the displayed primary endpoints on 2026-08-14.
The same-stem sidecars were generated exactly once with ARS
`pdf_read_preflight/1.0.0`; all returned `PASS`, with declared, enumerated, and
reader page counts equal and empty warning arrays.  SHA-256 hashes cover the
exact local bytes.

| Local full text | Primary endpoint | Pages | PDF SHA-256 | Preflight sidecar SHA-256 |
|---|---|---:|---|---|
| `sources/nov-deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | <https://arxiv.org/pdf/1807.06400v4> | 119 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `54f65cfbb7c93e22b3b44245beec103a8252bba5c693a89944f1a0e841c9b5a9` |
| `sources/nov-neshveyev-kms-nonprincipal-groupoids-v3.pdf` | <https://arxiv.org/pdf/1106.5912v3> | 13 | `d447ac68a7b13f573a24c7b339a645b3850cdf026043f40131f86c4a6c20931f` | `882abef569275ecebebcaf92a6d02a83234d89d5138846eb060d7c223a3a7cf6` |
| `sources/nov-christensen-neshveyev-primitive-etale-v3.pdf` | <https://arxiv.org/pdf/2405.02025v3> | 34 | `4b857e99c5e1a73822898175d06ceb0a883bf3ef2ed3b9636d8e3cf8d18d4cf5` | `09650e31cc79a34b59efc3f2d99540723bd52d8dd2f55cd90c2cc358279706eb` |
| `sources/nov-miller-scarparo-invariant-measures-traces-etale-v2.pdf` | <https://arxiv.org/pdf/2603.04020v2> | 20 | `2bdc32e8b35572b4c2c5b8f8044aae85b97b911f87e7c353a4ecb89f4887c2fe` | `0906fcbbee7a8228593d824fe1adae54b0097ac7ed24401795ee4f82e81add7c` |
| `sources/nov-renault-continuity-dual-haar-2021.pdf` | <https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.183.pdf> | 6 | `d703672f7d3f70256a3f83ae5ba6c3cdd7ab87a65249fb51d7b544cc3095387f` | `ab3ac1df892acd3850bfd1c5a4f3374804dd297fbfa00a22dfd2c2daaa85da8d` |

## 7. Safe downstream novelty language

Safe:

> To our knowledge, based on the arXiv, OpenAlex, Crossref-metadata,
> publisher/author-page, exact-web, and retained-full-text searches documented
> here through 14 August 2026, we did not locate a primary paper that connects
> Deninger's rational-Witt finite-kernel prime packets to the continuous-`R`
> transformation-groupoid `C*`/Plancherel construction or formulates the same
> trivial-isotropy-character normality obstruction.  The closest results are
> generic continuous group-bundle Plancherel theory and étale/discrete
> groupoid trace or isotropy-character theory.

Unsafe:

- “This is the first groupoid trace construction for arithmetic dynamics.”
- “No previous paper contains this obstruction.”
- “Étale isotropy-trace theorems already prove the continuous-`R` case.”
- “The normality obstruction itself is new.”

## 8. Limitations and disclosure

- This is a deliberately bounded exclusion audit, not an exhaustive systematic
  review or proof of global nonexistence.  Recent-source citation graphs are
  sparse, terminology varies, and one bibliographic API degraded.
- Search-index absence and term absence are supporting indicators, never theorem
  evidence.  The five retained primary texts were read at the stated scope; no
  human-read attestation is asserted.
- AI-assisted retrieval, deduplication, full-text term screening, metadata
  checking, and drafting were used.  Any publication-level novelty sentence
  should retain the search bound above and receive an independent human check.

