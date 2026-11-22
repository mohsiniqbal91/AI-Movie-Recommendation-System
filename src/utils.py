import requests
import streamlit as st


@st.cache_data
def get_movie_poster(movie_title):

    api_key = st.secrets["TMDB_API_KEY"]

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": api_key,
        "query": movie_title
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if data["results"]:
            poster_path = data["results"][0].get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return None
