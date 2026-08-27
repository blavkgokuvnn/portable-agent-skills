#!/usr/bin/env python3
"""Synchronize or verify eight standalone skills and their generated mirrors."""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


SKILL_NAMES = (
    "anti-over-engineering",
    "codemap",
    "evidence-grounding",
    "intent-lock",
    "provenance-memory",
    "safe-edit",
    "statem-single-agent",
    "version-milestones",
)


def file_hashes(root: Path) -> dict[str, str]:
    if not root.is_dir():
        raise FileNotFoundError(f"missing skill directory: {root}")
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts
    }


def require_child(path: Path, parent: Path) -> Path:
    resolved = path.resolve()
    resolved.relative_to(parent.resolve())
    return resolved


def compare(source: Path, mirror: Path, label: str) -> bool:
    source_files = file_hashes(source)
    mirror_files = file_hashes(mirror)
    if source_files == mirror_files:
        print(f"PASS {label}: {len(source_files)} files")
        return True
    missing = sorted(source_files.keys() - mirror_files.keys())
    extra = sorted(mirror_files.keys() - source_files.keys())
    changed = sorted(
        name
        for name in source_files.keys() & mirror_files.keys()
        if source_files[name] != mirror_files[name]
    )
    print(f"FAIL {label}: missing={missing} extra={extra} changed={changed}")
    return False


def replace_tree(source: Path, mirror: Path, safe_parent: Path) -> None:
    require_child(mirror, safe_parent)
    if mirror.exists():
        shutil.rmtree(mirror)
    shutil.copytree(source, mirror)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite generated mirrors")
    parser.add_argument(
        "--repos-root",
        type=Path,
        default=repo_root.parent,
        help="directory containing the eight canonical standalone repositories",
    )
    parser.add_argument(
        "--legacy-repo",
        type=Path,
        default=repo_root.parent / "single-agent-skills",
        help="checkout containing the legacy StateM-only mirror",
    )
    parser.add_argument(
        "--skip-legacy",
        action="store_true",
        help="skip the optional cross-repository StateM mirror check",
    )
    args = parser.parse_args()

    bundle_root = repo_root / "plugins" / "portable-agent-skills" / "skills"
    repos_root = args.repos_root.resolve()
    sources = {
        name: repos_root / name / "plugins" / name / "skills" / name
        for name in SKILL_NAMES
    }

    for name, source in sources.items():
        file_hashes(source)
        require_child(bundle_root / name, bundle_root)

    bundle_root.mkdir(parents=True, exist_ok=True)
    unexpected = sorted(
        path.name
        for path in bundle_root.iterdir()
        if path.is_dir() and path.name not in SKILL_NAMES
    )
    if unexpected:
        raise SystemExit(f"refusing to touch unexpected bundle directories: {unexpected}")

    legacy_skill = (
        args.legacy_repo.resolve()
        / "plugins"
        / "single-agent-skills"
        / "skills"
        / "statem-single-agent"
    )

    if args.write:
        for name, source in sources.items():
            replace_tree(source, bundle_root / name, bundle_root)
        if not args.skip_legacy:
            legacy_parent = legacy_skill.parent
            if not legacy_parent.is_dir():
                raise FileNotFoundError(f"missing legacy skills directory: {legacy_parent}")
            replace_tree(sources["statem-single-agent"], legacy_skill, legacy_parent)

    ok = True
    for name, source in sources.items():
        ok = compare(source, bundle_root / name, f"bundle/{name}") and ok
    if not args.skip_legacy:
        ok = compare(
            sources["statem-single-agent"],
            legacy_skill,
            "legacy/statem-single-agent",
        ) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
