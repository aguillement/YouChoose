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

    request_query = 'search "{}"; fields screenshots.*;'.format(game_name)

    response = requests.post('https://api.igdb.com/v4/games', headers=headers, data=request_query)
    data = json.loads(response.content)
    
    # Replace t_thumb with t_1080p, to get bigger image
    image_url = data[0]["screenshots"][0]["url"].replace("t_thumb", "t_1080p")

    return "https:{}".format(image_url)

