## gd_translator

用于 Goldendict 的翻译脚本

### Requirements

```bash
pip install requests
```

### Usage

将 `config.example.ini` 重命名为 `config.ini`， 并改为自己的 API KEY

```bash
usage: gd_translator.py [-h] [-e ENGINE] [-s SOURCE] [-t TARGET] text

Translator for goldendict

positional arguments:
  text                  Text to be translated

optional arguments:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        Translator engine
  -s SOURCE, --source SOURCE
                        Source language
  -t TARGET, --target TARGET
                        Target language
```

### Engines

目前使用了 百度、有道、谷歌、微软  的接口，需要自行申请 API KEY

| 引擎名称 | 说明 | 免费额度 | 链接 |
| - | - | - | - |
| baidu | 百度通用翻译 | 每月前200万个字符免费 | [链接](https://api.fanyi.baidu.com/product/11) |
| youdao | 有道智云文本翻译 | 新用户50元体验金 | [链接](https://ai.youdao.com/product-fanyi-text.s) |
| google | Google Cloud Translation 基本版 | 每月前50万个字符免费 | [链接](https://cloud.google.com/translate?hl=zh-CN) |
| bing | Microsoft Azure Translator | 每月前200万个字符免费 | [链接](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/) |

### Goldendict

配置实例：

![](Example/goldendict.png)

