import pickle

def save_corpus(corpus, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(corpus, f)

def load_corpus(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)
