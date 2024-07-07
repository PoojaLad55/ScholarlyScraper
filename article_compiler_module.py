import requests
import time
import re
from bs4 import BeautifulSoup
from article_scraper_module import scrape_articles

'''
Scrapes Google Scholar for article links based on a search query.
'''

def get_link(search_terms, base_query):
    # Initial URL and base URL for Google Scholar
    base_url = 'https://scholar.google.com'
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q={base_query}'

    article_links = []

    # Page limit and count to control how many pages to scrape
    page_limit = 2
    page_count = 0

    # Navigate through multiple pages of search results
    while url and page_count < page_limit:
        try:
            response = requests.get(url)
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, 'html.parser')

            for result in soup.select('.gs_ri'):
                title_tag = result.select_one('.gs_rt a')
                if title_tag:
                    link = title_tag['href']
                    article_links.append(link) # Adding link of each article to list

            # Checking for the 'Next' button to navigate to the next page of results
            next_button = soup.select_one('button[aria-label="Next"]') 
            if next_button:
                onclick_attr = next_button.get('onclick')
                match = re.search(r"'/scholar\?[^']+", onclick_attr) if onclick_attr else None
                url = base_url + match.group(0)[1:].replace("\\x3d", "=").replace("\\x26", "&") if match else None
            else:
                url = None

            page_count += 1
            time.sleep(3)

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            break

    scrape_articles(search_terms, article_links)