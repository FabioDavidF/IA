from sklearn.svm import LinearSVC

import pandas as pd



ratings_uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
ratings = pd.read_csv(ratings_uri)
ratings.columns = ["userId", "movieId", "rating", "title"]
rating_column = ratings["rating"]



# apresentar um filme novo do tom cruise para as pessoas
def pessoa_to_data(pessoa):
    global GENRE_IDS
    converted_data = []
    for genre in pessoa:
        try:
            converted_data.append(GENRE_IDS[genre])
        except KeyError:
            converted_data.append(0)
    
    return converted_data


GENRE_IDS = {
    "ação": 1,
    "comédia": 2,
    "romance": 3,
    "terror": 4,
    "musical": 5
}

pessoa1 = ["ação", "comédia", "romance"]
pessoa2 = ["terror", "ação", "musical"]
pessoa3 = ["musical", "comédia", "romance"]


treino_x = [pessoa_to_data(pessoa1), pessoa_to_data(pessoa2), pessoa_to_data(pessoa3)]
treino_y = [1, 1, 0,] # 1=gosta, 0=não gosta

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)


pessoa_aleatoria = ["comédia", "romance", "musical"]
print(modelo.predict([pessoa_to_data(pessoa_aleatoria)]))