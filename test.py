# ファイルを開くために 'with' ステートメントを使用します。
# './test.txt' は開きたいファイルの名前です。
with open('./test.txt') as f:
    # ファイルからすべての行を読み込み、'lines' 変数にリストとして格納します。
    lines = f.readlines()

    # with ステートメントを使っているため、ファイルを閉じる処理は不要です。
    # f.close()

    # 翻訳機能を持つ Translator クラスのインスタンスを作成します。
    translator = Translator()

    # 'lines' 内の各行に対して繰り返し処理を行います。
    for line in lines:
        # Translator インスタンスの 'translate' メソッドを使って、
        # 対象の行を日本語 (dest="ja") に翻訳し、結果を 'translated' 変数に格納します。
        translated = translator.translate(line, dest="ja")

        # 翻訳前の行を表示します。
        print(line)  # 翻訳したい文章

        # 翻訳後の行を表示します。
        print(translated.text)  # 翻訳後の文章
