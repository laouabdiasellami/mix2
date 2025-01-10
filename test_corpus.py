import pytest
from .document import Document
from .corpus import Corpus

def test_corpus_singleton():
    corpus1 = Corpus()
    corpus2 = Corpus()
    assert corpus1 is corpus2  # Ensure singleton pattern

def test_add_document_to_corpus():
    corpus = Corpus()
    doc = Document("Title", "Author", "2023-01-01", "Sample content.")
    corpus.add_document(doc)
    assert len(corpus.documents) == 1
    assert corpus.documents[0].title == "Title"
