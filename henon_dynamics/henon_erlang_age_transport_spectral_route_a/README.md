# HCS-C272 — Erlang age-transport spectral transition

This package proves an exact semigroup theorem for a McKendrick transport
equation with an Erlang fertility boundary.  It derives every Euler–Lotka root
and proves the missing spectral gate:

\[
\lambda_j\text{ is an }L^1\text{ eigenvalue}
\quad\Longleftrightarrow\quad \Re\lambda_j>-\mu.
\]

The result separates the `beta=1` essential-edge transition from the later
population threshold.  Run the six commands in `code/README.md`; the final
paper is [`paper/main.pdf`](paper/main.pdf).  Route A is rejected, Route B is
disabled, and scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
