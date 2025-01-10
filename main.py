from corpus import Corpus  # Importation de la classe Corpus pour gérer les documents
from arxiv_collector import collect_arxiv_data  # Importation de la fonction pour collecter les données d'Arxiv
from wikipedia_collector import collect_wikipedia_data  # Importation de la fonction pour collecter les données de Wikipedia
from utils.save_load import save_corpus, load_corpus  # Importation des fonctions pour sauvegarder et charger le corpus

if __name__ == "__main__":  # Vérifie si le script est exécuté directement
    corpus = Corpus()  # Création d'une instance unique du corpus

    # Collecte des données depuis Arxiv et Wikipedia
    arxiv_documents = collect_arxiv_data()  # Collecte des documents d'Arxiv
    wikipedia_documents = collect_wikipedia_data()  # Collecte des documents de Wikipedia

    # Ajout des documents collectés dans le corpus
    for doc in arxiv_documents + wikipedia_documents:  # Parcours des deux listes de documents
        corpus.add_document(doc)  # Ajout de chaque document au corpus

    # Affichage de tous les documents dans le corpus
    corpus.display_documents()

    # Sauvegarde du corpus dans un fichier
    save_corpus(corpus, "corpus.pkl")

    # Chargement du corpus depuis le fichier sauvegardé
    loaded_corpus = load_corpus("corpus.pkl")

    # Affichage des documents chargés depuis le fichier
    loaded_corpus.display_documents()
