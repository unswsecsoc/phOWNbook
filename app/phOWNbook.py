#!/usr/bin/env python3
# Zachery Ellis (Top Hat) - 9 Feb 2019
# Challenge for SecSoc o-week ctf 2019

from flask import Flask, render_template, request
# T1dF RUt7 R290 dGEt Qi1T bjNB a3kt Q2hA cmxp ZS1T bjNB a3l9
FLAG = 'OWEEK{cASe_IssUeS_AlWaYs_rEmiNd_ME_oF_sPoNGeBoB}'
PORT = 9090
app = Flask(__name__)

phOWNbook = {}
phOWNbook["administrator"] = ["Zero Cool", "thementor@example.com", FLAG, "A secret? 1/11 - T1dF"]
phOWNbook["john"] = ["John Smith", "jsmith@example.com", "Secretly likes Java", "A secret? Hmm, maybe, but not here."]
phOWNbook["jane"] = ["Jane Doe", "jdoe@example.com", "Once beat Chuck Norris in a fight", "A secret? Hmm, maybe, but not here."]
phOWNbook["zac"] = ["Zachery Ellis", "zac@unswsecurity.com", "Has coffee rather than blood running through veins - Believes this fact is equivalent to a personality - Writes ctf challenges in third person", "2/11 - RUt7"]
phOWNbook["viv"] = ["Vivian Dang", "viv@unswsecurity.com", "DNA testing suggests she may have been bitten by a radioactive kitten - like spiderman but meows", "3/11 - R290"]
phOWNbook["vincent"] = ["Vincent Chen", "vincent@unswsecurity.com", "When not gaming, can be found participating in PC soc activities", "4/11 - dGEt"]
phOWNbook["joshua"] = ["Joshua Kwong", "joshua@unswsecurity.com", "Rock climber & arc whisperer, not to be confused with rock whisperer", "5/11 - Qi1T"]
phOWNbook["michael"] = ["Michael Yoo", "michael@unswsecurity.com", "In charge of the numbers. We suspect he may just be a whole bunch of numbers in the shape of a human person", "6/11 - bjNB"]
phOWNbook["eric"] = ["Eric Nguyen", "eric@unswsecurity.com", "Currently planning a series of fortunate events", "7/11 - a3kt"]
phOWNbook["penny"] = ["Penny ???", "?????????", "Elusive, mysterious, some claim she can walk through walls", "8/11 - Q2hAc"]
phOWNbook["melena"] = ["Melana", "melena@unswsecurity.com", "Ok Melana, will I need an umbrella today?", "9/11 - mxpZS"]
phOWNbook["andrew"] = ["arc", "andrewc@unswsecurity.com", "*To the tune of bob the builder theme* Andrew Carmichael, can he hack it? Andrew Carmichael, yes he can.", "10/11 - 1TbjN"]
phOWNbook["flora"] = ["Flora Li", "flora@unswseucurity.com", "Requires plenty of water and sunlight, not to be confused with fauna@unswsecurity.com", "11/11 - Ba3l9"]


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