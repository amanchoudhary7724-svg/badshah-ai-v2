from badshah_ai.tools.file_tools import write_text_file

def create_static_website(project_name: str = "badshah_site") -> str:
    safe_name = "".join(c for c in project_name.lower().replace(" ", "_") if c.isalnum() or c in {"_", "-"})
    if not safe_name:
        safe_name = "badshah_site"

    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BADSHAH Website</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="hero">
    <nav>
      <h2>BADSHAH</h2>
      <a href="#contact">Contact</a>
    </nav>
    <div class="hero-content">
      <h1>Premium Modern Website</h1>
      <p>Fast, responsive and ready to customize.</p>
      <a class="btn" href="#contact">Get Started</a>
    </div>
  </header>
  <section class="cards">
    <div><h3>Modern Design</h3><p>Clean responsive layout.</p></div>
    <div><h3>SEO Ready</h3><p>Structured content and fast pages.</p></div>
    <div><h3>Lead Focused</h3><p>Contact form and CTA ready.</p></div>
  </section>
  <section id="contact" class="contact">
    <h2>Contact</h2>
    <form>
      <input placeholder="Name" />
      <input placeholder="Email" />
      <textarea placeholder="Message"></textarea>
      <button type="button">Submit</button>
    </form>
  </section>
</body>
</html>'''

    css = '''*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;background:#0f172a;color:#fff}a{color:inherit;text-decoration:none}.hero{min-height:80vh;padding:24px;background:linear-gradient(135deg,#111827,#1d4ed8)}nav{display:flex;justify-content:space-between;align-items:center}.hero-content{max-width:720px;margin:120px auto;text-align:center}.hero h1{font-size:56px;margin:0 0 16px}.hero p{font-size:20px;color:#dbeafe}.btn,button{display:inline-block;background:#fff;color:#1d4ed8;padding:14px 24px;border-radius:999px;font-weight:bold;border:0;cursor:pointer}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px;padding:50px;max-width:1100px;margin:auto}.cards div,.contact{background:#111827;border:1px solid #334155;border-radius:20px;padding:24px}.contact{max-width:700px;margin:40px auto}.contact form{display:grid;gap:14px}input,textarea{padding:14px;border-radius:10px;border:1px solid #475569;background:#020617;color:#fff}textarea{min-height:120px}@media(max-width:600px){.hero h1{font-size:38px}.cards{padding:20px}}'''

    js = "console.log('BADSHAH website ready');"

    write_text_file(f"{safe_name}/index.html", html)
    write_text_file(f"{safe_name}/style.css", css)
    write_text_file(f"{safe_name}/script.js", js)
    return f"Static website created inside workspace/{safe_name}/. Open index.html in browser."
