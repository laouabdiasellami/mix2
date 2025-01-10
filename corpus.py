from document import Document, ArxivDocument, WikipediaDocument

class Corpus:
    # Initialisation d'une instance unique de la classe Corpus
    _instance = None

    def __new__(cls):
        # Si l'instance unique n'existe pas, on la crée
        if cls._instance is None:
            cls._instance = super(Corpus, cls).__new__(cls)
            cls._instance.documents = []  # Liste vide pour stocker les documents
        return cls._instance  # Retourne l'instance unique

    # Méthode pour ajouter un document à la collection
    def add_document(self, document):
        self.documents.append(document)

    # Méthode pour afficher tous les documents du corpus
    def display_documents(self):
        for doc in self.documents:
            print("=" * 80)  # Séparation pour chaque document
            print(doc)  # Affichage du document
