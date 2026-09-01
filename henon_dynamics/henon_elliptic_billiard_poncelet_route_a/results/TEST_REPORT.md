# C275 test report

The high-precision producer evaluates elliptic integrals and Jacobi functions
with software parameter `m=e^2`.  The independent checker reconstructs all
values through SciPy, rechecks the confocal dual-tangency equation, both
monotone directions, endpoint convergence, every porism vertex, coprimality,
least period, and the sector/claim firewalls.

SymPy verifies 208 exact identities covering the eccentricity domain,
Jacobi-covering equation, inverse-porism algebra, endpoint arguments, and
primitive-period logic.  Fresh byte replay and 24 repaired-hash semantic
mutations are mandatory.  Release additionally requires three substantively
different deterministic LuaLaTeX PDFs, embedded/subset fonts, warning-free
settled logs, visual inspection, and exact manifest closure.
