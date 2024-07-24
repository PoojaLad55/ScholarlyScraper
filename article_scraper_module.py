from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from term_counter_module import term_counter
from output_module import output_csv
from utils import setup_browser, random_delay
import requests

def scrape_articles(search_terms, article_details):
    articles_data = {}
    driver = setup_browser()

    for article in article_details:
        title = article['title']
        authors = article['authors']
        link = article['link']

        if "books.google" in link:
            print(f"Skipping book link: {link}")
            continue

        try:
            driver.get(link)
            random_delay()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            main_content_element = driver.find_element(By.TAG_NAME, 'body')  # Change this to a more specific tag if needed

            # Extract body text from the initial page
            paragraphs = main_content_element.find_elements(By.XPATH, './/p')
            article_text = ' '.join([p.text.strip() for p in paragraphs])           
                
            term_freq_dict = term_counter(article_text, search_terms)

            data = {
                'Author(s)': authors,
                'Terms and Frequency': term_freq_dict,
                'Link': link
            }

            # Add article detail to final csv dictionary
            articles_data[title] = data

        except requests.exceptions.RequestException as e:
            print("Error:", e)
    
    driver.quit()
    print(f'article data: {articles_data}')
    output_csv(articles_data)