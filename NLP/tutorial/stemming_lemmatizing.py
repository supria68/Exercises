"""
Definition:

Stemming is a process of reducing infected words to a base word (word stem). The base word need not have any meaning!
Eg:
    books      --->    book
    looked     --->    look
    denied     --->    deni
    flies      --->    fli
Application of Stemming:
    - Used in sentiment analysis, email spam classifier etc

*******************

Lemmatizing is a process of reducing infected words to a base word such that
this base word has a proper meaning. Lemmatize takes a part of speech parameter, “pos” If not supplied, the default is “noun.”

Eg:
    rocks : rock
    corpora : corpus
    better : good
Application of Lemmatizing:
    - Used in chatbots, search engines etc

Reference: Krish Naik Playlist on youtube - https://www.youtube.com/playlist?list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm
"""

import nltk
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Former President APJ Abdul Kalam's Speech at IIT.
para = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""


#Pre-processing
para_lower = para.lower() #convert paragraph to lowercase
para_lower = re.sub(r'[^\w\s]','',para_lower) #remove punctuation

# Stemming Process
stemmer = PorterStemmer()
words = nltk.word_tokenize(para_lower)
stem_words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
print("Completed Stemming words...")

# Lemmatizing Process
lemmatizer = WordNetLemmatizer()
lemma_words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
print("Completed Lemmatizing words...")

#Let's add them in a tabular format!
import pandas as pd
data = pd.DataFrame(stem_words, columns = ['Stemmed'])
data['Lemmatized'] = pd.Series(lemma_words)
print(data.head(10))
data.to_csv('stem_lemmatized.csv')
