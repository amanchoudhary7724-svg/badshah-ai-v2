from rich.console import Console
from badshah_ai.config.logging_config import setup_logging
from badshah_ai.config.settings import settings
from badshah_ai.core.brain import Brain
from badshah_ai.voice.speaker import Speaker
from badshah_ai.voice.listener import Listener

console = Console()

def main():
    setup_logging()
    brain = Brain()
    speaker = Speaker()
    listener = Listener()
    wake = settings.wake_word.lower()

    console.print(f"[bold green]BADSHAH-AI Voice Mode started. Wake word: {wake}[/bold green]")
    speaker.say("Badshah AI voice mode started")

    while True:
        text = listener.listen_once()
        if not text:
            continue

        console.print(f"[cyan]Heard:[/cyan] {text}")
        lower = text.lower().strip()

        if wake not in lower:
            continue

        command = lower.replace(wake, "", 1).strip()
        if not command:
            speaker.say("Ji, boliye")
            continue

        if command in {"exit", "quit", "close", "band karo"}:
            speaker.say("Goodbye")
            break

        response = brain.run(command)
        console.print(f"[magenta]BADSHAH >[/magenta] {response}")
        speaker.say(response[:500])

if __name__ == "__main__":
    main()
