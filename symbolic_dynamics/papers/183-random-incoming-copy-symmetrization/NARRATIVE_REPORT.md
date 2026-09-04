# Narrative report — P183

## Problem

A loopless directed graph has two independent bits on each unordered vertex
pair.  At every epoch, a uniformly selected vertex replaces its outgoing star
by its incoming star.  The goal is to determine absorption, every-time labelled
endpoints, and inverse geometry without treating the process as a generic
finite Markov chain.

## Mechanism

Unequal opposite arcs define a simple conflict graph.  Selecting a vertex
deletes exactly its incident conflict edges.  The missing vertices after a
history therefore induce the unresolved conflict graph, making absorption an
independent-set condition.  The finer endpoint is not support-only: on each
conflict edge, the endpoint selected first determines the common surviving
bit.  Set partitions of time positions count histories with a prescribed
first-occurrence order.

## Theorem-level progress

- Conflict deletion is exact, and recurrent states are precisely the
  `2^binom(n,2)` symmetric digraphs.
- The length-`t` absorption CDF is
  `n^(-t) sum_{M independent in H(A)} (n-|M|)! S(t,n-|M|)`.
- Every labelled source-to-target multiplicity is a sum of `S(t,|S|)` over
  explicit support/first-order pairs producing the target.
- A target with `k` isolated conflict vertices has `k*2^(n-1)` labelled
  predecessor/action pairs and, if `k>0`,
  `1+k(2^(n-1)-1)` distinct predecessor states.
- The `n=1` and `t=0` boundaries are included.

## Subtraction and status

Network reciprocity, generic semigroup walks, coupon support, Stirling numbers,
and independence polynomials receive zero contribution credit.  P179 is the
closest internal clock, but its maps commute and endpoints depend only on
support; P183 has noncommuting local maps and order-sensitive endpoints.
P145, P159, and P177 use different graph operations and proof engines.

The owner search is bounded.  No novelty or priority claim is made, and the
paper remains `HOLD_EXTERNAL`.

