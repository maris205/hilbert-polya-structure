# P203 source verification and contribution boundary

Date: 2026-09-05 UTC. **OWNER_AMBER / HOLD_EXTERNAL**. No global novelty
or priority claim. This is an author source memo, not a manuscript review.

## Actual primary metadata and reading

Both bibliography entries were retrieved by DOI content negotiation with
`Accept: application/x-bibtex`, then checked against actual primary text.
Fomin's metadata response completed in tool receipt `01d170`; Johnson's
DataCite/arXiv response in `058045`. Only keys, TeX accents and dash syntax
were normalized when writing references.bib. There are exactly two cited
entries and no invented internal papers in the external bibliography.

| Entry | Verified metadata | Actual claim-supporting reading |
|---|---|---|
| Fomin, Golovach, Strømme, Thilikos, Subgraph Complementation | Algorithmica 82(7), 1859–1880 (2020), DOI 10.1007/s00453-020-00677-8 | Author-hosted publisher PDF, abstract and §1 through formal induced-complement definition and stated algorithmic scope |
| Shuldiner, Oldford, The Clique Structure of Johnson Graphs | arXiv:2208.12710v1 [math.CO] (2022), DOI 10.48550/arXiv.2208.12710 | Primary v1 HTML and arXiv record; §3 Propositions3.1–3.2, Remark3.3, full Theorem3.4 proof and Corollary3.5 |

Primary access links:
[Fomin publisher PDF](https://fedorvf.github.io/articles/2020/2020d.pdf),
[Johnson v1 text](https://arxiv.org/html/2208.12710v1),
[Johnson arXiv record](https://arxiv.org/abs/2208.12710).
Exact retrieved bytes are physically stored in sources/ and covered by its
own manifest. The Fomin PDF contains publisher front matter before the
article, so the formal definition occurs on physical PDF page4 (1-based),
not an invented article page citation. No claim of reading all later
algorithmic proofs is made. The Johnson bibliography explicitly cites the
read v1 preprint, not an unverified later publication.

## Fully deducted prior inputs

The Fomin operation changes the induced subgraph on a chosen vertex set;
our size-three flip is an instance. The primitive is not new. Its inspected
algorithmic scope asks whether some set reaches a chosen graph class, not
the repeated least-monochromatic-triple schedule.

Johnson star/top containment and capacity are classical static input.
Applying the familiar classification to three-subsets yields capacities
n−2 and four. Both the classification and this bound receive zero credit;
the elementary three-set proof is reproduced with explicit attribution.
The schedule-specific inverse work is actual D/C feasibility, attainable
targets and the S/K colour/order iff certificates, not a new clique theorem.

Generic least-involution descent, undoing a candidate move, eventual fixed
or two-cycle behavior, Ramsey background and finite-state enumeration also
receive zero credit. The residual temporal theorem uses alternating
colours to exclude vertex returns, especially the initially retired
vertex, and a uniform sharp construction. The inverse and temporal proofs
do not follow from one another.

## Internal owner boundaries

The exact earlier history search and primary query list are physically
preserved in current_inputs/SOURCE_OWNER.md. This author inspected the
focused Q01 section, P112 literal, P123 component update, P152 stochastic
triad literal, and the previously fully reviewed P200 row-support proof.
Q01/LFCTR is one historical literal, not two new controls: least cyclic
triangle reversal on tournaments. The generic selector is common, but the
same-n full maps differ (n4 fixed counts24 versus18). That obstruction
does not exclude every possible restriction, embedding or time change.
P200's row-comparability pivot mechanism is a serious generic proof-engine
neighbor; it does not by itself supply the MCT alternating-colour return
obstruction or the ordered-colour star/top feasibility theorem. Different
carrier nouns are not taken as proof of originality.

The record is bounded. In particular P51–P56 artifact gaps remain; no
claim that all historical manuscripts or every external source was reread
is made. The current root adjudication and LFCTR count correction are
physical snapshots for provenance, not live dependencies or manuscript
breadth-count claims.

## Review and archival limits

Stage1 accepted internally amber but retained Minor1 for missing authentic
intermediate author-code bytes. PROVENANCE.md gives the unchanged old pin
and distinguishes it from complete current paper inputs. Stage1 is not
paper A or B. Fifth and LZK contributed the mathematics and cannot be the
independent P203 manuscript reviewers. FOSP's optional vertex-zero lemma
is not in this manuscript or used to repair its original proof. No
external review endpoint, model-diversity endorsement or upload is claimed.
