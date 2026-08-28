[English](README.md) | [Tiếng Việt](README.vi.md)

# Bộ skill agent dùng lại được

Cài tám skill quy trình tập trung chỉ trong một lần.

## Nguồn gốc

Nghiên cứu và dự án chỉ định hướng thiết kế kỹ thuật; chúng không chuyển kết quả đo lường sang skill chỉ gồm prompt. README và toàn bộ ghi chú nguồn gốc nằm ngoài payload được cài.

| Skill | Tác dụng cơ bản | Nền tảng công khai |
|---|---|---|
| [anti-over-engineering](https://github.com/blavkgokuvnn/anti-over-engineering) | Giữ việc phức tạp trên con đường ngắn nhất mà vẫn đúng. | [YAGNI](https://martinfowler.com/bliki/Yagni.html), [Ponytail](https://github.com/DietrichGebert/ponytail), [CRITIC](https://arxiv.org/abs/2305.11738), [giới hạn tự sửa](https://arxiv.org/abs/2310.01798), [Devil's Advocate](https://arxiv.org/abs/2405.16334), [smolagents](https://huggingface.co/docs/smolagents/main/en/reference/agents) |
| [codemap](https://github.com/blavkgokuvnn/codemap) | Lập bản đồ phụ thuộc cấu trúc và phạm vi ảnh hưởng. | [C4](https://c4model.com/introduction), [Reflexion Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html), [ISO 42010](https://webstore.iec.ch/en/publication/80194) |
| [evidence-grounding](https://github.com/blavkgokuvnn/evidence-grounding) | Gắn claim quan trọng với bằng chứng và độ bất định. | [FActScore](https://aclanthology.org/2023.emnlp-main.741.pdf), [RARR](https://aclanthology.org/2023.acl-long.910.pdf), [verbal uncertainty](https://arxiv.org/abs/2205.14334), [NIST AI RMF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) |
| [intent-lock](https://github.com/blavkgokuvnn/intent-lock) | Làm rõ mơ hồ có thể đổi quyết định. | [Good Questions](https://aclanthology.org/P18-1255.pdf), [AmbigQA](https://aclanthology.org/2020.emnlp-main.466.pdf), [clarification questions](https://aclanthology.org/2023.findings-emnlp.772.pdf), [Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306.pdf) |
| [provenance-memory](https://github.com/blavkgokuvnn/provenance-memory) | Duy trì memory dự án đã được phép cùng nguồn gốc. | [PROV-DM](https://www.w3.org/TR/prov-dm/), [PROV Constraints](https://www.w3.org/TR/prov-constraints/), [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) |
| [safe-edit](https://github.com/blavkgokuvnn/safe-edit) | Giữ hành vi khi thay đổi code dùng chung. | [Refactoring](https://refactoring.com/), [regression-test selection](https://digitalcommons.unl.edu/csearticles/13/), [Approval Tests](https://approvaltests.com/) |
| [statem-single-agent](https://github.com/blavkgokuvnn/statem-single-agent) | Theo dõi phase bền cho việc cục bộ dài. | [StateM](https://github.com/henryqin1997/statem/tree/8c3309ad3e7b265e23a4db011ff98c5f6a132bd8), [paper](https://arxiv.org/abs/2608.15089), [Statecharts](https://doi.org/10.1016/0167-6423%2887%2990035-9) |
| [version-milestones](https://github.com/blavkgokuvnn/version-milestones) | Giữ hành vi theo phiên bản và bằng chứng release đồng bộ. | [SemVer](https://semver.org/spec/v2.0.0.html), [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), [SLSA provenance](https://slsa.dev/spec/v1.2/build-provenance) |

Mỗi tên skill liên kết đến repository riêng và bộ cài riêng.

## Cài cả bộ

~~~text
codex plugin marketplace add blavkgokuvnn/portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills
~~~

Mở task mới sau khi cài. Không cài bản riêng cùng bundle vì chúng cung cấp trùng tên skill.

StateM Single Agent còn cần dependency ngoài đã pin, được hướng dẫn trong repository riêng.

## Cập nhật hoặc gỡ

~~~text
codex plugin marketplace upgrade portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills

codex plugin remove portable-agent-skills@portable-agent-skills
codex plugin marketplace remove portable-agent-skills
~~~

Giấy phép MIT. Payload đã cài chỉ chứa manifest, hướng dẫn dùng lại và template đã khai báo; không có thông tin xác thực, telemetry, dữ liệu cá nhân, log dự án hay StateM runtime.
