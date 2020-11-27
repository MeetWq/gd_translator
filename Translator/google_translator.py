import requests
import json
from configparser import ConfigParser
from .translator import Translator


class GoogleTranslator(Translator):
    def __init__(self, lang_from, lang_to):
        super().__init__(lang_from, lang_to)
        self.name = 'google'
        config = ConfigParser()
        config.read(self.config_path)
        self.api_key = config['google']['api_key']

    def __translate__(self, text):
        params = {
            'q': text,
            'source': self.lang_from,
            'target': self.lang_to,
            'key': self.api_key
        }
        url = 'https://translation.googleapis.com/language/translate/v2'
        response = requests.get(url, params=params).text
        json_data = json.loads(response)
        result = json_data['data']['translations'][0]['translatedText']
        return result
