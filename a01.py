import pandas as pd
from matplotlib import pyplot


movies_uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
movies = pd.read_csv(movies_uri)
movies.columns = ["id", "title", "genres"]
genres_column = movies["genres"]

genres = {}
c = 0
for line in genres_column:
    line_genres = line.split("|")
    for genre in line_genres:
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1

df = pd.DataFrame.from_dict(genres, orient="index")

df.plot(kind="bar")
pyplot.draw()



ratings_uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
ratings = pd.read_csv(ratings_uri)
ratings.columns = ["userId", "movieId", "rating", "title"]
rating_column = ratings["rating"]

pyplot.figure(4)
rating_column.plot(kind="hist")
pyplot.draw()
pyplot.show()
