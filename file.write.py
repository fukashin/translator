from deep_translator import GoogleTranslator
import os

# 翻訳元のファイル名と翻訳後のファイル名を指定
source_file = "english_document.txt"
translated_file = "japanese_document.txt"

# 翻訳先の言語を定義（この場合は日本語）
target_language = "ja"

# 翻訳元のファイルを開く
with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 翻訳後のテキストを格納するリストを作成
translated_lines = []

# 各行を翻訳してリストに追加
for line in lines:
    translated_text = GoogleTranslator(source='en', target=target_language).translate(text=line)
    translated_lines.append(translated_text)

# 翻訳後のファイルに翻訳されたテキストを書き込む
with open(translated_file, 'w', encoding='utf-8') as f:
    for line in translated_lines:
        f.write(line + os.linesep)
