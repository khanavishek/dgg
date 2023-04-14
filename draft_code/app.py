import random
import json

def definePlayers(): 
    playerInput = input("Who is playing? (Enter a comma seprated list of names): ")
    playerList = playerInput.strip().split(",")
    return playerList

def createWallets(playerList): 
    # session = open("session.txt", "") #creates room
    f = open("dareList.txt", "r").readlines()
    numDares = sum(1 for line in f if line.rstrip())
    
    
    numPlayers = len(playerList)
    dareIndices = [i for i in range(numDares)]
    random.shuffle(dareIndices)
    
    walletMap = {}
    for player in playerList:
        missions = []
        # print(dareIndices.pop())
        for i in range(6):
            x = dareIndices.pop(0)
            print(x)
            missions.append((f[x].strip(), "Not Attempted"))
        walletMap[player] = missions
    
    with open("room1.json", "w") as outfile:
        json.dump(walletMap, outfile)

            



if __name__ == "__main__":
    print ("Welcome to Don't Get Got!")
    # playerList = definePlayers()
    playerList = "Avishek, Brandon, Jeremy, Aditya, Vishal, Noah, Chris".strip().split(",")
    createWallets(playerList)