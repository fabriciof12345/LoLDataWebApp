from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import numpy as np
import LeagueOfLegendsRank as rank
import LeagueOfLegendsMatchHistory as mh

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def homePage():
    if request.method == "POST":
        user = request.form["nm"]
        return(redirect(url_for("user", usr = user)))
    return render_template("index.html")


@app.route("/summoner/<usr>")
def user(usr):
    '''usr is the username entered in the form
    can call usr from other functions'''
    tupleRank = rank.mainFunction(usr)
    player = f"{usr}"
    rankinfo = f"{tupleRank['tier'].title()} {tupleRank['rank']} {tupleRank['lp']} LP"
    wlratio = f"{tupleRank['wins']}W {tupleRank['losses']}L {np.round(100 * tupleRank['wins']/ (tupleRank['losses']+tupleRank['wins'] ),2)}%"
    matchHistory = mh.displayMatchHistory(usr)[0]
    kda = mh.displayMatchHistory(usr)[1]
    return render_template("summoner.html", user=player, rank=rankinfo, winloss=wlratio, matchHistory = matchHistory, kda = kda)

if __name__ == "__main__":
    app.run(debug = True)