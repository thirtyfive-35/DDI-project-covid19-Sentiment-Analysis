from collections import Counter
import re
from gensim.models import Word2Vec

def en_cok_gecen_kelimeler(txt_dosyasi, limit=20):
    try:
        with open(txt_dosyasi, 'r', encoding='utf-8') as dosya:
            metin = dosya.read()
            kelimeler = re.findall(r'\b\w+\b', metin.lower())
            kelime_sayilari = Counter(kelimeler)
            en_cok_gecenler = kelime_sayilari.most_common(limit)

            print(f"En çok geçen {limit} kelime:")
            for kelime, sayi in en_cok_gecenler:
                print(f"{kelime}: {sayi} kez")
            
            # En çok geçen kelimeleri bir listeye ekleyelim
            en_cok_gecen_kelimeler_listesi = [kelime for kelime, _ in en_cok_gecenler]

            return en_cok_gecen_kelimeler_listesi
    except FileNotFoundError:
        print(f"{txt_dosyasi} dosyası bulunamadı.")
        return []

# Kullanım örneği:
dosya_adi = 'final_covid19.txt'
en_cok_gecen_kelimeler_listesi = en_cok_gecen_kelimeler(dosya_adi)

# Word2Vec modelini eğitmek için kullandığımız kod
with open('final_covid19.txt', 'r', encoding='utf-8') as file:
    sentences = file.readlines()

preprocessed_sentences = [sentence.split() for sentence in sentences]
model = Word2Vec(preprocessed_sentences, vector_size=100, window=5, min_count=1, workers=4)

# En çok geçen 20 kelimenin her biri için benzer kelimeleri bulalım
for word in en_cok_gecen_kelimeler_listesi:
    similar_words = model.wv.most_similar(word, topn=5)
    
    print(f"\n{word} kelimesine benzer kelimeler:")
    for similar_word, score in similar_words:
        print(f"{similar_word}: {score}")