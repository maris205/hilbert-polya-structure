# Narrative report

The Moser--Tardos process turns an existential local-lemma condition into a random repair dynamics.  Its state is not just the current assignment: an infinite independent table for every variable owns every future refresh.  Once those tables are fixed, any legal rule for choosing a currently violated event produces a deterministic log.

The decisive object is a proper witness tree reconstructed backward from one resampling.  Every vertex records a bad event and every child overlaps its parent.  Occurrence of a fixed tree forces a disjoint collection of table tests, giving a product of event probabilities.  A multitype branching process then sums all such trees exactly under the asymmetric local-lemma witness condition.  Distinct resamplings of one event produce distinct trees, so the tree sum bounds the resampling count.

Finite expectation rules out an infinite log, and a finite log can stop only at an assignment avoiding every bad event.  The proof never uses the lexicographic choice made by the executable examples; it works for every legal sequential rule.  The exact examples are therefore normalization and implementation audits, not empirical support for a general termination claim.
