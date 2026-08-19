# C74 source audit

C74 uses only the frozen finite coordinate and hypergraph certificates from
C72 and C73:

```text
C72 evidence   8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51
C72 manifest   5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b
C73 evidence   e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5
C73 manifest   a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d
```

The C72 coordinates are treated as a presentation-dependent named multiset,
not as a canonical basis or an abstractly labelled group.  C73 supplies only
the comparison order `345600` for its abstract generation hypergraph.  No
external arithmetic or local source is introduced.  The scope firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
