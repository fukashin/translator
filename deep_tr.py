#参考URL
#https://github.com/nidhaloff/deep-translator
#https://laboratory.kazuuu.net/translation-in-python-with-deep-translator/

# GoogleTranslatorをインポート
from deep_translator import GoogleTranslator

# 翻訳先の言語を定義（この場合は日本語）
target_language = "ja"

# ファイルを開いてテキストを読み込む
with open('./test.txt') as f:
    # ファイルから1行ずつ読み込む
    lines = f.readlines()

    # 各行を翻訳して表示する
    for line in lines:
        # GoogleTranslatorを使って翻訳を実行
        # source: 翻訳元言語、target: 翻訳先言語、text: 翻訳したいテキスト
        translated_text = GoogleTranslator(source='en', target=target_language).translate(text=line)

        # 翻訳されたテキストを表示
        print(translated_text)