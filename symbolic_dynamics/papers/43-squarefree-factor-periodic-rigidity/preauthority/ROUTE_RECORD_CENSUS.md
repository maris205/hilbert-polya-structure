# Route-record and predecessor-seal census

## Read-only authority state

A fresh read-only check observed:

```text
authority commit = 18530b90317f6efc43ec2e4601ed8cef57daaddc
known status = untracked symbolic_dynamics/papers/40-gauss-mayer-projection-firewalls only
Phase-1 authority writes = 0
Phase-1 Git operations = 0
```

The preexisting Paper-40 directory was not edited.

## Integrated Route records through terminal Paper 39

The path-distinct Route-A census under the authority papers tree remains:

```text
record_count = 42
path_list_sha256 = 63439d5f3a57e42837edaa4514a922743b98265b96c34dcb19c56ccca3770054
path_sorted_absolute_sha256sum_stream_sha256 = 4ae213350dd1aadedea717bd46ebf54e888b7f108a8b6cf35644aece39944d86
last integrated candidate = SD-C41
```

The path-list hash is over C-sorted, newline-terminated, repository-relative
POSIX paths. The second value identifies the independently replayed
path-sorted byte-hash stream. Proposed Papers 40--43 are not added to this
integrated count.

## Terminal Paper-39 seal

```text
PAPER_MANIFEST.sha256 sha256 = 9fe17f0e746fa57a3dbbec7c96d4578b480b6cebcd04c7cb1be03209692516bd
manifest verification = PASS 91/91
research Route sha256 = 7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd
sealed Route sha256 = 3a5da787a2d20439f345610b7523a565bf1eb55a618b977933ef1046eab0dbb8
research lock sha256 = 24f180a30990c3cd581f0732dabeb641dac9e962b17300883a28f77a3844e43a
ranking_performed = false
candidate_selected = false
```

P39 supplies no successor ranking or authorization.

## Separate Paper-40 research seal

```text
candidate = proposed SD-C42
historical parent = SD-C04
RESEARCH_LOCK.json sha256 = e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5
RESEARCH_LOCK.sha256 sha256 = 530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e
immutable research files = 11
verification = PASS 11/11
role = Gauss--Mayer collision boundary only
```

## Separate Paper-41 frozen package

```text
candidate = proposed SD-C43
historical parent = SD-C06
RESEARCH_LOCK.json sha256 = 010b1633369fd0a0e622bdf22224145b860d139ec70cc3f5f30fe2fe5a01025a
SHA256SUMS.txt sha256 = 55214e6af4457ba22ea41d406524d6e94f7fe99c7274c08644822fe7505d41bb
verification = PASS 15/15
role = rooted Knauf collision boundary only
```

## Separate Paper-42 repaired and accepted package

An independent DA first found an artifact-base path defect. The owner changed
only the Route base to the frozen `preauthority` namespace and cascaded the
seals. The repaired bytes were then independently accepted.

```text
candidate = proposed SD-C44
historical parent = SD-C01
ROUTE_EXPECTATION.yaml sha256 = 79eafee424590e0e1b65ffa7dc48d2a066a4822513ff1520f6bcf35593c6f71c
RESEARCH_LOCK.json sha256 = fc4d3613165bebdd812789f0407329de983e1ec81020ef1024a665563293ffc2
SHA256SUMS.txt sha256 = f8f3ada901a3e26735819db05e3bcd01a26e571a8f9bd6cc4af8e1a2e705a433
manifest verification = PASS 16/16
independent DA decision = DA_ACCEPT_PREAUTHORITY
independent DA report sha256 = e46ecdab5aec15a3aa3dd5b80277e62f32677cd5162d803100a565b812bb265d
independent DA sidecar sha256 = 1f691de1d3fd87c096fe95e65bd42b30b0664ac7bc24e8a5f37dfbcfb2c34585
role = function-field collision and chronology boundary only
```

Paper 42 remains outside the integrated Route census and does not rank or
authorize Paper 43.

## Proposed Paper-43 state

`SD-C45` is a commissioned proposal pending independent DA and root
authorization. Its historical parent is C02. Numerical adjacency among
candidate identifiers carries no semantic or governance meaning.

The only selector is the explicitly retrospective three-card rule in
`SELECTION_AND_PROVENANCE.md`. Its chronology limitations remain binding.

