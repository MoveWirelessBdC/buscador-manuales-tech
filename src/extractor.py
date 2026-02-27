# src/extractor.py (Versión 13.0 - Lógica de Lotes Definitiva)
import os
import asyncio
import logging
import random
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, BrowserContext
from concurrent.futures import ThreadPoolExecutor
import config

def download_image(url):
    try:
        filename = os.path.basename(url.split('?')[0])
        if not filename: return "Error"
        response = requests.get(url, timeout=30, stream=True); response.raise_for_status()
        file_path = os.path.join(config.IMAGES_DIR, filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192): f.write(chunk)
        return "Éxito"
    except requests.exceptions.RequestException: return "Error"

async def fetch_one_guide(context: BrowserContext, url: str):
    """Procesa una única guía, ahora sin pausas internas."""
    page = None
    try:
        page = await context.new_page()
        logging.info(f"Procesando: {url}")
        await page.goto(url, timeout=config.DEFAULT_TIMEOUT, wait_until="domcontentloaded")
        await page.wait_for_selector(", ".join(config.CONTENT_SELECTORS), timeout=config.DEFAULT_TIMEOUT)
        html_content = await page.content()
        soup = BeautifulSoup(html_content, 'html.parser')
        image_urls = {urljoin(url, img.get('src')) for img in soup.find_all('img') if img.get('src')}
        video_urls = {iframe.get('src') for iframe in soup.find_all('iframe') if iframe.get('src') and 'youtube.com' in iframe.get('src')}
        filename_part = url.strip('/').split('/')[-1]
        filename = f"{filename_part}.html" if not filename_part.endswith('.html') else filename_part
        file_path = os.path.join(config.HTML_RAW_DIR, filename)
        with open(file_path, 'w', encoding='utf-8') as f: f.write(html_content)
        logging.info(f"Éxito -> {filename}")
        await page.close()
        return {"status": "Éxito", "image_urls": list(image_urls), "video_urls": list(video_urls)}
    except Exception as e:
        logging.error(f"Fallo <- {url}. Causa: {e}", exc_info=False)
        if page: await page.close()
        return {"status": "Fallo", "image_urls": [], "video_urls": []}

async def _run_extraction_logic():
    username = os.environ.get("PORTAL_USER")
    password = os.environ.get("PORTAL_PASS")
    if not username or not password: raise ValueError("Credenciales no configuradas.")
    os.makedirs(config.HTML_RAW_DIR, exist_ok=True); os.makedirs(config.IMAGES_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=config.HEADLESS_MODE)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
        page = await context.new_page()
        try:
            await page.goto(config.INDEX_URL, wait_until="networkidle")
            await page.fill(config.LOGIN_USER_SELECTOR, username)
            await page.fill(config.LOGIN_PASS_SELECTOR, password)
            await page.click(config.LOGIN_BUTTON_SELECTOR)
            await page.wait_for_selector(f"{config.TFA_REMIND_SELECTOR}, {config.GUIDE_LINK_SELECTOR}")
            if await page.is_visible(config.TFA_REMIND_SELECTOR): await page.click(config.TFA_REMIND_SELECTOR)
            await page.wait_for_selector(config.GUIDE_LINK_SELECTOR)
            logging.info("Login completado.")
        except Exception as e: await browser.close(); raise e
        
        links = await page.query_selector_all(config.GUIDE_LINK_SELECTOR)
        guide_urls = list({urljoin(config.INDEX_URL, await link.get_attribute("href")) for link in links if await link.get_attribute("href") and not (await link.get_attribute("href")).startswith('#')})
        logging.info(f"Se encontraron {len(guide_urls)} guías únicas.")
        
        await page.close()
        
        # --- LÓGICA DE PROCESAMIENTO POR LOTES ---
        all_results = []
        total_batches = (len(guide_urls) + config.BATCH_SIZE - 1) // config.BATCH_SIZE
        logging.info(f"Iniciando procesamiento en {total_batches} lotes de tamaño {config.BATCH_SIZE}.")

        for i in range(0, len(guide_urls), config.BATCH_SIZE):
            batch_urls = guide_urls[i:i + config.BATCH_SIZE]
            logging.info(f"--- Procesando Lote {i // config.BATCH_SIZE + 1} de {total_batches} ---")
            
            tasks = [fetch_one_guide(context, url) for url in batch_urls]
            batch_results = await asyncio.gather(*tasks)
            all_results.extend(batch_results)
            
            if i + config.BATCH_SIZE < len(guide_urls):
                logging.info(f"Pausa de {config.BATCH_DELAY} segundos antes del siguiente lote.")
                await asyncio.sleep(config.BATCH_DELAY)
        
        # --- RECOPILACIÓN DE RESULTADOS ---
        all_image_urls, all_video_urls, success_guides = set(), set(), 0
        for result in all_results:
            if result and result["status"] == "Éxito":
                success_guides += 1
                all_image_urls.update(result["image_urls"])
                all_video_urls.update(result["video_urls"])
        logging.info(f"--- Reporte de Extracción de Guías: {success_guides} exitosas / {len(guide_urls) - success_guides} fallidas ---")
        
        if all_video_urls:
            with open(config.VIDEO_URLS_FILE, 'w', encoding='utf-8') as f:
                for url in sorted(list(all_video_urls)): f.write(url + '\n')
            logging.info(f"Se guardaron {len(all_video_urls)} URLs de video.")
        
        if all_image_urls:
            logging.info(f"Iniciando descarga de {len(all_image_urls)} imágenes...")
            with ThreadPoolExecutor(max_workers=config.MAX_DOWNLOAD_WORKERS) as executor:
                download_results = list(executor.map(download_image, all_image_urls))
            success_images = download_results.count("Éxito")
            logging.info(f"--- Reporte de Descarga de Imágenes: {success_images} exitosas / {len(all_image_urls) - success_images} fallidas ---")
        
        await browser.close()
        logging.info("Proceso de extracción finalizado.")

def run():
    try:
        asyncio.run(_run_extraction_logic())
    except Exception:
        logging.critical("El proceso de extracción se detuvo por un error fatal.")
        raise