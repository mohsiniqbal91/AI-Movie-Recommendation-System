import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Calculate average rating and number of ratings
movie_ratings = ratings.groupby("movieId").agg(
    avg_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()

# Add rating information to movies
movies = movies.merge(
    movie_ratings,
    on="movieId",
    how="left"
)

# Handle missing values
movies["avg_rating"] = movies["avg_rating"].fillna(0)
movies["rating_count"] = movies["rating_count"].fillna(0)

# Prepare movie genres
movies["genres"] = movies["genres"].fillna("").str.replace(
    "|", " ", regex=False
)

# Convert genres into TF-IDF features
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Calculate movie similarity
similarity_matrix = cosine_similarity(tfidf_matrix)


def recommend_movies(movie_title, number_of_recommendations=5):

    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        return []

    movie_index = matching_movies.index[0]
    similarity_scores = enumerate(similarity_matrix[movie_index])

    recommendations = []

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        rating = float(movies.iloc[index]["avg_rating"])
        rating_count = float(movies.iloc[index]["rating_count"])

        # Rating reliability
        rating_reliability = rating_count / (rating_count + 10)

        # Adjust rating based on reliability
        adjusted_rating = (rating / 5) * rating_reliability

        # Hybrid recommendation score
        hybrid_score = (score * 0.7) + (adjusted_rating * 0.3)

        recommendations.append({
            "title": movies.iloc[index]["title"],
            "similarity": round(float(score), 3),
            "rating": round(rating, 2),
            "rating_count": int(rating_count),
            "hybrid_score": round(float(hybrid_score), 3)
        })

    recommendations.sort(
        key=lambda movie: movie["hybrid_score"],
        reverse=True
    )

    return recommendations[:number_of_recommendations]