# Source and collision audit

Metadata were checked on 2026-09-02 against publisher DOI records and Crossref.
The sources establish terminology and classical ownership; the formulas and
executable evidence in this package are reconstructed locally.

1. Paul J. Flory, “Intramolecular Reaction between Neighboring Substituents of
   Vinyl Polymers,” *Journal of the American Chemical Society* **61**(6),
   1518–1521 (1939), DOI `10.1021/ja01875a053`.  This is the classical
   one-dimensional blocking/jamming lineage.
2. J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of
   Modern Physics* **65**(4), 1281–1329 (1993), DOI
   `10.1103/RevModPhys.65.1281`.  This is the authoritative review source for
   RSA terminology and model context.
3. Mathew D. Penrose, “Random Parking, Sequential Adsorption, and the Jamming
   Limit,” *Communications in Mathematical Physics* **218**(1), 153–176
   (2001), DOI `10.1007/s002200100387`.  This supplies rigorous general RSA and
   jamming-limit context.
4. Martin Dyer and Alan Frieze, “Randomized greedy matching,” *Random
   Structures & Algorithms* **2**(1), 29–45 (1991), DOI
   `10.1002/rsa.3240020104`.  This supplies algorithmic random-greedy-matching
   lineage; its broader graph questions are not imported as proof here.

## Claim-use boundary

The paper does not claim that the model, Flory density, random greedy matching,
or one-dimensional RSA is new.  Its contribution is a self-contained exact
finite reconstruction with one closed theorem statement, explicit path/cycle
boundary effects, and a replayable integrity chain.  This is not a
literature-level originality or priority claim.

## Collision snapshot

The package freezes the semantic token
`C291_READ_ONLY_COLLISION_SNAPSHOT_AT_7fbe9db3`; it does not pin mutable global
registry bytes.  The closest in-repository packages are:

- `HCS-C208`, whose PGF belongs to continuous-time linear birth–death
  branching, not a finite greedy adsorption;
- `HCS-C243`, whose “dimer” is a Bose–Josephson Hamiltonian two-mode system;
- `HCS-C285`, whose stochastic owner is a closed Gordon–Newell queueing network
  with product form and condensation.

None has the edge-order greedy owner, path/cycle first-edge PGF convolution,
binary-gap support, or same-size boundary correction proved here.  Direct-owner
risk remains high because the RSA model and limit density are classical.  The
appropriate obstruction record is `HEN-O275`.
