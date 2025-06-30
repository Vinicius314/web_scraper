import pandas as pd
from scraper_playwright import get_quotes_playwright
import os


def main():
    quotes = get_quotes_playwright()

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(quotes)
    df.to_csv("data/quotes.csv", index=False, encoding='utf-8-sig', sep=';')
    print(f"[SUCESSO] {len(quotes)} citações salvas em data/quotes.csv")


if __name__ == "__main__":
    main()
