#!/usr/bin/env python3
"""Check positive and negative routing metadata encoded in skill descriptions."""

from __future__ import annotations

import json
import re
from pathlib import Path


def frontmatter_description(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"missing frontmatter: {skill_file}")
    fields = match.group(1).splitlines()
    description = next(
        (line.split(":", 1)[1].strip() for line in fields if line.startswith("description:")),
        "",
    )
    if not description:
        raise ValueError(f"missing description: {skill_file}")
    return description.lower()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    cases = json.loads((repo_root / "tests" / "routing_cases.json").read_text(encoding="utf-8"))
    bundle = repo_root / "plugins" / "portable-agent-skills" / "skills"
    failures: list[str] = []

    for case in cases:
        skill = case["skill"]
        description = frontmatter_description(bundle / skill / "SKILL.md")
        if f"${skill}" in case["positive_prompt"] or f"${skill}" in case["negative_prompt"]:
            failures.append(f"{skill}: fixture must test implicit routing, not explicit invocation")
        for term in case["positive_description_terms"]:
            if term.lower() not in description:
                failures.append(f"{skill}: missing positive term {term!r}")
        for term in case["negative_description_terms"]:
            if term.lower() not in description:
                failures.append(f"{skill}: missing negative term {term!r}")
        print(f"CASE {skill}: positive={case['positive_prompt']}")
        print(f"CASE {skill}: negative={case['negative_prompt']}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print(f"PASS routing metadata: {len(cases)} positive + {len(cases)} negative")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
