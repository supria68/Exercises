"""
Simple python script to pre-process any textual data.
"""

# Basic imports
import nltk
import re
import inflect
import contractions
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

def replace_digits(words):
    """Replace digits to their equivalent text representation"""
    new_words = []
    for word in words:
        if word.isdigit():
            new_words.append(inflect.engine().number_to_words(word))
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(text):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in text:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stemming_words(words):
    """Stem words in list of tokenized words"""
    stemmer = PorterStemmer()
    stems = [stemmer.stem(word) for word in words]
    return stems

def lemmatizing_words(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, pos = 'v') for word in words]
    return lemmas

def preprocess(text):
    """
    This function does
    - converts text to lowercase
    - remove URLs
    - removes contractions if any
    - remove punctuations
    - tokenize the text to words
    - remove stopwords
    - replace digits to their equivalent texts
    """
 
    text = text.lower() 
    print('Text data is converted to lowercase...')
    text = re.sub(r'http\S+','',text) #remove url
    print('Any URLs in the text data has been removed...')
    text = contractions.fix(text)
    print('Contractions in the text data has been removed...')
    text = re.sub(r'[^\w\s]','',text)
    print('Punctuations in the text data has been removed...')
    words = nltk.word_tokenize(text)
    print('Text data is now tokenized...')
    words = remove_stopwords(words)
    print('Typical stopwords are removed...')
    words = replace_digits(words)
    print('Digits have been replaced by their texts...')

    #save preprocess data
    words_save = map(lambda x:x+'\n', words)
    with open('preprocessed_data.txt','w') as f:
        f.write('****** Preprocessed data ***********\n')
        f.writelines(words_save)
    print('Pre-processed data is now saved..............\n')
    return words

def further_process(words):
    """
    This function performs stemming, lemmatization
    """

    stem = stemming_words(words)
    lemma = lemmatizing_words(words)
    print('Stemming and Lemmatizing text data is completed...') 
    return stem,lemma 


if __name__ ==  "__main__":
    
    sample = """A book is a medium for recording information in the form of writing or images, typically composed of many pages (made of papyrus, parchment, vellum, or paper) bound together and protected by a cover. The technical term for this physical arrangement is codex (plural, codices). In the history of hand-held physical supports for extended written compositions or records, the codex replaces its predecessor, the scroll. A single sheet in a codex is a leaf and each side of a leaf is a page. As an intellectual object, a book is prototypically a composition of such great length that it takes a considerable investment of time to compose and a still considerable, though not so extensive, investment of time to read. In a restricted sense, a book is a self-sufficient section or part of a longer composition, a usage that reflects the fact that, in antiquity, long works had to be written on several scrolls and each scroll had to be identified by the book it contained. Each part of Aristotle's Physics is called a book. In an unrestricted sense, a book is the compositional whole of which such sections, whether called books or chapters or parts, are parts. The intellectual content in a physical book need not be a composition, nor even be called a book. Books can consist only of drawings, engravings or photographs, crossword puzzles or cut-out dolls. In a physical book, the pages can be left blank or can feature an abstract set of lines to support entries, in an account book, an appointment book, an autograph book, a notebook, a diary or a sketchbook. Some physical books are made with pages thick and sturdy enough to support other physical objects, like a scrapbook or photograph album. Books may be distributed in electronic form as e-books and other formats. Although in ordinary academic parlance a monograph is understood to be aspecialist academic work, rather than a reference work on a scholarly subject,in library and information science monograph denotes more broadly any non-serial publication complete in one volume (book) or a finite number of volumes (even a novel like Proust's seven-volume In Search of Lost Time), in contrast to serial publications like a magazine, journal or newspaper. An avid reader or collector of books is a bibliophile or colloquially, "bookworm". A place where books are traded is a bookshop or bookstore. Books are also sold elsewhere and can be borrowed from libraries. Google has estimated that in 2010, approximately 130,000,000 titles had been published. In some wealthier nations, the sale of printed books has decreased because of the increased usage of e-books."""
    
    # pre-processing text data
    words = preprocess(sample)

    # Further process
    stems, lemmas = further_process(words)

    print('There are {} words in the sample'.format(len(words)))
   
    import pandas as pd
    data = pd.DataFrame(stems, columns = ['Stemmed'])
    data['Lemmatized'] = pd.Series(lemmas)
    print(data.head(10))
