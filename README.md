[English](README.md) | [Tiếng Việt](README.vi.md)

# Portable Agent Skills

Install eight focused workflow skills at once.

## Provenance

Research and projects guide the engineering design; they do not transfer measured results to prompt-only skills. This README and all provenance notes stay outside the installed payload.

| Skill | Basic effect | Public basis |
|---|---|---|
| [anti-over-engineering](https://github.com/blavkgokuvnn/anti-over-engineering) | Keeps complex work on the shortest correct route. | [YAGNI](https://martinfowler.com/bliki/Yagni.html), [Ponytail](https://github.com/DietrichGebert/ponytail), [EvoHarness-RL](https://arxiv.org/abs/2608.05446), [PonderNet](https://arxiv.org/abs/2107.05407) |
| [codemap](https://github.com/blavkgokuvnn/codemap) | Maps structural dependencies and change impact. | [C4](https://c4model.com/introduction), [Reflexion Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html), [ISO 42010](https://webstore.iec.ch/en/publication/80194) |
| [evidence-grounding](https://github.com/blavkgokuvnn/evidence-grounding) | Grounds material claims and reports uncertainty. | [FActScore](https://aclanthology.org/2023.emnlp-main.741.pdf), [RARR](https://aclanthology.org/2023.acl-long.910.pdf), [verbal uncertainty](https://arxiv.org/abs/2205.14334), [NIST AI RMF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) |
| [intent-lock](https://github.com/blavkgokuvnn/intent-lock) | Clarifies ambiguity that would change the decision. | [Good Questions](https://aclanthology.org/P18-1255.pdf), [AmbigQA](https://aclanthology.org/2020.emnlp-main.466.pdf), [clarification questions](https://aclanthology.org/2023.findings-emnlp.772.pdf), [Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306.pdf) |
| [provenance-memory](https://github.com/blavkgokuvnn/provenance-memory) | Maintains authorized project memory with provenance. | [PROV-DM](https://www.w3.org/TR/prov-dm/), [PROV Constraints](https://www.w3.org/TR/prov-constraints/), [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) |
| [safe-edit](https://github.com/blavkgokuvnn/safe-edit) | Preserves behavior while shared code changes. | [Refactoring](https://refactoring.com/), [regression-test selection](https://digitalcommons.unl.edu/csearticles/13/), [Approval Tests](https://approvaltests.com/) |
| [statem-single-agent](https://github.com/blavkgokuvnn/statem-single-agent) | Tracks durable phases for long local work. | [StateM](https://github.com/henryqin1997/statem/tree/8c3309ad3e7b265e23a4db011ff98c5f6a132bd8), [paper](https://arxiv.org/abs/2608.15089), [Statecharts](https://doi.org/10.1016/0167-6423%2887%2990035-9) |
| [version-milestones](https://github.com/blavkgokuvnn/version-milestones) | Keeps versioned behavior and release evidence aligned. | [SemVer](https://semver.org/spec/v2.0.0.html), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [SLSA provenance](https://slsa.dev/spec/v1.2/build-provenance) |

Each skill name links to its standalone repository and individual installer.

## Install all

~~~text
codex plugin marketplace add blavkgokuvnn/portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills
~~~

Start a new task after installation. Do not install standalone copies beside the bundle because they expose the same skill names.

StateM Single Agent also requires the pinned external dependency documented in its standalone repository.

## Update or remove

~~~text
codex plugin marketplace upgrade portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills

codex plugin remove portable-agent-skills@portable-agent-skills
codex plugin marketplace remove portable-agent-skills
~~~

MIT licensed. The installed payload contains reusable manifests, instructions, and declared templates only; it has no credentials, telemetry, personal data, project logs, or bundled StateM runtime.
