
import streamlit as st
import pandas as pd
from recommender import recommend_movies
from utils import get_movie_poster

movies = pd.read_csv("data/movies.csv")

st.title("AI Movie Recommendation System")

st.write("Welcome! Find movies similar to your favourite movie.")

movie_list = movies["title"].tolist()

movie_name = st.selectbox(
    "Select your favourite movie",
    movie_list
)

if st.button("Recommend Movies"):

    recommendations = recommend_movies(movie_name)

    if recommendations:
        st.subheader("Recommended Movies")

        for movie in recommendations:
            with st.container(border=True):
                st.subheader(movie["title"])

                poster_url = get_movie_poster(movie["title"])

                if poster_url:
                    st.image(poster_url, width=180)
                else:
                    st.info("Movie poster not available.")

                st.write(
                    "Similarity Score:",
                    f'{movie["similarity"] * 100:.0f}%'
                )

                st.write(
                    "Total Ratings:",
                    movie["rating_count"]
                )

    else:
        st.warning("Movie not found! Please check the title.")
