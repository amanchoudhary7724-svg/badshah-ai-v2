from datetime import datetime
from badshah_ai.config.settings import settings
def create_draft(channel, target, message):
    out = settings.safe_workspace / "drafts" / f"{channel}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    out.write_text(f"CHANNEL: {channel}\nTO: {target}\nSTATUS: DRAFT ONLY\n\n{message}", encoding="utf-8")
    return f"Draft saved: {out}"
def show_drafts():
    files = sorted((settings.safe_workspace / "drafts").glob("*.txt"), reverse=True)
    return "\n".join(map(str, files[:20])) or "No drafts."
