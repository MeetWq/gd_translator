import os
import sys
import traceback


class Translator(object):
    def __init__(self, lang_from, lang_to):
        self.name = ''
        self.lang_to = lang_to
        self.lang_from = lang_from
        self.config_path = os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0], 'config.ini')

    def translate(self, text):
        try:
            text = self.__translate__(text)
        except:
            return 'Error occurred in {} translator:\n{}'.format(self.name, traceback.format_exc())
        return text

    def __translate__(self, text):
        return text
