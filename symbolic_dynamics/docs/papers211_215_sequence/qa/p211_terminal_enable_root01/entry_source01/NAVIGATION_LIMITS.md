# Documentary navigation limitations

Two preliminary inline Node schema-display commands had an extraneous closing
brace and exited 1 at JavaScript parsing before their file reads. A dependent
orchestration JSON parse also failed after the second failed display. Neither
invoked precheck.js, Python, a dependency query, or a build; no output phase
was created. Corrected bounded schema displays then returned complete data.
The source's ENV4 check was changed to compare a plain spread of process.env
before the first source execution; the final complete source read is recorded
in SOURCE_READ_NATIVE.json. These are not failed scientific/build runs and
are not relabelled as successful commands.
