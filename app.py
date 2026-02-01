from flask import Flask, render_template, request
from recommender import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend_movie():
    movie_name = request.form["movie"]
    recommendations = recommend(movie_name)

    if recommendations is None:
        return render_template(
            "index.html",
            error="Movie not found. Please try another movie."
        )

    return render_template(
        "index.html",
        recommendations=recommendations,
        movie_name=movie_name
    )

if __name__ == "__main__":
    app.run(debug=True)
