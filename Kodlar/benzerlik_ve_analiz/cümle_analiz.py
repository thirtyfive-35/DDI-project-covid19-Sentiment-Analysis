from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dosyadan cümleleri oku
with open('final_covid19.txt', 'r', encoding='utf-8') as file:
    preprocessed_sentences = file.readlines()

# TF-IDF matrisini oluştur
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_sentences)

# Benzerlik analizi için cümle listesi
query_sentences = [
    "test distinguish sarscov influenza b respiratory syncytial virus",
    "vaccine attitudes covid vaccine intention among parents children kidney disease primary hypertension",
    "thought pandemic wasnt real covid trick played pharma",
    "efficacy safety prophylaxis systematic review metaanalysis randomized trials",
    "ask health care provider treatment"
]

# TF-IDF vektörlerini oluştur ve benzerlik skorlarını hesapla
tfidf_vectors_query = tfidf_vectorizer.transform(query_sentences)
similarity_scores = cosine_similarity(tfidf_vectors_query, tfidf_matrix)

# Her bir cümle için en benzer 3 cümleyi seç
most_similar_indices = similarity_scores.argsort(axis=1)[:, ::-1][:, 1:4]  # Her cümle için en büyük üç benzerlik skorunu al
most_similar_sentences = [[preprocessed_sentences[i] for i in indices] for indices in most_similar_indices]

# Sonuçları yazdır
for i, query_sentence in enumerate(query_sentences):
    print(f"\nOrjinal Cümle {i + 1}: {query_sentence}")
    print("En Benzer 3 Cümle:")
    for j, sentence in enumerate(most_similar_sentences[i], start=1):
        print(f"{j}. {sentence}")
