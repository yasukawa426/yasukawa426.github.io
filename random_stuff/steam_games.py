# This script will load all my steam games and then format it into html <li> tags
import requests
import steam_secrets


# Load my steam owned games directly from their api.
# Return as tuple : (games count, list[{name, playtime}])
def loadGamesFromApi() -> tuple[int, list[dict]]:
    """Load all my owned steam games directly from steam api. Needs the file `steam_secrets.py` to get all the secrets.

    Returns:
        `tuple[int, list[dict]]`: A tuple contaning the number of owned games and a list of dict: `[{name: str, playtime: int,}, ...]`
    """

    games_response: dict = requests.get(
        f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={steam_secrets.STEAM_WEB_API_KEY}&steamid={steam_secrets.STEAM_ID}&include_appinfo=true&format=json"
    ).json()["response"]

    # number of owned games.
    game_count: int = games_response["game_count"]
    owned_games: dict = games_response["games"]

    # list of games names and their playtime
    # [
    #     {
    #         "name" : "Game Name"
    #         "playtime" : Hours
    #     },
    # ]
    formated_games: list[dict] = []

    for game in owned_games:
        formated_games.append(
            {
                "name": game["name"],
                # the request return the time in minutes, we convert it to hours and then round with one decimial digit.
                "playtime": round(game["playtime_forever"] / 60, 1),
            }
        )

    return game_count, formated_games


# Expects a list of strin
# Turns a list of dicts into a string containig html elements.
# Each line will be the "<li>dict.name - dict.playtime hours </li>"
# Returns the generated html.
def formatGameListToHtml(gamesList: list[dict]) -> str:
    """
    Expects a list of dictionaries - `[{name: str, playtime: int,}, ...]`.
    Turns the list of dicts into a string containig html elements.
    Each line will be: ``<li>dict.name - dict.playtime h played </li>``
    <br>
    Returns the generated html.

        Returns:
            str - The generated html containing "li" elements with game name and playtime.
    """

    html = ""

    for game in gamesList:
        html = html + f"<li>{game["name"]} - {game["playtime"]}h played.</li>" + "\n"

    return html


if __name__ == "__main__":
    pass
    # games = open("games.txt", "r")
    # gamesString = games.read()
    # games.close()

    # gamesList = txtToList(gamesString)

    # print(gamesList)
    # gamesHtml = listToHtmlLi(gamesList)

    # print(gamesHtml)

    # f = open("games_list.txt", "w")
    # f.write(gamesHtml)
    # f.close()
