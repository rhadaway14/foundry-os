from foas.document import FoasDocument


def generate_mermaid(docs: list[FoasDocument]) -> str:
    lines = ["graph TD"]

    by_id = {doc.id: doc for doc in docs if doc.id}

    for doc in docs:
        if not doc.id:
            continue

        label = f'{doc.id}["{doc.id}<br/>{doc.title or ""}"]'
        lines.append(f"  {label}")

        for dep in doc.depends_on:
            if dep in by_id:
                lines.append(f"  {dep} --> {doc.id}")

        for ref in doc.references:
            if ref in by_id:
                lines.append(f"  {doc.id} -.-> {ref}")

    return "\n".join(lines) + "\n"
