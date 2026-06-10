import asyncio
from datetime import datetime
from badshah_ai.config.settings import settings
def _normalize_url(url):
    if not url.startswith(("http://","https://")): return "https://" + url
    return url
async def _page_title(url):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=settings.browser_headless)
        page = await browser.new_page()
        await page.goto(_normalize_url(url), wait_until="domcontentloaded", timeout=30000)
        title = await page.title()
        await browser.close()
        return title or "No title"
async def _page_text(url):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=settings.browser_headless)
        page = await browser.new_page()
        await page.goto(_normalize_url(url), wait_until="domcontentloaded", timeout=30000)
        text = await page.locator("body").inner_text(timeout=15000)
        await browser.close()
        return text[:8000]
async def _screenshot(url):
    from playwright.async_api import async_playwright
    out_dir = settings.safe_workspace / "browser"; out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=settings.browser_headless)
        page = await browser.new_page(viewport={"width": 1366, "height": 768})
        await page.goto(_normalize_url(url), wait_until="domcontentloaded", timeout=30000)
        await page.screenshot(path=str(out), full_page=True)
        await browser.close()
        return f"Screenshot saved: {out}"
def browser_title(url):
    try: return asyncio.run(_page_title(url))
    except Exception as e: return "Browser title error. Run installer\\INSTALL_BROWSER_ENGINE.bat. Error: " + str(e)
def browser_text(url):
    try: return asyncio.run(_page_text(url))
    except Exception as e: return "Browser text error. Run installer\\INSTALL_BROWSER_ENGINE.bat. Error: " + str(e)
def browser_screenshot(url):
    try: return asyncio.run(_screenshot(url))
    except Exception as e: return "Browser screenshot error. Run installer\\INSTALL_BROWSER_ENGINE.bat. Error: " + str(e)
