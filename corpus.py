# Définition de la classe Corpus
class Corpus:
    _instance = None  # Attribut pour implémenter le modèle Singleton

    # Méthode spéciale __new__ pour garantir qu'il n'y a qu'une seule instance de Corpus
    def __new__(cls):
        if cls._instance is None:  # Si l'instance n'existe pas encore
            cls._instance = super(Corpus, cls).__new__(cls)  # Crée une nouvelle instance
            cls._instance.documents = []  # Initialisation de la liste des documents
        return cls._instance  # Retourne l'instance unique du Corpus

    # Méthode pour ajouter un document à la liste des documents
    def add_document(self, document):
        self.documents.append(document)  # Ajoute le document à la liste des documents

    # Méthode pour afficher les documents du corpus
    def display_documents(self):
        for doc in self.documents:  # Parcours chaque document dans la liste
            print("=" * 80)  # Affiche une ligne de séparation
            print(doc)  # Affiche le document
