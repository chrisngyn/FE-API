import requests
from bs4 import BeautifulSoup


def execute():
    response = requests.get('https://serenesforest.net/blazing-sword/characters/recruitment')
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    character_list = {}

    for character in characters[1:]:
        data = character.text.split('\n')
        k = data[1]

        if len(data) < 6:
            v = data[4]
        else:
            v = data[5]

        character_list[k] = v

    return character_list
