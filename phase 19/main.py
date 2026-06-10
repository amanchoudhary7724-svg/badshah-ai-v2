from rich.console import Console
from badshah_ai.config.logging_config import setup_logging
from badshah_ai.core.brain import Brain

console = Console()

def main():
    setup_logging()
    brain = Brain()
    console.print("[bold green]BADSHAH-AI v1.9 Final Hardening[/bold green]")
    console.print("[yellow]Type help. Type exit to close.[/yellow]")
    while True:
        q = console.input("[cyan]You > [/cyan]").strip()
        if q.lower() in {"exit","quit","close"}:
            break
        if q:
            console.print(f"[magenta]BADSHAH >[/magenta] {brain.run(q)}")

if __name__ == "__main__":
    main()
