import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def combine_features(row):
    return f"{row['keywords']}{row['cast']}{row['genres']}{row['director']}"

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
 

df = pd.read_csv("movie_dataset.csv")
titles = df["title"]
print("Escolha qual filme você gosta para a IA recomendar outros")
print("-" * 40)
print(titles.head(30))
print("-" * 40)

features = ["keywords", "cast", "genres", "director"]

for feature in features:
    df[feature] = df[feature].fillna("")

df["combined_features"] = df.apply(combine_features, axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cos_similarity = cosine_similarity(count_matrix)


while True:
    try:
        movie_user_likes = str(input("Qual filme você gosta?: "))
        movie_index = get_index_from_title(movie_user_likes)
        break
    except:
        print("Filme inválido")
        pass

similar_movies = list(enumerate(cos_similarity[movie_index]))
similar_movies.sort(key=lambda x:x[1], reverse=True)
sorted_list = similar_movies
print("Filmes recomendados:")
for c in range(1, 20):
    print("-" * 40)
    movie_title = get_title_from_index(sorted_list[c][0])
    print(movie_title)

