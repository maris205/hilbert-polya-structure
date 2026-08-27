# Deterministic control results

`python3 code/verify_racg_join.py` checks every graph in the NetworkX atlas
through seven vertices.  It checks 995 nontrivial complement-connected local
automata, then verifies the support index, universal subset, ordered state
set, and entrywise Kronecker-sum matrix of every recurrent component in all
1252 graphs.  It also asserts the maximal-component multiplicity and extracts
the explicit two-factor spectrum from an actual joined defining graph.
Status: **PASS**.
