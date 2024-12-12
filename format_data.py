import pandas as pd

# Load data
movies = pd.read_csv("raw_data/title.basics.tsv", sep='\t')
reviews = pd.read_csv("raw_data/REVIEWS_FILE")

# Filter and rename columns
movies_filtered = movies[['tconst', 'primaryTitle']].rename(columns={'tconst': 'movie_id', 'primaryTitle': 'movie_title'})

# Merge columns
combined = pd.merge(reviews, movies_filtered, on='movie_id', how='inner')

# Save to a combined CSV
combined.to_csv("prepared_data/data.csv", index=False)