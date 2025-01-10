import textwrap

# Classe de base Document représentant un document générique
class Document:
    def __init__(self, title, author, date, text=""):
        # Initialisation des attributs du document
        self.title = title
        self.author = author
        self.date = date
        self.text = text
        self.type = self.getType()  # Détermine le type de document

    # Méthode pour retourner le type de document, ici "Document"
    def getType(self):
        return "Document"

    # Méthode pour afficher les informations du document sous forme de chaîne
    def __str__(self):
        # Utilisation de textwrap.fill pour formater le texte sur des lignes de 80 caractères
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.date}\nType: {self.type}\nContent:\n{textwrap.fill(self.text, 80)}"

# Classe dérivée ArxivDocument représentant un document de type Arxiv
class ArxivDocument(Document):
    def __init__(self, title, authors, date, text=""):
        # Initialisation de l'objet de la classe parente avec une liste d'auteurs
        super().__init__(title, ", ".join(authors), date, text)
        self.authors = authors  # Liste des auteurs spécifiques à ArxivDocument

    # Redéfinition de la méthode getType pour retourner "Arxiv"
    def getType(self):
        return "Arxiv"

    # Méthode pour afficher les informations du document de type Arxiv
    def __str__(self):
        authors_str = ", ".join(self.authors)  # Conversion des auteurs en chaîne
        # Affichage formaté des informations du document
        return (
            f"Title: {self.title}\n"
            f"Authors: {authors_str}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )

# Classe dérivée WikipediaDocument représentant un document de type Wikipedia
class WikipediaDocument(Document):
    def __init__(self, title, author, date, text=""):
        # Initialisation de l'objet de la classe parente
        super().__init__(title, author, date, text)
    
    # Redéfinition de la méthode getType pour retourner "Wikipedia"
    def getType(self):
        return "Wikipedia"

    # Méthode pour afficher les informations du document de type Wikipedia
    def __str__(self):
        # Affichage formaté des informations du document
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )
