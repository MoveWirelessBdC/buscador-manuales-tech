import asyncio
import json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        apis_interceptadas = []

        # Escuchar todas las respuestas de red
        async def handle_response(response):
            if "json" in response.headers.get("content-type", "") and "api" in response.url:
                try:
                    data = await response.json()
                    apis_interceptadas.append({"url": response.url, "data": data})
                except:
                    pass

        page.on("response", handle_response)

        await page.goto("https://support.ezviz.com/download", wait_until="networkidle")
        await page.wait_for_timeout(5000)

        # Hacer click en algunas categorias para forzar llamadas
        try:
             botones = await page.query_selector_all(".nav-menu__cate-name, .menu-item")
             for btn in botones[:5]:
                  await btn.click()
                  await page.wait_for_timeout(1000)
        except:
             pass

        with open("ezviz_apis.json", "w") as f:
             json.dump(apis_interceptadas, f, indent=2)

        print(f"Interceptadas {len(apis_interceptadas)} respuestas API JSON.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
