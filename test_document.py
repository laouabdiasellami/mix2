import pytest
from .document import Document, ArxivDocument, WikipediaDocument

# Test de la classe Document
def test_document():
    doc = Document("Test", "Author", "2025-01-01", "Text")
    # Vérifie que le titre du document est bien "Test"
    assert doc.title == "Test"
    # Vérifie que l'auteur du document est bien "Author"
    assert doc.author == "Author"
    # Vérifie que le type du document est bien "Document"
    assert doc.getType() == "Document"

# Test de la classe ArxivDocument
def test_arxiv_document():
    doc = ArxivDocument("Test", ["Author1", "Author2"], "2025-01-01", "Text")
    # Vérifie que le titre du document est bien "Test"
    assert doc.title == "Test"
    # Vérifie que l'auteur du document est bien "Author1, Author2"
    assert doc.author == "Author1, Author2"
    # Vérifie que le type du document est bien "Arxiv"
    assert doc.getType() == "Arxiv"

# Test de la classe WikipediaDocument
def test_wikipedia_document():
    doc = WikipediaDocument("Test", "Wikipedia", "2025-01-01", "Text")
    # Vérifie que le titre du document est bien "Test"
    assert doc.title == "Test"
    # Vérifie que l'auteur du document est bien "Wikipedia"
    assert doc.author == "Wikipedia"
    # Vérifie que le type du document est bien "Wikipedia"
    assert doc.getType() == "Wikipedia"
