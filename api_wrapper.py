import requests

class PokeApi:
    BASE_URL = 'https://pokeapi.co/api/v2/'
    
    def find_pokemon_by_number(self, number):
        url = f"{self.BASE_URL}pokemon/{number}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()