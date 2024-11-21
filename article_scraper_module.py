from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from term_counter_module import term_counter
from output_module import output_csv
from utils import setup_browser, random_delay
import requests

'''
Scrapes text content from a list of article links, processes the content to 
count the frequency of specified search terms, and organizes the data for output. 
'''

def scrape_articles(search_terms, article_details, chromedriver_path):
    articles_data = {}
    driver = setup_browser(chromedriver_path)

    # Iterate over each article in the provided article details
    for article in article_details:
        # Extract title, authors, and link from the article details
        title = article['title']
        authors = article['authors']
        link = article['link']

        # Skip articles that are books based on the presence of "books.google" in the link
        if "books.google" in link:
            print(f"Skipping book link: {link}")
            continue

        try:
            driver.get(link)
            random_delay()

            # Extract text content of the articles
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            main_content_element = driver.find_element(By.TAG_NAME, 'body') 

            paragraphs = main_content_element.find_elements(By.XPATH, './/p')
            article_text = ' '.join([p.text.strip() for p in paragraphs])           
            
            # Count the frequency of search terms in the article text
            term_freq_dict = term_counter(article_text, search_terms)

            # Create a dictionary with the extracted data for this article
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
    # Output the article data to a CSV file
    output_csv(articles_data)