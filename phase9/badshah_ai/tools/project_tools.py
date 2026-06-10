from badshah_ai.tools.file_tools import write_text_file

def create_static_website(name="badshah_site"):
    name = "".join(c for c in name.replace(" ","_").lower() if c.isalnum() or c in "_-") or "badshah_site"
    html = "<!doctype html><html><head><title>BADSHAH</title><link rel='stylesheet' href='style.css'></head><body><section><h1>BADSHAH Website</h1><p>Production polish ready.</p></section></body></html>"
    css = "body{margin:0;font-family:Arial;background:#0f172a;color:white}section{min-height:100vh;display:grid;place-content:center;text-align:center}h1{font-size:56px}"
    write_text_file(f"{name}/index.html", html)
    write_text_file(f"{name}/style.css", css)
    return f"Website created: workspace/{name}"
