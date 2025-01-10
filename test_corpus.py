import pytest
from .document import Document
from .corpus import Corpus

# Test pour vérifier que l'instance de Corpus suit le pattern Singleton
def test_corpus_singleton():
    corpus1 = Corpus()  # Création de la première instance du Corpus
    corpus2 = Corpus()  # Création de la deuxième instance du Corpus
    assert corpus1 is corpus2  # Vérifie que les deux instances sont identiques (Singleton)

# Test pour vérifier l'ajout d'un document au corpus
def test_add_document_to_corpus():
    corpus = Corpus()  # Création d'une nouvelle instance de Corpus
    doc = Document("Title", "Author", "2023-01-01", "Sample content.")  # Création d'un document
    corpus.add_document(doc)  # Ajout du document au corpus
    assert len(corpus.documents) == 1  # Vérifie qu'il y a un document dans le corpus
    assert corpus.documents[0].title == "Title"  # Vérifie que le titre du document ajouté est correct
