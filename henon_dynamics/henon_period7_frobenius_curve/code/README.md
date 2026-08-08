# Code

`c19_producer.py` first compares the literal printed Eq. (16) with an adopted
constant using an exact \(\mathbb F_{103}\) reversal pair.  Generic Hénon
certification is performed separately by the neighbor scripts below.  The
producer uses SymPy for exact algebra of the septic and `galois` for
finite-field point counts.
`c19_independent_check.py` does not import either the
producer or `galois`; it builds explicit polynomial-quotient fields.  The
checker also counts \(\mathbb F_{5^4}\) directly, a point not used to fit the
candidate numerator.

`c19_neighbor_correspondence.py` is the producer-side exact certificate for
the generic two-neighbor relation of the frozen septic.
`c19_neighbor_independent_check.py` reconstructs the septic without importing
either producer, reduces the full subresultant chain over
`Q(sigma)[x]/(P)`, checks the neighbor-sum, discriminant and loop remainders,
and directly enumerates the ordered-edge `tau` cycles over `F_103` and the
regular split control fibre over `F_43`.  The selected finite primes are
controls, not claimed good-reduction certificates.

```bash
python c19_producer.py --output ../results
python c19_independent_check.py \
  --certificate ../results/c19_certificate.json \
  --output ../results/c19_independent_check.json
python c19_neighbor_correspondence.py \
  --output ../results/c19_neighbor_correspondence.json
python c19_neighbor_independent_check.py \
  --certificate ../results/c19_neighbor_correspondence.json \
  --output ../results/c19_neighbor_independent_check.json
cd .. && python -m unittest discover -s code -p 'test_c19.py' -v
```
