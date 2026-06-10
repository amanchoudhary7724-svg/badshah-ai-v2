from pathlib import Path
from datetime import datetime
def handle(command: str) -> str:
    out_dir = Path("workspace") / "plugin_notes"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    out.write_text(command.replace("custom note", "", 1).strip(), encoding="utf-8")
    return f"Custom note saved: {out}"
