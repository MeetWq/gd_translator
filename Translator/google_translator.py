import requests
import json
from .translator import Translator


class GoogleTranslator(Translator):
    def __init__(self, lang_from, lang_to):
        super().__init__(lang_from, lang_to)
        self.name = 'google'
        self.api_key = self.config['google']['api_key']

    def detect_language(self, text):
        params = {
            'q': text,
            'key': self.api_key
        }
        url = 'https://translation.googleapis.com/language/translate/v2/detect'
        response = requests.get(url, params=params).text
        json_data = json.loads(response)
        lang = json_data['data']['detections'][0][0]['language']
        return lang

    def __translate__(self, text):
        if self.lang_from == 'auto':
            self.lang_from = self.detect_language(text)
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
