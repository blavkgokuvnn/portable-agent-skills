---
name: statem-single-agent
description: Track durable phase state for long, multi-phase work with a minimal StateM runbook. Use only when the active surface has a local Python environment and writable project filesystem, and the work has at least three substantial phases or durable mutable execution state that may outlive the current context. Do not invoke on web or mobile surfaces, in environments without local Python/filesystem access, or for short tasks and ordinary checklists.
---

# StateM single agent

Use the official StateM core as an external dependency. This plugin contains only a portable
`scope -> work -> verify -> done` profile; never vendor or fork the core into the plugin.

## Dependency gate

The supported core is StateM `0.1.0` at upstream commit
`8c3309ad3e7b265e23a4db011ff98c5f6a132bd8` (Apache-2.0).

Check availability before creating or advancing task state:

```text
python -m statem --help
```

If the command is unavailable, stop and offer this pinned, user-authorized setup command:

```text
python -m pip install "git+https://github.com/henryqin1997/statem.git@8c3309ad3e7b265e23a4db011ff98c5f6a132bd8"
```

Rerun the availability check after setup. If it still fails, do not create or advance StateM state.
Report the exact error and continue without this skill only when the user agrees.

Resolve `<skill-dir>` as the directory containing this `SKILL.md`. Before starting a run, validate
the included profile against the installed core:

```text
python -m statem validate "<skill-dir>/assets/single-agent.yaml" --strict
```

If strict validation fails, stop. Do not weaken the profile to bypass a compatibility error.

## Start or resume

Implicit activation does not authorize writing task state. Start a new run only when the user
explicitly requested durable phase tracking, or when the authorized task already includes local
task-state files. For answer, review, or read-only diagnosis requests, do not create `.statem/`;
describe the option instead. Reading an existing run is allowed only when it is in scope.

Choose one stable, task-specific run id:

```text
python -m statem start "<skill-dir>/assets/single-agent.yaml" --run-id <id> --json
python -m statem cur --run-id <id> --json
```

StateM writes runtime state to `.statem/` by default. Keep that directory untracked.

Advance only after the current phase is complete:

```text
python -m statem goto <next> --run-id <id> --yes --json
```

`--yes` confirms that the phase conditions were checked; it is not evidence. At `verify`, register a
bounded `predicate` or `command` only when a deterministic check exists. Do not invent a check for
judgment-only work.

## Boundaries

- Transition only at meaningful phase boundaries, not after every action.
- Treat StateM history as execution state, not semantic truth; final claims still need current evidence.
- If StateM blocks progress incorrectly, report the exact gate and repair the profile or continue
  without it after user agreement. Never weaken a safety condition merely to advance.
