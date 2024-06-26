import argparse
import source_scraper_module

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

    for source in sources:
        if source.lower() != 'google scholar':
            print(f"Source '{source}' not supported. At the moment, we only support Google Scholar.")
            return
    try:
        source_scraper_module.scrape_google_scholar(search_terms)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
