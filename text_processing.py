import string
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk

# Téléchargement des ressources nécessaires de NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Fonction pour nettoyer le texte : conversion en minuscules, suppression de la ponctuation, des chiffres et des stopwords
def clean_text(text, use_stemming=False, use_lemmatization=True):
    text = text.lower()  # Convertir tout le texte en minuscules
    text = text.translate(str.maketrans('', '', string.punctuation))  # Supprimer la ponctuation
    text = ''.join([i for i in text if not i.isdigit()])  # Supprimer les chiffres
    words = word_tokenize(text)  # Tokenisation du texte en mots
    stop_words = set(stopwords.words('english'))  # Liste des mots vides (stopwords)
    words = [word for word in words if word not in stop_words]  # Suppression des mots vides

    # Appliquer le stemming ou la lemmatisation selon les choix de l'utilisateur
    if use_stemming:
        stemmer = PorterStemmer()  # Utilisation du stemmer de Porter
        words = [stemmer.stem(word) for word in words]  # Appliquer le stemming à chaque mot
    elif use_lemmatization:
        lemmatizer = WordNetLemmatizer()  # Utilisation du lemmatiseur WordNet
        words = [lemmatizer.lemmatize(word) for word in words]  # Appliquer la lemmatisation à chaque mot
    
    return words  # Retourner la liste des mots nettoyés

# Fonction pour calculer la fréquence des termes (TF) d'un document
def compute_tf(document):
    tf = {}  # Dictionnaire pour stocker la fréquence des termes
    words = clean_text(document.text)  # Nettoyer le texte du document
    word_count = len(words)  # Compter le nombre de mots dans le document
    for word in words:
        tf[word] = tf.get(word, 0) + 1  # Comptabiliser le nombre d'occurrences de chaque mot
    for word in tf:
        tf[word] = tf[word] / word_count  # Normaliser les fréquences des termes
    return tf  # Retourner le dictionnaire des fréquences des termes normalisées

# Fonction pour calculer l'IDF (Inverse Document Frequency) pour l'ensemble du corpus
def compute_idf(corpus):
    idf = {}  # Dictionnaire pour stocker les valeurs IDF
    total_documents = len(corpus.documents)  # Nombre total de documents dans le corpus
    for doc in corpus.documents:  # Parcourir chaque document du corpus
        words = set(clean_text(doc.text))  # Récupérer les mots uniques du document
        for word in words:
            if word not in idf:
                idf[word] = 0  # Initialiser l'IDF pour ce mot
            idf[word] += 1  # Augmenter le compteur de documents contenant ce mot
    for word in idf:
        idf[word] = math.log(total_documents / (1 + idf[word])) + 1  # Calculer l'IDF pour chaque mot
    return idf  # Retourner le dictionnaire des valeurs IDF

# Fonction pour calculer le TF-IDF (Term Frequency - Inverse Document Frequency) pour tous les documents du corpus
def compute_tfidf(corpus):
    idf = compute_idf(corpus)  # Calculer les valeurs IDF
    tfidf_docs = []  # Liste pour stocker le TF-IDF de chaque document
    for doc in corpus.documents:  # Parcourir chaque document du corpus
        tf = compute_tf(doc)  # Calculer le TF pour le document
        tfidf = {}  # Dictionnaire pour stocker les valeurs TF-IDF
        for word in tf:  # Pour chaque mot du document
            tfidf[word] = tf[word] * idf.get(word, 0)  # Calculer le TF-IDF pour ce mot
        tfidf_docs.append(tfidf)  # Ajouter le dictionnaire TF-IDF du document à la liste
    return tfidf_docs  # Retourner la liste des TF-IDF des documents
