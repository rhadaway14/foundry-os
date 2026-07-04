import argparse
from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

from foas.parser.parser import discover_documents
from foas.validator.validator import validate_documents
from foas.graph.graph import generate_mermaid
from foas.reports.status import status_report
from foas.bootstrap import bootstrap_docs


console = Console()


def cmd_status(args):
    docs = discover_documents(Path(args.root))

    table = Table(title="FOAS Documents")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Path")

    for doc in sorted(docs, key=lambda d: d.id or ""):
        table.add_row(
            doc.id or "MISSING",
            doc.title or "MISSING",
            doc.status or "MISSING",
            str(doc.path),
        )

    console.print(table)


def cmd_validate(args):
    docs = discover_documents(Path(args.root))
    errors = validate_documents(docs)

    if not errors:
        console.print("[green]FOAS validation passed.[/green]")
        return

    console.print("[red]FOAS validation failed.[/red]")
    for error in errors:
        console.print(f"[red]- {error}[/red]")

    sys.exit(1)


def cmd_graph(args):
    docs = discover_documents(Path(args.root))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate_mermaid(docs), encoding="utf-8")
    console.print(f"[green]Wrote Mermaid graph to {output}[/green]")


def cmd_report(args):
    docs = discover_documents(Path(args.root))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(status_report(docs), encoding="utf-8")
    console.print(f"[green]Wrote status report to {output}[/green]")


def cmd_bootstrap(args):
    changed = bootstrap_docs(Path(args.root), owner=args.owner)

    if not changed:
        console.print("[green]No documents needed bootstrapping.[/green]")
        return

    console.print(f"[green]Bootstrapped {len(changed)} documents:[/green]")
    for path in changed:
        console.print(f"- {path}")


def main():
    parser = argparse.ArgumentParser(description="FOAS Toolchain")
    parser.add_argument("--root", default="docs", help="Documentation root")

    sub = parser.add_subparsers(required=True)

    status = sub.add_parser("status")
    status.set_defaults(func=cmd_status)

    validate = sub.add_parser("validate")
    validate.set_defaults(func=cmd_validate)

    graph = sub.add_parser("graph")
    graph.add_argument("--output", default="tools/foas/output/foas-graph.md")
    graph.set_defaults(func=cmd_graph)

    report = sub.add_parser("report")
    report.add_argument("--output", default="tools/foas/output/status-report.md")
    report.set_defaults(func=cmd_report)

    bootstrap = sub.add_parser("bootstrap")
    bootstrap.add_argument("--owner", default="Robert Hadaway")
    bootstrap.set_defaults(func=cmd_bootstrap)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
