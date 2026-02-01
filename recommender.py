import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
credits = pd.read_csv("data/credits.csv")

# Merge
movies = movies.merge(credits, on="title")

movies = movies[
    ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
]

# Helpers
def convert(text):
    return [i["name"] for i in ast.literal_eval(text)]

def convert_cast_with_role(text):
    cast_list = []
    for i in ast.literal_eval(text)[:3]:
        cast_list.append({
            "name": i["name"],
            "role": "Actor / Actress"
        })
    return cast_list

def fetch_director(text):
    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            return {
                "name": i["name"],
                "role": "Director"
            }
    return {"name": "Unknown", "role": "Director"}

movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(convert_cast_with_role)
movies["crew"] = movies["crew"].apply(fetch_director)
movies["overview"] = movies["overview"].fillna("").apply(lambda x: x.split())

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
)

movies["tags"] = movies["tags"].apply(lambda x: " ".join(x).lower())

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["tags"]).toarray()
similarity = cosine_similarity(vectors)

def recommend(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in movies["title"].str.lower().values:
        return None

    index = movies[movies["title"].str.lower() == movie_name].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        movie_data = movies.iloc[i[0]]
        recommendations.append({
            "title": movie_data.title,
            "director": movie_data.crew,
            "cast": movie_data.cast
        })

    return recommendations
