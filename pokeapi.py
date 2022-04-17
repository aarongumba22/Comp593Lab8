import requests

def get_pokemon_info(name):
    """
    Gets info about a specified pokemon 
    :para, name: Pokemon name
    :return: Dictionary of pokemon info
    
    
    """
    print('Getting Pokemon Info...', end='')
    
    url="https://pokeapi.co/api/v2/pokemon/" + name
    resp_msg = requests.get(url)
    
    if resp_msg.status_code == 200:
        print('success')
        return resp_msg.json()
    
    else:
        print('failed. Code', resp_msg.status_code)
        print("That's not a pokemon, Please try another name")
        return
    
    