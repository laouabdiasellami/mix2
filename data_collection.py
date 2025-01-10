import urllib.request
import xmltodict
import datetime
import wikipediaapi
from document import ArxivDocument, WikipediaDocument
import time

def collect_arxiv_data():
    query = "covid"
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=100'
    time.sleep(1)

    with urllib.request.urlopen(url) as response:
        data = response.read()

    parsed_data = xmltodict.parse(data)
    documents = []
    for entry in parsed_data['feed']['entry']:
        authors = [author['name'] for author in entry['author']] if isinstance(entry['author'], list) else [entry['author']['name']]
        doc = ArxivDocument(
            title=entry['title'],
            authors=authors,
            date=entry['published'],
            text=entry['summary'].replace("\n", " ")
        )
        documents.append(doc)
    return documents

def collect_wikipedia_data():
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='MoteurRecherchePython/1.0 (contact@example.com)'
    )

    titles = [
        "COVID-19_pandemic", "COVID-19_vaccines", "COVID-19_testing",
        "COVID-19_pandemic_in_Italy", "COVID-19_pandemic_in_the_United_States",
    ]

    documents = []
    for title in titles:
        page = wiki.page(title)
        if page.exists():
            doc = WikipediaDocument(
                title=page.title,
                author="Wikipedia",
                date=datetime.datetime.now().strftime("%Y-%m-%d"),
                text=page.summary
            )
            documents.append(doc)
    return documents
