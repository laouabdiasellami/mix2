from .text_processing import clean_text, compute_tf, compute_idf
from .corpus import Corpus
from .document import Document

# Test de la fonction clean_text
def test_clean_text():
    text = "Hello, World! 123."
    cleaned = clean_text(text)
    # Vérifie que "hello" est bien dans le texte nettoyé (en minuscules)
    assert "hello" in cleaned
    # Vérifie que "world" est bien dans le texte nettoyé
    assert "world" in cleaned
    # Vérifie que les chiffres (ici "123") ne sont pas dans le texte nettoyé
    assert "123" not in cleaned

# Test de la fonction compute_tf
def test_compute_tf():
    doc = Document("Title", "Author", "2023-01-01", "Test content content.")
    tf = compute_tf(doc)
    # Vérifie que la fréquence du mot "content" est supérieure à celle de "test"
    assert tf["content"] > tf["test"]

# Test de la fonction compute_idf
def test_compute_idf():
    corpus = Corpus()
    doc1 = Document("Title1", "Author1", "2023-01-01", "word common")
    doc2 = Document("Title2", "Author2", "2023-01-02", "common unique")
    corpus.add_document(doc1)
    corpus.add_document(doc2)
    idf = compute_idf(corpus)
    # Vérifie que le mot "common" a un IDF plus faible que "unique"
    assert idf["common"] < idf["unique"]
