# Compile report — C116

The final `main.tex` was compiled in two clean isolated directories with
`SOURCE_DATE_EPOCH=0` and `TZ=UTC`.  Both builds and the package artifact have
the byte-identical SHA-256 digest

```text
a66073cf8185b528869e22be0527ed8bf80caba9b2568505eeddbab74796b6dd
```

The paper has two pages.  All fonts reported by `pdffonts` are embedded; the
final logs contain no overfull/underfull box, undefined reference/citation, or
package warning.  Text extraction and visual inspection of both pages found
no clipping or stale content.
