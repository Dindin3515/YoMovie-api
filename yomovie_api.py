import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from yomovie_search import search_yomovies
from yomovie_info import scrape_movie_details
from yomovie_iframe1_js import scrape_iframe_js
from yomovie_iframe2 import scrape_iframe2
from yomovie_iframe1 import scrape_iframe1
from yomovie_category import scrape_category
from yomovie_catalog import scrape_catalog
from yomovie_language import scrape_language
from yomovie_genre import scrape_genre
from flask import Flask, request, jsonify
from flask_cors import CORS

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, current_dir)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

baseUrl = "https://yomovies.tax/"

@app.route("/api/search", methods=["GET"])
def search_yomovies_api():
    query = request.args.get("query")
    url = baseUrl
    search_results = search_yomovies(url, query) 
    return json.dumps(search_results)

@app.route("/api/movie/<path:path>", methods=["GET"])
def get_movie_info(path):
    url = f"{baseUrl}{path}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_details = scrape_movie_details(response.text)
        return jsonify(movie_details)
    else:
        return jsonify({"error": "Failed to fetch movie details"}), 404

@app.route("/api/iframe/js/<path:path>", methods=["GET"])
def get_iframe_js(path):
    url = f"{baseUrl}{path}"
    response = requests.get(url)
    if response.status_code == 200:
        iframe_js = scrape_iframe_js(response.text)
        return jsonify(iframe_js)
    else:
        return jsonify({"error": "Failed to fetch movie details"}), 404
    
# Define the API endpoint
@app.route('/api/iframe1/<path:path>', methods=['GET'])
def get_iframe1(path):
    url = f"{baseUrl}{path}"
    iframe_src = scrape_iframe1(url)
    return jsonify({'iframe_src': iframe_src})
    
@app.route("/api/iframe2/<path:path>", methods=["GET"])
def get_iframe2(path):
    url = f"{baseUrl}{path}"
    response = requests.get(url)
    if response.status_code == 200:
        iframe2 = scrape_iframe2(response.content)
        return jsonify(iframe2)
    else:
        return jsonify({"error": "Failed to fetch movie details"}), 404
    
@app.route("/api/category", methods=["GET"])
def category_yomovies_api():
    query = request.args.get("query")
    page = request.args.get("page")
    url = baseUrl + query + "/page/" + page
    category_posts = scrape_category(url) 
    return json.dumps(category_posts)

@app.route("/api/language", methods=["GET"])
def language_yomovies_api():
    query = request.args.get("query")
    page = request.args.get("page")
    url = baseUrl + "translator/" + query + "/page/" + page
    language_posts = scrape_language(url) 
    return json.dumps(language_posts)

@app.route("/api/catalog", methods=["GET"])
def catalog_yomovies_api():
    query = request.args.get("query")
    page = request.args.get("page")
    url = baseUrl + "catalog/" + query + "/page/" + page
    catalog_posts = scrape_catalog(url) 
    return json.dumps(catalog_posts)

@app.route("/api/genre", methods=["GET"])
def genre_yomovies_api():
    query = request.args.get("query")
    page = request.args.get("page")
    url = baseUrl + query + "/page/" + page
    genre_posts = scrape_genre(url) 
    return json.dumps(genre_posts)

if __name__ == "__main__":
    app.run(debug=True)