# HCS-P51: Abel-graded all-orbit packet germ

HCS-P51 upgrades the finite HCS-P50 prime-ideal ledger to a genuine
all-primitive-orbit analytic object.  For every primitive orbit \(\gamma\)
of the certified H6 survivor and every cyclotomic index \(n>2\), let

\[
D_{\gamma,n}=\operatorname{Div}_{F_\gamma}
\!\left(\lambda_\gamma^{-\varphi(n)/2}
\Phi_n(\lambda_\gamma)\right)
\]

in the free tagged divisor space.  The two-variable series

\[
\mathcal G(s,u)=
\sum_{\gamma\ {\rm primitive}}
e^{-s h_*\log|\Lambda_\gamma|}
\sum_{n\ge3}u^nD_{\gamma,n}
\]

converges absolutely and is Banach-valued holomorphic for

\[
|u|<1,\qquad
\Re s>\frac{\log(2\varphi)}{h_*\log J_*}.
\]

Using the certified bounds \(h_*\ge0.277980\) and
\(J_*=(\sqrt{17}+\sqrt{13})/2\), the fully executable safe half-plane is
\(\Re s>3.125206884004\ldots\).  The residue-degree rational norm map is a
continuous norm-one pushforward and is isometric on every positive packet.

The grading variable is essential.  Flatters' primitive-divisor theorem
applied to the exact period-four multiplier proves
\(\|D_{\gamma_4,n}\|\ge\log2\) for every \(n>12\).  Hence the fixed-orbit
series has radius exactly one in \(u\), and the ungraded value \(u=1\)
diverges before any all-orbit issue arises.

## Status

- **PROVED:** all-orbit Abel-graded Banach-valued analytic germ;
- **PROVED:** continuous rational norm pushforward;
- **PROVED / SOURCE-BACKED:** exact \(u\)-radius one on the period-four orbit;
- **REFUTED:** direct ungraded \(u=1\) packet sum;
- **OPEN:** Abel-boundary renormalization, analytic continuation, a
  von-Mangoldt trace law, a Fredholm determinant, and a Hilbert--Pólya
  operator.

Route A is
\((\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\mathrm{A4\_FORMAL\_HINT})\)
with overall **ROUTE_A_EXPLORATORY**.  Route B is not yet authorized.

## Reproduce

    bash code/run_c51.sh
    python -B code/generate_figure.py
    cd paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

The compiled article is [paper/paper.pdf](paper/paper.pdf).  The compact
machine certificate is
[results/c51_certificate.json](results/c51_certificate.json).
