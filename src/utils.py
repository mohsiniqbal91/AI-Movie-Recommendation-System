
import requests
import streamlit as st


@st.cache_data
def get_movie_poster(movie_title):

    api_key = st.secrets["TMDB_API_KEY"]

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": api_key,
        "query": movie_title,
        "include_adult": False
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        results = response.json().get("results", [])

        for movie in results:
            poster_path = movie.get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.RequestException:
        return None

    return None
