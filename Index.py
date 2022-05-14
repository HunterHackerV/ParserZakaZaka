from bs4 import BeautifulSoup
import requests as rq
import json
url = "https://zaka-zaka.com/search/sort/sale.desc/offset/"
def mainDef():
    counter = 0
    HtmlCode = ""
    while True:
        tempHtmlCode = rq.get(url + str(counter)).text
        ifBool = BeautifulSoup(tempHtmlCode, "html.parser").find("div", class_="search-results").text.replace("\n", "").replace(" ", "") != "Показатьпредыдущие"
        if ifBool:
            HtmlCode += str(BeautifulSoup(tempHtmlCode, "html.parser").find("div", class_="search-results"))
            counter += 10
            print(counter)
        else:
            break
    file = open("result.txt", "w", encoding='utf-8')
    file.writelines(HtmlCode)
    file.close()
def filter():
    file = open("result.txt", "r", encoding='utf-8')
    games = {}
    games["game"] = []
    htmlcode = BeautifulSoup(file.read(), "html.parser").findAll("a", class_="game-block")
    for game in htmlcode:
        games["game"].append({
            "Href" : game["href"],
            "Name" : game.find("div", class_="game-block-name").text,
            "Price": game.find("div", class_="game-block-price").text
        })
    with open('data.json', 'w') as outfile:
        json.dump(games, outfile)
if __name__ == '__main__':
    filter()