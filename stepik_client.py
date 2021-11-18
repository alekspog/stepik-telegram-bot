# Run with Python 3
import requests
from requests import api

api_host = 'https://stepik.org'

class Stepik():

    def __init__(self, client_id: str, client_secret: str) -> None:
        client_id = client_id
        client_secret = client_secret
        # 2. Get a token
        auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        response = requests.post('https://stepik.org/oauth2/token/',
                                data={'grant_type': 'client_credentials'},
                                auth=auth)
        self.token = response.json().get('access_token', None)
        if not self.token:
            print('Unable to authorize with provided credentials')
            exit(1)

    def fetch_object(self, obj_class, obj_id):
        api_url = '{}/api/{}s/{}'.format(api_host, obj_class, obj_id)
        response = requests.get(api_url,
                                headers={'Authorization': 'Bearer ' + self.token}).json()
        return response['{}s'.format(obj_class)][0]

    def fetch_object_with_params(self, obj_class, params):
        api_url = '{}/api/{}s?{}'.format(api_host, obj_class, params)
        response = requests.get(api_url,
                                headers={'Authorization': 'Bearer ' + self.token}).json()
        return response['{}s'.format(obj_class)]
