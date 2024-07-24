import argparse
from urllib.parse import quote
from article_compiler_module import get_link

'''
This script scrapes research papers from Google Scholar based on user-provided search terms.
It uses the argparse module to handle command-line arguments for search terms and sources.
The search terms and sources are processed to ensure they are valid and supported.
Currently, only Google Scholar is supported as a source.
'''

def main():
    parser = argparse.ArgumentParser(description="Scrape research papers from Google Scholar.") 
    parser.add_argument('--base-query', required=True, help='Base Google Scholar search query')
    parser.add_argument('--terms', required=True, help='Comma-separated list of search terms')
    parser.add_argument('--sources', required=True, help='Comma-separated list of sources')
    args = parser.parse_args()

    base_query = quote(args.base_query)  
    
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
        get_link(search_terms, base_query)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()