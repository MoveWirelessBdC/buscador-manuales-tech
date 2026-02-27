# diagnose_url.py (Versión 1.1 - Corregida)
import asyncio
import sys
import time
import os  # <-- LA LÍNEA QUE FALTABA
from playwright.async_api import async_playwright
import config

async def measure_load_time(url: str):
    """Navega a una URL y mide el tiempo que tarda en cargar y encontrar el contenido."""
    print(f"Iniciando diagnóstico para: {url}\n")
    username = os.environ.get("PORTAL_USER")
    password = os.environ.get("PORTAL_PASS")
    if not username or not password:
        print("ADVERTENCIA: Las credenciales del portal no están configuradas.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            print("Iniciando sesión en el portal para asegurar la autenticación...")
            await page.goto(config.INDEX_URL, wait_until="networkidle")
            await page.fill(config.LOGIN_USER_SELECTOR, username)
            await page.fill(config.LOGIN_PASS_SELECTOR, password)
            await page.click(config.LOGIN_BUTTON_SELECTOR)
            await page.wait_for_selector(f"{config.TFA_REMIND_SELECTOR}, {config.GUIDE_LINK_SELECTOR}")
            if await page.is_visible(config.TFA_REMIND_SELECTOR):
                await page.click(config.TFA_REMIND_SELECTOR)
            await page.wait_for_selector(config.GUIDE_LINK_SELECTOR)
            print("Login completado.\n")
            
            start_time = time.monotonic()
            test_timeout = 120000 
            
            print(f"Navegando a la URL de prueba y esperando 'domcontentloaded' (Timeout: {test_timeout / 1000}s)...")
            await page.goto(url, timeout=test_timeout, wait_until="domcontentloaded")
            
            dom_loaded_time = time.monotonic()
            print(f"-> 'domcontentloaded' alcanzado en: {dom_loaded_time - start_time:.2f} segundos.")
            
            print("Esperando que el selector de contenido sea visible...")
            content_selector = ", ".join(config.CONTENT_SELECTORS)
            await page.wait_for_selector(content_selector, timeout=test_timeout)
            
            content_visible_time = time.monotonic()
            print(f"-> Contenido visible en: {content_visible_time - start_time:.2f} segundos.")
            
            print("\n--- ✅ Diagnóstico Exitoso ---")
            
        except Exception as e:
            print(f"\n--- ❌ Diagnóstico Fallido ---")
            print(f"Causa: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python diagnose_url.py \"<url_a_probar>\"")
    else:
        url_to_test = sys.argv[1]
        asyncio.run(measure_load_time(url_to_test))