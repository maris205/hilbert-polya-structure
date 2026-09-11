# One-use root grant: P215 Review A source-only build

2026-09-11 UTC. Root authorizes exactly one invocation from workspace root:

`/bin/bash docs/papers211_215_sequence/qa/p215_a_build_preparation01/BUILD_REQUEST.current.sh --execute-under-separate-root-grant`

This grant binds recipe `e71b018872a73f7487ce632959c9aca87a5c42e54a73a56280f39c45a86f72cd`,
request `48cbfbb3092f12ac83d82f818d94a503059316791af011561b11e3a303befd33`,
the 227-row runtime manifest `bcad5ca8f77003ff4fbbf0b52c6017c8bea463d70ce3583a04574b890e555b12`,
the eight-row source manifest `4a9bae9505450b81d46ca2a94e00c723da2d87eb872e58f59dcb2e50c7d92e7b`,
accepted Round0 receipt `15b145e0fe573fb86ca1886e6fa56c7da55302913fd916323afae1e5957b9d59`
and accepted A strict-pair receipt `1544e10bdbd4be8dffc8a710d645f93f59da5ea933b44ee219be3f4792bb1337`.

The exact fresh output is `reviews/p215_a/build01`. The grant is consumed by
the immediately following single submission. No retry, cleanup, PDF adoption,
final Review A acceptance, Round1, Git or external action is authorized.
