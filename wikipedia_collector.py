import datetime  # Importation de la bibliothèque datetime pour manipuler les dates
import wikipediaapi  # Importation de la bibliothèque wikipediaapi pour accéder à l'API de Wikipedia
from document import WikipediaDocument  # Importation de la classe WikipediaDocument pour représenter les documents collectés

# Fonction pour collecter les données de Wikipedia à partir de pages spécifiques
def collect_wikipedia_data():
    # Initialisation de l'API Wikipedia avec la langue anglaise et un agent utilisateur spécifique
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='MoteurRecherchePython/1.0 (contact@example.com)'  # Spécifie un agent utilisateur pour respecter les bonnes pratiques
    )

    # Liste des titres de pages Wikipedia à collecter
    titles = [
        "COVID-19_pandemic", "COVID-19_vaccines", "COVID-19_testing",
        "COVID-19_pandemic_in_Italy", "COVID-19_pandemic_in_the_United_States",
    ]

    documents = []  # Liste pour stocker les documents collectés

    # Parcours des titres de pages
    for title in titles:
        page = wiki.page(title)  # Récupère la page Wikipedia correspondant au titre
        if page.exists():  # Vérifie si la page existe
            # Création d'un objet WikipediaDocument avec les informations de la page
            doc = WikipediaDocument(
                title=page.title,  # Titre de la page
                author="Wikipedia",  # L'auteur est défini comme "Wikipedia"
                date=datetime.datetime.now().strftime("%Y-%m-%d"),  # Date de collecte (aujourd'hui)
                text=page.summary  # Résumé de la page
            )
            # Ajout du document à la liste des documents
            documents.append(doc)

    # Retourne la liste des documents collectés
    return documents
