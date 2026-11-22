import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
tags = pd.read_csv("data/tags.csv")

# Calculate average rating and number of ratings
movie_ratings = ratings.groupby("movieId").agg(
    avg_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()

# Add rating information to movies
movies = movies.merge(movie_ratings, on="movieId", how="left")

movies["avg_rating"] = movies["avg_rating"].fillna(0)
movies["rating_count"] = movies["rating_count"].fillna(0)

# Combine tags for each movie
tags["tag"] = tags["tag"].fillna("").astype(str)

movie_tags = tags.groupby("movieId")["tag"].apply(
    lambda values: " ".join(values)
).reset_index(name="tags")

movies = movies.merge(movie_tags, on="movieId", how="left")
movies["tags"] = movies["tags"].fillna("")

# Prepare genres
movies["genres"] = movies["genres"].fillna("").str.replace(
    "|", " ", regex=False
)

# Convert genres and tags into TF-IDF features
genre_tfidf = TfidfVectorizer()
genre_matrix = genre_tfidf.fit_transform(movies["genres"])

tag_tfidf = TfidfVectorizer(stop_words="english")
tag_matrix = tag_tfidf.fit_transform(movies["tags"])


def recommend_movies(movie_title, number_of_recommendations=5):

    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        return []

    movie_index = matching_movies.index[0]

    # Calculate similarity using genres and tags
    genre_scores = cosine_similarity(
        genre_matrix[movie_index], genre_matrix
    ).flatten()

    tag_scores = cosine_similarity(
        tag_matrix[movie_index], tag_matrix
    ).flatten()

    # If selected movie has no tags, use genres only
    if tag_matrix[movie_index].nnz == 0:
        similarity_scores = genre_scores
    else:
        similarity_scores = (
            genre_scores * 0.6
        ) + (
            tag_scores * 0.4
        )

    recommendations = []

    for index, score in enumerate(similarity_scores):

        if index == movie_index:
            continue

        rating = float(movies.iloc[index]["avg_rating"])
        rating_count = float(movies.iloc[index]["rating_count"])

        # Rating reliability
        rating_reliability = rating_count / (rating_count + 10)

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
