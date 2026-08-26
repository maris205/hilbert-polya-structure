# P22 Stage 4 non-literature revision draft

Status: drafting aid only. This file does not apply a patch and does not modify the manuscript, the anchored base, the block manifest, the immutable roadmap, or the author-adjudication sidecar.

Authority boundary:

- Included: `REV-002`, `REV-004`, `REV-005`, and `REV-006`, each with `author_triage: will_address`.
- Excluded without drafting: `REV-001` and `REV-003`.
- Authorized surfaces: `B0016`, `B0019`, `B0020`, `B0023`, `B0069`, `B0073`, `B0091`, and `B0092` only.
- No claim-strength authorization is present. The text below preserves the theorem's quantifiers, the two-topology scope, and the stated nonvanishing conclusions.
- Every replacement below is complete block content and deliberately omits `<!--block:...-->` markers.

## B0016 — REV-005

- Authorized operation: `replace_block`
- Manifest `old_hash`: `761cd65a2563`

### Complete `new_text`

```latex
The topology called finite-flat in
\cite[Sec.~4]{Deninger2025Rational} is distinct from the fppf topology.
Here a finite-flat covering family of an affine scheme \(U\) means a
jointly surjective family \(\{U_i\to U\}\) in which every morphism is finite
and flat; on affines, the corresponding ring maps are finite locally free
and their spectra jointly cover \(U\).  We use the associated subcanonical
topology, so representable presheaves, and in particular the structure
sheaf used below, satisfy descent.  We therefore state the finite-flat
conclusion separately rather than deriving it formally from
Theorem~\ref{thm:fppf}.
```

### Mathematical reason

This replacement fixes the convention at its first use: covers may be families, joint surjectivity supplies the covering condition, and finite flat maps are finite locally free in the affine setting used throughout the proof. It also states the exact subcanonicity consequence later used to interpret restrictions and the structure sheaf. The original separation between the fppf theorem and the finite-flat theorem is unchanged.

### Potential TeX or semantic risk

The set braces in `\{U_i\to U\}` must remain escaped. No new macro or label is introduced. The phrase “covering family” intentionally matches the later family-based refinement argument; changing the intended convention to singleton covers would require an author decision, not a TeX repair.

## B0019 — REV-004

- Authorized operation: `replace_block`
- Manifest `old_hash`: `3ec0dcea42b6`

### Complete `new_text`

```latex
There is also a useful extension-theoretic formulation.  For
\(\tau\in\{\fppf,\ff\}\), regard \(\omega\colon\Zsh\to\Wsh\) as a morphism
in \(\mathrm{Ab}(\mathscr C_\tau)\), put
\(\Ksh_\tau=\ker(\omega)\), and let
\[
 e_\tau:\quad 0\longrightarrow\Ksh_\tau\longrightarrow\Zsh
 \xrightarrow{\omega}\Wsh\longrightarrow0
 \tag{1.1}\label{eq:extension}
\]
denote its class in
\(\Ext^1_{\mathrm{Ab}(\mathscr C_\tau)}(\Wsh,\Ksh_\tau)\).
When one topology is fixed below, the unadorned symbols \(\Ksh\) and \(e\)
abbreviate \(\Ksh_\tau\) and \(e_\tau\), respectively.  Standard
pushout--pullback functoriality then gives the following consequence.
```

### Mathematical reason

The two extension classes now visibly live in different abelian categories. Indexing `\Ksh_\tau`, `e_\tau`, and the Ext category removes any suggestion that the fppf and finite-flat classes are literally one object. The explicit abbreviation convention keeps later unindexed occurrences meaningful without touching blocks outside the authorized scope.

### Potential TeX or semantic risk

`\Ksh_\tau` expands safely as `\mathcal K_\tau`, and the existing `\Ext` operator accepts the category subscript. The unique equation tag and label are retained. The long inline Ext expression may create an overfull line under narrow layouts, but it is syntactically valid and can be line-broken later without changing content.

## B0020 — REV-004

- Authorized operation: `replace_block`
- Manifest `old_hash`: `dc200f870c5f`

### Complete `new_text`

```latex
\begin{corollary}[Extension obstruction]\label{cor:ext}
For \(\tau\in\{\fppf,\ff\}\), \(N>1\), and every endomorphism
\(u\colon\Ksh_\tau\to\Ksh_\tau\) in
\(\mathrm{Ab}(\mathscr C_\tau)\),
\[
 u_*e_\tau\ne V_N^*e_\tau
 \qquad\text{in }
 \Ext^1_{\mathrm{Ab}(\mathscr C_\tau)}(\Wsh,\Ksh_\tau).
\]
In particular, \(e_\tau\ne0\) and \(V_N^*e_\tau\ne0\) for both values of
\(\tau\).
\end{corollary}
```

### Mathematical reason

The corollary now quantifies the topology before the kernel endomorphism and states the inequality in the correct topology-specific Ext group. It preserves the original universal quantifiers over `N` and `u` and preserves both nonvanishing consequences.

### Potential TeX or semantic risk

The display is longer than the original and may need ordinary line breaking, but all commands are already available. The wording “for both values of `\tau`” refers exactly to the displayed closed set and does not introduce a third site.

## B0023 — REV-006

- Authorized operation: `replace_block`
- Manifest `old_hash`: `a2884928fac8`

### Complete `new_text`

```latex
The proof isolates a reusable descent-obstruction template.  Let
\(p\colon Z\twoheadrightarrow W\) be an epimorphism of abelian sheaves,
let \(w\in W(U)\), and suppose that a cover \(f\colon V\to U\) admits a
unique section \(z_V\in Z(V)\) with \(p(z_V)=f^*w\).  If the two pullbacks
of \(z_V\) to \(V\times_U V\) differ by a nonzero section of
\(\ker(p)\), then \(w\) has no global preimage in \(Z(U)\): any global
preimage would restrict to \(z_V\) and hence would have equal pullbacks.
Whenever a proposed middle-object lift would supply such a global
preimage, that lift is impossible; for a short exact sequence with class
\(e\), Proposition~\ref{prop:extcriterion} translates the same
nonexistence into the inequality \(u_*e\ne v^*e\) for every possible
induced kernel endomorphism \(u\).

In the present argument, \(p=\omega\), \(U=\Spec k[x]\),
\(V=\Spec k[s]\), and \(w=1-xT^N\).  The roots-of-unity product supplies
the local preimage, Dedekind injectivity makes it unique, finite freeness
and subcanonicity validate the cover and its restrictions on each site,
and the truncated-nilpotent big-Witt detector together with
torsion-freeness proves that the overlap difference is nonzero.  These
are the arithmetic and site-specific inputs; the preceding implication is
the reusable categorical core.
```

### Mathematical reason

The first paragraph extracts only the formal implication already used by the proof: local uniqueness forces the restriction of any hypothetical global preimage, while a nonzero double-overlap difference contradicts descent. The second paragraph identifies, without strengthening them, the exact Witt-theoretic, arithmetic, and site-dependent ingredients that discharge this template in the manuscript. The final Ext statement is explicitly tied to Proposition 5.1 rather than to a new Čech-to-derived comparison.

### Potential TeX or semantic risk

All notation uses existing commands; `V\times_U V`, `\ker(p)`, and `\Spec` compile without new packages. The abstract template assumes a single covering morphism, matching the finite-free root cover actually used. Generalizing it to an arbitrary covering family would require extra indexing and is intentionally avoided.

## B0069 — REV-004

- Authorized operation: `replace_block`
- Manifest `old_hash`: `b2e8b3bd4d8d`

### Complete `new_text`

```latex
For each \(\tau\in\{\fppf,\ff\}\), we relate the concrete failure to the
topology-indexed extension class \(e_\tau\) in
\eqref{eq:extension}.  The required statement is formal in the abelian
category \(\mathrm{Ab}(\mathscr C_\tau)\), but making the two functorial
directions explicit prevents a common ambiguity.
```

### Mathematical reason

This sentence binds Section 5 to the same topology-specific family introduced in B0019. It does not change the formal proposition that follows; it only identifies the ambient category in which that proposition is applied.

### Potential TeX or semantic risk

The replacement depends on the indexed notation introduced in B0019 and should travel in the same revision. The existing equation reference is preserved, and no environment boundary changes.

## B0073 — REV-004

- Authorized operation: `replace_block`
- Manifest `old_hash`: `b74b0e53b294`

### Complete `new_text`

```latex
\begin{proof}[Proof of Corollary~\ref{cor:ext}]
Fix \(\tau\in\{\fppf,\ff\}\).  Apply
Proposition~\ref{prop:extcriterion} in
\(\mathrm{Ab}(\mathscr C_\tau)\) to the extension \(e_\tau\) in
\eqref{eq:extension}, with \(v=V_N\).  Equality
\(u_*e_\tau=V_N^*e_\tau\) would produce an additive middle-object
morphism \(\Zsh\to\Zsh\) on \(\mathscr C_\tau\) lifting \(V_N\), contrary
to Theorem~\ref{thm:fppf} when \(\tau=\fppf\) and to
Theorem~\ref{thm:ff} when \(\tau=\ff\).  Hence the two classes are unequal
for every \(u\colon\Ksh_\tau\to\Ksh_\tau\).  In the final paragraph of
this proof, the unadorned \(e\) and \(\Ksh\) abbreviate \(e_\tau\) and
\(\Ksh_\tau\).
```

### Mathematical reason

The proof now fixes one topology, applies the abstract criterion in its correct abelian category, and dispatches to the matching nonlift theorem. The last sentence is scope-preserving: B0074 remains unedited but its unindexed `e` is explicitly an abbreviation for the fixed `e_\tau`.

### Potential TeX or semantic risk

Do not add `\end{proof}` to this block: the proof continues through B0074, which already closes the environment. Removing the abbreviation sentence without separately authorizing B0074 would reintroduce the notation ambiguity this revision is meant to resolve.

## B0091 — REV-002

- Authorized operation: `delete_block`
- Manifest `old_hash`: `02b300464d60`

### Complete `new_text`

`new_text = ""` (the actual `delete_block` operation carries no `new_text` field).

### Mathematical reason

The deleted paragraph contains only project-internal Route and Gate labels. B0090 already states the mathematical scope, and B0092 already states the conclusion, so removing B0091 changes no definition, hypothesis, proof step, or conclusion.

### Potential TeX or semantic risk

There is no TeX environment or label in the deleted block. The deterministic block deletion must retain normal paragraph separation between B0090 and B0092; no replacement prose is needed.

## B0092 — REV-006

- Authorized operation: `replace_block`
- Manifest `old_hash`: `8210745f6eae`

### Complete `new_text`

```latex
The conclusion is therefore exact and modest.  Local root factorization
does produce the expected rational Witt section, but Dedekind injectivity
forces a local representative whose double-overlap difference survives
sheafification.  That single explicit descent failure rules out every
nontrivial additive Verschiebung lift on both sites and, for each
\(\tau\in\{\fppf,\ff\}\), realizes the failure as the nonzero pullback
extension class \(V_N^*e_\tau\).

The reusable mechanism is the implication from a unique cover-local
preimage with a nonzero overlap difference to the absence of a global
preimage, followed by the formal pushout--pullback translation.  The
example-specific verification consists of four finite algebra
calculations: a root cover, a roots-of-unity product, one tensor-product
overlap, and one truncated-polynomial specialization.  This explicit
chain is the principal verification artifact of the note.
```

### Mathematical reason

The first paragraph preserves the all-index, two-site nonlift and nonzero pullback-class conclusions while making the topology index explicit. The second separates the categorical implication from the four concrete algebra calculations, echoing the abstract template in B0023 without adding a broader theorem or changing the paper's stated scope.

### Potential TeX or semantic risk

`e_\tau` depends on B0019 landing in the same revision round. The blank line intentionally creates two paragraphs. No citation, label, environment, or new macro is introduced.

## Cross-block consistency notes

- B0019 defines `e_\tau` and `\Ksh_\tau`; B0020 states the indexed result; B0069 and B0073 use the same notation.
- B0073 explicitly licenses the unindexed `e` in untouched B0074 for the fixed topology. No edit outside the authorized target set is required.
- B0023 states the abstract descent template; B0092 gives only its compact conclusion-level recap.
- Deleting B0091 leaves B0090's precise scope limitations and B0092's mathematical conclusion adjacent and self-contained.
- No text for REV-001 or REV-003 is proposed here.
