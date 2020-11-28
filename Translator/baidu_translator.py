import requests
import time
import hashlib
import json
from .translator import Translator


class BaiduTranslator(Translator):
    def __init__(self, lang_from, lang_to):
        super().__init__(lang_from, lang_to)
        self.name = 'baidu'
        self.app_id = self.config['baidu']['app_id']
        self.api_key = self.config['baidu']['api_key']

    def __translate__(self, text):
        salt = str(round(time.time() * 1000))
        sign_raw = self.app_id + text + salt + self.api_key
        sign = hashlib.md5(sign_raw.encode('utf8')).hexdigest()
        params = {
            'q': text,
            'from': self.lang_from,
            'to': self.lang_to,
            'appid': self.app_id,
            'salt': salt,
            'sign': sign
        }
        url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        response = requests.get(url, params=params).text
        json_data = json.loads(response)
        result = ''
        for res in json_data['trans_result']:
            result += res['dst'] + '\n'
        return result
