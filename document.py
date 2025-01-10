# Classe principale Document
class Document:
    # Initialisation du document avec son titre, auteur, date et contenu (par défaut vide)
    def __init__(self, title, author, date, text=""):
        self.title = title  # Le titre du document
        self.author = author  # L'auteur du document
        self.date = date  # La date de publication du document
        self.text = text  # Le contenu du document
        self.type = self.getType()  # Détermine le type du document (par défaut "Document")

    # Méthode pour obtenir le type du document
    def getType(self):
        return "Document"

    # Méthode pour afficher une représentation sous forme de chaîne du document
    def __str__(self):
        import textwrap  # Pour formater le texte à une largeur de 80 caractères
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.date}\nType: {self.type}\nContent:\n{textwrap.fill(self.text, 80)}"

# Classe ArxivDocument qui hérite de Document
class ArxivDocument(Document):
    # Initialisation d'un document Arxiv avec un titre, auteurs, date et contenu
    def __init__(self, title, authors, date, text=""):
        super().__init__(title, ", ".join(authors), date, text)  # Appel du constructeur parent
        self.authors = authors  # Liste des auteurs du document

    # Méthode pour obtenir le type du document (Spécifique à Arxiv)
    def getType(self):
        return "Arxiv"

    # Méthode pour afficher une représentation sous forme de chaîne du document Arxiv
    def __str__(self):
        import textwrap  # Pour formater le texte à une largeur de 80 caractères
        authors_str = ", ".join(self.authors)  # Convertit la liste des auteurs en une chaîne
        return (
            f"Title: {self.title}\n"
            f"Authors: {authors_str}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )

# Classe WikipediaDocument qui hérite de Document
class WikipediaDocument(Document):
    # Initialisation d'un document Wikipedia avec un titre, auteur, date et contenu
    def __init__(self, title, author, date, text=""):
        super().__init__(title, author, date, text)  # Appel du constructeur parent
    
    # Méthode pour obtenir le type du document (Spécifique à Wikipedia)
    def getType(self):
        return "Wikipedia"

    # Méthode pour afficher une représentation sous forme de chaîne du document Wikipedia
    def __str__(self):
        import textwrap  # Pour formater le texte à une largeur de 80 caractères
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )
