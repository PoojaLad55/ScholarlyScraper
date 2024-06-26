import argparse
from scraper_module import scrape_data

def main():
    parser = argparse.ArgumentParser(description="Scrape research papers from Google Scholar.")
    parser.add_argument('--terms', required=True, help='Comma-separated list of search terms')
    parser.add_argument('--sources', required=True, help='Comma-separated list of sources')
    args = parser.parse_args()

    search_terms = [term.strip() for term in args.terms.split(',')]
    sources = [source.strip() for source in args.sources.split(',')]

    if not search_terms:
        search_terms = input("Enter search terms (comma-separated): ").split(',')
    if not sources:
        sources = input("Enter sources (comma-separated): ").split(',')

    try:
        scrape_data(search_terms, sources)
        print("Scraping completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
