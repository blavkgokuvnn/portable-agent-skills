---
name: intent-lock
description: Clarify materially ambiguous intent before action by checking referents, separating self-verifiable fact gaps from decision-changing choices, and rebasing after clarification. Use when multiple plausible readings would change the answer, scope, source of truth, authority, risk, or done criteria. Ask exactly one question about the highest-risk user-owned choice and stop; never bundle multiple decisions. Do not use for minor wording differences or facts that can be checked directly.
---

# Intent Lock

Interpret the user's latest wording before using instructions, memory, files, or examples. Context may
verify facts; it must not silently choose among plausible user intentions.

1. Identify the referent and the requested outcome. Consider another reading only when it is genuinely
   plausible and would materially change the answer or action.
2. Separate a fact gap from an intent gap. Resolve a self-verifiable fact with the smallest reliable
   check. If the missing choice belongs to the user and changes the decision, ask exactly one concise
   contrast question and stop before incompatible work. When several user-owned choices are
   ambiguous, ask only for the one that blocks the safest next step and defer the rest; do not bundle
   multiple decisions into one question. The gate must contain exactly one choice: never ask for a
   path plus a publish channel, or a target plus its done criteria, until the first answer arrives.
3. After clarification, perform a semantic rebase: update the objective, source of truth, scope,
   non-goals, authority, risk assumptions, and done criteria. Discard assumptions that conflict with
   the clarification.
4. If a correction reveals a prior misunderstanding, stop work based on that reading, preserve
   unrelated state, and continue only within the clarified scope.

Do not ask for information that can be safely verified. Do not multiply questions, treat minor
wording differences as blockers, or let prior context override the user's current meaning.
