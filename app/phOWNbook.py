#!/usr/bin/env python3
# Zachery Ellis (Top Hat) - 9 Feb 2019
# Challenge for SecSoc o-week ctf 2019

from flask import Flask, render_template, request

FLAG = 'OWEEK{cASe_IssUeS_AlWaYs_rEmiNd_ME_oF_sPoNGeBoB}'
PORT = 9090
app = Flask(__name__)

phOWNbook = {}
phOWNbook["administrator"] = ["Zero Cool", "thementor@example.com", FLAG]
phOWNbook["john"] = ["John Smith", "jsmith@example.com", "Secretly likes Java"]
phOWNbook["jane"] = ["Jane Doe", "jdoe@example.com", "Once beat big bird in a fight"]
phOWNbook["zac"] = ["Zachery Ellis", "zac@unswsecurity.com", "Has coffee rather than blood running through veins - Believes this fact is equivalent to a personality - Writes ctf challenges in third person"]
phOWNbook["viv"] = ["Vivian Dang", "viv@unswsecurity.com", "DNA testing suggests she may have been bitten by a radioactive kitten - like spiderman but meows"]
phOWNbook["vincent"] = ["Vincent Chen", "vincent@unswsecurity.com", "When not gaming, can be found participating in PC soc activities"]
phOWNbook["joshua"] = ["Joshua Kwong", "joshua@unswsecurity.com", "Rock climber & arc whisperer, not to be confused with rock whisperer"]
phOWNbook["michael"] = ["Michael Yoo", "michael@unswsecurity.com", "In charge of the numbers. We suspect he may just be a whole bunch of numbers in the shape of a human person"]
phOWNbook["eric"] = ["Eric Nguyen", "eric@unswsecurity.com", "Eventful!"]
phOWNbook["penny"] = ["Penny ???", "?????????", "Elusive, mysterious, some claim she can walk through walls"]
phOWNbook["melana"] = ["Melana", "melana@unswsecurity.com", "Ok Melana, will I need an umbrella today?"]
phOWNbook["andrew"] = ["arc", "andrewc@unswsecurity.com", "*To the tune of bob the builder theme* Andrew Carmichael, can he hack it? Andrew Carmichael, yes he can."]
phOWNbook["flora"] = ["Flora Li", "flora@unswseucurity.com", "Requires plenty of water and sunlight, not to be confused with fauna@unswsecurity.com"]


def do_search(search):
    search = search.lower()
    if search in phOWNbook:
        return (phOWNbook[search])
    return()

@app.route('/', methods=['GET','POST'])
def main_page():
    if request.method == 'POST':
        search = request.form.get("username").strip()
        if search.isupper():
            search = search.lower()
        if search == "administrator":
            search = ""
        return render_template('home.html', searchTerm="You searched for: '" + search + "'", results=do_search(search), msg="No Results")
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = '\x8ff\x90T\xc4\xdd\x98d\x8d#'
    app.run(debug=True, use_reloader=True, port=PORT)