# Narrative report — TH-0001 on-shell real caustic

## One-sentence contribution

For the frozen ordered three-kick FIO with half-integer parameters, the
internal Hessian caustic is a real on-shell singularity of the stationary
canonical relation, with an exact rational rank-one witness, so a global
single reduced phase chart is unavailable even though the factorized operator
remains the declared object.

## Frozen object

The phase is

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\qquad
S_a(x,y)=xy-x+\frac a3x^3.
\]

The internal variables are (q_1,q_2), and the source lock fixes exact
rational arithmetic, the three-factor clock, (\hbar=1), and the positive-real
factor normalization.  No determinant, spectrum, prime table, or zero table
is part of this stage.

## Claims and evidence

| Claim | Evidence | Boundary |
|---|---|---|
| The caustic is on-shell | (15q_1q_2-1=0) and the two stationary equations give the exact (t)-parameterization | Proved for every real (t\ne0) in the frozen chart |
| It is a projection singularity | (\partial(q_0,q_3)/\partial(q_1,q_2)=-H_{\rm int}) | Local geometric identity only |
| The singularity is regular at a rational point | At (t=1), rank (H_{\rm int}=1), null vector ((-1,3)), and (D^3_{(-1,3)}\Phi=132) | One exact witness; no global normal form claimed |
| Route-A effect | A4 natural quantization remains exploratory; OBR-011 is strengthened | No Route-B authorization |

## Interpretation

The previous off-shell Hessian calculation could have been dismissed as an
artifact of arbitrary internal integration variables.  The parameterization

\[
q_1=t,\quad q_2=\frac1{15t},\quad
q_0=1-\frac32t^2-\frac1{15t},\quad
q_3=1-t-\frac1{90t^2}
\]

removes that ambiguity: the same determinant-zero set is reached by actual
stationary endpoint data.  At (t=1), direct substitution into the three
canonical kicks gives six zero residuals.  The nonzero cubic derivative in the
Hessian null direction certifies a regular rank-one caustic in the frozen
chart.

## Strict nonclaims

This stage does not provide a multi-chart phase or Maslov transition ledger,
an arithmetic orbit law, a determinant or trace formula, a spectral census,
Route B, a Hilbert–Pólya operator, or an RH result.  It is a reusable
structural obstruction and a stopping point for this sub-audit.

## Reproduction

The exact generator is copied under both `experiments/` and `src/`.  The test
rebuilds the report, checks source hashes, regenerates the JSON certificate in
a temporary directory, and verifies byte equality with the canonical artifact.
