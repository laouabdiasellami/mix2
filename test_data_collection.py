from .data_collection import collect_arxiv_data, collect_wikipedia_data

def test_collect_arxiv_data():
    """
    Teste la fonction de collecte des données depuis Arxiv.
    Ce test vérifie que des documents sont collectés et que tous
    les documents collectés sont correctement marqués comme provenant d'Arxiv.
    """
    documents = collect_arxiv_data()  # Appelle la fonction pour collecter les données d'Arxiv
    
    # Vérifie que la liste des documents n'est pas vide
    assert len(documents) > 0  
    
    # Vérifie que tous les documents collectés sont de type "Arxiv"
    assert all(doc.getType() == "Arxiv" for doc in documents)

def test_collect_wikipedia_data():
    """
    Teste la fonction de collecte des données depuis Wikipedia.
    Ce test vérifie que des documents sont collectés et que tous
    les documents collectés sont correctement marqués comme provenant de Wikipedia.
    """
    documents = collect_wikipedia_data()  # Appelle la fonction pour collecter les données de Wikipedia
    
    # Vérifie que la liste des documents n'est pas vide
    assert len(documents) > 0  
    
    # Vérifie que tous les documents collectés sont de type "Wikipedia"
    assert all(doc.getType() == "Wikipedia" for doc in documents)
