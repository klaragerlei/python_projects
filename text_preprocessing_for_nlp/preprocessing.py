from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
import pandas as pd
import numpy as np
import nltk, re

#read csv file
def read_data(file_path):
    return pd.read_csv(file_path)

#create a vectorize
#used to the first step of preprocessing and for
#trasforming text into vectors
def build_vectorizer(name):
    if name == "cv":
        return CountVectorizer(stop_words='english', analyzer="word",)
    elif name == "tfidf":
        return TfidfVectorizer(stop_words='english', analyzer="word",)

#lemmatize an entire column of a dataframe using WordNet lemmatizer from nltk
def lemmatize_data(dataframe, col_name):
    wnl = WordNetLemmatizer()
    rows = []
    count = 0
    #iterate over dataframe rows
    for index,row in dataframe.iterrows():
        count += 1
        #lemmatize each word separately
        #only adjectives, nouns and verbs are lemmatized
        words = [wnl.lemmatize(i,j[0].lower()) if j[0].lower() in ['a','n','v'] else wnl.lemmatize(i) for i,j in pos_tag(word_tokenize(str(row[col_name])))]
        #join all the words back into a single string
        res.append(' '.join(w for w in words))
    #return a new dataframe with lemmatized text
    return pd.DataFrame(rows)

#preprocess a dataframe and return a new dataframe with preprocessed text
def preprocess_dataframe(dataframe, processer):
    # conversion to lowercase, stopwords removal, punctuation removal
    dataframe = dataframe.applymap(lambda x: " ".join(s for s in processer(x)))
    #numbers removal
    dataframe = dataframe.applymap(lambda x: re.sub(r'[0-9]+',"",x))
    # OPTIONAL: remove text with less than threshold words
    dataframe = dataframe.applymap(lambda x: " ".join(s for s in x.split() if len(s) > threshold))
    return dataframe

#feeds the data to the vectorizer which transforms it into vectors
def feed_data(dataframe, col_name):
    #feed one text line at a time
    for index,row in dataframe.iterrows():
        yield row[col_name]

# code execution
if __name__ == "__main__":
    file_name = "path_to_the_file.csv"

    text_data = read_data(file_name)

    #instantiate a CounVectorizer
    #transforms words as one-hot vectors
    vectorizer = build_vectorizer("cv")

    #instantiate the analyzer
    #this is the module that handles preprocessing
    analyzer = vectorizer.build_analyzer()

    #lemmatize text data from the chosen column
    #WARNING: the returned dataframe has only one column !
    lemmatized_data = lemmatize_data(text_data, 'name_of_the_text_column')

    #preprocess textual data to remove noise and uninformative data
    preprocessed_text = preprocess_dataframe(lemmatized_data, analyzer)

    #transform preprocessed text into vectors in the vector space
    vectorized_data = vectorizer.fit_transform(feed_data(preprocessed_text, 'name_of_the_text_column'))

    #now you can use vectorized_data for your application i.e.:
    #   - clustering
    #   - train a machine learning model
    #   - train word embeddings
    #   - and so on...
