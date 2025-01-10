class Document:
    def __init__(self, title, author, date, text=""):
        self.title = title
        self.author = author
        self.date = date
        self.text = text
        self.type = self.getType()

    def getType(self):
        return "Document"

    def __str__(self):
        import textwrap
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.date}\nType: {self.type}\nContent:\n{textwrap.fill(self.text, 80)}"

class ArxivDocument(Document):
    def __init__(self, title, authors, date, text=""):
        super().__init__(title, ", ".join(authors), date, text)
        self.authors = authors

    def getType(self):
        return "Arxiv"

    def __str__(self):
        import textwrap
        authors_str = ", ".join(self.authors)
        return (
            f"Title: {self.title}\n"
            f"Authors: {authors_str}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )

class WikipediaDocument(Document):
    def __init__(self, title, author, date, text=""):
        super().__init__(title, author, date, text)
    
    def getType(self):
        return "Wikipedia"

    def __str__(self):
        import textwrap
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Date: {self.date}\n"
            f"Type: {self.type}\n"
            f"Content:\n{textwrap.fill(self.text, 80)}"
        )
