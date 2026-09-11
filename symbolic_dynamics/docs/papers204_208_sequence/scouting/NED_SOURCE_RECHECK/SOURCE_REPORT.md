# NED bounded primary-source recheck: body still unavailable

2026-09-07 UTC. **HOLD_SOURCE / NO_PROMOTION**.

The six authorized routes did not obtain the primary full body of C.
Cannings and J. Haigh, *Montreal Solitaire*, Journal of Combinatorial
Theory, Series A 60(1), 50–66 (1992),
[DOI 10.1016/0097-3165(92)90037-U](https://doi.org/10.1016/0097-3165(92)90037-U).
No theorem/proof range from that paper was newly read. The source hold is
unchanged; this does not close or otherwise rescue NED's old proof/value
obligations.

## Exact bounded routes and outcomes

Routes were declared before fresh retrieval in [INTAKE.md](INTAKE.md).
All six finished within 45 seconds; the longest was approximately 3.947
seconds. No retry loop, specialist contact, paywall bypass, credential use,
manuscript upload or seventh route occurred.

| Route | Literal route and elapsed time | Actual result | Evidence |
|---|---|---|---|
| 01 | One bounded web call: exact title/authors/PDF, arXiv-indexed exact title, and exact PII/PDF queries; 3.489 s | Bibliographic and secondary results; no retrieved primary full body. The arXiv fallback query is recorded even though it did not yield this original article. | [Request](routes/01/request.json), [complete tool return](routes/01/tool_return.json), [elapsed receipt](routes/01/receipt.json) |
| 02 | DOI resolver followed by native redirects; 3.947 s | HTTP 200, 2,627-byte HTML **redirect page** at Elsevier Linking Hub, not article text or PDF. Its ordinary target is ScienceDirect. | [Native receipt](commands/route_02/receipt.json), [HTTP/status output](commands/route_02/stdout.raw), [headers](routes/02/response.headers), [body](routes/02/response.body) |
| 03 | OpenAlex exact DOI record; 0.886 s | HTTP 200, 6,405-byte metadata JSON. It reports closed access, no repository full text and no PDF URL. Those fields are this index's report, not proof that no legal copy exists anywhere. | [Native receipt](commands/route_03/receipt.json), [returned JSON](routes/03/response.body) |
| 04 | Semantic Scholar exact DOI/openAccessPdf fields; 1.039 s | HTTP 200, 441-byte metadata JSON. It reports BRONZE/publisher-specific OA, but its purported PDF URL is only the DOI resolver, not a fetched PDF. | [Native receipt](commands/route_04/receipt.json), [returned JSON](routes/04/response.body) |
| 05 | Direct public ScienceDirect PII `/pdf` endpoint; 1.920 s | HTTP 403 and 832,802-byte HTML response, not PDF. Curl itself exits 0 because it successfully transfers the HTTP error response; acquisition fails at the HTTP/body level. | [Native receipt](commands/route_05/receipt.json), [HTTP/status output](commands/route_05/stdout.raw), [headers](routes/05/response.headers), [complete error body](routes/05/response.body) |
| 06 | Final ordinary browser open of the primary ScienceDirect article landing page; 2.205 s | Tool reports an internal fetch failure caused by HTTP 403 Forbidden. No primary text is returned. | [Request](routes/06/request.json), [complete tool return](routes/06/tool_return.json), [elapsed receipt](routes/06/receipt.json) |

The OpenAlex and Semantic Scholar access labels conflict. Neither label is
treated as body access, nor is the conflict resolved by guessing. The
publisher responses actually obtained here are a redirect page and an
access-error body. No PDF extraction, primary-page count, PDF preflight,
visual reading or complete-source PASS is claimed. No unavailable source
is replaced by the bibliography, OEIS, survey or search-result snippets.

## What can and cannot be compared with NED

The exact three old local notes were physically copied and pinned before
their new complete body read. [ORIGINAL_ROLES.json](ORIGINAL_ROLES.json)
maps original paths to copies and hashes; commands 01–02 retain native
copy/read argv, before/after pins, exit and full raw outputs.

From that original NED intake, the candidate is on the fixed labelled ring
$X_{n,M}=\{x\in\mathbb Z_{\ge0}^n:\sum_i x_i=M\}$. When old zeros exist,
each old positive coordinate sends one chip to its first old zero clockwise;
all sends are simultaneous. An all-positive ring is held. This is the
candidate's recorded definition, not a new theorem or an assertion about
Cannings–Haigh's primary text.

The old `SOURCE_SUPPLEMENT.md` says its author had read the stated section
of Drensky's **secondary** survey, which describes nonnegative compositions
with exterior-zero identification and a line rule that can create an end
position. It also flags reversibility of the survey's described line model
as a reason to be cautious about claiming novelty for NED's low-mass result.
That is preserved historical secondary-source evidence. This recheck did
not newly read the survey or verify the original paper behind it.

Because the 1992 body is still unavailable, this task cannot determine:

- the primary paper's exact line/ring, label, translation, exterior-zero
  trimming and all-positive-state conventions;
- whether its theorem statements or proofs already include a fixed-ring
  case, a relevant factor/quotient, inverse structure, or recurrence result;
- an exact theorem-level deduction or complete conjugacy between its full
  state space and the fixed labelled NED carrier.

The shared dispatch primitive suggested by the old secondary read is a
source lead, not a proved full-system conjugacy. Literal boundary differences
alone do not establish novelty or exclude a published ring theorem. No new
mathematical claim is made in either direction. The required next evidence
would be the actual primary body and an exact relevant theorem/proof read;
this package does not initiate another acquisition task.

## Skills, scope and closure

The project and research-lit skills were fully read. They required tracing
claims to exact original context, distinguishing metadata from primary
body evidence, and using an available fallback. Current advertised tool
discovery returned no Zotero/Obsidian names; root separately reported its
actual arXiv-helper no-match. This recheck used bounded web/arXiv-indexed
discovery and ordinary public requests, not a fabricated helper execution.
The explicit source-only scope excludes the generic skill's broad local
paper traversal and recent-literature survey.

Only this directory was written. No old NED proof, scientific kernel,
canonical, pilot, parameter box, candidate gate, review, numbered manuscript,
protected scientific body, central index or Git path was read or changed
for this task. The three original context notes contain historical exposure
disclosures; reading those disclosures does not repair the old failure or
mean their protected links were followed now. No children or new candidate
work were started.

[DOCUMENTARY_AUDIT.json](DOCUMENTARY_AUDIT.json) and its native command
record the actual checks of original copies/pins, complete old-context
stdout bytes, route count/times and preserved native outputs. Web returns
are complete serialized tool-return strings, distinguished from native
HTTP headers and bodies. `SHA256SUMS` seals every nonself artifact. Hash
closure is documentary only: the final disposition remains
**HOLD_SOURCE / PRIMARY_BODY_NOT_OBTAINED / NO_PROMOTION**.
