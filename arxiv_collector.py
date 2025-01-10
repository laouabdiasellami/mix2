import time  # Importation de la bibliothèque time pour ajouter des délais
import urllib.request  # Importation de la bibliothèque pour effectuer des requêtes HTTP
import xmltodict  # Importation de la bibliothèque pour convertir des données XML en dictionnaire
from document import ArxivDocument  # Importation de la classe ArxivDocument pour représenter les documents collectés

# Fonction pour collecter les données d'Arxiv en fonction d'un terme de recherche (par défaut "covid")
def collect_arxiv_data(query="covid"):
    # URL de l'API Arxiv avec une requête de recherche basée sur le mot-clé
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=100'
    
    time.sleep(1)  # Ajout d'une pause de 1 seconde pour éviter de surcharger l'API avec trop de requêtes

    # Envoi de la requête HTTP à l'API d'Arxiv et lecture de la réponse
    with urllib.request.urlopen(url) as response:
        data = response.read()  # Récupération des données de la réponse

    # Conversion des données XML en dictionnaire Python
    parsed_data = xmltodict.parse(data)
    
    documents = []  # Liste pour stocker les documents collectés
    
    # Parcours des entrées (articles) récupérées dans les données XML
    for entry in parsed_data['feed']['entry']:
        # Récupération des auteurs : vérifie si la liste des auteurs existe
        authors = [author['name'] for author in entry['author']] if isinstance(entry['author'], list) else [entry['author']['name']]
        
        # Création d'un objet ArxivDocument avec les informations de l'article
        doc = ArxivDocument(
            title=entry['title'],  # Titre de l'article
            authors=authors,  # Liste des auteurs
            date=entry['published'],  # Date de publication
            text=entry['summary'].replace("\n", " ")  # Résumé de l'article, les sauts de ligne sont remplacés par un espace
        )
        
        # Ajout du document à la liste des documents
        documents.append(doc)
    
    # Retourne la liste des documents collectés
    return documents
