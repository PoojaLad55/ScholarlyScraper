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

def get_link(search_terms, base_query, num_pages, chromedriver_path):
    base_url = 'https://scholar.google.com'
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q={base_query}'

    article_details = []
    page_count = 0

    driver = setup_browser(chromedriver_path)

    # Navigate through multiple pages of search results
    while page_count < num_pages:
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

            # After scraping all articles, check for the next page
            try:
                # Locate the next button by its 'aria-label'
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Next')]"))
                )

                if next_button:
                    onclick_attr = next_button.get_attribute('onclick')
                    if onclick_attr:
                        next_url_suffix = re.search(r"window.location='(/scholar.*?)'", onclick_attr).group(1)
                        next_url_suffix = next_url_suffix.replace("\\x3d", "=").replace("\\x26", "&")

                        # Construct the new URL for the next page
                        url = base_url + next_url_suffix
                        page_count += 1  
                        random_delay() 
                    else:
                        print("No more pages to navigate.")
                        break 
                else:
                    print("Next button not found.")
                    break

            except Exception as e:
                print("Next button not found or clickable:", e)
                break  # Exit if there's an issue finding the next button

        except Exception as e:
            print("Error:", e)
            break
            
    driver.quit()
    scrape_articles(search_terms, article_details, chromedriver_path)
