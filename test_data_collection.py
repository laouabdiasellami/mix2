from .data_collection import collect_arxiv_data, collect_wikipedia_data

# Test pour vérifier la collecte des données depuis arXiv
def test_collect_arxiv_data():
    documents = collect_arxiv_data()  # Collecte des documents depuis arXiv
    assert len(documents) > 0  # Vérifie que des documents ont bien été collectés
    # Vérifie que tous les documents collectés sont de type "Arxiv"
    assert all(doc.getType() == "Arxiv" for doc in documents)

# Test pour vérifier la collecte des données depuis Wikipedia
def test_collect_wikipedia_data():
    documents = collect_wikipedia_data()  # Collecte des documents depuis Wikipedia
    assert len(documents) > 0  # Vérifie que des documents ont bien été collectés
    # Vérifie que tous les documents collectés sont de type "Wikipedia"
    assert all(doc.getType() == "Wikipedia" for doc in documents)
