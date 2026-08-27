# Feature ledger template

Use this ledger as the current index of durable behavior and its protection. Keep detailed chronology
in the changelog.

| Feature or contract | Introduced | Last changed | Protected by | Status | Rationale |
|---|---|---|---|---|---|

## Status vocabulary

- `ACTIVE`: supported current behavior.
- `EXPERIMENTAL`: intentionally unstable and clearly bounded.
- `DEPRECATED`: still present with a documented replacement or retirement condition.
- `REMOVED`: absent from the current version; record the removal version and reason in the rationale.

## Milestone check

Before accepting a version change, confirm that the implementation version, changelog, verification
evidence, release or verifier pin, and every affected ledger row agree. Any unexplained mismatch fails
the milestone.
