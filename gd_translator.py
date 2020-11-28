import sys
import argparse
from Translator.baidu_translator import BaiduTranslator
from Translator.youdao_translator import YoudaoTranslator
from Translator.google_translator import GoogleTranslator


def main():
    parser = argparse.ArgumentParser(description='Translator for goldendict')
    parser.add_argument('-e', '--engine', default='baidu', help='Translator engine')
    parser.add_argument('-s', '--source', default='auto', help='Source language')
    parser.add_argument('-t', '--target', default='zh', help='Target language')
    parser.add_argument('text', help='Text to be translated')
    [engine, source, target, text] = vars(parser.parse_args()).values()

    engines = {
        'google': GoogleTranslator,
        'baidu': BaiduTranslator,
        'youdao': YoudaoTranslator
    }
    if engine in engines.keys():
        translator = engines[engine](source, target)
        result = translator.translate(text)
        sys.stdout.buffer.write(result.encode(sys.stdout.encoding, 'ignore'))
    else:
        print('Error: Unknown engine')


if __name__ == '__main__':
    main()
