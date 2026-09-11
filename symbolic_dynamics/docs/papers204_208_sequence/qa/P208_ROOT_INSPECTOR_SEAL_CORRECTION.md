# P208 root-inspector seal correction

2026-09-06 UTC. The first actual inspection completed its declared input,
runtime, snapshot and raw-comparison checks, but its final seal writer
opened SHA256SUMS before enumerating the directory. It therefore wrongly
included the empty newly opened manifest itself. That outer seal is invalid.
The first receipt's internal-check PASS does not establish package closure.

The complete original directory p208_round0_input_inspection, including
the actual defective manifest and executed code snapshot, is preserved.
No author, manuscript, numerical output, build or view evidence changed.
The correction computes manifest content before exclusive creation and
then checks complete nonself closure. It uses a separate exclusive output
directory p208_round0_input_inspection_v2 and reruns the actual artifact
inspection and raw comparisons. Only a successful v2 receipt plus its
checked nonself seal may supply Round0 artifact adoption. This is a root
evidence-writer defect, not a paper mathematical failure or a new review.
