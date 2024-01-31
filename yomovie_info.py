import json
import requests
from bs4 import BeautifulSoup

def scrape_movie_details(html):
    soup = BeautifulSoup(html, "html.parser")

    movie_data = {
        "title": soup.find("h1").text.strip(),
        "year": soup.find("li", class_="release").span.text.strip(),
        "original_language": soup.find("li", class_="country").span.text.strip(),
    }

    duration_list = soup.find("div", class_="cast").find_next("div", class_="duration list")
    if duration_list is not None:
        movie_data["runtime"] = duration_list.text.strip()
    else:
        movie_data["runtime"] = None

    duration_list = soup.find("div", class_="cast").find_next("div", class_="duration list").find_next_sibling()
    if duration_list is not None:
        movie_data["director"] = duration_list.text.strip()
    else:
        movie_data["director"] = None

    movie_data["cast"] = [x.strip() for x in soup.find("div", class_="actors list").text.strip()[len("cast(s)"):-1].split(",")]

    genre_elements = soup.find("div", class_="category").find_all("a")
    movie_data["genre"] = [genre_element.text.strip() for genre_element in genre_elements]

    movie_data["description"] = soup.find("div", class_="description").find("p").text.strip()

    poster_element = soup.find("div", class_="poster")
    movie_data["poster"] = poster_element.img["src"] if poster_element else None

    rating_data = soup.find("div", class_="rating-data")
    movie_data["rating"] = {
        "value": rating_data.find("span", class_="rating-vgs").text.strip(),
        "votes": rating_data.find("div", class_="rating-votenote").find("span").text.strip()
    }

    return movie_data
    