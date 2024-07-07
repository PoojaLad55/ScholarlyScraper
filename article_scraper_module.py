import requests
from bs4 import BeautifulSoup
from term_counter_module import term_counter
from output_module import output_csv

'''
Scrapes article data from a list of article links, including title, authors, and frequency of user's search terms.
'''

def scrape_articles(search_terms, article_links):
    articles_data = {}

    for link in article_links:

        try:
            response = requests.get(link)
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the article title
            title_elem = soup.select_one('h1[data-article-title]') or soup.select_one('h1#screen-reader-main-title span.title-text')
            title = title_elem.text.strip() if title_elem else 'Unable to identify title'

            # Extract the article authors
            author_elems = soup.select('ul.c-article-author-list li.c-article-author-list__item a[data-test="author-name"]') or soup.select_one('.react-xocs-alternative-link .given-name, .react-xocs-alternative-link .text.surname')
            article_authors = [author.text.strip() for author in author_elems] if author_elems else 'Unable to identify author(s)'
            
            # Extract paragraphs of the article text
            paragraphs = soup.find_all('p')  # Adjust based on HTML structure
            article_text = ' '.join([p.text.strip() for p in paragraphs])

            # Count term frequencies in the article text
            term_freq_dict = term_counter(article_text, search_terms)

            data = {
                'Author(s)': article_authors,
                'Terms and Frequency': term_freq_dict,
                'Link': link
            }

            # Add article detail to final csv dictionary
            articles_data[title] = data

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    # Output the scraped data to a CSV file
    output_csv(articles_data)