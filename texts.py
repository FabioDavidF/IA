from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London", "Paris Paris London", "Paris Paris Paris", "guacamole nigga penis"]
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
print(count_matrix)
print("*-" * 20)
print(cv.get_feature_names())
print(count_matrix.toarray())

print(cosine_similarity(count_matrix))