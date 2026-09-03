# Source audit

The source lineage was checked against primary publisher records.

- A.-L. Barabási and R. Albert, “Emergence of scaling in random networks,” *Science* 286 (1999), 509–512, DOI `10.1126/science.286.5439.509`.  This is used for the historical preferential-attachment mechanism, not for our exact seed-dependent constants.
- B. Bollobás, O. Riordan, J. Spencer, and G. Tusnády, “The degree sequence of a scale-free random graph process,” *Random Structures & Algorithms* 18 (2001), 279–290, DOI `10.1002/rsa.1009`.  This is used for rigorous degree-sequence lineage.
- Á. Backhausz, “Limit distribution of degrees in random family trees,” *Electronic Communications in Probability* 16 (2011), 29–37, DOI `10.1214/ECP.v16-1598`.  This is used as direct fixed-vertex limit lineage.

The degree-sequence paper formulates a linearized-chord-diagram process, and the family-tree paper permits model formulations whose initial condition must be matched carefully.  Neither seed/self-loop convention is silently imported here.  Our model instead starts at `T_2={{1,2}}`, adds exactly one new leaf, and selects an old endpoint with probability `d_v(n)/[2(n-1)]`.  Every displayed constant is derived for that declared convention.

No priority claim is made for the classical preferential-attachment results.  The package contribution is a boundary-complete, convention-locked proof-and-evidence synthesis joining fixed-vertex all-order moments to the global `L2` degree profile.  Neither source is used to support arithmetic local data, Euler factors, root numbers, automorphy, divisors, functional equations, zero matching, or Hilbert–Pólya operators.
