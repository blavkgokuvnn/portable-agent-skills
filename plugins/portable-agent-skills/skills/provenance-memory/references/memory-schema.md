# Provenance memory schema

Use stable identifiers and concise records. Store source paths relative to the project whenever
possible, and never copy credentials or sensitive payloads into memory.

## Fact record

```markdown
#### F-001 · Concise conclusion
Status: ACTIVE
Confidence: high, verified by a current test
Valid from: 2026-01-01
Review when: the documented interface or verification method changes
Valid while: the named contract and its acceptance check remain unchanged
Conclusion: State the fact, scope, and important exclusions.
Method: State the reproducible check that established it.
Source: Cite the project-relative source and relevant section.
Related: List stable record identifiers only when useful.
```

## Correction or decision record

```markdown
#### C-001 · Concise correction or decision
Previous: State the assumption or behavior that was rejected.
Decision: State the corrected intent faithfully.
Rule: State the testable rule that future work must follow.
Status: ACTIVE
Source: Cite the user decision or project evidence.
Related: List stable record identifiers only when useful.
```

## Unresolved work record

```markdown
#### U-001 · Concise unresolved item
Status: OPEN
Blocker: State the missing evidence, input, or authority.
Next signal: State the observation that would make progress possible.
Source: Cite the latest reliable handoff or evidence.
```

Use `WAITING_EXTERNAL`, `WAITING_USER`, `STALE`, or `RESOLVED` when those states are more accurate.
Supersede records by linking the replacement identifier; do not erase the earlier provenance.
