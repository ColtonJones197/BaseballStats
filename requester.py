import requests as rq


class statRequester:
    # Sends and recieves API requests

    hostAddress = 'http://lookup-service-prod.mlb.com'

    playerSuffix =
    '/json/named.search_player_all.bam?sport_code=\'mlb\''

    playerSw = '&active_sw={active_sw}'

    playerName = "&name_part={name_part}"

    # Active players defaults to no
    def __init__(self, baseAddress, activePlayers=''):
        self.base = baseAddress
        if activePlayers == '':
            playerSuffix = playerSuffix + playerName

    def getPlayer(self, playerNumber):
