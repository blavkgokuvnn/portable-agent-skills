---
name: codemap
description: Map repository dependencies and structural blast radius before moving, renaming, splitting, or refactoring files; changing imports, entry points, shared schemas, or state ownership; or answering what produces or consumes an artifact. Do not use for isolated behavior-only edits with known callers and no structural impact.
---

# Codemap

Treat a repository map as an index, not proof. Verify every relevant edge against current source and
configuration before relying on it.

## Map the change

1. Find the smallest existing architecture or code-map section that covers the target. If no map
   exists and creating one is authorized, use the [CODEMAP template](references/codemap-template.md).
2. Identify the current owner, producers, consumers, imports, entry points, shared state, schemas,
   generated artifacts, and path assumptions.
3. Trace each relevant edge in current source. Mark uncertain or stale edges instead of completing
   them by inference.
4. State the blast radius and required companion edits before a structural mutation.

For a read-only request, report the verified map without changing project files. A request to explain
dependencies does not authorize a refactor.

## Keep the map current

When an authorized change alters an import, entry point, producer-consumer edge, shared schema,
directory owner, or persistent-state location, update the repository map in the same change. Keep
historical rationale in the project's decision history or changelog rather than accumulating it in
the current structural map.

Run path, link, build, and integration checks that exercise the changed edges. Behavioral
characterization and regression protection remain a separate editing concern; this skill owns the
structural dependency map.
