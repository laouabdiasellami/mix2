# test_all.py
import pytest  # Importation de pytest pour les tests unitaires
from document import Document, ArxivDocument, WikipediaDocument  # Importation des classes Document, ArxivDocument et WikipediaDocument
from corpus import Corpus  # Importation de la classe Corpus pour tester son comportement

# Fixtures
@pytest.fixture
def base_document():
    # Fixture qui crée un document de base pour les tests
    return Document(
        title="Test Document",  # Titre du document
        author="Test Author",  # Auteur du document
        date="2025-01-01",  # Date du document
        text="This is a test document."  # Contenu du document
    )

@pytest.fixture
def arxiv_document():
    # Fixture qui crée un document spécifique pour Arxiv
    return ArxivDocument(
        title="Test Arxiv",  # Titre du document
        authors=["Author 1", "Author 2"],  # Liste des auteurs
        date="2025-01-01",  # Date de publication
        text="This is a test arxiv document."  # Contenu du document
    )

@pytest.fixture
def wikipedia_document():
    # Fixture qui crée un document spécifique pour Wikipedia
    return WikipediaDocument(
        title="Test Wiki",  # Titre de la page Wikipedia
        author="Wikipedia",  # Auteur défini comme "Wikipedia"
        date="2025-01-01",  # Date de publication
        text="This is a test wikipedia document."  # Résumé de la page Wikipedia
    )

@pytest.fixture
def empty_corpus():
    # Fixture qui réinitialise le singleton de Corpus et retourne une nouvelle instance vide
    Corpus._instance = None  # Réinitialisation de l'instance singleton de Corpus
    return Corpus()  # Retourne une nouvelle instance de Corpus

# Document Tests
def test_document_initialization(base_document):
    # Test de l'initialisation d'un document de base
    assert base_document.title == "Test Document"  # Vérifie que le titre est correct
    assert base_document.author == "Test Author"  # Vérifie que l'auteur est correct
    assert base_document.date == "2025-01-01"  # Vérifie que la date est correcte
    assert base_document.text == "This is a test document."  # Vérifie que le texte est correct
    assert base_document.getType() == "Document"  # Vérifie que le type est "Document"

def test_document_str_representation(base_document):
    # Test de la représentation en chaîne de caractères d'un document
    expected = (
        "Title: Test Document\n"
        "Author: Test Author\n"
        "Date: 2025-01-01\n"
        "Type: Document\n"
        "Content:\nThis is a test document."
    )
    # Vérifie que la sortie de str() correspond à la valeur attendue
    assert str(base_document).strip() == expected.strip()

def test_arxiv_initialization(arxiv_document):
    # Test de l'initialisation d'un document spécifique pour Arxiv
    assert arxiv_document.title == "Test Arxiv"  # Vérifie que le titre est correct
    assert arxiv_document.authors == ["Author 1", "Author 2"]  # Vérifie que la liste des auteurs est correcte
    assert arxiv_document.author == "Author 1, Author 2"  # Vérifie que l'auteur est bien une chaîne formatée
    assert arxiv_document.date == "2025-01-01"  # Vérifie que la date est correcte
    assert arxiv_document.getType() == "Arxiv"  # Vérifie que le type est "Arxiv"

def test_wikipedia_initialization(wikipedia_document):
    # Test de l'initialisation d'un document spécifique pour Wikipedia
    assert wikipedia_document.title == "Test Wiki"  # Vérifie que le titre est correct
    assert wikipedia_document.author == "Wikipedia"  # Vérifie que l'auteur est "Wikipedia"
    assert wikipedia_document.getType() == "Wikipedia"  # Vérifie que le type est "Wikipedia"

# Corpus Tests
def test_corpus_singleton(empty_corpus):
    # Test pour vérifier que le singleton de Corpus fonctionne correctement
    corpus2 = Corpus()  # Crée une nouvelle instance de Corpus
    assert empty_corpus is corpus2  # Vérifie que l'instance retournée est la même (singleton)

def test_add_document(empty_corpus, base_document):
    # Test pour vérifier que l'ajout d'un document au corpus fonctionne correctement
    empty_corpus.add_document(base_document)  # Ajoute le document au corpus
    assert len(empty_corpus.documents) == 1  # Vérifie qu'il y a un document dans le corpus
    assert empty_corpus.documents[0] is base_document  # Vérifie que le document ajouté est bien celui attendu

def test_display_documents(empty_corpus, base_document, capsys):
    # Test pour vérifier l'affichage des documents dans le corpus
    empty_corpus.add_document(base_document)  # Ajoute un document au corpus
    empty_corpus.display_documents()  # Affiche les documents
    captured = capsys.readouterr()  # Capture la sortie affichée
    # Vérifie que le titre et l'auteur du document apparaissent bien dans la sortie
    assert "Test Document" in captured.out
    assert "Test Author" in captured.out

def test_collect_wikipedia_data(mocker):
    # Test pour vérifier la collecte des données Wikipedia
    mock_page = mocker.MagicMock()  # Crée un mock pour une page Wikipedia
    mock_page.exists.return_value = True  # Définit que la page existe
    mock_page.title = "Test Page"  # Définition du titre du mock
    mock_page.summary = "Test summary"  # Définition du résumé du mock

    # Patch de la méthode pour intercepter la création de l'objet Wikipedia et retourner notre mock
    mock_wiki = mocker.patch('wikipediaapi.Wikipedia')
    mock_wiki.return_value.page.return_value = mock_page

    from wikipedia_collector import collect_wikipedia_data  # Import de la fonction à tester
    documents = collect_wikipedia_data()  # Appel de la fonction pour collecter les documents

    # Vérifie que des documents ont bien été collectés et qu'ils sont bien de type WikipediaDocument
    assert len(documents) > 0
    assert isinstance(documents[0], WikipediaDocument)
    assert documents[0].title == "Test Page"  # Vérifie que le titre du premier document est correct
