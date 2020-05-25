import requests

region = "NA1"
APIKey = "RGAPI-dc6019f9-3c76-4b11-bb59-a1d11978716b"

def getSummonerInformation(region, summonerName, APIKey):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def getSummonerRankedData(region, summonerID, APIKey):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def mainFunction(summonerName):
    retrievedJson = getSummonerInformation(region, summonerName, APIKey)
    summonerID = str(retrievedJson['id'])
    retrievedJsonRank =  getSummonerRankedData(region, summonerID, APIKey)

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

mainFunction("fabricio12345")