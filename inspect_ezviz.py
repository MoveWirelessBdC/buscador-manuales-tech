import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://support.ezviz.com/download", wait_until="networkidle")
        
        # Guardar todo el HTML para inspeccionarlo nosotros localmente con un script rapido
        html = await page.content()
        with open("ezviz_dom.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        print("DOM guardado en ezviz_dom.html")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
