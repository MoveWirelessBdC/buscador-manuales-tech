import logging
from playwright.async_api import async_playwright

async def obtener_pdf_ezviz(modelo: str) -> dict:
    """Busca el manual en PDF para un modelo específico de EZVIZ en su sitio de soporte."""
    url_base = "https://www.ezviz.com/es/support"
    try:
        async with async_playwright() as p:
            # Iniciamos navegador en modo headless
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
            page = await context.new_page()

            logging.info(f"Navegando a soporte EZVIZ buscando modelo: {modelo}")
            await page.goto(url_base, wait_until="domcontentloaded")

            # Buscando el elemento de input de busqueda en soporte. Note: los selectores exactos
            # pueden variar dependiendo de la estructura de la web de EZVIZ.
            # Esta es una aproximación estándar a la barra de búsqueda general:
            search_input_selector = 'input[type="text"], input[name="search"], .search-input'
            await page.wait_for_selector(search_input_selector, timeout=10000)
            
            await page.fill(search_input_selector, modelo)
            await page.keyboard.press("Enter")

            # Esperando que carguen resultados y buscando enlaces a PDF
            # EZVIZ suele usar subdominios como mfs.ezvizlife.com o descargas directas que terminan en .pdf
            # Esperamos algunos segundos para que se rendericen los resultados
            await page.wait_for_timeout(3000)
            
            # Buscando anchors que contengan .pdf en su href
            pdf_links = await page.query_selector_all('a[href$=".pdf"]')
            
            # Si no encuentra .pdf directamente, buscamos botones que digan "Manual" o "User Manual" 
            # que apunten a mfs.ezvizlife.com
            if not pdf_links:
                pdf_links = await page.query_selector_all('a[href*="mfs.ezvizlife.com"]:has-text("Manual"), a[href*="mfs.ezvizlife.com"]:has-text("User"), a[href$=".pdf"]')
                
            pdf_url = None
            for link in pdf_links:
                href = await link.get_attribute('href')
                if href and ('.pdf' in href.lower() or 'mfs.ezvizlife.com' in href.lower()):
                    pdf_url = href
                    break
            
            await browser.close()

            if pdf_url:
                logging.info(f"PDF encontrado para {modelo}: {pdf_url}")
                return {"status": "success", "pdf_url": pdf_url}
            else:
                logging.warning(f"No se encontró PDF para el modelo {modelo}")
                return {"status": "error", "message": "Manual PDF no encontrado tras la búsqueda."}

    except Exception as e:
        logging.error(f"Error buscando PDF de EZVIZ para {modelo}: {e}")
        return {"status": "error", "message": f"Fallo interno en la búsqueda web: {str(e)}"}
