# Preserved post-success duplicate invocation failure

Root's one authorized B build01 invocation had already completed successfully
and created the fixed output. A subsequently submitted duplicate command hit
the first exclusive `mkdir` guard and exited 1 with `File exists`. It did not
enter controller redirection or run TeX, and did not change the successful
tree. This is a PRE-EXEC failure, not a retry or second build, and is not PASS
evidence. The successful tree is retained unchanged.
