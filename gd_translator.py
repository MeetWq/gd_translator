import argparse
from Translator.baidu_translator import BaiduTranslator
from Translator.youdao_translator import YoudaoTranslator
from Translator.google_translator import GoogleTranslator


def gd_trasnlator(args):
    engine = args.engine
    source = args.source
    target = args.target
    text = args.text

    if text == '':
        return ''
    text = text.encode('gbk', 'ignore').decode('gbk', 'ignore')
    text = text.replace('- ', '')

    if engine == 'baidu':
        translator = BaiduTranslator(source, target)
    elif engine == 'youdao':
        translator = YoudaoTranslator(source, target)
    elif engine == 'google':
        translator = GoogleTranslator(source, target)
    else:
        return 'Error: Unknown engine'
    return translator.translate(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translator for goldendict')
    parser.add_argument('-e', '--engine', default='baidu', help='Translator engine')
    parser.add_argument('-s', '--source', default='en', help='Source language')
    parser.add_argument('-t', '--target', default='zh', help='Target language')
    parser.add_argument('text', help='Text to be translated')
    print(gd_trasnlator(parser.parse_args()))
