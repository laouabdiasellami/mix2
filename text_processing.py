import string
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk

# Télécharge les ressources nécessaires de NLTK (tokenisation, stopwords, et lemmatiseur)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text, use_stemming=False, use_lemmatization=True):
    """
    Nettoie un texte en supprimant la ponctuation, les chiffres et les mots vides (stopwords).
    Optionnellement, applique le stemming ou la lemmatisation sur les mots.

    Arguments:
    text -- Le texte à nettoyer.
    use_stemming -- Booléen pour activer ou non le stemming (par défaut False).
    use_lemmatization -- Booléen pour activer ou non la lemmatisation (par défaut True).

    Retourne :
    Une liste de mots nettoyés.
    """
    text = text.lower()  # Convertit le texte en minuscules
    text = text.translate(str.maketrans('', '', string.punctuation))  # Supprime la ponctuation
    text = ''.join([i for i in text if not i.isdigit()])  # Supprime les chiffres
    words = word_tokenize(text)  # Tokenise le texte en mots
    
    # Charge les mots vides (stopwords) en anglais
    stop_words = set(stopwords.words('english'))
    
    # Supprime les mots vides de la liste des mots
    words = [word for word in words if word not in stop_words]

    # Applique le stemming si activé
    if use_stemming:
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words]
    # Sinon, applique la lemmatisation si activée
    elif use_lemmatization:
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
    
    return words

def compute_tf(document):
    """
    Calcule la fréquence des termes (TF) d'un document.
    
    Arguments:
    document -- Le document pour lequel on veut calculer le TF.
    
    Retourne :
    Un dictionnaire où les clés sont les mots et les valeurs sont les fréquences des mots dans le document.
    """
    tf = {}
    words = clean_text(document.text)  # Nettoie le texte du document
    word_count = len(words)  # Compte le nombre total de mots dans le texte
    # Calcule la fréquence des mots
    for word in words:
        tf[word] = tf.get(word, 0) + 1
    # Normalise les fréquences par rapport au nombre total de mots
    for word in tf:
        tf[word] = tf[word] / word_count
    return tf

def compute_idf(corpus):
    """
    Calcule l'IDF (Inverse Document Frequency) pour chaque mot dans un corpus.
    
    Arguments:
    corpus -- Le corpus qui contient plusieurs documents.
    
    Retourne :
    Un dictionnaire où les clés sont les mots et les valeurs sont les IDF de ces mots.
    """
    idf = {}
    total_documents = len(corpus.documents)  # Nombre total de documents dans le corpus
    # Pour chaque document du corpus
    for doc in corpus.documents:
        words = set(clean_text(doc.text))  # Récupère les mots uniques du document
        for word in words:
            if word not in idf:
                idf[word] = 0
            idf[word] += 1  # Compte le nombre de documents dans lesquels le mot apparaît
    # Calcule l'IDF pour chaque mot
    for word in idf:
        idf[word] = math.log(total_documents / (1 + idf[word])) + 1  # Ajoute 1 dans le dénominateur pour éviter une division par zéro
    return idf

def compute_tfidf(corpus):
    """
    Calcule le TF-IDF pour tous les documents dans un corpus.
    
    Arguments:
    corpus -- Le corpus qui contient plusieurs documents.
    
    Retourne :
    Une liste de dictionnaires où chaque dictionnaire contient le TF-IDF des mots pour un document donné.
    """
    idf = compute_idf(corpus)  # Calcule l'IDF pour tous les mots du corpus
    tfidf_docs = []  # Liste pour stocker les résultats de TF-IDF pour chaque document
    # Pour chaque document du corpus
    for doc in corpus.documents:
        tf = compute_tf(doc)  # Calcule le TF pour le document
        tfidf = {}
        # Calcule le TF-IDF pour chaque mot
        for word in tf:
            tfidf[word] = tf[word] * idf.get(word, 0)  # Multiplie le TF par l'IDF
        tfidf_docs.append(tfidf)  # Ajoute le résultat au tableau des documents
    return tfidf_docs
