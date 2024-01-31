import json
import requests
from bs4 import BeautifulSoup
import re

def scrape_iframe_js(html):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the HTML section
    html_section = soup.find('div', {'class': 'tabs__content tabs__content_1 active'})

    # Check if the HTML section exists
    if html_section is not None:

        # Extract the whole content inside the script tag
        script_content = html_section.find('script').text.strip()

        # Extract the src attribute from the second script tag
        src = html_section.find_all('script')[1]['src']

        return {
            "Script tag content": script_content,
            "Script tag src": src 
            }