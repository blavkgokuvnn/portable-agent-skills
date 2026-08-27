---
name: version-milestones
description: Protect durable behavior across version changes. Use when bumping a version, adding, removing, deprecating, or replacing behavior in a versioned product or library, or reconciling conflicting code, changelog, verification, and feature-status records. Do not use for unversioned changes with no compatibility or release boundary.
---

# Version Milestones

## Establish the milestone

Read the current version source, relevant changelog entry, code markers, acceptance checks, and the
feature ledger when the project has one. Decide whether the request repairs an implementation
defect or intentionally changes an established contract. Do not infer permission to publish, tag,
deploy, or release from a request to edit versioned code.

If no feature ledger exists and creating one is authorized, use the
[feature-ledger template](references/feature-ledger-template.md). If creation is not authorized,
continue with the project's existing version and changelog sources; do not create a new artifact.

## Protect durable behavior

1. State the behavior being introduced, preserved, deprecated, or removed.
2. When the project already uses inline current markers, keep them concise near non-obvious logic;
   keep chronology in the changelog and, when present, the feature ledger.
3. Protect durable behavior with a characterization, golden, invariant, or compatibility case that
   exercises the real implementation.
4. Keep the code version, changelog, any existing verifier or release pin, and any existing
   feature-ledger status synchronized.
5. When a feature ledger exists, preserve removed behavior there with the removal version and rationale.

Run the complete affected suite, not only a new case. Treat any unexplained mismatch among code,
version metadata, changelog, verification evidence, and any feature ledger the project already
uses as a failed milestone.

This skill owns version provenance and release synchronization. Structural dependency mapping and
behavioral regression analysis remain separate concerns.
