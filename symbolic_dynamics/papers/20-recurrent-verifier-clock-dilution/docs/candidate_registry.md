# SD-C22 Candidate Registry

## SD-C22 — recurrent verifier clock dilution

    family: Symbolic Dynamics
    phase_space: one-sided countable Markov edge shift
    dynamics: expanded deterministic Q-state verifier with accepted paths closed into disjoint cycles
    endpoint: contracted terminal verification state returns directly to input
    function_space: ell^2 of graph vertices
    determinant_question: ordinary det(I-zL_s) of the whole adjacency
    orbit_product_domain: Re(s)>1 and |z|<=1
    route_b_invocation_allowed: false
    status: rejected_at_whole_operator_compactness

### Positive structural result

The alphabet-sum/tensor skeleton supplies successor, multiplication, order,
and entropy. Without a prime or factor table, the expanded verifier produces
one simple recurrent cycle for each prime. Its exact length is

\[
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\lceil p/d\rceil
\sim\frac12p\log p.
\]

Giving this cycle total roof \(\log p\) produces the correct primitive
magnitude \(p^{-s}\) and its temporal repetitions.

### Stopping boundary

The clock is spread over superlogarithmically many graph steps. Under every
nonnegative exact-clock allocation, the whole adjacency has essential norm
one and lies in no finite Schatten class. The combinatorial orbit product
survives at \(z=1\), but first return contracts the object to the Paper 04
diagonal prime-loop operator. Padded total deciders reproduce the obstruction
for arbitrary decidable supports.

### Frozen Route tuple

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_FAIL,
     A3_FAIL,
     A4_FAIL)

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED
