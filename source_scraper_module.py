import output_module, term_counter_module, time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def scrape_google_scholar(search_terms):

    print(f"Scraping data for terms: {search_terms} from Google Scholar")

    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
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
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='content']")))
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
        
        output_module.output_csv(all_articles)

    except NoSuchElementException as e:
        print(f"Element not found: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")   
    finally:
        driver.quit()
