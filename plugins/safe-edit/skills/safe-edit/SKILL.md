---
name: safe-edit
description: Change or refactor shared, high-impact, or branch-sensitive code while preserving established behavior. Use when a function has multiple callers, meaningful side effects, compatibility constraints, or regression risk. Do not use for documentation-only or isolated edits with no behavioral contract or meaningful regression risk.
---

# Safe Edit

## Bound behavioral impact

Find the current implementation, direct and indirect callers, affected branches, side effects, and
existing tests. If the repository has a maintained code map, or a codemap capability is available,
use it as an optional index and verify its claims against current source. Do not require such a map
when direct source tracing is sufficient.

A read-only review or diagnosis does not authorize an edit. Deployment, release, and external-state
changes require their own authority.

## Capture the contract

Before changing behavior, run or add focused characterization cases for important current invariants.
Prefer the smallest real function or component that exposes the decision. Avoid loading an entry
point that can trigger unrelated side effects merely to reach testable logic.

Record which baseline differences are intended. Preserve unrelated behavior and existing user
changes.

## Patch narrowly

Change one coherent behavior at a time. Add a meaningful case for the requested result, and keep
unaffected branches stable. Do not combine cleanup or speculative redesign with the scoped repair.

## Verify proportionally

Run focused cases first, then the complete component suite and affected integration, compatibility,
and platform checks. Explain every baseline difference. Repeat only when a concrete failure or
contradiction requires a bounded repair.

This skill owns behavioral characterization and regression protection. Structural dependency-map
maintenance and version-ledger synchronization remain separate concerns.
