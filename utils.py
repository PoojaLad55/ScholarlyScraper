import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

'''
Configures and launches a Chrome browser with specific settings to avoid 
detection and improve performance in an automated environment. Also creates
random pauses between actions to mimic human behavior and avoid detection
by websites that might block bots.
'''

def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--log-level=1")
    chrome_options.add_argument("--enable-unsafe-swiftshader")

    service = Service('C:/Users/pooja/Downloads/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def random_delay():
    time.sleep(random.uniform(2, 5))