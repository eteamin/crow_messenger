import requests


class Messenger(object):
    def __init__(self, text, token, receiving_channel):
        self.token = token
        self.text = text
        self.receiving_channel = receiving_channel
	self.crow_api = 'http://crow.farakav.com/api/message'

        self.message = {
                'token': self.token,
                'text': self.text,
                'channel': self.receiving_channel
        }

    def deliver(self):
        response = requests.post(self.crow_api, json=self.message)
        return response.json()
