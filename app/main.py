import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random


users={}
tables = ['lap_dep']
service_tag = ['https://dell.com/']
lemmatizer = WordNetLemmatizer()
model = load_model('app/trained-data/chatbot_model.h5')
intents = json.loads(open('app/training-data/intents.json').read())
words = pickle.load(open('app/trained-data/words.pkl','rb'))
classes = pickle.load(open('app/trained-data/classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s: 
                bag[i] = 1
                if show_details:
                     print ("found in bag: %s" % word)
    return(np.array(bag))

def predict_class(sentence):
    p = bag_of_words(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    result = ""
    context = ""
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            context = i['context']
            break
    return result, context

def send(msg,user):
    if msg != '':
        if users[user][0]==1 and users[user][0] != 'NULL':
            if users[user][1] in tables:
                db = users[user][1]
                res = db
            elif users[user][1] in service_tag:
                res = "The details of your Service Tag: "+msg+"<br/><a href='https://dell.com'>Click Here for More Details</a>"
            users[user][0]=0
            users[user][1]='NULL'
            return res
        else:
            ints = predict_class(msg)
            res, con = getResponse(ints, intents)
            if len(con[0]) > 0:
                users[user][0]=1
                users[user][1]=con[0]
            return res
