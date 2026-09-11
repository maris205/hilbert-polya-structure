# Exact V2 source repair — SOURCE_ONLY

The original receiver, CONTRACT.md and DATA_REQUEST.proposed.json remain
unchanged. Proposed replacement carrier: receive_data.v2.proposed.mjs.txt.
The existing request contains no receiver filename, so no request revision
is needed; all actual input/acceptance fields remain null. V2 adopts the
same contract and holds, with only these exact four textual changes:

1. ref(): require typeof r.pin.sha256 === 'string' before the digest regex.
2. input(): require object(r) before the empty Object.keys branch.
3. input(): validate optional error and close_error whenever Object.hasOwn
   reports them, instead of using value truthiness.
4. input(): complete success requires both error properties absent, instead
   of merely falsy.

Consequently array-coerced digest values, empty arrays/strings as request
records, and false/zero/null optional errors cannot pass these branches.
An actual empty object remains permitted only for incomplete entry failure.
No other source edits, new authority, actual keys, input bytes or grants.
No proposed source execution/import, parser/syntax/AST testing or future
host/raw/binding query. Only fixed prior source/template reads and literal
documentary text substitutions via apply_patch. Independent same-reviewer
exact-diff acceptance remains pending. HOLD_OPERATIONAL / HOLD_EXTERNAL.
