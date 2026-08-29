# C234 test report

Checks are producer-independent wherever stated.  The checker enforces exact
top-level and nested schemas, numerical reconstruction, citation lock, route
tuple, all-false scope flags and row counts.  It also locks each field of all
five boundary rows, including their conditions, flow types, energy changes
and sampled fixed-set classifications.  The corrected Lakshmanan metadata is
the issue-369(1939), pp.1280--1300 record with DOI 10.1098/rsta.2010.0319.
The independent checker passes 186 assertions; SymPy passes 14 identities;
byte replay is exact; and the hostile suite rejects 37/37 mutations,
including repaired-hash boundary and citation edits.
