import re

# Formats the string from steamdb to a list containing only the games titles
def txtToList(games):
    unformatedGamesVector = re.split("\s{2,}", games)
    
    formatedGamesList = []

    for game in unformatedGamesVector:
        texts = game.split("\t")
        
        formatedGamesList.append(texts[0])
        
    return formatedGamesList

def listToHtmlLi(gamesList):
    html = ""
    
    for game in gamesList:
        html = html + "<li>" + game + "</li>" + "\n"
    
    return html


games = open("games.txt", "r")
gamesString = games.read()
games.close()

gamesList = txtToList(gamesString)
gamesHtml = listToHtmlLi(gamesList)

print(gamesHtml)

f = open("games_list.txt", "w")
f.write(gamesHtml)
f.close()



