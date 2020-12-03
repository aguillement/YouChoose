import json
import requests

from settings import AUTHORIZATION_IGDB, TWITCH_CLIENT_ID

def get_game_picture(game_name):
    """
    Returns the url image of game parameter.
    """

    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': 'Bearer {}'.format(AUTHORIZATION_IGDB),
        'Accept': 'application/json',
    }

    data = 'search "{}"; fields screenshots.*;'.format(game_name)

    response = requests.post('https://api.igdb.com/v4/games', headers=headers, data=data)
    
    data = json.loads(response.content)
    
    # replace t_thumb with t_1080p
    image_url = data[0]["screenshots"][0]["url"].replace("t_thumb", "t_1080p")

    return "https:{}".format(image_url)

