
# 🎬 AI Movie Recommendation System

An AI-powered movie recommendation system built using Python, Machine Learning, and Streamlit. It recommends movies based on genre similarity, user tags, and rating information.

## 🚀 Live Demo

[Try the AI Movie Recommendation System](https://ai-movie-recommendation-mohsin.streamlit.app/)

## 📌 Project Overview

This project helps users discover movies similar to their favourite movies.

It uses TF-IDF Vectorization and Cosine Similarity to measure movie similarity. A hybrid recommendation algorithm combines content similarity with rating quality to generate recommendations.

## ✨ Features

- Movie recommendations based on a selected movie
- Genre-based similarity
- Tag-based similarity
- TF-IDF text vectorization
- Cosine similarity calculation
- Hybrid recommendation scoring
- Average movie ratings
- Total number of ratings
- Interactive Streamlit interface
- Movie poster integration using TMDB API

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TF-IDF Vectorization
- Cosine Similarity
- TMDB API
- Git and GitHub

## 🧠 Recommendation Algorithm

The recommendation system works through these steps:

1. Loads movie, rating, and tag datasets.
2. Combines movie genres and tags to create movie descriptions.
3. Applies TF-IDF Vectorization to convert text into numerical features.
4. Calculates Cosine Similarity between movies.
5. Calculates average ratings and rating counts.
6. Combines similarity and rating quality into a hybrid score.
7. Returns the top recommended movies.

## 📊 Dataset

This project uses the MovieLens Latest Small Dataset.

- Movies: 9,742
- Ratings: 78,049
- Tags: 3,683

## 📂 Project Structure

```text
AI-Movie-Recommendation-System/
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│   └── tags.csv
│
├── src/
│   ├── main.py
│   ├── recommender.py
│   ├── data_preprocessing.py
│   └── utils.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mohsiniqbal91/AI-Movie-Recommendation-System.git
```

### 2. Open the project folder

```bash
cd AI-Movie-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run src/main.py
```

## 🔐 API Configuration

The application uses the TMDB API to retrieve movie posters.

Configure your TMDB API key through Streamlit secrets:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Never commit your actual API key to GitHub.

## 👨‍💻 Author

**Muhammad Mohsin**

GitHub: [mohsiniqbal91](https://github.com/mohsiniqbal91)

## 📄 License

This project is developed for educational and portfolio purposes.
