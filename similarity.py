import math
from text_processing import clean_text, compute_idf

def cosine_similarity(vec1, vec2):
    all_words = set(vec1.keys()).union(set(vec2.keys()))
    dot_product = sum(vec1.get(word, 0) * vec2.get(word, 0) for word in all_words)
    magnitude1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
    magnitude2 = math.sqrt(sum(value ** 2 for value in vec2.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)

class BM25:
    def __init__(self, corpus, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = corpus
        self.N = len(corpus.documents)
        self.avgdl = self._calculate_avgdl()
        self.doc_lengths = self._calculate_doc_lengths()
        self.idf = compute_idf(corpus)

    def _calculate_doc_lengths(self):
        return [len(clean_text(doc.text)) for doc in self.corpus.documents]

    def _calculate_avgdl(self):
        total_len = sum(self._calculate_doc_lengths())
        return total_len / self.N

    def score(self, query, doc_idx):
        query_words = clean_text(query)
        doc = self.corpus.documents[doc_idx]
        doc_words = clean_text(doc.text)
        tf = {}
        for word in doc_words:
            tf[word] = tf.get(word, 0) + 1

        score = 0.0
        doc_len = self.doc_lengths[doc_idx]
        for word in query_words:
            if word in tf:
                idf = self.idf.get(word, 0)
                tf_val = tf[word]
                numerator = tf_val * (self.k1 + 1)
                denominator = tf_val + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                score += idf * (numerator / denominator)
        return score

def find_most_relevant_articles(corpus, query, method='cosine'):
    similarities = []

    if method == 'cosine':
        query_words = clean_text(query)
        query_tf = {}
        query_word_count = len(query_words)
        for word in query_words:
            query_tf[word] = query_tf.get(word, 0) + 1
        for word in query_tf:
            query_tf[word] = query_tf[word] / query_word_count

        query_tfidf = {}
        idf = compute_idf(corpus)
        for word in query_tf:
            query_tfidf[word] = query_tf[word] * idf.get(word, 0)

        from text_processing import compute_tfidf
        for idx, doc in enumerate(corpus.documents):
            doc_tfidf = compute_tfidf(corpus)[idx]
            similarity = cosine_similarity(query_tfidf, doc_tfidf)
            similarities.append((similarity, doc))

    elif method == 'bm25':
        bm25 = BM25(corpus)
        for idx, doc in enumerate(corpus.documents):
            score = bm25.score(query, idx)
            similarities.append((score, doc))

    similarities.sort(reverse=True, key=lambda x: x[0])
    top_articles = similarities[:5]

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
        print(textwrap.fill(doc.text, width=80))
