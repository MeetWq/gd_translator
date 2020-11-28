import requests
import time
import hashlib
import json
from .translator import Translator


class YoudaoTranslator(Translator):
    def __init__(self, lang_from, lang_to):
        super().__init__(lang_from, lang_to)
        self.name = 'youdao'
        self.app_id = self.config['youdao']['app_id']
        self.api_key = self.config['youdao']['api_key']

    def translate(self, query_text):
        if query_text == '':
            return ''
        salt = str(round(time.time() * 1000))
        sign_raw = self.app_id + query_text + salt + self.api_key
        sign = hashlib.md5(sign_raw.encode('utf8')).hexdigest()
        params = {
            'q': query_text,
            'from': self.lang_from,
            'to': self.lang_to,
            'appKey': self.app_id,
            'salt': salt,
            'sign': sign
        }
        base_url = 'https://openapi.youdao.com/api'
        response = requests.get(base_url, params=params).text
        json_data = json.loads(response)
        result = json_data['translation'][0]
        return result
