# Root import-only preload syntax failure

The first actual import-only probe, native 019322/exit 1, failed at JavaScript
parse time because root's new node_preload.js line 84 contained one extra
closing parenthesis. That exact source and actual diagnostic remain intact.
The semantic receiver was not loaded, imported, parsed or executed.

The separately named node_preload02.js removes only that parenthesis.
This is a root infrastructure correction, not a submitted semantic-source
change or an accepted execution. Its actual import-only result must be
received before a new binding can name it. No failure is overwritten.
