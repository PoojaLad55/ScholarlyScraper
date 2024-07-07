# currently only handles HTML results not PDF
import requests
import time
import re
from bs4 import BeautifulSoup
from term_counter_module import scrape_data
from output_module import output_csv

def get_link(search_terms, base_query):
    base_url = 'https://scholar.google.com'
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q={base_query}'

    article_links = []
    page_limit = 1
    page_count = 0

    while url and page_count < page_limit:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url)
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, 'html.parser')

            for result in soup.select('.gs_ri'):
                title_tag = result.select_one('.gs_rt a')
                if title_tag:
                    link = title_tag['href']
                    article_links.append(link)

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
    
    return article_links

articles = get_link()

def get_articles(articles):
    articles_data = {}
    
    limit = 2
    count = 0

    for link in articles:

        if link in articles:
            if count >= limit:
                break

        try:
            response = requests.get(link)
            response.raise_for_status() 
            soup = BeautifulSoup(response.content, 'html.parser')

            title_elem = soup.select_one('h1[data-article-title]') or soup.select_one('h1#screen-reader-main-title span.title-text')
            title = title_elem.text.strip() if title_elem else 'Unable to identify title'

            author_elems = soup.select('ul.c-article-author-list li.c-article-author-list__item a[data-test="author-name"]') or soup.select_one('.react-xocs-alternative-link .given-name, .react-xocs-alternative-link .text.surname')
            article_authors = [author.text.strip() for author in author_elems] if author_elems else 'Unable to identify author(s)'
            
            paragraphs = soup.select('div.c-article-section__content p') or soup.select('div.Body.u-font-serif.text-s p')
            article_text = ' '.join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else 'No text content identified'

            term_freq_dict = scrape_data(article_text, 'coral')

            data = {
                'Author(s)': article_authors,
                'Terms and Frequency': term_freq_dict
            }

            articles_data[title] = data
            count += 1

        except requests.exceptions.RequestException as e:
            print("Error:", e)


    return articles_data

articles_data = get_articles(articles)

output_csv(articles_data)