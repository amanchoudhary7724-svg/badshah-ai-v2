import json
from datetime import datetime
from badshah_ai.config.settings import settings

CONTACTS_FILE = settings.safe_workspace / "contacts.json"
DRAFTS_DIR = settings.safe_workspace / "drafts"
CAL_DIR = settings.safe_workspace / "calendar"

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

def _contact(name):
    return _load_contacts().get(name.lower(), {"name": name, "value": ""})

def email_draft(target, message, subject="BADSHAH-AI Draft"):
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    c = _contact(target)
    out = DRAFTS_DIR / f"email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    body = f'''TYPE: EMAIL DRAFT
TO_NAME: {c.get("name", target)}
TO: {c.get("value", "")}
SUBJECT: {subject}
STATUS: DRAFT ONLY - REVIEW BEFORE SEND

BODY:
{message}
'''
    out.write_text(body, encoding="utf-8")
    return f"Email draft saved: {out}"

def followup_email(target, topic):
    msg = f"Hello {target},\n\nThis is a follow-up regarding: {topic}.\n\nPlease let me know the update.\n\nRegards"
    return email_draft(target, msg, subject=f"Follow-up: {topic}")

def meeting_invite(target, topic):
    msg = f"Hello {target},\n\nI would like to schedule a meeting for: {topic}.\n\nPlease confirm your availability.\n\nRegards"
    email_result = email_draft(target, msg, subject=f"Meeting Invite: {topic}")
    cal_result = calendar_draft(f"Meeting: {topic}", f"Invitee: {target}\nTopic: {topic}")
    return email_result + "\n" + cal_result

def calendar_draft(title, details):
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    out = CAL_DIR / f"calendar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    body = f'''TYPE: CALENDAR EVENT DRAFT
TITLE: {title}
STATUS: DRAFT ONLY - REVIEW BEFORE CREATE

DETAILS:
{details}
'''
    out.write_text(body, encoding="utf-8")
    return f"Calendar draft saved: {out}"

def show_drafts():
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(DRAFTS_DIR.glob("*.txt"), reverse=True)
    return "\n".join(str(p) for p in files[:20]) if files else "No email drafts found."

def show_calendar_drafts():
    CAL_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(CAL_DIR.glob("*.txt"), reverse=True)
    return "\n".join(str(p) for p in files[:20]) if files else "No calendar drafts found."
