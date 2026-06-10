from badshah_ai.config.logging_config import setup_logging
from badshah_ai.core.brain import Brain
from rich.console import Console

console = Console()

def main() -> None:
    setup_logging()
    brain = Brain()
    console.print("[bold green]BADSHAH-AI v2 Phase 2 started. Type 'exit' to quit.[/bold green]")
    console.print("[yellow]Examples: read pdf path/to/file.pdf | analyze excel path/to/file.xlsx | search web AI news | write file notes.txt hello[/yellow]")

    while True:
        try:
            query = console.input("[bold cyan]You > [/bold cyan]").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold yellow]Goodbye.[/bold yellow]")
            break

        if query.lower() in {"exit", "quit", "band karo", "close"}:
            console.print("[bold yellow]Goodbye.[/bold yellow]")
            break

        if not query:
            continue

        response = brain.run(query)
        console.print(f"[bold magenta]BADSHAH >[/bold magenta] {response}")

if __name__ == "__main__":
    main()
