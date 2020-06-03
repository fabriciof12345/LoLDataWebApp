import requests
import time
start_time = time.time()
#print("My program took", time.time() - start_time, "to run")

region = "NA1"
APIKey = "RGAPI-afc00d0b-be3f-4e46-bba6-2b26e5fbcf11"

def retrieveMatchHistory(summonerName):
    session = requests.session()
    encryptedID = session.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}').json()['accountId']
    response = session.get(f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{encryptedID}?api_key={APIKey}')
    lengthTotalMatchesFound = len(response.json()['matches'])
    totalMatches = []
    for x in range(lengthTotalMatchesFound):
        totalMatches.append(response.json()['matches'][x]['gameId'])
    return totalMatches


def displayMatchHistory(summonerName):
    session = requests.session()
    totalMatches = retrieveMatchHistory(summonerName)
    lastMatches = []      
    kdaTracker = []
    for matchID in range(0,10):
        jsonFileURL = f'https://{region}.api.riotgames.com/lol/match/v4/matches/{str(totalMatches[matchID])}?api_key={APIKey}'
        response = session.get(jsonFileURL).json()['participantIdentities']
        allPlayers = [session.get(jsonFileURL).json()['teams'][0]['win']]
        kda = session.get(jsonFileURL).json()['participants']
        for participantID in range(10):
            allPlayers.append(response[participantID]['player']['summonerName'])
            killDeathAssist = f"{kda[participantID]['stats']['kills']}/{kda[participantID]['stats']['deaths']}/{kda[participantID]['stats']['assists']}"
            kdaTracker.append(killDeathAssist)
        lastMatches.append(allPlayers)
    print("the displayMatchHistoryParticipants function took", time.time() - start_time, "seconds to run")
    return lastMatches, kdaTracker


def mhFast(summonerName):
    session = requests.session()


#print(retrieveMatchHistory(summonerName))

print(displayMatchHistory("fabricio12345"))