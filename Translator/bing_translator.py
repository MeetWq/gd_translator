import requests
import json
from .translator import Translator


class BingTranslator(Translator):
    def __init__(self, lang_from, lang_to):
        super().__init__(lang_from, lang_to)
        self.name = 'bing'
        self.region = self.config['bing']['region']
        self.api_key = self.config['bing']['api_key']

    def __translate__(self, text):
        params = {
            'to': self.lang_to
        }
        data = [{'Text': text}]
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.region
        }
        if self.lang_from != 'auto':
            params['from'] = self.lang_from
        url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
        response = requests.post(url, headers=headers, params=params, json=data).text
        json_data = json.loads(response)
        result = ''
        for res in json_data:
            result += res['translations'][0]['text'] + '\n'
        return result
