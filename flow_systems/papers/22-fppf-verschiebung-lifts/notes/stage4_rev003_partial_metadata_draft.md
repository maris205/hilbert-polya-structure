# P22 Stage 4 REV-003 partial metadata draft

Status: **PARTIAL_METADATA_ONLY — AUTHOR CONTRIBUTIONS STILL PENDING**

This is a drafting aid only.  It does not modify or apply any revision patch,
manuscript, anchored base, block manifest, roadmap, adjudication, or author
event.  It uses only the facts explicitly supplied in
stage4_rev003_author_event_20260825.txt and normalized in
stage4_rev003_author_metadata_input.json.

## Explicit-fact boundary

The supplied input confirms only the following facts:

- author name and byline order: Liang Wang;
- affiliation label 1 and the stated School, University, street address,
  postal code, province, and country;
- contact email: wangliang.f@gmail.com;
- no specific funding for this work; and
- no competing interests.

The contact email is confirmed, but corresponding-author status is explicitly
not designated.  The byline below therefore labels it only as Contact and does
not add a corresponding-author symbol or assertion.

The author-contribution field remains pending explicit confirmation.  The
proposed contribution sentence stored in the normalized input is not an
author-confirmed fact and is not used below.  A one-author byline does not by
itself establish Conceptualization, Formal analysis, Validation, Writing, or
any other CRediT role.

## B0005 — complete proposed new_text

The scientific title and draft date are retained exactly from the anchored
base.  Only explicitly confirmed author metadata replaces the placeholder.

~~~latex
\title{\textbf{A Descent Obstruction to Verschiebung Lifts\\
on fppf and Finite-Flat Sites}}
\author{Liang Wang\textsuperscript{1}\\
\small \textsuperscript{1}School of Artificial Intelligence and Automation,\\
\small Huazhong University of Science and Technology,\\
\small Luoyu Road 1037, 430070, Hubei, P.R. China\\
\small Contact: \texttt{wangliang.f@gmail.com}}
\date{Draft of 24 August 2026}
~~~

## B0097 — complete proposed new_text

~~~latex
\paragraph{Funding.}
The author received no specific funding for this work.
~~~

## B0098 — complete proposed new_text

~~~latex
\paragraph{Competing interests.}
The author declares no competing interests.
~~~

## B0096 — no replacement issued

B0096 remains pending and must not be represented as resolved.  No complete
new_text is emitted for that block.  The current input status is
pending_explicit_confirmation, and the overall REV-003 status is
WAITING_FOR_EXPLICIT_AUTHOR_CONTRIBUTION_CONFIRMATION.  A later author event
must explicitly approve or replace the contribution wording before any B0096
operation is drafted.

## TeX-safety and claim-surface check

- Liang Wang contains no TeX-reserved character.
- The affiliation and postal address contain only letters, spaces, digits,
  commas, and periods; no escaping is required.
- The email contains only letters, periods, the at sign, and ASCII domain
  characters.  It is placed inside \texttt{...}; no underscore, percent sign,
  ampersand, hash, dollar sign, brace, tilde, caret, or backslash needs
  escaping.
- \textsuperscript{1}, \small, and \texttt are available in the existing
  LaTeX setup; no package or preamble change is proposed.
- The title and date are unchanged.  B0097 and B0098 are declarations, not
  mathematical claims.  None of the proposed text changes the theorem,
  topology, quantifiers, evidence, originality language, or contribution
  claim.
- No corresponding-author status, CRediT role, funding source, grant number,
  or competing-interest detail has been inferred.
