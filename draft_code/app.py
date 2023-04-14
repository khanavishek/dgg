import random
import json

def definePlayers(): 
    playerInput = input("Who is playing? (Enter a comma seprated list of names): ")
    playerList = playerInput.strip().split(",")
    return playerList

def createWallets(playerList): 
    f = open("dareList.txt", "r").readlines()
    numDares = sum(1 for line in f if line.rstrip())
    dareIndices = [i for i in range(numDares)]
    random.shuffle(dareIndices)
    
    walletMap = {}
    for player in playerList:
        player = player.strip()
        missions = []
        for i in range(6):
            x = dareIndices.pop(0)
            missions.append((f[x].strip(), "Not Attempted"))
        walletMap[player] = missions
    
    with open("room1.json", "w") as outfile:
        json.dump(walletMap, outfile)

def failedDare(playerName, dare, wallets, roomName): 

    toIndex = wallets[playerName]
    ind = toIndex.index([dare, "Not Attempted"])
    wallets[playerName][ind] = [dare, "Failed"]

    # print(wallets[playerName])
    return wallets

def accomplishedDare(playerName,dare,wallets,roomName):
    toIndex = wallets[playerName]
    ind = toIndex.index([dare, "Not Attempted"])
    wallets[playerName][ind] = [dare, "Complete"]
    # print(wallets[playerName])
    return wallets


            

def playGame(roomName):
    f = open(roomName)
    wallets = json.load(f)
    playerAuth = input("Which player are you? ").strip()
    for i in range(len(wallets[playerAuth])):
        print (i + 1, ". ", wallets[playerAuth][i][0], " - ", wallets[playerAuth][i][1])
    
    while(True):
        takeInput = input("Did you complete a dare?: ")
        if takeInput != "end":
            inputList = takeInput.strip().split("-")
            if inputList[1].strip() == "yes":
                wallets = accomplishedDare(playerAuth, inputList[0].strip(), wallets, roomName)
            else: 
                wallets = failedDare(playerAuth, inputList[0].strip(), wallets, roomName)
            for i in range(len(wallets[playerAuth])):
                print (i + 1, ". ", wallets[playerAuth][i][0], " - ", wallets[playerAuth][i][1])
        else:
            break

if __name__ == "__main__":
    print ("Welcome to Don't Get Got!")
    # playerList = definePlayers()
    playerList = "Avishek, Brandon, Jeremy, Aditya, Richie".strip().split(",")
    createWallets(playerList)
    playGame("room1.json")


