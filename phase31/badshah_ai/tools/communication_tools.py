import json
from datetime import datetime
from badshah_ai.config.settings import settings
CONTACTS_FILE = settings.safe_workspace / "contacts.json"
DRAFTS_DIR = settings.safe_workspace / "drafts"
def _contacts():
    if CONTACTS_FILE.exists():
        try: return json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))
        except Exception: return {}
    return {}
def add_contact(name, value):
    data = _contacts()
    data[name.lower()] = {"name": name, "value": value}
    CONTACTS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return f"Contact saved: {name}"
def list_contacts():
    data = _contacts()
    return "\n".join([f"{v['name']}: {v['value']}" for v in data.values()]) or "No contacts."
def create_draft(channel, target, message):
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    out = DRAFTS_DIR / f"{channel}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    out.write_text(f"CHANNEL: {channel}\nTO: {target}\nSTATUS: DRAFT ONLY\n\n{message}", encoding="utf-8")
    return f"Draft saved: {out}"
def show_drafts():
    files = sorted(DRAFTS_DIR.glob("*.txt"), reverse=True)
    return "\n".join(map(str, files[:20])) or "No drafts."
