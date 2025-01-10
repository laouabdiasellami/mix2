from .text_processing import clean_text, compute_tf, compute_idf
from .corpus import Corpus
from .document import Document

def test_clean_text():
    text = "Hello, World! 123."
    cleaned = clean_text(text)
    assert "hello" in cleaned
    assert "world" in cleaned
    assert "123" not in cleaned

def test_compute_tf():
    doc = Document("Title", "Author", "2023-01-01", "Test content content.")
    tf = compute_tf(doc)
    assert tf["content"] > tf["test"]

def test_compute_idf():
    corpus = Corpus()
    doc1 = Document("Title1", "Author1", "2023-01-01", "word common")
    doc2 = Document("Title2", "Author2", "2023-01-02", "common unique")
    corpus.add_document(doc1)
    corpus.add_document(doc2)
    idf = compute_idf(corpus)
    assert idf["common"] < idf["unique"]
