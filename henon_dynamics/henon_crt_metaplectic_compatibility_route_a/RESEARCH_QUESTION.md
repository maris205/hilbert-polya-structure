# Research question — HCS-C136

For the C131 odd-level quantization of

\[
A=\begin{pmatrix}3&-1\\1&0\end{pmatrix},
\]

does the canonical Chinese-remainder identification of
`C^(MN)` with `C^M tensor C^N` intertwine the frozen Weyl, Fourier, chirp,
and unitary operators when `M,N>1` are coprime odd levels?

Does the canonical antiunitary `Theta_[r,c]=F_[r,c] K_r` both reverse the
generalized evolution and factor under the same CRT map, so that the claimed
natural quantization includes an exact time-reversal test rather than only
unitarity and Egorov covariance?

The question is deliberately split into two falsifiable parts:

1. Which local additive characters are induced by the standard character at
   level `MN`, and do they give an exact tensor identity without an unspecified
   scalar?
2. For a fixed ordered list of pairwise-coprime odd factors, does iterating the
   construction give the same local characters for every binary split schedule
   and parenthesization, without asserting factor-permutation coherence?
3. Does `Theta` satisfy `Theta^2=I`, `Theta U Theta^(-1)=U^(-1)`, and
   `Theta W(q,p) Theta^(-1)=W(p,q)` for every odd level and unit character?

A mandatory negative control asks whether one may erase the induced inverse
scalings and tensor the standard `c=1` factors directly.  The theorem must
reject that shortcut already at `(M,N)=(3,5)`.

Success means an exact, source-owned cross-level coherence theorem.  It does
not mean a target divisor match, an analytic completion, a semiclassical trace
law, or Route-B readiness.
