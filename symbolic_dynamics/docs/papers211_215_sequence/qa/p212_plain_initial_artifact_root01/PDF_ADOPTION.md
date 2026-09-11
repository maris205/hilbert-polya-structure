# Actual initial PDF adoption

After RECEPTION.md was written, actual cec42d exited 0. The shell used
`set -e`, checked live `papers/212-closed-pointer-orbits/main.pdf` was
neither present nor a symlink, copied with `cp -pn` from
`qa_initial/plain_build01/source_only/main.pdf`, and compared the entire
source and destination with `cmp`. No old PDF was overwritten. The final
hash output was:

```
bff4ca3a777782091f5f5595d5152df57d148af6140d9394f7f2ee3ae71e7e87  papers/212-closed-pointer-orbits/main.pdf
```

This adopts only the accepted initial six-page PDF. It neither builds a
new PDF nor establishes physical Round0, manuscript A/B or final QA.
