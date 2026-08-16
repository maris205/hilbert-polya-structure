# Paper 39 figure specification — SD-C41

All three figures are writer-owned pure TikZ.  They contain no raster image,
external artwork, opacity-dependent distinction, or empirical value awaiting
integration.  Solid versus dashed lines, node shapes, labels, and border styles
keep every semantic distinction legible in grayscale.

## Figure 1 — structural spine and expanded proof fibers

File: `figures/spine_and_expanded_dag.tex`.

- The upper row is the six-node/five-edge structural spine:
  `N35_OBJECT_FIREWALL`, `N36_CELLULAR_CANCELLATION`,
  `N37_COEFFICIENT_SATURATION`, `N38_TREE_ORBITAL_TRILEMMA`,
  `N39_AFFINE_BRANCH_CLOSED`, and `N_REGISTRY_HANDOFF`.
- The lower row displays four nontrivial expanded-node fibers---seven Paper-35
  nodes, two Paper-36 nodes, three Paper-37 nodes, and five Paper-38 nodes---and
  five exact singleton mappings: `N00 -> AUX_CONTRACT_ROOT`,
  `NX -> AUX_NONMEMBERSHIP_SINK`, `NC -> N39_AFFINE_BRANCH_CLOSED`,
  `NR -> N_REGISTRY_HANDOFF`, and `NS -> AUX_EMPTY_REGISTRY_FALLBACK`.
  These disjoint fibers total 22 nodes.
- Thin dotted projection arrows are labeled `total, many-to-one`; they do not
  imply inverse reconstruction from the spine alone.
- A contract badge records `14 classes / 16 tokens / 17 internal tags`.
- A partition badge records `28 = 17 internal + 5 closure + 3 token exits + 1
  non-domain firewall + 2 guards`.
- The registry node is visually separated as governance, not candidate success.

Caption requirement: state that the spine communicates and executes the coarse
history while the expanded DAG owns the proof distinctions; the projection has
explicit fibers but is not injective.

## Figure 2 — finite request classification

File: `figures/request_classification.tex`.

- Left solid-border column: six `OBSTRUCTED` classes and their six frozen-family
  tokens.
- Center split-border column: two `MIXED` classes, each with one obstructed
  canonical token and one alternative EXIT token.
- Right dashed-border column: six `EXIT_ONLY` classes and their six explicit
  exit tokens.
- Solid arrows terminate at a box labeled `nonempty failed-Good set`.
- Dashed arrows terminate at a box labeled `EXIT / empty failed-Good set`.
- A bottom rule states `8 obstructed tokens + 8 exit tokens = Sigma_16`.
- No generic `OTHER_INSTANCE` or compound-request bucket appears.

Caption requirement: distinguish class dispositions from token dispositions and
state that EXIT is a category boundary, never evidence for `not Good`.

## Figure 3 — reset and zero-credit firewalls

File: `figures/reset_and_firewall.tex`.

- Left panel: expanded `E07` projected to structural `E36_37`; object, marker,
  operator owner, and determinant owner are each labeled `RESET / P37`.
- Source and target objects are separately named to rule out an “unfill plus
  coefficients” interpretation.
- Right panel: `E22 : N37N -> NX` is labeled `AUXILIARY_NON_DOMAIN_FIREWALL`;
  its token and class fibers are empty, and it has no failed-`Good` classifier
  role because it is outside the quantified domain.
- A stop badge says `historical boundary retained / closure credit = 0`.
- A bottom bar states that inherited obligation and historical provenance are
  audit metadata, not transported candidate identity.

Caption requirement: explain that E07/E36_37 prevents identity inheritance and
E22 prevents an unquantified alternative-instance edge from receiving coverage
credit.

## Shared visual language

- `formalblue`: frozen contract, exact IDs, and proved mappings;
- `deepgreen`: valid obstruction endpoint or completed audit statement;
- `warningamber`: typed category exit or reset boundary;
- `stopred`: failed obligation or zero-credit guard;
- `governancepurple`: registry/governance action;
- `softgray`: grouped fibers and metadata.

Solid arrows denote proved in-domain implications.  Dashed arrows denote typed
exits.  Dotted arrows denote projection or audit-only association.  A barred
line denotes forbidden credit transfer.

## Figure quality checklist

- pure vector TikZ;
- no title inside the artwork;
- minimum text remains legible in the compiled A4 manuscript;
- no red/green-only distinction;
- line style and text preserve meaning in grayscale;
- no crossing arrow hides an endpoint;
- captions are self-contained;
- every figure is introduced before or at first placement;
- exact counts and IDs agree with `DAG_BRIDGE.json`.
