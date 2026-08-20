# C78 theorem package

## Definition (repair distance)

Let \(L=\{S_1,\ldots,S_{16}\}\) be the frozen labels.  For a deletion set
\(D\subseteq L\), let \(A=L\setminus D\) be retained and let
\(\Phi(A)\leq Q\) be its generated subgroup.  Define

\[
 \rho(D)=\min\{|R|:R\subseteq D,
                  \Phi((L\setminus D)\cup R)=Q\}.
\]

The minimum exists because the complete label set generates \(Q\).  The
quantity counts restored labels, so it is different from the deletion count
\(|D|\) (and from the retained count \(16-|D|\)).

## Theorem 1 (finite repair bound)

For every one of the 65536 deletion sets, \(0\leq\rho(D)\leq3\).  Exact
enumeration gives

\[
 |\{D:\rho(D)=0\}|=30400,
\quad |\{D:\rho(D)=1\}|=32704,
\]
\[
 |\{D:\rho(D)=2\}|=2368,
\quad |\{D:\rho(D)=3\}|=64.
\]

The four counts sum to \(2^{16}\).

## Theorem 2 (bivariate inventory)

Set

\[
 \mathcal P(x,y)=\sum_{D\subseteq L}x^{|D|}y^{\rho(D)}
 =\sum_{k=0}^{16}\sum_{r=0}^{3}N_{k,r}x^ky^r.
\]

The exact coefficient vectors \((N_{k,0},N_{k,1},N_{k,2},N_{k,3})\) are

\[
\begin{array}{c|rrrr}
k&0&1&2&3\\\hline
0&1&0&0&0\\
1&15&1&0&0\\
2&105&15&0&0\\
3&455&105&0&0\\
4&1364&456&0&0\\
5&2992&1375&1&0\\
6&4950&3047&11&0\\
7&6269&5116&55&0\\
8&6095&6609&166&0\\
9&4504&6595&341&0\\
10&2461&5040&506&1\\
11&940&2871&551&6\\
12&224&1151&430&15\\
13&25&289&226&20\\
14&0&34&71&15\\
15&0&0&10&6\\
16&0&0&0&1
\end{array}
\]

Here \(x\) marks deleted labels (not retained labels).  Consequently,

\[
 \mathcal P(x,1)=(1+x)^{16},
 \qquad
 \mathcal P(1,y)=30400+32704y+2368y^2+64y^3.
\]

## Proof/certificate boundary

The statements are finite, exact consequences of the point-set group law and
the frozen named coordinates.  The producer and independent checker enumerate
all masks; neither relies on floating point, random sampling, or an abstract
isomorphic subgroup lattice.  The receipt records source hashes and is tested
by clean replay and hostile semantic mutations.

No arithmetic/local, Euler-factor, root-number, automorphy, full
Burnside-ring/table-of-marks, or Hilbert--Polya claim follows from this finite
theorem.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
