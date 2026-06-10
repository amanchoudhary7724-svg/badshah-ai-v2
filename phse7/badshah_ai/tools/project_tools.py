from badshah_ai.tools.file_tools import write_text_file

def create_static_website(name="badshah_site"):
    name = "".join(c for c in name.replace(" ","_").lower() if c.isalnum() or c in "_-") or "badshah_site"
    html = '''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>BADSHAH</title><link rel="stylesheet" href="style.css"></head><body><section><h1>BADSHAH Website</h1><p>Modern responsive website ready.</p><button>Contact</button></section></body></html>'''
    css = '''body{margin:0;font-family:Arial;background:#0f172a;color:white}section{min-height:100vh;display:grid;place-content:center;text-align:center}h1{font-size:56px}button{padding:14px 26px;border:0;border-radius:30px}'''
    write_text_file(f"{name}/index.html", html)
    write_text_file(f"{name}/style.css", css)
    return f"Website created: workspace/{name}"
