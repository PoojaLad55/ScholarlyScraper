import requests
import time
import re
from bs4 import BeautifulSoup

def get_link():
    url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q=coralreef"
    base_url = "https://scholar.google.com"

    article_links = []
    page_limit = 3
    page_count = 0

    while url and page_count < page_limit:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url)
            response.raise_for_status() 
            response = response.content
            soup = BeautifulSoup(response, 'html.parser')

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
    

