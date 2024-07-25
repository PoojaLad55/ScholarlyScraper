import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from article_scraper_module import scrape_articles
from utils import setup_browser, random_delay

'''
Scrapes Google Scholar for article links based on the specified search query. 
It navigates through multiple pages of search results, extracts information 
about articles, and compiles a list of details.
'''

def get_link(search_terms, base_query):
    base_url = 'https://scholar.google.com'
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q={base_query}'

    article_details = []

    # Page limit and count to control how many pages to scrape
    page_limit = 1
    page_count = 0

    driver = setup_browser()

    # Navigate through multiple pages of search results
    while url and page_count < page_limit:
        try:
            driver.get(url)
            random_delay()

            results = driver.find_elements(By.CSS_SELECTOR, '.gs_ri')
            for result in results:
                # Extract title
                title_elem = result.find_element(By.CSS_SELECTOR, '.gs_rt a')
                title = title_elem.text.strip() if title_elem else 'Unable to identify title'
                
                # Extract link
                link = title_elem.get_attribute('href') if title_elem else 'No link'

                # Extract authors using primary method
                author_elems = result.find_elements(By.CSS_SELECTOR, 'div.gs_a a')
                if author_elems:
                    authors = [author.text.strip() for author in author_elems]
                else:
                    # Fallback method if primary method fails
                    author_text = result.find_element(By.CSS_SELECTOR, 'div.gs_a').text
                    authors = re.split(r'\s*-\s*', author_text)[0].strip().split(',') if author_text else ['Unable to identify author']
                    authors = [author.strip() for author in authors]
                    
                # Append details to the list
                article_details.append({
                    'title': title,
                    'authors': authors,
                    'link': link
                })

            # Navigate to the next page
            next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
            if next_button:
                onclick_attr = next_button.get_attribute('onclick')
                match = re.search(r"'/scholar\?[^']+", onclick_attr) if onclick_attr else None
                url = base_url + match.group(0)[1:].replace("\\x3d", "=").replace("\\x26", "&") if match else None
            else:
                url = None

            page_count += 1
            random_delay()

        except Exception as e:
            print("Error:", e)
            break

    driver.quit()
    scrape_articles(search_terms, article_details)