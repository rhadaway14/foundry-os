from pathlib import Path
from datetime import date
import re
import yaml


API_IDS = {
    "REST-API.md": ("SPEC-001", "REST API"),
    "WebSocket-API.md": ("SPEC-002", "WebSocket API"),
    "Event-API.md": ("SPEC-003", "Event API"),
}

SDK_IDS = {
    "Worker-SDK.md": ("SPEC-006", "Worker SDK"),
    "Agent-SDK.md": ("SPEC-007", "Agent SDK"),
    "Plugin-SDK.md": ("SPEC-008", "Plugin SDK"),
}


def title_from_slug(slug: str) -> str:
    slug = slug.replace(".md", "")
    slug = re.sub(r"^(ARC|SPEC|MODEL|GOV|ADR|FOAS)-?\d+-?", "", slug)
    slug = re.sub(r"^\d+-", "", slug)
    slug = slug.replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() if word.upper() not in {"API", "SDK", "OS"} else word.upper() for word in slug.split())


def infer_metadata(path: Path) -> dict:
    name = path.name
    text_path = str(path).replace("\\", "/")

    if name == "FOAS-000-Architecture-Index.md":
        return {
            "id": "FOAS-000",
            "title": "Foundry OS Architecture Specification",
            "status": "Active",
        }

    if "/architecture/adr/" in text_path:
        match = re.match(r"(\d{4})-(.+)\.md", name)
        if match:
            return {
                "id": f"ADR-{match.group(1)}",
                "title": title_from_slug(match.group(2)),
                "status": "Accepted" if name in {
                    "0002-worker-agent-separation.md",
                    "0003-event-driven-core.md",
                    "0004-state-store.md",
                } else "Draft",
            }

    if name.startswith("ARC-"):
        match = re.match(r"(ARC-\d+)-(.+)\.md", name)
        if match:
            return {
                "id": match.group(1),
                "title": title_from_slug(match.group(2)),
                "status": "Draft",
            }

    if name in API_IDS:
        doc_id, title = API_IDS[name]
        return {"id": doc_id, "title": title, "status": "Draft"}

    if name in SDK_IDS:
        doc_id, title = SDK_IDS[name]
        return {"id": doc_id, "title": title, "status": "Draft"}

    if name == "README.md":
        if text_path == "docs/README.md":
            return {"id": "DOCS-README", "title": "Documentation README", "status": "Draft"}
        if text_path == "docs/architecture/README.md":
            return {"id": "ARC-README", "title": "Architecture README", "status": "Draft"}

    return {
        "id": None,
        "title": title_from_slug(name),
        "status": "Draft",
    }


def has_front_matter(content: str) -> bool:
    return content.startswith("---\n")


def bootstrap_document(path: Path, owner: str = "Robert Hadaway") -> bool:
    content = path.read_text(encoding="utf-8")

    if has_front_matter(content):
        return False

    meta = infer_metadata(path)

    if not meta.get("id"):
        return False

    front_matter = {
        "id": meta["id"],
        "title": meta["title"],
        "status": meta["status"],
        "version": "1.0",
        "owner": owner,
        "reviewers": ["Robert Hadaway"],
        "depends_on": [],
        "references": [],
        "implemented_by": [],
        "last_updated": date.today().isoformat(),
    }

    yaml_text = yaml.safe_dump(front_matter, sort_keys=False).strip()

    new_content = f"---\n{yaml_text}\n---\n\n{content.lstrip()}"
    path.write_text(new_content, encoding="utf-8")

    return True


def bootstrap_docs(root: Path, owner: str = "Robert Hadaway") -> list[Path]:
    changed = []

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue

        if bootstrap_document(path, owner):
            changed.append(path)

    return changed
