import os
import requests
os.system('clear')


def get_url(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'
    response = requests.get(url=url)
    data = response.json()
    return data

def get_location(id):
    character = get_url(id)
    for i in character.keys():
        if i == 'location':
            name_location = character['location']['name']
            url_location = character['location']['url']
            if url_location not in '':
                location_responce = requests.get(url_location)
                data = location_responce.json()
                info = f"""Название локации: {name_location}
Тип локации: {data['type']}
Измерение локации: {data['dimension']}
Дата создания локации: {data['created']}"""
                return info
            else:
                info = f"""Название локации: {name_location}
Тип локации: Unknown
Измерение локации: Unknown
Дата создания локации: Unknown""" 
                return info

def get_character(id):
    if id <= 826:
        character = get_url(id)
        info = f"""
Айди персонажа: {character['id']}
Имя персонажа: {character['name']}
Пол персонажа: {character['gender']}
Раса: {character['species']}
Жизненное положение: {character['status']}
Личность: {character['type']}
Дата создание: {character['created']}

{get_location(id)}"""
        return info
    else:
        return 'Не правельный ID персонажа'


id_characters = int(input("Введи айди персонажа: "))

print(get_character(id_characters))




# try:
#     a = int(input('Введите цифру: '))
# except ValueError:
#     print('Invalid Тут нужно вводить цифру')
# else:
#     print("Ok")
# finally:
#     print('123c 123')

    # a = int(input('Введите цифру: '))

# try:
#     with open('image/a.txt', 'r') as f:
#         f.read()

# except FileNotFoundError:
#     os.mkdir('image')
#     os.system('touch image/a.txt')
#     with open('image/a.txt', 'r') as f:
#         f.read()
# else:
#     print('все было окей')



    


































