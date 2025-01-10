class Corpus:
    # Déclaration d'une variable de classe _instance qui va contenir l'unique instance du corpus
    _instance = None

    # Méthode spéciale __new__ pour implémenter le pattern Singleton
    def __new__(cls):
        # Si l'instance n'existe pas, en créer une nouvelle
        if cls._instance is None:
            # Appel de la méthode __new__ de la classe parente pour créer l'instance
            cls._instance = super(Corpus, cls).__new__(cls)
            # Initialisation d'une liste vide pour stocker les documents
            cls._instance.documents = []
        # Retour de l'instance unique du corpus
        return cls._instance

    # Méthode pour ajouter un document à la liste
    def add_document(self, document):
        # Ajoute le document à la liste des documents
        self.documents.append(document)

    # Méthode pour afficher tous les documents du corpus
    def display_documents(self):
        # Parcours de tous les documents dans la liste
        for doc in self.documents:
            # Affiche une ligne de séparation
            print("=" * 80)
            # Affiche le contenu du document
            print(doc)
