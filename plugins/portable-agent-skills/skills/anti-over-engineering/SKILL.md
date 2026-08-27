---
name: anti-over-engineering
description: Prevent scope drift, premature architecture, speculative artifacts, repeated polling, and excessive verification. Use for significant changes, research, complex debugging, or long work with several plausible routes; skip tiny clear edits and urgent containment.
---

# Anti-Over-Engineering

Find and falsify the shortest correct route. Minimality ranks below correctness, authorization,
trust-boundary checks, data-loss prevention, and the user's explicit completion condition.

## Lock one outcome and route

If the target, scope, source of truth, or authority still has a decision-changing ambiguity, let the
intent gate own the next turn. Ask for one user choice only; do not collect the objective, done
criteria, route, or other downstream fields until that choice is resolved. Do not activate or
report this skill for that turn.

Before deep work, record:

```text
OBJECTIVE: one user-visible outcome
DONE: observable pass condition
NON-GOALS: attractive adjacent work excluded now
CONSTRAINTS: authorization, safety, files, time, compatibility
ROUTE: simplest causal model -> observed break -> smallest repair
NEXT SIGNAL: cheapest observation that could change the route
```

Use the user's system decomposition as the baseline unless current evidence contradicts it. Keep at
most five plan steps and one active route. A downstream stage waits for its upstream acceptance
signal. Change `DONE` only when the user changes the requested outcome.

## Stop discovery at sufficiency

Discovery is sufficient when current evidence forms a complete
`input -> owner or boundary -> wrong state or action` chain for every in-scope symptom.

1. Run the cheapest disconfirming check once.
2. If the chain survives, use the first working rung:
   `answer or no change -> existing code or configuration -> native capability or installed dependency -> smallest local edit -> new artifact or dependency`.
3. Escalate only after evidence rules out the earlier rung.

Do not add a queue, cache, schema, worker, abstraction, or parallel pipeline merely because it has a
plausible consumer. It must fix an observed failure or required invariant that the direct repair
cannot satisfy.

For every next action ask:

1. Does `DONE` or a required invariant fail without it?
2. Can `NEXT SIGNAL` change the next decision?
3. Is this the cheapest reliable discriminator?

If any answer is no, park the action in one line without investigating it.

## Hard interrupts

| Cue | Required response |
|---|---|
| The user says the route is indirect or too complex | Pause, report route and artifact counts, then run the removal audit below. |
| One causal chain explains all in-scope symptoms | Stop exploring, run one cheapest falsifier, then act at the responsible owner or boundary. |
| An upstream stage has not passed | Do not start its consumer. Return to the missing acceptance signal. |
| Two related routes fail | State the mechanism delta, falsifier, cheapest test, and why earlier failures do not predict the next route; otherwise leave that family. |
| A new stateful mechanism or nontrivial artifact appears | Prove the direct route insufficient, then run the preflight below and a tiny canary. |
| A job may run longer than a few minutes | Declare a deadline, one progress source, a resource ceiling, and recovery before launch. |
| Two observations show no decision-relevant change | Back off or use a native wait. Add no undeclared probe. |
| Ten reads or tool resumptions yield no decision, edit, or completed check | Synthesize once and run one discriminator; otherwise ask or park. |
| `DONE` first passes after the last edit | Run one proportional verification pass, then stop unless it reveals a concrete defect. |

```text
REMOVE: What work could disappear while DONE still passes?
DISCONFIRM: What would prove the active route is waste?
CHEAPER: What smaller action resolves the same decision?
STOP NOW: Has DONE already passed, or is sunk cost keeping work alive?
```

## Preflight nontrivial artifacts

Before a helper, dataset, cache, or long job, record:

```text
CONSUMER: exact decision or command that will read it
ESTIMATE: files, disk, peak memory, and runtime
CANARY: smallest representative slice and pass condition
CEILING: abort threshold and safe recovery
OBSERVE: one progress source and cadence
```

Reject the path if its consumer is speculative, the direct route remains untested, or the canary
breaches the ceiling. Query large inputs with counts or slices instead of loading them whole.

## Reframe and finish

An experiment stop rule closes a family, not the task. Record `FAMILY_REJECTED`, return to the
frozen outcome, and choose a mechanism-distinct route or new information source. If none exists,
report the exact missing input, authorization, or user decision.

Finish with:

```text
RESULT: DONE or the concrete unmet condition
ROUTE: route used and any mechanism-level switch
COST: artifacts, long jobs, and unchanged observations
VERIFY: proportional pass and any defect-triggered rerun
PARKED: nonblocking ideas, or none
```

Never simplify away authorization checks, credential handling, trust-boundary validation,
data-loss prevention, rollback, or verification required by the system being changed.
