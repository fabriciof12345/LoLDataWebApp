import requests
import time
start_time = time.time()
#print("My program took", time.time() - start_time, "to run")

region = "NA1"
APIKey = "RGAPI-dc6019f9-3c76-4b11-bb59-a1d11978716b"
summonerName = "Centillion"


def retrieveMatchHistory(region, APIKey):
    session = requests.session()
    encryptedID = session.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}').json()['accountId']
    response = session.get(f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{encryptedID}?api_key={APIKey}')
    lengthTotalMatchesFound = len(response.json()['matches'])
    totalMatches = []
    for x in range(lengthTotalMatchesFound):
        totalMatches.append(response.json()['matches'][x]['gameId'])
    print("My program took", time.time() - start_time, "to run")
    return totalMatches


def viewMatchHistoryParticipants(region,APIKey):
    session = requests.session()
    totalMatches = retrieveMatchHistory(region, APIKey)
    lastMatches = []
    for matchID in range(0,21):
        jsonFileURL = f'https://{region}.api.riotgames.com/lol/match/v4/matches/{str(totalMatches[matchID])}?api_key={APIKey}'
        response = session.get(jsonFileURL).json()['participantIdentities']
        allPlayers = {}
        for participantID in range(10):
            playerIdentity = response[participantID]['player']['summonerName']
            allPlayers.update({participantID: playerIdentity})
        lastMatches.append(allPlayers)
    print(lastMatches)
    print("My program took", time.time() - start_time, "to run")
    return lastMatches


viewMatchHistoryParticipants(region, APIKey)
