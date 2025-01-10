import tkinter as tk
from tkinter import scrolledtext, messagebox
from corpus import Corpus
from text_processing import clean_text, compute_tfidf, compute_idf
from data_collection import collect_arxiv_data, collect_wikipedia_data
from similarity import cosine_similarity

# Fonction pour afficher le contenu complet d'un document dans une nouvelle fenêtre
def display_document_content(doc):
    """
    Ouvre une nouvelle fenêtre pour afficher le contenu complet d'un document.
    """
    doc_window = tk.Toplevel()  # Crée une nouvelle fenêtre
    doc_window.title(doc.title)  # Définit le titre de la fenêtre avec le titre du document

    # Création d'une zone de texte défilante pour le contenu du document
    text_area = scrolledtext.ScrolledText(doc_window, width=80, height=25, wrap=tk.WORD)
    text_area.pack(pady=10, padx=10)
    text_area.config(state=tk.NORMAL)
    
    # Insertion des informations du document dans la zone de texte
    text_area.insert(tk.END, f"Title: {doc.title}\n")
    text_area.insert(tk.END, f"Author: {doc.author}\n")
    text_area.insert(tk.END, f"Date: {doc.date}\n")
    text_area.insert(tk.END, f"Type: {doc.type}\n\n")
    text_area.insert(tk.END, f"Content:\n{doc.text}\n")
    text_area.config(state=tk.DISABLED)

    # Ajout d'un bouton pour revenir à la liste des résultats
    back_button = tk.Button(doc_window, text="Back to List", command=doc_window.destroy)
    back_button.pack(pady=10)

# Fonction pour afficher les résultats de la recherche dans une nouvelle fenêtre
def display_search_results(search_results):
    """
    Affiche la liste des résultats de recherche dans une fenêtre défilante.
    """
    results_window = tk.Toplevel()  # Crée une nouvelle fenêtre pour les résultats de recherche
    results_window.title("Search Results")

    # Frame défilante pour les résultats
    frame = tk.Frame(results_window)
    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configuration de la zone défilante pour afficher tous les résultats
    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Ajout des résultats de la recherche sous forme de boutons
    for doc in search_results:
        result_button = tk.Button(
            scrollable_frame,
            text=doc.title,
            command=lambda doc=doc: display_document_content(doc),
            width=70,
            anchor="w",
        )
        result_button.pack(pady=2, padx=10, anchor="w")

    # Bouton pour revenir à la recherche
    back_button = tk.Button(results_window, text="Back to Search", command=results_window.destroy)
    back_button.pack(pady=10)

# Fonction pour rechercher les documents pertinents dans le corpus selon la requête de l'utilisateur
def search_documents():
    """
    Recherche les documents dans le corpus pour leur pertinence par rapport à la requête de l'utilisateur.
    """
    query = search_entry.get().strip()  # Récupère la requête de recherche
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")  # Affiche un avertissement si la requête est vide
        return

    similarities = []  # Liste des similarités entre la requête et les documents
    query_words = clean_text(query)  # Traitement du texte de la requête
    query_tf = {}  # Dictionnaire pour stocker les fréquences de termes de la requête
    query_word_count = len(query_words)  # Compte le nombre de mots dans la requête
    for word in query_words:
        query_tf[word] = query_tf.get(word, 0) + 1  # Compte les occurrences des mots
    for word in query_tf:
        query_tf[word] = query_tf[word] / query_word_count  # Calcule les fréquences relatives des mots

    query_tfidf = {}  # Dictionnaire pour stocker les valeurs TF-IDF de la requête
    idf = compute_idf(corpus)  # Calcule les valeurs IDF pour le corpus
    for word in query_tf:
        query_tfidf[word] = query_tf[word] * idf.get(word, 0)  # Calcule les valeurs TF-IDF pour chaque mot de la requête

    for idx, doc in enumerate(corpus.documents):
        doc_tfidf = compute_tfidf(corpus)[idx]  # Récupère les valeurs TF-IDF pour chaque document
        similarity = cosine_similarity(query_tfidf, doc_tfidf)  # Calcule la similarité cosinus entre la requête et le document
        similarities.append((similarity, doc))  # Ajoute la similarité et le document à la liste

    # Trie les résultats par similarité décroissante et sélectionne les 20 meilleurs
    similarities.sort(key=lambda x: x[0], reverse=True)
    top_results = [doc for _, doc in similarities[:20]]

    display_search_results(top_results)  # Affiche les résultats de la recherche

# Crée le corpus et ajoute les documents Arxiv et Wikipedia
corpus = Corpus()
arxiv_docs = collect_arxiv_data()  # Récupère les documents Arxiv
for doc in arxiv_docs:
    corpus.add_document(doc)

wiki_docs = collect_wikipedia_data()  # Récupère les documents Wikipedia
for doc in wiki_docs:
    corpus.add_document(doc)

# Crée la fenêtre principale de l'application GUI
window = tk.Tk()
window.title("Document Search")
window.geometry("600x400")

# Centre la fenêtre sur l'écran
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"+{x}+{y}")

# Barre de recherche et bouton
search_label = tk.Label(window, text="Enter Search Query:")
search_label.pack(pady=10)

search_entry = tk.Entry(window, width=50)
search_entry.pack(pady=5)

search_button = tk.Button(window, text="Search", command=search_documents)
search_button.pack(pady=10)

# Démarre la boucle principale de l'interface graphique
window.mainloop()
