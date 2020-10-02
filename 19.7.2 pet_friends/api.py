import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    """API библиотека к PetFriends"""
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):
        """Функция делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        с уникальным ключем пользователя с указанными email и password"""

        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status,result


    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком наденных питомцев, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо 'my_pets' - получить список
        собственных питомцев"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
