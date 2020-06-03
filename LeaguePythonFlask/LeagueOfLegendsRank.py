import requests

region = "NA1"
APIKey = "RGAPI-afc00d0b-be3f-4e46-bba6-2b26e5fbcf11"

def getSummonerInformation(summonerName):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def getSummonerRankedData(summonerID):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def mainFunction(summonerName):
    retrievedJson = getSummonerInformation(summonerName)
    summonerID = str(retrievedJson['id'])
    retrievedJsonRank =  getSummonerRankedData(summonerID)

    x = len(retrievedJsonRank)
    for n in range(0,x):
        queueType = retrievedJsonRank[n]['queueType']
        if queueType == "RANKED_SOLO_5x5":
            index = n
            break

    tier = retrievedJsonRank[index]['tier']
    rank = retrievedJsonRank[index]['rank'] 
    lp = retrievedJsonRank[index]['leaguePoints']
    wins = retrievedJsonRank[index]['wins']
    losses = retrievedJsonRank[index]['losses']  
    return {'tier': tier, 'rank': rank, 'lp': lp, 'wins': wins, 'losses': losses}

