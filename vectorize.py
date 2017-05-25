import spacy
import numpy as np

def load_glove_model(glove_file):
    print "Loading Glove Model"
    f = open(glove_file,'r')
    model = {}
    for line in f:
        split_line = line.split()
        word = split_line[0]
        embedding = [float(val) for val in split_line[1:]]
        model[word] = embedding
    print("{} words loaded".format(len(model)))
    return model

def tokenize_sent(sent):
    sent = sent.strip()
    sent = unicode(sent)
    nlp = spacy.load('en')
    doc = nlp(sent)
    tokens = [token for token in doc if token.is_stop == False]
    return tokens

def get_sent_vector(sent_tokens):
    word_vectors = []
    for token in sent_tokens:
        try:
            token = str(token)
            token = token.lower()
            word_vector = model[token]
            word_vector = np.array(word_vector)
            word_vectors.append(word_vector)
        except KeyError:
            pass
    word_vectors = np.array(word_vectors)
    sent_vector = word_vectors.mean(axis=0)
    sent_vector = sent_vector.tolist()
    return sent_vector

model_file = 'glove/glove.6B.300d.txt'
model = load_glove_model(model_file)
