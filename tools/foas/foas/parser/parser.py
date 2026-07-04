from pathlib import Path
import yaml

from foas.document import FoasDocument


def parse_front_matter(content: str) -> tuple[dict, str]:
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)

    if len(parts) < 3:
        return {}, content

    raw_yaml = parts[1]
    body = parts[2]

    data = yaml.safe_load(raw_yaml) or {}

    return data, body


def parse_document(path: Path) -> FoasDocument:
    content = path.read_text(encoding="utf-8")
    front_matter, _ = parse_front_matter(content)

    return FoasDocument(
        path=path,
        id=front_matter.get("id"),
        title=front_matter.get("title"),
        status=front_matter.get("status"),
        version=str(front_matter.get("version")) if front_matter.get("version") else None,
        owner=front_matter.get("owner"),
        depends_on=front_matter.get("depends_on", []) or [],
        references=front_matter.get("references", []) or [],
        implemented_by=front_matter.get("implemented_by", []) or [],
        raw_front_matter=front_matter,
    )


def discover_documents(root: Path) -> list[FoasDocument]:
    docs = []

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue

        docs.append(parse_document(path))

    return docs
