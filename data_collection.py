# Importation des modules nécessaires
import urllib.request  # Pour effectuer des requêtes HTTP
import xmltodict  # Pour analyser les données XML
import datetime  # Pour travailler avec les dates et heures
import wikipediaapi  # Pour interagir avec l'API de Wikipedia
from document import ArxivDocument, WikipediaDocument  # Importation des classes ArxivDocument et WikipediaDocument
import time  # Pour gérer les pauses dans le code

# Fonction pour collecter des données depuis l'API Arxiv
def collect_arxiv_data():
    query = "covid"  # Le terme de recherche pour les articles Arxiv
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=100'  # URL pour interroger l'API d'Arxiv
    time.sleep(1)  # Ajoute une pause pour éviter d'envoyer trop de requêtes en peu de temps

    # Envoie la requête HTTP et lit la réponse
    with urllib.request.urlopen(url) as response:
        data = response.read()

    # Analyse la réponse XML en un dictionnaire Python
    parsed_data = xmltodict.parse(data)
    documents = []  # Liste pour stocker les documents collectés

    # Parcours des résultats dans la réponse et création des objets ArxivDocument
    for entry in parsed_data['feed']['entry']:
        # Récupère les auteurs (s'ils existent) et crée un document
        authors = [author['name'] for author in entry['author']] if isinstance(entry['author'], list) else [entry['author']['name']]
        doc = ArxivDocument(
            title=entry['title'],  # Titre du document
            authors=authors,  # Liste des auteurs
            date=entry['published'],  # Date de publication
            text=entry['summary'].replace("\n", " ")  # Résumé de l'article, les sauts de ligne sont supprimés
        )
        documents.append(doc)  # Ajoute le document à la liste
    return documents  # Retourne la liste des documents collectés

# Fonction pour collecter des données depuis Wikipedia
def collect_wikipedia_data():
    # Initialise l'API Wikipedia pour l'anglais
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='MoteurRecherchePython/1.0 (contact@example.com)'  # Identifiant de l'agent utilisateur pour éviter les restrictions
    )

    # Liste des titres des pages à collecter
    titles = [
        "COVID-19_pandemic", "COVID-19_vaccines", "COVID-19_testing",
        "COVID-19_pandemic_in_Italy", "COVID-19_pandemic_in_the_United_States",
        "COVID-19_pandemic_in_India", "COVID-19_pandemic_in_China",
        "COVID-19_pandemic_in_Brazil", "COVID-19_pandemic_in_France",
    ]

    documents = []  # Liste pour stocker les documents collectés

    # Parcours des titres de pages Wikipédia et création des documents WikipediaDocument
    for title in titles:
        page = wiki.page(title)  # Récupère la page Wikipédia correspondant au titre
        if page.exists():  # Si la page existe
            doc = WikipediaDocument(
                title=page.title,  # Titre de la page
                author="Wikipedia",  # L'auteur est fixé à "Wikipedia"
                date=datetime.datetime.now().strftime("%Y-%m-%d"),  # Date actuelle
                text=page.summary  # Résumé de la page
            )
            documents.append(doc)  # Ajoute le document à la liste
    return documents  # Retourne la liste des documents collectés
