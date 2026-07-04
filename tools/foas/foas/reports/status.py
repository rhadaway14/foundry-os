from collections import Counter
from foas.document import FoasDocument


def status_report(docs: list[FoasDocument]) -> str:
    status_counts = Counter(doc.status or "Missing" for doc in docs)

    lines = [
        "# FOAS Status Report",
        "",
        f"Total documents: {len(docs)}",
        "",
        "## Status Counts",
        "",
    ]

    for status, count in sorted(status_counts.items()):
        lines.append(f"- {status}: {count}")

    lines.extend([
        "",
        "## Documents",
        "",
        "| ID | Title | Status | Path |",
        "|---|---|---|---|",
    ])

    for doc in sorted(docs, key=lambda d: d.id or ""):
        lines.append(
            f"| {doc.id or 'MISSING'} | {doc.title or 'MISSING'} | {doc.status or 'MISSING'} | {doc.path} |"
        )

    return "\n".join(lines) + "\n"
