from rich.console import Console
from badshah_ai.config.logging_config import setup_logging
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings
from badshah_ai.voice.speaker import Speaker

console = Console()

def main():
    setup_logging()
    brain = Brain()
    speaker = Speaker()
    console.print("[bold green]BADSHAH-AI v2 Phase 9 Production Polish[/bold green]")
    console.print("[yellow]Type: help | suggest | validate env | smoke test[/yellow]")
    while True:
        q = console.input("[cyan]You > [/cyan]").strip()
        if q.lower() in {"exit","quit","close"}:
            break
        if not q:
            continue
        ans = brain.run(q)
        console.print(f"[magenta]BADSHAH >[/magenta] {ans}")
        if settings.voice_enabled:
            speaker.say(ans[:400])

if __name__ == "__main__":
    main()
