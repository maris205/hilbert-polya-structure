# Hostile review

## Round 1: mathematical interface audit

### Finding 1: trace-field descent was implicit

The draft wrote \(D_n=\operatorname{Div}_{\mathbb Q}(\beta_n)\) without
immediately saying why the packet trace field is \(\mathbb Q\).

**Resolution:** the source section now states
\(T=L+L^{-1}=578\), hence \(\mathbb Q(T)=\mathbb Q\), before defining the
divisor.

### Finding 2: PDF provenance metadata was empty

The visible author was correct, but the PDF author/title metadata fields were
blank.

**Resolution:** explicit `hypersetup` metadata was added and independently
read back with `pdfinfo`.

### Attack 1: double the Abel constant

Dropping the reciprocal factor \(L^{-\varphi(n)/2}\) replaces the true
constant \(3\log L/\pi^2\) by the false value \(6\log L/\pi^2\).

**Verdict:** rejected by the exact packet identity, checker and unit tests.

### Attack 2: first-order Abel scaling

Normalizing by \(\tau\) instead of \(\tau^2\) diverges because the packet
mass has linear average order.

**Verdict:** rejected by the asymptotic theorem and an executable mutation.

## Round 2: topology and claim-strength audit

### Finding 3: “universal” was too broad

The first draft called the Gamma profile universal without specifying the
class of sequences.

**Resolution:** the paper now calls it canonical for the frozen packet and
derives its shape from the exact totient main term.

### Attack 3: turn scalar mass convergence into vector convergence

Every fixed source coordinate tends to zero, while the mass functional tends
to \(A_L>0\).

**Verdict:** norm and weak convergence are both refuted, including every
subnet.

### Attack 4: replace Gamma\((2,1)\) by an exponential profile

At \(s=1\), the exact limiting Laplace transform is \(1/4\), not \(1/2\).

**Verdict:** rejected analytically and by the finite Laplace sentinels.

### Attack 5: promote one orbit to all primitive orbits

P52 does not prove a pressure-uniform remainder or exchange the orbit and
boundary limits.

**Verdict:** rejected by the theorem ledger, Route-A record, abstract and
conclusion.

## Final verdict

**PASS WITH SCOPED CLAIMS.**  The scalar Abel law, Gamma escape profile and
tagged-space obstruction are rigorous.  The all-orbit boundary, determinant,
von-Mangoldt law and operator remain open.
