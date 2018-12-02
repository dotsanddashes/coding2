import json
import csv
import re

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/answer')
def answer():
    d = dict(request.args)
    f = open('data.csv', 'a')
    for key, value in sorted(d.items()):
        f.write(str(key) + ',' + str(value)[2:-2] + '\n')
    f.close()
    return '<h2>Ответ записан!</h2>'


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/stats')
def stats():
    with open('data.csv', 'r', encoding='utf-8') as f:
        text = f.read()
    men = len(re.findall('boys', text))
    women = len(re.findall('girls', text))
    gender_who = len(re.findall('other'), text)

    poz_react = len(re.findall('good'), text)
    neg_react = len(re.findall('bad'), text)
    neu_react = len(re.findall('neutral'), text)
    na_react = len(re.findall('react'), text)

    use_yes_one = len(re.findall('yesofcourse'), text)
    use_yes_two = len(re.findall('maybeyes'), text)
    use_no_one = len(re.findall('noofcourse'), text)
    use_no_two = len(re.findall('maybeno'), text)
    na_use = len(re.findall('use'), text)

    poz_need = len(re.findall('yep'), text)
    neg_need = len(re.findall('no'), text)
    na_need = len(re.findall('idk'), text)
    return render_template('stats.html', men=men, women=women, gender_who=gender_who, poz_react=poz_react,
                           neg_react=neg_react, neu_react=neu_react, na_react=na_react, use_yes_one=use_yes_one,
                           use_yes_two=use_yes_two, use_no_one=use_no_one, use_no_two=use_no_two, na_use=na_use,
                           poz_need=poz_need, neg_need=neg_need, na_need=na_need)


@app.route('/json')
def all_data():
    csvfile = open('data.csv', 'r')
    jsonfile = open('data.json', 'w')

    fieldnames = ("age", "city", "gender", "name", "need", "reaction", "usage")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    with open('data.json', 'r', encoding='utf-8') as f:
        json_str = f.read()
        return str(json_str)


if __name__ == '__main__':
    app.run(debug=True)
