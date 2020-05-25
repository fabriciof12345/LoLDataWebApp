from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import LeagueOfLegendsRank as rank
#import LeagueOfLegendsMatchHistory as mh

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
    print(tupleRank)
    #text = f"Your rank is {tupleRank['tier']} {tupleRank['rank']}"
    #othertext = f"{tupleRank['lp']} {tupleRank['wins']} {tupleRank['losses']}"
    player = f"{usr}"
    rankinfo = f"Your rank is {tupleRank['tier']} {tupleRank['rank']} {tupleRank['lp']} LP"
    wlratio = f"{tupleRank['wins']}W {tupleRank['losses']}L"

    return render_template("summoner.html", user=player, rank=rankinfo, winloss=wlratio)


if __name__ == "__main__":
    app.run(debug = True)