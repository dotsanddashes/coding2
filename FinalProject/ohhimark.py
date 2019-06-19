import random
import re
import numpy as np
from flask import Flask
from flask import render_template

def open_file(fname):  # открываем файл с подготовленным текстом
    with open(fname, encoding='utf-8') as f:
        text = f.read()
        text = re.sub('([аА-яЯ]+)([.,!?:;])', r'\1 \2', text)
        words = text.split(' ')
    return words


def word_distribution():  # создаем вложенный словарь распределения слов
    words = open_file('rifters.txt')
    d = {}
    d[words[0]] = {}
    d[words[0]][words[1]] = 1
    i = 2
    while i < len(words):
        if words[i - 1] not in d.keys():
            d[words[i - 1]] = {}
            d[words[i - 1]][words[i]] = 1
        elif words[i] not in d[words[i - 1]].keys():
            d[words[i - 1]][words[i]] = 1
        else:
            v_new = int(d[words[i - 1]][words[i]]) + 1
            d[words[i - 1]][words[i]] = v_new
        i += 1
    return d


def markov_alg():
    d = word_distribution()
    sentence = []
    last_word = ['.', '!', '?']
    first_word = []
    for i in range(len(last_word)):
        for key in d[last_word[i]].keys():
            first_word.append(key)
    word_now = random.choice(first_word)
    sentence.append(word_now)
    while word_now not in last_word:
        w = list(d[word_now].keys())
        freq = []
        a = 0
        b = 0
        for v in d[word_now].values():
            a = a + int(v)
        for v in d[word_now].values():
            b = int(v) / a
            freq.append(b)
        word_now = np.random.choice(w, p=freq)
        sentence.append(word_now)
    return sentence


def final():
    sentence = markov_alg()
    final_sentence = ' '.join(sentence)
    final_sentence = re.sub('([аА-яЯ]+)(\s)([.,!?:;])', r'\1\3', final_sentence)
    return final_sentence



app = Flask(__name__)

@app.route('/')
def sentence():
    final_sentence = final()
    return render_template('main.html', final_sentence = final_sentence)

if __name__ == '__main__':
    app.run(debug=False)