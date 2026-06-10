import json
from datetime import datetime
from pathlib import Path
from badshah_ai.config.settings import settings

CONTACTS_FILE = settings.safe_workspace / "contacts.json"
DRAFTS_DIR = settings.safe_workspace / "drafts"

def _load_contacts():
    if not CONTACTS_FILE.exists():
        return {}
    try:
        return json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}

def _save_contacts(data):
    CONTACTS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def add_contact(name, value):
    contacts = _load_contacts()
    contacts[name.lower()] = {"name": name, "value": value}
    _save_contacts(contacts)
    return f"Contact saved: {name} -> {value}"

def list_contacts():
    contacts = _load_contacts()
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{v['name']}: {v['value']}" for v in contacts.values()])

def resolve_contact(name):
    contacts = _load_contacts()
    return contacts.get(name.lower(), {"name": name, "value": ""})

def create_draft(channel, target, message):
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    contact = resolve_contact(target)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_channel = "".join(c for c in channel.lower() if c.isalnum() or c in "_-")
    out = DRAFTS_DIR / f"{safe_channel}_{ts}.txt"
    body = f'''CHANNEL: {channel}
TO: {contact.get("name", target)}
CONTACT: {contact.get("value", "")}
STATUS: DRAFT ONLY - REVIEW BEFORE SEND

MESSAGE:
{message}
'''
    out.write_text(body, encoding="utf-8")
    return f"{channel.title()} draft saved: {out}"

def show_drafts(limit=20):
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(DRAFTS_DIR.glob("*.txt"), reverse=True)[:limit]
    if not files:
        return "No drafts found."
    return "\n".join(str(p) for p in files)
