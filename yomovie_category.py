import requests
from bs4 import BeautifulSoup

# url = 'https://yomovies.tax/bollywood/page/1'

def scrape_category(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', class_='movie-box m-info col-6 col-lg-3 col-sm-4 col-xl-5')

    movies = []
    
    for article in articles:
        title = article.find('div', class_='movie-details existing-details').find('a')['title']
        image_url = article.find('div', class_='img').find('img')['src']
        category = article.find('div', class_='movie-details existing-details').find('div', class_='category').text

        movie = {
            'title': title,
            'image_url': image_url,
            'category': category
        }

        movies.append(movie)

    return movies