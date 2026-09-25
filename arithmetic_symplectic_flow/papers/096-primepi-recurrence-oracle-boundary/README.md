# 096 — PrimePi recurrence oracle boundary

**Record:** ASFS-SCOUT-20260914-65  
**Status:** PRE-P0 STOP — GLOBAL PRIME-COUNTING ORACLE IN THE UPDATE; EVENTUAL FIXED POINT DOES NOT REPAIR A0

The fixed five-step recurrence `a_n = pi(a_{n-1}+...+a_{n-5})`, started from five ones, reaches the constant state `66`; a reported general result says arbitrary nonnegative five-state seeds are eventually periodic.  But `pi` is already the global prime-counting function.  The recurrence queries a complete externally defined prime-distribution oracle rather than deriving a sieve-symbolic admissibility rule.

- [paper](paper.md) · [scope](candidate-card.md) · [claims](claim-ledger.md) · [evidence](evidence/README.md)
