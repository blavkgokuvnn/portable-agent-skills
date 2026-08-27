# Portable Agent Skills / Bộ skill agent dùng lại được

Eight small skills for grounded, scoped, and durable agent work in ChatGPT and Codex. Seven are
self-contained; `statem-single-agent` additionally requires a local Python/StateM environment.
Install one skill or the complete bundle.

**Tiếng Việt:** Tám skill nhỏ giúp agent trong ChatGPT và Codex làm việc có căn cứ, đúng phạm vi và
duy trì được qua công việc dài. Bảy skill tự chứa; riêng `statem-single-agent` cần thêm môi trường
Python/StateM cục bộ. Có thể cài một skill hoặc cả bộ.

## Research & provenance / Nghiên cứu & nguồn gốc

This table records the public research and projects used to shape this public version. `deep-read`
means relevant full-text methods, findings, and limits were reviewed; `abstract-only` means claims
are limited to the abstract or catalog record; `project inspiration` means an engineering project
informed the design. These sources do not imply that a prompt-only skill inherits measured results.

**Tiếng Việt:** Bảng này ghi lại các nghiên cứu và dự án công khai đã góp phần định hình bản công
khai. `deep-read / đọc toàn văn` nghĩa là đã xem phương pháp, kết quả và giới hạn liên quan trong
toàn văn; `abstract-only / chỉ đọc tóm tắt` giới hạn claim ở tóm tắt hoặc hồ sơ thư mục;
`project inspiration / cảm hứng dự án` nghĩa là một dự án kỹ thuật đã gợi ý cho thiết kế. Các nguồn
này không có nghĩa một skill chỉ gồm prompt thừa hưởng kết quả đo lường của nghiên cứu.

| Skill | Public research and project basis / Nền tảng nghiên cứu và dự án công khai | Evidence boundary / Giới hạn bằng chứng |
|---|---|---|
| `anti-over-engineering` | [YAGNI](https://martinfowler.com/bliki/Yagni.html) — deep-read / đọc toàn văn; [Ponytail](https://github.com/DietrichGebert/ponytail) — project inspiration / cảm hứng dự án; [EvoHarness-RL](https://arxiv.org/abs/2608.05446) — abstract-only / chỉ đọc tóm tắt; [PonderNet](https://arxiv.org/abs/2107.05407) — abstract-only / chỉ đọc tóm tắt | Supports deferring presumptive features and supplies limited concepts for selective effort. The control card, hard interrupts, and stop policy are this skill's synthesis.<br>**VN:** Hỗ trợ việc hoãn các tính năng mới chỉ là giả định và cung cấp khái niệm có giới hạn cho việc chọn mức nỗ lực. Thẻ kiểm soát, ngắt cứng và chính sách dừng là phần tổng hợp riêng của skill. |
| `evidence-grounding` | [FActScore](https://aclanthology.org/2023.emnlp-main.741.pdf) — deep-read / đọc toàn văn; [RARR](https://aclanthology.org/2023.acl-long.910.pdf) — deep-read / đọc toàn văn; [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) — deep-read / đọc toàn văn; [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) — deep-read / đọc toàn văn | Supports atomic claim checking, attribution and revision, calibrated uncertainty in the studied setting, and risk-proportional verification. `Unverified` and BLUF wording are design choices.<br>**VN:** Hỗ trợ kiểm tra từng claim nhỏ, dẫn nguồn và sửa claim, diễn đạt độ bất định đã hiệu chỉnh trong bối cảnh nghiên cứu, cùng mức kiểm chứng theo rủi ro. Cách dùng từ `Unverified` và BLUF là lựa chọn thiết kế. |
| `intent-lock` | [Learning to Ask Good Questions](https://aclanthology.org/P18-1255.pdf) — deep-read / đọc toàn văn; [AmbigQA](https://aclanthology.org/2020.emnlp-main.466.pdf) — deep-read / đọc toàn văn; [Asking Clarification Questions to Handle Ambiguity](https://aclanthology.org/2023.findings-emnlp.772.pdf) — deep-read / đọc toàn văn; [Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306.pdf) — deep-read / đọc toàn văn | Supports detecting multiple interpretations and asking useful contrast questions. “Fact gap vs intent gap,” one-question gating, and semantic rebase are this skill's synthesis.<br>**VN:** Hỗ trợ phát hiện nhiều cách hiểu và đặt câu hỏi đối chiếu hữu ích. “Thiếu fact hay thiếu ý định”, cổng một câu hỏi và semantic rebase là phần tổng hợp riêng của skill. |
| `codemap` | [C4 model](https://c4model.com/introduction) — project inspiration / cảm hứng dự án; [Software Reflexion Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html) — abstract-only / chỉ đọc tóm tắt; [ISO/IEC/IEEE 42010:2022](https://webstore.iec.ch/en/publication/80194) — abstract-only / chỉ đọc tóm tắt | Supports scoped structural views and comparison between source and high-level models. The owner/producer/consumer checklist is an engineering synthesis.<br>**VN:** Hỗ trợ góc nhìn cấu trúc có phạm vi và đối chiếu mã nguồn với mô hình cấp cao. Checklist owner/producer/consumer là một tổng hợp kỹ thuật. |
| `safe-edit` | [Refactoring](https://refactoring.com/) — deep-read / đọc toàn văn; [Analyzing Regression Test Selection Techniques](https://digitalcommons.unl.edu/csearticles/13/) — abstract-only / chỉ đọc tóm tắt; [Approval Tests](https://approvaltests.com/) — project inspiration / cảm hứng dự án | Supports small behavior-preserving changes, impact-aware regression selection, and captured-output baselines. It does not guarantee safety without relevant tests.<br>**VN:** Hỗ trợ thay đổi nhỏ có bảo toàn hành vi, chọn kiểm thử hồi quy theo ảnh hưởng và tạo baseline từ output đã ghi nhận. Không có kiểm thử liên quan thì skill không bảo đảm an toàn. |
| `provenance-memory` | [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) — deep-read / đọc toàn văn; [W3C PROV Constraints](https://www.w3.org/TR/prov-constraints/) — deep-read / đọc toàn văn; [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — project inspiration / cảm hứng dự án | Supports derivation, revision, invalidation, consistency, and append-only correction. The Markdown schema and authorization gate are this skill's synthesis.<br>**VN:** Hỗ trợ truy nguyên, sửa đổi, vô hiệu hóa, tính nhất quán và đính chính chỉ-ghi-thêm. Schema Markdown và cổng thẩm quyền là phần tổng hợp riêng của skill. |
| `statem-single-agent` | [StateM at the supported commit](https://github.com/henryqin1997/statem/tree/8c3309ad3e7b265e23a4db011ff98c5f6a132bd8) — deep-read / đọc toàn văn; [StateM paper](https://arxiv.org/abs/2608.15089) — abstract-only / chỉ đọc tóm tắt; [Statecharts: A Visual Formalism for Complex Systems](https://doi.org/10.1016/0167-6423%2887%2990035-9) — project inspiration / cảm hứng dự án | Upstream supports checked durable transitions; the paper abstract provides limited conceptual context. This thin sequential profile neither forks StateM core nor implements Statecharts hierarchy, concurrency, or broadcast semantics.<br>**VN:** Upstream hỗ trợ chuyển trạng thái bền có kiểm tra; tóm tắt paper chỉ cung cấp bối cảnh khái niệm có giới hạn. Profile tuần tự mỏng này không fork StateM core và cũng không triển khai cấu trúc phân cấp, xử lý đồng thời hoặc ngữ nghĩa broadcast của Statecharts. |
| `version-milestones` | [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — deep-read / đọc toàn văn; [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) — project inspiration / cảm hứng dự án; [SLSA Build Provenance 1.2](https://slsa.dev/spec/v1.2/build-provenance) — deep-read / đọc toàn văn | Supports explicit compatibility levels, human-readable change ledgers, and verifiable artifact inputs. The feature-ledger workflow is this skill's synthesis.<br>**VN:** Hỗ trợ mức tương thích tường minh, sổ thay đổi dễ đọc và input artifact có thể kiểm chứng. Quy trình feature-ledger là phần tổng hợp riêng của skill. |

The README is repository documentation outside every plugin source. It is visible on the repository
front page but is not installed or loaded as skill context.

**Tiếng Việt:** README là tài liệu ở gốc repository, nằm ngoài mọi nguồn plugin. Nội dung này hiện
ngay trên trang chính GitHub nhưng không được cài hoặc nạp vào context của skill.

## Skills / Danh sách skill

| Skill | Class / Loại | Use when / Khi dùng | Do not use when / Không dùng khi | Setup / Chuẩn bị |
|---|---|---|---|---|
| `anti-over-engineering` | A: universal / dùng chung | Significant work has several plausible routes or is growing speculative machinery.<br>**VN:** Công việc đáng kể có nhiều hướng hợp lý hoặc đang phình ra máy móc suy đoán. | The edit is tiny and clear, or safety and rollback are the only remaining work.<br>**VN:** Chỉnh sửa nhỏ và rõ, hoặc phần còn lại chỉ là an toàn và rollback. | None. Canonical source is the standalone repository; the bundle contains a checked mirror.<br>**VN:** Không cần. Nguồn chuẩn là repo độc lập; bundle chứa bản mirror đã kiểm. |
| `evidence-grounding` | A: universal / dùng chung | A material, current, niche, precise, or high-stakes claim needs evidence and uncertainty reporting.<br>**VN:** Claim quan trọng, hiện hành, ngách, chính xác hoặc rủi ro cao cần bằng chứng và báo cáo độ bất định. | The request is purely stylistic or the fact is immaterial.<br>**VN:** Yêu cầu chỉ về văn phong hoặc fact không ảnh hưởng kết quả. | None. / Không cần. |
| `intent-lock` | A: universal / dùng chung | Two reasonable readings would change outcome, scope, source of truth, authority, or risk.<br>**VN:** Hai cách hiểu hợp lý sẽ làm đổi kết quả, phạm vi, nguồn sự thật, thẩm quyền hoặc rủi ro. | A fact can be checked directly, or the ambiguity cannot change the decision.<br>**VN:** Có thể tự kiểm fact trực tiếp, hoặc sự mơ hồ không làm đổi quyết định. | None. / Không cần. |
| `codemap` | B: template-assisted / có template hỗ trợ | A move, split, shared schema, import, or structural refactor needs an owner and blast-radius map.<br>**VN:** Việc di chuyển, tách, đổi schema dùng chung, import hoặc refactor cấu trúc cần bản đồ owner và phạm vi ảnh hưởng. | A local behavior-only edit has known callers and no structural impact.<br>**VN:** Chỉnh sửa hành vi cục bộ đã biết caller và không ảnh hưởng cấu trúc. | Reuse an existing `CODEMAP.md` or the included template.<br>**VN:** Dùng lại `CODEMAP.md` hiện có hoặc template đi kèm. |
| `safe-edit` | B: test-assisted / có test hỗ trợ | Shared or hot behavior must change without breaking callers or platform constraints.<br>**VN:** Cần đổi hành vi dùng chung hoặc quan trọng mà không phá caller hay ràng buộc nền tảng. | A docs-only or isolated edit has no behavioral contract.<br>**VN:** Chỉnh sửa chỉ tài liệu hoặc cô lập, không có hợp đồng hành vi. | Existing tests are preferred; characterization cases can establish the baseline.<br>**VN:** Ưu tiên test hiện có; characterization case có thể thiết lập baseline. |
| `statem-single-agent` | B: external dependency / phụ thuộc ngoài | Work in a local Python workspace has at least three substantial phases or durable mutable state that may outlive context.<br>**VN:** Công việc trong workspace Python cục bộ có ít nhất ba phase thực chất hoặc state bền, có thể tồn tại lâu hơn context. | Work is short, ordinary compaction is enough, or the need is delegation or token metering.<br>**VN:** Công việc ngắn, compaction thường đã đủ, hoặc nhu cầu là giao việc hay đo token. | Install the pinned upstream StateM release described below.<br>**VN:** Cài bản StateM upstream đã pin như hướng dẫn bên dưới. |
| `version-milestones` | B: template-assisted / có template hỗ trợ | Versioned behavior, changelog, verification pins, and release metadata must stay aligned.<br>**VN:** Hành vi theo phiên bản, changelog, pin kiểm chứng và metadata release phải đồng bộ. | The change is unversioned and has no compatibility or release boundary.<br>**VN:** Thay đổi không có phiên bản, không có ranh giới tương thích hay release. | Reuse an existing ledger or the included template.<br>**VN:** Dùng lại ledger hiện có hoặc template đi kèm. |
| `provenance-memory` | C: genericized / khái quát hóa | An old project fact affects a decision, or an authorized durable correction must preserve source and validity.<br>**VN:** Fact dự án cũ ảnh hưởng quyết định, hoặc đính chính bền đã được phép cần giữ nguồn và điều kiện còn đúng. | The note is disposable session scratch, or no memory write was authorized.<br>**VN:** Ghi chú chỉ là scratch tạm của phiên, hoặc chưa được phép ghi memory. | Use the included portable memory schema.<br>**VN:** Dùng schema memory khả chuyển đi kèm. |

Classes: **A** is universal; **B** is general-purpose with a dependency, test baseline, or template;
**C** is a project-derived mechanism rewritten as a self-contained portable skill.

**Tiếng Việt:** Loại **A** dùng chung; **B** là skill đa dụng có dependency, baseline test hoặc template;
**C** là cơ chế bắt nguồn từ dự án nhưng đã được viết lại thành skill tự chứa và dùng lại được.

Only reusable workflow mechanics are shipped. Host-specific model, verbosity, and UI settings are
not skills and are not bundled. Domain-specific strategy logic, live-operation procedures, private
datasets or memory, credentials, and endpoints are intentionally excluded; a project-derived idea
is included only after it is generic, self-contained, and useful outside its source project.

**Tiếng Việt:** Chỉ các cơ chế workflow có thể tái sử dụng được đóng gói. Thiết lập model, độ dài
trả lời và UI riêng của máy không phải skill nên không nằm trong bundle. Logic chiến lược theo miền,
quy trình vận hành live, dataset hoặc memory riêng tư, thông tin xác thực và endpoint đều bị loại;
ý tưởng từ dự án chỉ được đưa vào sau khi đã khái quát hóa, tự chứa và hữu ích ngoài dự án nguồn.

## Install the complete set once / Cài cả bộ một lần

Add the GitHub marketplace and install the all-in-one plugin. / Thêm marketplace GitHub rồi cài
plugin tất-cả-trong-một:

```text
codex plugin marketplace add blavkgokuvnn/portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills
```

In the ChatGPT desktop app, refresh the Plugins Directory, select **Portable Agent Skills** from
the local source, and install it. Start a new conversation after installation.

**Tiếng Việt:** Trong ứng dụng ChatGPT desktop, làm mới Plugins Directory, chọn
**Portable Agent Skills** từ nguồn cục bộ rồi cài. Sau khi cài, hãy bắt đầu một cuộc trò chuyện mới.

Choose either the complete bundle or individual plugins, not both. If migrating from the legacy
StateM plugin or the standalone anti-over-engineering plugin, install the bundle first, then remove
the overlapping old plugins before starting a new conversation:

**Tiếng Việt:** Chọn hoặc bundle đầy đủ hoặc các plugin riêng lẻ, không dùng cả hai. Nếu chuyển từ
plugin StateM legacy hoặc plugin anti-over-engineering độc lập, hãy cài bundle trước, sau đó gỡ các
plugin cũ bị trùng trước khi bắt đầu cuộc trò chuyện mới:

```text
codex plugin remove anti-over-engineering@anti-over-engineering
codex plugin remove single-agent-skills@single-agent-skills
```

Likewise, remove any suite-owned individual selector before enabling the complete bundle. This
avoids two installed skills with the same `name`.

**Tiếng Việt:** Tương tự, hãy gỡ mọi selector riêng lẻ của bộ trước khi bật bundle đầy đủ. Việc này
tránh cài hai skill có cùng `name`.

## Install one skill / Cài một skill

Add this repository as shown above, then install any suite-owned plugin. / Thêm repository này như
hướng dẫn phía trên, rồi cài plugin riêng lẻ cần dùng:

```text
codex plugin add evidence-grounding@portable-agent-skills
codex plugin add intent-lock@portable-agent-skills
codex plugin add codemap@portable-agent-skills
codex plugin add safe-edit@portable-agent-skills
codex plugin add provenance-memory@portable-agent-skills
codex plugin add statem-single-agent@portable-agent-skills
codex plugin add version-milestones@portable-agent-skills
```

Individual suite plugins can be combined with one another. Do not install an individual selector
for a skill already supplied by the complete bundle. Choose either the legacy
`single-agent-skills` plugin or `statem-single-agent@portable-agent-skills`, because both expose
`statem-single-agent`.

**Tiếng Việt:** Có thể kết hợp các plugin riêng lẻ trong bộ với nhau. Không cài selector riêng cho
skill đã có trong bundle đầy đủ. Chỉ chọn một trong plugin legacy `single-agent-skills` hoặc
`statem-single-agent@portable-agent-skills`, vì cả hai cùng cung cấp `statem-single-agent`.

Install the canonical copy of `anti-over-engineering` from its standalone GitHub repository. /
Cài bản chuẩn của `anti-over-engineering` từ repository GitHub độc lập:

```text
codex plugin marketplace add blavkgokuvnn/anti-over-engineering
codex plugin add anti-over-engineering@anti-over-engineering
```

## StateM dependency / Dependency StateM

`statem-single-agent` keeps StateM core external. Install the supported upstream `0.1.0` commit:

**Tiếng Việt:** `statem-single-agent` giữ StateM core ở dạng dependency bên ngoài. Cài commit
upstream `0.1.0` được hỗ trợ:

```text
python -m pip install "git+https://github.com/henryqin1997/statem.git@8c3309ad3e7b265e23a4db011ff98c5f6a132bd8"
python -m statem --help
```

If the check fails, do not invoke that skill. The other seven skills do not depend on StateM.

**Tiếng Việt:** Nếu bước kiểm tra thất bại, không gọi skill đó. Bảy skill còn lại không phụ thuộc
StateM.

## Invocation and compatibility / Cách gọi và tương thích

- Codex: mention a skill as `$skill-name`; `/skills` can show installed skills. / Trong Codex, nhắc
  skill dưới dạng `$skill-name`; `/skills` có thể hiển thị các skill đã cài.
- ChatGPT: select a skill with `@`. / Trong ChatGPT, chọn skill bằng `@`.
- Seven self-contained skills permit implicit activation. Explicit invocation is more predictable
  when the trigger is not obvious. / Bảy skill tự chứa cho phép kích hoạt ngầm; gọi tường minh sẽ
  dễ đoán hơn khi trigger không rõ.
- `statem-single-agent` is only usable on a local surface that can run the pinned Python dependency
  and write `.statem/`; it requires explicit invocation and must not be invoked in ChatGPT web or
  mobile. The other seven skills have no runtime service or account dependency. /
  `statem-single-agent` chỉ dùng được trên môi trường cục bộ có thể chạy dependency Python đã pin
  và ghi `.statem/`; phải gọi tường minh và không được gọi trong ChatGPT web hoặc mobile. Bảy skill
  còn lại không phụ thuộc dịch vụ runtime hay tài khoản.
- The layout follows current Codex/ChatGPT skill and local-plugin conventions: one `SKILL.md` per
  skill, optional `agents/openai.yaml` and resources, one plugin manifest, and a repository
  marketplace manifest. / Cấu trúc theo quy ước skill và local-plugin hiện hành của Codex/ChatGPT:
  mỗi skill có một `SKILL.md`, có thể có `agents/openai.yaml` và resource, cùng một plugin manifest
  và một repository marketplace manifest.

## Canonical sources and drift check / Nguồn chuẩn và kiểm tra sai lệch

The standalone `anti-over-engineering` repository is canonical for that skill. The seven
suite-owned individual plugins are canonical for their skills. The all-in-one plugin contains
generated byte-for-byte mirrors; the legacy `single-agent-skills` repository contains only a
generated `statem-single-agent` mirror.

**Tiếng Việt:** Repository `anti-over-engineering` độc lập là nguồn chuẩn của skill đó. Bảy plugin
riêng lẻ do bộ sở hữu là nguồn chuẩn cho các skill tương ứng. Plugin tất-cả-trong-một chứa các mirror
giống từng byte; repository legacy `single-agent-skills` chỉ chứa mirror `statem-single-agent` được
sinh ra.

With the three repositories checked out as siblings, verify every mirror. / Khi ba repository được
checkout cạnh nhau, kiểm tra mọi mirror:

```text
python scripts/sync_bundle.py
```

Rewrite mirrors deterministically after an intentional canonical edit. / Sau khi chủ động sửa nguồn
chuẩn, ghi lại mirror một cách xác định:

```text
python scripts/sync_bundle.py --write
```

## Update and uninstall / Cập nhật và gỡ cài đặt

After a newer GitHub version is published, refresh the marketplace and reinstall the selected
plugin. / Sau khi bản GitHub mới được phát hành, làm mới marketplace và cài lại plugin đã chọn:

```text
codex plugin marketplace upgrade portable-agent-skills
codex plugin add portable-agent-skills@portable-agent-skills
```

Remove the bundle and marketplace with the following commands. / Gỡ bundle và marketplace bằng
các lệnh sau:

```text
codex plugin remove portable-agent-skills@portable-agent-skills
codex plugin marketplace remove portable-agent-skills
```

For an individual suite plugin, replace `portable-agent-skills` before `@` with that plugin's name.
Remove the marketplace only after all plugins installed from it have been removed.

**Tiếng Việt:** Với plugin riêng lẻ của bộ, thay `portable-agent-skills` đứng trước `@` bằng tên
plugin đó. Chỉ gỡ marketplace sau khi đã gỡ mọi plugin được cài từ marketplace này.

## Privacy and license / Quyền riêng tư và giấy phép

Installed plugin payloads contain only manifests, reusable instructions, and declared templates.
They contain no credentials, telemetry, personal data, task logs, private endpoints, or network
client. StateM writes runtime state to `.statem/`; keep it untracked and review it before sharing.

**Tiếng Việt:** Payload plugin đã cài chỉ chứa manifest, hướng dẫn tái sử dụng và template đã khai
báo. Không chứa thông tin xác thực, telemetry, dữ liệu cá nhân, log task, endpoint riêng tư hay
network client. StateM ghi runtime state vào `.statem/`; hãy giữ thư mục này untracked và kiểm tra
trước khi chia sẻ.

The repository is MIT licensed. StateM is an external Apache-2.0 dependency and is not bundled.

**Tiếng Việt:** Repository dùng giấy phép MIT. StateM là dependency Apache-2.0 bên ngoài và không
được đóng gói trong bundle.
