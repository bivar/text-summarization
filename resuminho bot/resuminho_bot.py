import os
import telebot
import spacy
import os
# language = portuguese
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import pt_core_news_sm
nlp = pt_core_news_sm.load()

# API_TOKEN
token = os.environ['BOT_API_TOKEN']

# BOT 
bot = telebot.TeleBot(token)

# ENDPOINTS
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Olá! Envia um texto pra mim que eu darei meu melhor pra resumir pra você!")
    

@bot.message_handler(content_types=['text'])
def send_summarized_text(message):
    new_text = summarize(message)
    new_text = ' '.join([str(sentence) for sentence in new_text])
    bot.reply_to(message, new_text)
    
    
def summarize(message):
    text = message.text
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
    
    return summary
    
    
bot.polling()
