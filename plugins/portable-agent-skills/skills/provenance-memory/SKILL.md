---
name: provenance-memory
description: Retrieve and maintain a small provenance-aware project memory when an earlier fact, correction, decision, or unresolved item affects current work, or when the user explicitly asks to remember, update, consolidate, or resume project knowledge. Do not use for disposable session scratch, and never write memory without explicit user authority.
---

# Provenance Memory

Use the project's declared memory location. Do not create a new memory tree merely because none is
present.

## Authority

Reading relevant project memory is allowed when it supports the current request. Create, append,
supersede, consolidate, or delete memory only when the user has authorized a memory change. A request
to edit code or finish a task does not by itself authorize a memory write.

Memory never grants authority for destructive, external, production, or irreversible action. Verify
current state independently when it matters.

## Retrieve narrowly

1. Search for the exact topic, identifier, or decision key.
2. Read only the complete matching record and, when needed, one directly related record.
3. Check provenance, status, confidence, and the stated invalidation condition.
4. Re-verify any condition that may have changed before letting an old fact alter the route.
5. Report conflicts instead of silently selecting one record.

If two targeted searches find no relevant record, stop the lookup and continue without memory.

## Record with provenance

When a write is authorized, use the [memory schema](references/memory-schema.md). Keep facts,
corrections, decisions, and unresolved items distinct. Append new evidence and supersede an outdated
record instead of rewriting history. Delete only with explicit authority.

A candidate memory or workflow change is not proven by one successful result. Promote it only when
current acceptance improves without regressing representative prior cases, and retain a clear
invalidation or retirement path.

Keep current-state summaries small. Put chronology in history records and structural relationships in
the repository's architecture map.
