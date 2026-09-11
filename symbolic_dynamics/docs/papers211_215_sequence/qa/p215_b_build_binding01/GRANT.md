# One-use root grant: P215 Review B source-only build

2026-09-11 UTC. Root authorizes exactly one execution from the workspace root:

`/bin/bash docs/papers211_215_sequence/qa/p215_b_build_preparation01/BUILD_REQUEST.current.sh --execute-under-separate-root-grant`

The preparation seal is `5df77263572cc45112763e41814e97773df846637a3cb7ba888aa53f3676c56f`;
the freshly checked 227-row runtime manifest is
`bcad5ca8f77003ff4fbbf0b52c6017c8bea463d70ce3583a04574b890e555b12`;
the eight-row frozen Round1 source manifest is
`4a9bae9505450b81d46ca2a94e00c723da2d87eb872e58f59dcb2e50c7d92e7b`;
and the accepted strict-pair receipt is
`e88d7c77eece4b01b3fb7c5dec993b01dda25512011d43630ea9b960563bcf8b`.
The output `reviews/p215_b/build01` is absent. Any result consumes this grant
and must be preserved. No retry, Round2, terminal build, central-index, Git or
external action is authorized.
