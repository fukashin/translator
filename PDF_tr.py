import pdfplumber
from deep_translator import GoogleTranslator
import os

#pip install pdfplumber deep-translator
#pip install deep-translator

# 翻訳元のPDFファイル名、出力フォルダ名、翻訳後のテキストファイル名を指定
source_file = "test_pdf.pdf"
output_folder = "translated_pdf"
translated_file = "japanese_pdf_document.txt"

# 翻訳先の言語を定義（この場合は日本語）
target_language = "ja"

# 出力フォルダが存在しない場合、作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 翻訳後のファイルのパスを生成
translated_file_path = os.path.join(output_folder, translated_file)

# PDFファイルを開く
with pdfplumber.open(source_file) as pdf:
    # 各ページのテキストを格納するリストを作成
    all_text = []

    # PDFの各ページを処理
    for page in pdf.pages:
        # ページからテキストを抽出
        text = page.extract_text()
        all_text.append(text)

# テキストを翻訳して、翻訳後のテキストを格納するリストを作成
translated_lines = []

# 全てのテキストを翻訳し、リストに追加
for text in all_text:
    # GoogleTranslatorを使って翻訳を実行
    # source: 翻訳元言語、target: 翻訳先言語、text: 翻訳したいテキスト
    translated_text = GoogleTranslator(source='en', target=target_language).translate(text=text)
    translated_lines.append(translated_text)

# 翻訳後のファイルに翻訳されたテキストを書き込む
with open(translated_file_path, 'w', encoding='utf-8') as f:
    for line in translated_lines:
        f.write(line + os.linesep)
