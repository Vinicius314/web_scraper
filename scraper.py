from playwright.sync_api import sync_playwright
import os
import requests


def baixar_imagem(url, nome_arquivo):
    if not url:
        return
    try:
        img = requests.get(url, timeout=10)
        with open(nome_arquivo, 'wb') as f:
            f.write(img.content)
    except Exception as e:
        print(f"[ERRO] Não foi possível baixar {url}: {e}")


def get_quotes_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://quotes.toscrape.com", timeout=60000)

        quotes_data = []
        pagina = 1

        while True:
            print(f"[INFO] Página {pagina}...")

            page.wait_for_selector(".quote")
            quote_elems = page.query_selector_all(".quote")

            # Primeiro passo: extrair infos em memória
            quote_infos = []
            for quote in quote_elems:
                text = quote.query_selector(".text").inner_text()
                author = quote.query_selector(".author").inner_text()
                tags = [t.inner_text() for t in quote.query_selector_all(".tag")]
                author_link = quote.query_selector("a").get_attribute("href")
                quote_infos.append({
                    'text': text,
                    'author': author,
                    'tags': tags,
                    'author_url': f"http://quotes.toscrape.com{author_link}"
                })

            # Segundo passo: visitar cada autor e baixar a imagem
            for info in quote_infos:
                page.goto(info['author_url'])
                try:
                    img_elem = page.query_selector("img")
                    img_url = img_elem.get_attribute("src") if img_elem else None
                    full_img_url = f"http://quotes.toscrape.com{img_url}" if img_url else None

                    os.makedirs("data/images", exist_ok=True)
                    caminho_img = f"data/images/{info['author'].replace(' ', '_')}.jpg"
                    baixar_imagem(full_img_url, caminho_img)
                except:
                    print(f"[AVISO] Sem imagem para {info['author']}")

                # Armazena a citação
                quotes_data.append({
                    'text': info['text'],
                    'author': info['author'],
                    'tags': ", ".join(info['tags'])
                })

            # Voltar para página de citações
            next_btn = page.query_selector(".next > a")
            if not next_btn:
                break
            next_btn.click()
            pagina += 1

        browser.close()
        return quotes_data
