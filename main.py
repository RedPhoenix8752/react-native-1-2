from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demofiltering import output
from contentfiltering import get_recommendation
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][19], 
        "poster-link": all_movies[0][27]
        "release_date": all_movies[0][13] or "N/A",
        "duration": all_movies[0][15]
        "rating": all_movies[0][20]
        "overview":[0][9]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })
@app.route("/liked_movie", methods = ["POST"])
def liked_movies():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201
@app.route("/not_liked_movie", methods = ["POST"])
def liked_movies():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201
@app.route("/popular-movie")
def popular_movies():
    movie_data = []
    for movie in  output:
        _d = {
            
            "title": all_movies[0][19], 
            "poster-link": all_movies[0][27]
            "release_date": all_movies[0][13] or "N/A",
            "duration": all_movies[0][15]
            "rating": all_movies[0][20]
            "overview":[0][9]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200
@app.route("/recommended-movie")
def recommended-movies():
    all_recommended = []
    for liked_movie in liked_movie:
        output = get_recommendations(liked_movie[19])
        for data in output: all_recommended.append(data)
        