# Importation des classes et fonctions nécessaires
from corpus import Corpus  # Classe pour gérer le corpus de documents
from data_collection import collect_arxiv_data, collect_wikipedia_data  # Fonctions pour collecter les données depuis Arxiv et Wikipedia
from similarity import find_most_relevant_articles  # Fonction pour trouver les articles les plus pertinents

# Exécution du script principal
if __name__ == "__main__":
    # Création d'un nouvel objet corpus
    corpus = Corpus()

    # Collecte des documents Arxiv et Wikipedia
    arxiv_docs = collect_arxiv_data()  # Récupère les documents depuis Arxiv
    wiki_docs = collect_wikipedia_data()  # Récupère les documents depuis Wikipedia

    # Ajout des documents collectés dans le corpus
    for doc in arxiv_docs + wiki_docs:  # Combine les documents Arxiv et Wikipedia et les ajoute dans le corpus
        corpus.add_document(doc)

    # Définition de la requête de recherche
    query = "deaths"  # Mot-clé pour rechercher les documents pertinents

    # Affichage du message de recherche
    print(f"Searching for most relevant documents related to: '{query}'\n")

    # Recherche des articles les plus pertinents avec deux méthodes différentes
    find_most_relevant_articles(corpus, query, method='cosine')  # Utilisation de la méthode 'cosine'
    find_most_relevant_articles(corpus, query, method='bm25')  # Utilisation de la méthode 'bm25'
