import spacy
import os
# language = portuguese
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import pt_core_news_sm
nlp = pt_core_news_sm.load()

# ----- IMPORTANT ----- #
'''
I MUST CHANGE THIS PART
BELLOW TO READ THE
ARTICLE FROM A WEBSITE.
'''
# ----- --------- ----- #

with open("text.txt", "r", encoding = "utf-8") as f:
    text = " ".join(f.readlines())

doc = nlp(text)

# Matrix of token counts (sentences)
print("Extraindo sentenças do texto...")
corpus = [sent.text.lower() for sent in doc.sents]
count_vec = CountVectorizer(stop_words = list(STOP_WORDS))
count_vec_fit = count_vec.fit_transform(corpus)
words = count_vec.get_feature_names()
count_list = count_vec_fit.toarray().sum(axis=0)

words_freq = dict(zip(words, count_list))

# Determine the relevance of sentences based on
# the accumulative frequency of words within it
sentence_rank = {}
print("Ranqueando sentenças...")
for sent in doc.sents:
    for word in sent:
        if(word.text.lower() in words_freq.keys()):
            if(sent in sentence_rank.keys()):
                sentence_rank[sent] += words_freq[word.text.lower()]
            else:
                sentence_rank[sent] = words_freq[word.text.lower()]

# Sorting and selecting sentences to add to summary
top_sentences = sorted(sentence_rank.values())[::-1]
top_sentences = top_sentences[:3]

# Finally creating summary
summary = []
print("Criando resumo...")
for sent,strength in sentence_rank.items():
    if strength in top_sentences:
        summary.append(sent)
    else:
        continue

# ----- IMPORTANT ----- #
'''
I MUST CHANGE THIS PART
BELLOW TO SAVE AND COMPARE
WITH OTHER ARCTICLES.
'''
# ----- --------- ----- #

# Saving summary
if not os.path.exists('summary.txt'):
    with open('summary.txt', 'w') as file:
        for sentence in summary:
            file.write(str(sentence))

print("Tudo pronto!")
