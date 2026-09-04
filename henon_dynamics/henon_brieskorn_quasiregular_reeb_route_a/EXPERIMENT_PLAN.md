# Exact verification plan

## Claim gates

1. Verify the declared contact-form normalization by checking
   \(\alpha(R)=1\), \(\iota_Rd\alpha=-d\|z\|^2\) in the ambient space, and
   \(df(R)=2\pi i f\).
2. For every allowed pair with (q\le101), reconstruct the principal period
   (2pq), three exceptional periods, isotropy orders, and quotient dimensions.
3. Classify every integer time (1\le T\le2pq) using the divisibility set
   (J_T=\{j:T/a_j\in\mathbb Z\}). Commit per-pair and global streaming
   digests.
4. Recompute the three transverse rotation numbers, real return determinants,
   first degenerate covers, and every nondegenerate pre-degeneracy CZ index.
5. Recompute the reduced orbifold Euler characteristic and the principal
   Robbin--Salamon index, including the unique positive pair and absence of a
   zero-index pair.

## Frozen scale

- 1,003 coprime odd parameter pairs (3\le p<q\le101);
- 5,469,178 fixed-time classification cells;
- 4,012 orbit-type rows;
- 3,009 transverse-rotation rows;
- 103,749 nondegenerate CZ-index cells;
- 1,003 Seifert/index rows.

## Independent lanes

- canonical producer with strict YAML input;
- checker sharing no producer code and rebuilding the complete ledger;
- SymPy normalization and identity checks;
- two isolated byte-identical producer replays;
- repaired-hash semantic, type, JSON, YAML, scope, and mathematical mutations;
- three manuscript rounds, each compiled twice in fresh directories at epoch
  `1788480000`;
- exact 27-payload manifest closure.

Finite enumeration is a regression receipt, not a proof of the uniform
theorem. The analytic proof is in `THEOREM_PACKAGE.md` and `paper/main.tex`.
