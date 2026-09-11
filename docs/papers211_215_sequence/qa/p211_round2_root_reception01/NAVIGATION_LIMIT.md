# Original closing-record navigation limit

The saved NAVIGATION_TRUNCATED_CLOSING_READ.json is the actual root native
return from an oversized display of the independent closing records. Its
exit was 0, but its returned output explicitly states truncation. Missing
display bytes are not reconstructed or claimed received from that return.
The complete original CLOSING_NATIVE.json remains immutable and is consumed
directly by the separate full documentary reception helper. This navigation
is not a failed submitted execution, a complete source-output comparison or
a basis for physical acceptance. All complete independent source, raw output
and exact full-key recheck records remain separately preserved.
