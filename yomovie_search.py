import requests
from bs4 import BeautifulSoup

def search_yomovies(url, query):

    form_data = {
        "do": "search",
        "subaction": "search",
        "story": query
    }

    response = requests.post(url, data=form_data)
    soup = BeautifulSoup(response.text, "html.parser")

    movie_boxes = soup.find_all("article", class_="movie-box")

    movies = []
    for movie_box in movie_boxes:
        movie = {
            "name": movie_box.find("div", class_="name").a.text,
            "poster": movie_box.find("div", class_="img").img["src"],
            "category": movie_box.find("div", class_="category").text,
            "url": movie_box.find("div", class_="name").a["href"]
        }

        movies.append(movie)

    return movies