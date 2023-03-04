import json
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
# Importing Gensim
import gensim
from gensim import corpora

# Adapted from our 3rd X-Hour Workshop

def clean(doc):
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

def topic_analysis(doc_complete):
    #cleaning the text in each document in our list
    doc_clean = [clean(doc).split() for doc in doc_complete] 
    print(doc_clean)
    # Creating the term dictionary of our corpus, where every unique term is assigned an index.
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above. (in gensmin doc2bow will create the matrix of word quantities for us, on the dictionary object)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel
    # Running and Training LDA model on the document term matrix.
    ldamodel = Lda(doc_term_matrix, num_topics=20, id2word = dictionary, passes=50)
    return (ldamodel.print_topics(num_topics=20, num_words=3))

with open('data/fizz/post_text.json') as data_file:    
    data = json.load(data_file)
    fizz_data = data['posts']
    topics = topic_analysis(fizz_data)
    print(topics)
    with open('TOPICS/fizz.txt', 'w') as outfile:
        for topic in topics:
            outfile.write(str(topic[0])+'\t'+topic[1]+'\n')
        outfile.close() 

with open('data/twitter/textual_data.json') as data_file:    
    data = json.load(data_file)
    twitter_data = data['posts']
    topics = topic_analysis(twitter_data)
    print(topics)
    with open('TOPICS/twitter.txt', 'w') as outfile:
        for topic in topics:
            outfile.write(str(topic[0])+'\t'+topic[1]+'\n')
        outfile.close() 