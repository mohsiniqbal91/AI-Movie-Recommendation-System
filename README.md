# AI Movie Recommendation System

An AI-powered movie recommendation system built using Python, Machine Learning, and Streamlit.

## Project Overview

This project recommends movies based on genre similarity and user ratings.

It uses TF-IDF Vectorization and Cosine Similarity to identify movies with similar genres.

A hybrid recommendation algorithm combines movie similarity and rating information to rank recommendations.

## Features

- Movie recommendations
- Genre-based similarity
- Average movie ratings
- Total number of ratings
- Hybrid recommendation scoring
- Interactive Streamlit interface

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TF-IDF
- Cosine Similarity

## Dataset

MovieLens Latest Small Dataset.

- 9,742 movies
- 78,049 ratings

## How to Run

1. Clone or download this project.
2. Open the project folder.
3. Create and activate a virtual environment.
4. Install dependencies:

   pip install -r requirements.txt

5. Run the application:

   streamlit run src/main.py

## Project Structure

AI-Movie-Recommendation-System/
- data/
- src/
  - main.py
  - recommender.py
  - data_preprocessing.py
  - utils.py
- README.md
- requirements.txt