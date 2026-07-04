from collections import Counter
from foas.document import FoasDocument


VALID_STATUSES = {
    "Planned",
    "Draft",
    "Review",
    "Accepted",
    "Implemented",
    "Deprecated",
    "Active",
}


def validate_documents(docs: list[FoasDocument]) -> list[str]:
    errors = []

    ids = [doc.id for doc in docs if doc.id]
    id_counts = Counter(ids)

    for doc in docs:
        rel = str(doc.path)

        if not doc.id:
            errors.append(f"{rel}: missing id")

        if not doc.title:
            errors.append(f"{rel}: missing title")

        if not doc.status:
            errors.append(f"{rel}: missing status")

        if doc.status and doc.status not in VALID_STATUSES:
            errors.append(f"{rel}: invalid status '{doc.status}'")

    for doc_id, count in id_counts.items():
        if count > 1:
            errors.append(f"duplicate id: {doc_id}")

    known_ids = set(ids)

    for doc in docs:
        for dep in doc.depends_on:
            if dep not in known_ids:
                errors.append(f"{doc.id}: depends_on missing document {dep}")

        for ref in doc.references:
            if ref not in known_ids:
                errors.append(f"{doc.id}: references missing document {ref}")

    return errors
