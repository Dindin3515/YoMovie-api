from bs4 import BeautifulSoup
import requests
import json

def scrape_iframe2(html):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the HTML section
    html_section = soup.find('div', {'class': 'tabs__content tabs__content_4'})

    # Check if the HTML section exists
    if html_section is not None:
        # Find the iframe tag in the HTML section
        iframe_tag = html_section.find('iframe')

        # Extract the data-src and src attributes
        data_src = iframe_tag['data-src']

        return {"data-src": data_src}