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

            # NUEVO ENFOQUE: Navegar directamente al Centro de Soporte de EZVIZ 
            # usando interacciones web controladas en lugar del search input roto.
            url_soporte_global = "https://support.ezviz.com/es-es/"
            logging.info(f"Navegando al centro de descargas manual de EZVIZ: {url_soporte_global}")
            
            await page.goto(url_soporte_global, wait_until="networkidle")
            
            # Buscar el botón o icono de "Manuales"
            await page.wait_for_timeout(2000)
            try:
                # Ocultar banners de cookies u otros iframes superpuestos de chateo
                has_cookie_btn = await page.query_selector("button:has-text('Aceptar')")
                if has_cookie_btn: await has_cookie_btn.click()
            except Exception:
                pass
                
            # Buscar directamente en Duckduckgo la seccion "download" de la marca
            search_query = f"site:ezviz.com/page/download {modelo}"
            ddg_url = f"https://html.duckduckgo.com/html/?q={search_query.replace(' ', '+')}"
            
            logging.info(f"Buscando el área de decodificación en DDG: {search_query}")
            await page.goto(ddg_url, wait_until="domcontentloaded")
            
            # Tomamos cualquier PDF que salga indexado ahí, o cualquier URL de página de descarga
            direct_pdf_result = page.locator('a.result__url[href$=".pdf"]').first
            if await direct_pdf_result.is_visible():
                pdf_url = await direct_pdf_result.get_attribute("href")
                pdf_url_clean = await page.evaluate("(element) => element.href", await direct_pdf_result.element_handle())
                await browser.close()
                return {"status": "success", "pdf_url": pdf_url_clean}
                
            first_result = page.locator('a.result__url[href*="ezviz.com/"]').first
            
            if not await first_result.is_visible():
                logging.warning(f"No se encontró el producto de forma convencional. Retornando a URL manual en base a deducción.")
                # Muchos de los manuales en ezviz siguen este estándar si conocemos el modelo, 
                # Intentamos forzar la URL
                posible_url = f"https://mfs.ezvizlife.com/E-user-manual_{modelo}_ES.pdf"
                await browser.close()
                return {"status": "success", "pdf_url": posible_url, "nota": "Aproximado por estándar, verificar validez de link."}

            url_soporte = await first_result.get_attribute("href")
            # Extraer de duckduckgo wrapper si existe
            if 'uddg=' in url_soporte:
                import urllib.parse
                parsed = urllib.parse.urlparse(url_soporte)
                qs = urllib.parse.parse_qs(parsed.query)
                if 'uddg' in qs: url_soporte = qs['uddg'][0]

            logging.info(f"Navegando a primera coincidencia web de soporte: {url_soporte}")
            await page.goto(url_soporte, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)
            
            pdf_links = await page.query_selector_all('a[href$=".pdf"], a[href*="mfs.ezvizlife.com"]')
            pdf_url = None
            
            if not pdf_links:
                logging.info(f"Intentando hacer click en pestañas de Documentos o Manuales")
                # Intentando clickear la pestaña 'Manuals', 'Downloads', 'Documents' en el DOM del producto
                tabs = await page.query_selector_all('.tab, .nav-item, li, button')
                for tab in tabs:
                    texto = await tab.inner_text()
                    if texto and any(kw in texto.lower() for kw in ('manual', 'descarga', 'download', 'document')):
                        await tab.click()
                        await page.wait_for_timeout(2000)
                        break
                pdf_links = await page.query_selector_all('a[href$=".pdf"], a[href*="mfs.ezvizlife.com"]')
            
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
