# Importation des modules nécessaires
import math
from text_processing import clean_text, compute_idf  # Fonctions pour nettoyer le texte et calculer l'IDF (Inverse Document Frequency)

# Fonction de similarité cosinus entre deux vecteurs
def cosine_similarity(vec1, vec2):
    # Récupère l'ensemble des mots des deux vecteurs
    all_words = set(vec1.keys()).union(set(vec2.keys()))
    
    # Calcul du produit scalaire entre les deux vecteurs
    dot_product = sum(vec1.get(word, 0) * vec2.get(word, 0) for word in all_words)
    
    # Calcul des magnitudes (longueurs) des deux vecteurs
    magnitude1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
    magnitude2 = math.sqrt(sum(value ** 2 for value in vec2.values()))
    
    # Si l'une des magnitudes est égale à 0, la similarité est 0
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    # Retourne la similarité cosinus
    return dot_product / (magnitude1 * magnitude2)

# Classe pour le modèle BM25 (Best Matching 25)
class BM25:
    def __init__(self, corpus, k1=1.5, b=0.75):
        self.k1 = k1  # Paramètre pour ajuster l'importance du terme dans un document
        self.b = b  # Paramètre pour ajuster la longueur du document
        self.corpus = corpus  # Le corpus de documents
        self.N = len(corpus.documents)  # Nombre total de documents
        self.avgdl = self._calculate_avgdl()  # Longueur moyenne des documents
        self.doc_lengths = self._calculate_doc_lengths()  # Longueur de chaque document
        self.idf = compute_idf(corpus)  # Calcul de l'IDF pour chaque mot

    def _calculate_doc_lengths(self):
        # Calcul de la longueur de chaque document dans le corpus
        return [len(clean_text(doc.text)) for doc in self.corpus.documents]

    def _calculate_avgdl(self):
        # Calcul de la longueur moyenne des documents
        total_len = sum(self._calculate_doc_lengths())
        return total_len / self.N

    def score(self, query, doc_idx):
        # Calcul du score BM25 pour un document donné
        query_words = clean_text(query)  # Nettoyage de la requête
        doc = self.corpus.documents[doc_idx]  # Récupère le document par index
        doc_words = clean_text(doc.text)  # Nettoyage du texte du document
        tf = {}  # Dictionnaire pour le calcul du terme fréquence (TF)
        
        # Calcul de la fréquence des termes dans le document
        for word in doc_words:
            tf[word] = tf.get(word, 0) + 1

        score = 0.0
        doc_len = self.doc_lengths[doc_idx]  # Longueur du document
        for word in query_words:
            if word in tf:
                idf = self.idf.get(word, 0)  # Récupère l'IDF du mot
                tf_val = tf[word]  # Fréquence du mot dans le document
                numerator = tf_val * (self.k1 + 1)  # Numérateur de la formule BM25
                denominator = tf_val + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)  # Dénominateur de la formule BM25
                score += idf * (numerator / denominator)  # Calcul du score BM25
        return score

# Fonction pour trouver les articles les plus pertinents en fonction de la méthode spécifiée (cosine ou BM25)
def find_most_relevant_articles(corpus, query, method='cosine'):
    similarities = []  # Liste pour stocker les similarités ou scores des documents

    if method == 'cosine':
        # Nettoyage de la requête et calcul de la fréquence des termes
        query_words = clean_text(query)
        query_tf = {}
        query_word_count = len(query_words)
        for word in query_words:
            query_tf[word] = query_tf.get(word, 0) + 1
        for word in query_tf:
            query_tf[word] = query_tf[word] / query_word_count  # Normalisation du TF

        # Calcul du TF-IDF pour la requête
        query_tfidf = {}
        idf = compute_idf(corpus)  # Calcul de l'IDF pour le corpus
        for word in query_tf:
            query_tfidf[word] = query_tf[word] * idf.get(word, 0)  # Calcul du TF-IDF pour chaque mot

        from text_processing import compute_tfidf  # Importation de la fonction de calcul du TF-IDF pour les documents
        for idx, doc in enumerate(corpus.documents):
            doc_tfidf = compute_tfidf(corpus)[idx]  # Calcul du TF-IDF pour le document
            similarity = cosine_similarity(query_tfidf, doc_tfidf)  # Calcul de la similarité cosinus
            similarities.append((similarity, doc))  # Ajout de la similarité et du document à la liste

    elif method == 'bm25':
        # Utilisation de BM25 pour calculer les scores
        bm25 = BM25(corpus)
        for idx, doc in enumerate(corpus.documents):
            score = bm25.score(query, idx)  # Calcul du score BM25 pour le document
            similarities.append((score, doc))  # Ajout du score et du document à la liste

    # Trie les documents en fonction des scores ou similarités, du plus élevé au plus bas
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Sélection des 5 premiers articles les plus pertinents
    top_articles = similarities[:5]

    # Affichage des résultats
    print(f"\nResults using {method.upper()} scoring:")
    for idx, (score, doc) in enumerate(top_articles):
        print("=" * 80)
        print(f"Rank {idx + 1} - Score: {score:.4f}")
        print(f"Title: {doc.title}")
        print(f"Author: {doc.author}")
        print(f"Date: {doc.date}")
        print(f"Type: {doc.type}")
        print("Content:")
        import textwrap
        print(textwrap.fill(doc.text, width=80))  # Affichage du contenu du document formaté
