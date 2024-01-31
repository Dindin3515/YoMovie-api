from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Set up the Selenium driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
driver = webdriver.Chrome(options=options)

# Navigate to the website
def scrape_iframe1(url):
    driver.get(url)

    # Find the "click me" button and click it
    click_me_btn = driver.find_element(By.XPATH, '//span[@id="click_me"]')
    click_me_btn.click()

    # Wait for the iframe to load
    time.sleep(5)

    # Get the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the iframe src
    iframe_src = soup.find('iframe')['src']

    # Close the Selenium driver
    driver.quit()

    return iframe_src