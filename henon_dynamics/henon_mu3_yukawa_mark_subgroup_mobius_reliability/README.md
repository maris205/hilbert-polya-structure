# HCS-C77 subgroup-lattice Möbius reliability

C77 takes the source-bound C76 support atlas one step further.  Instead of
only counting supports orbits, it computes the exact generating-closure
probability for each of the twenty subgroups of

\[
Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2.
\]

There are sixteen named labels.  A label is retained with probability
`1-q` and deleted with probability `q`, independently.  For a subgroup `H`
let `n_H` be the number of named labels whose cyclic closure is contained in
`H`.  Then

```text
P_{<=H}(q) = q^(16-n_H)
P_{=H}(q)  = sum_{K<=H} mu(K,H) q^(16-n_K).
```

The producer evaluates these expressions on the actual twenty-subgroup
poset, and independently enumerates all `2^16 = 65536` supports.  The two
polynomial constructions agree coefficient-by-coefficient for every `H`.
The top row is

```text
P_{=Q}(q) = 1-q-q^4+q^5-q^7-q^8+5q^9-3q^10
          = (1-q)(1-q^4-q^7-2q^8+3q^9),
```

which is the C73 homogeneous reliability result.

The C73--C76 authorities are bound byte-for-byte:

```text
C73 evidence: e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5
C73 manifest:  a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d
C75 evidence: 8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98
C75 manifest: 7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb
C76 evidence: 42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94
C76 manifest:  55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5
```

The canonical C77 evidence hash is
`f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.

Entry points are the producer,
independent checker, a Möbius/finite-polynomial cross-check, clean replay,
and hostile semantic mutation test under `code/`.  The canonical evidence is
under `results/`.

This is an exact finite reliability calculation for a named presentation. It
does not assert an arithmetic or local interpretation, an Euler factor, a
root number, automorphy, a full Burnside ring, or a Hilbert--Polya operator.
The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
