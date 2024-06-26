import output_module, term_counter_module, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def scrape_google_scholar(search_terms):

    print(f"Scraping data for terms: {search_terms} from Google Scholar")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        all_articles = []

        for term in search_terms:
            driver.get(f"https://scholar.google.com/scholar?q={'+'.join(term.split())}")
            time.sleep(2)

            search_results = driver.find_elements(By.XPATH, "//div[@class='gs_ri']")

            articles = []
            for result in search_results:
                title_element = result.find_element(By.XPATH, ".//h3[@class='gs_rt']/a")
                title = title_element.text
                href = title_element.get_attribute("href")
            
                snippet_element = result.find_element(By.XPATH, ".//div[@class='gs_rs']")
                snippet = snippet_element.text if snippet_element else ""

                driver.get(href)
                article_text = driver.find_element(By.XPATH, "//div[@id='content']").text

                term_freq = term_counter_module(article_text)

                articles.append( {
                    'title': title,
                    'href': href,
                    'snippet': snippet,
                    'term_frequencies': term_freq
                })

        all_articles.append ({
            'search_term': term,
            'articles': articles
        })
        
    except Exception as e:
        print(f"Error scraping: {str(e)}")
    finally:
        driver.quit()

    output_module(all_articles)