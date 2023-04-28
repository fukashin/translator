from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#このプログラムはPDFを作成するプログラムです。
output_file = "test_pdf.pdf"

# ページサイズを指定し、PDFのキャンバスを作成
c = canvas.Canvas(output_file, pagesize=letter)

# フォントとサイズを指定
c.setFont("Helvetica", 12)

# テキストを描画する位置を指定（x, y）
c.drawString(50, 750, "Hello, this is a test PDF document.")

# ページを追加して、キャンバスに描画
c.showPage()

# PDFファイルを保存
c.save()
