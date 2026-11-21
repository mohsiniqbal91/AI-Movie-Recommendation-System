
import pandas as pd

# Load the movie dataset
movies = pd.read_csv("data/movies.csv")

# Display first 5 movies
print("\n--- First 5 Movies ---")
print(movies.head())

# Display dataset information
print("\n--- Dataset Information ---")
movies.info()

# Display total rows and columns
print("\n--- Dataset Shape ---")
print(movies.shape)

# Check missing values
print("\n--- Missing Values ---")
print(movies.isnull().sum())

# Convert genres into Python lists
movies["genres"] = movies["genres"].apply(
    lambda x: x.split("|") if isinstance(x, str) else x
)

# Display movie titles and their genres
print("\n--- Movies with Converted Genres ---")
print(movies[["title", "genres"]].head())





# Load the ratings dataset
ratings = pd.read_csv("data/ratings.csv")

# Display first 5 ratings
print("\n--- First 5 Ratings ---")
print(ratings.head())

# Display ratings dataset shape
print("\n--- Ratings Dataset Shape ---")
print(ratings.shape)

# Display rating statistics
print("\n--- Ratings Statistics ---")
print(ratings["rating"].describe())



# Count unique users
total_users = ratings["userId"].nunique()

# Count unique rated movies
total_movies = ratings["movieId"].nunique()

print("\n--- User and Movie Statistics ---")
print("Total Users:", total_users)
print("Total Rated Movies:", total_movies)

# Find movies with the most ratings
movie_rating_counts = ratings["movieId"].value_counts()

print("\n--- Top 5 Most Rated Movie IDs ---")
print(movie_rating_counts.head())



# Merge ratings with movie titles
merged_data = ratings.merge(
    movies[["movieId", "title"]],
    on="movieId"
)

# Display first 10 records
print("\n--- Ratings with Movie Titles ---")
print(merged_data[["userId", "title", "rating"]].head(10))


# Calculate average rating for each movie
average_ratings = merged_data.groupby("title")["rating"].mean()

# Sort movies by average rating
average_ratings = average_ratings.sort_values(ascending=False)

# Display top 10 movies
print("\n--- Top 10 Highest Rated Movies ---")
print(average_ratings.head(10))

# Count ratings for each movie
rating_counts = merged_data.groupby("title")["rating"].count()

# Keep movies with at least 10 ratings
popular_movies = rating_counts[rating_counts >= 10].index

# Filter average ratings
reliable_ratings = average_ratings[average_ratings.index.isin(popular_movies)]

# Display top 10 reliable movies
print("\n--- Top 10 Reliable Highest Rated Movies ---")
print(reliable_ratings.sort_values(ascending=False).head(10))

# Create a combined genre string for each movie
movies["genres"] = movies["genres"].apply(
    lambda x: " ".join(x) if isinstance(x, list) else x
)

# Display movie titles with genres
print("\n--- Movies with Combined Genres ---")
print(movies[["title", "genres"]].head(10))

from sklearn.feature_extraction.text import TfidfVectorizer

print("TF-IDF library imported successfully!")