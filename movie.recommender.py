import pandas as pd

# Load dataset
data = pd.read_csv("movies.csv")

# Convert genres into sets
data["Genre_Set"] = data["Genre"].apply(lambda x: set(x.split()))

def recommend(movie_name):
    if movie_name not in data["Title"].values:
        print("Movie not found")
        return
    
    # Get selected movie genres
    target_genre = data[data["Title"] == movie_name]["Genre_Set"].values[0]
    
    scores = []
    
    for index, row in data.iterrows():
        if row["Title"] == movie_name:
            continue
        
        # Count common genres
        common = len(target_genre.intersection(row["Genre_Set"]))
        scores.append((row["Title"], common))
    
    # Sort by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print("\nTop Recommendations:")
    for movie, score in scores[:5]:
        if score > 0:
            print(movie)

# User input
movie = input("Enter movie name: ")
recommend(movie)
