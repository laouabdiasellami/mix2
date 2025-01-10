import pytest
from .document import Document, ArxivDocument, WikipediaDocument

def test_document_creation():
    doc = Document("Sample Title", "Author", "2023-01-01", "Sample content.")
    assert doc.title == "Sample Title"
    assert doc.author == "Author"
    assert doc.date == "2023-01-01"
    assert doc.text == "Sample content."
    assert doc.getType() == "Document"

def test_arxiv_document_creation():
    doc = ArxivDocument("Arxiv Title", ["Author1", "Author2"], "2023-01-01", "Arxiv content.")
    assert doc.authors == ["Author1", "Author2"]
    assert doc.getType() == "Arxiv"

def test_wikipedia_document_creation():
    doc = WikipediaDocument("Wiki Title", "Wikipedia", "2023-01-01", "Wikipedia content.")
    assert doc.getType() == "Wikipedia"
