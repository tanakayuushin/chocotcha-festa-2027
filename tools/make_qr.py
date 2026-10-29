# チラシ用QRコードを生成する（トップページへ）。実行: python3 tools/make_qr.py .   （出力先 tools/qr/）
# 必要: pip install qrcode pillow。文字入り版は tools/fonts/Zen900.ttf, Zen700.ttf, Zen500.ttf が必要
import sys, os, qrcode, qrcode.image.svg
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont
root = sys.argv[1] if len(sys.argv) > 1 else '.'
out = os.path.join(root, 'tools', 'qr'); os.makedirs(out, exist_ok=True)
URL = 'https://chocotcha.jp/?utm_source=flyer&utm_medium=qr&utm_campaign=festa2027'
def make(ec, box, border, fill):
    q = qrcode.QRCode(error_correction=ec, box_size=box, border=border); q.add_data(URL); q.make(fit=True)
    return q.make_image(fill_color=fill, back_color='white').convert('RGB')
make(ERROR_CORRECT_H, 30, 4, 'black').save(f'{out}/qr-flyer-black.png')
make(ERROR_CORRECT_H, 30, 4, '#5a2a17').save(f'{out}/qr-flyer-choco.png')
q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4, image_factory=qrcode.image.svg.SvgPathImage); q.add_data(URL); q.make(fit=True)
q.make_image().save(f'{out}/qr-flyer.svg')
F = os.path.join(root, 'tools', 'fonts')
try:
    f1 = ImageFont.truetype(f'{F}/Zen900.ttf', 44); f2 = ImageFont.truetype(f'{F}/Zen700.ttf', 30); f3 = ImageFont.truetype(f'{F}/Zen500.ttf', 26)
except OSError:
    print('フォントが無いので文字入り版は作りません'); sys.exit(0)
qr = make(ERROR_CORRECT_H, 24, 2, '#5a2a17'); W = qr.width + 80; H = qr.height + 230
c = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(c)
d.rounded_rectangle((12, 12, W - 12, H - 12), radius=28, outline='#5a2a17', width=6)
for y, t, f, col in [(40, '公式サイトはこちら', f1, '#5a2a17'), (110 + qr.height + 8, 'やまぐちチョコっちゃ!!フェスタ 2027 公式サイト', f2, '#5a2a17'), (110 + qr.height + 56, 'chocotcha.jp', f3, '#70584e')]:
    d.text(((W - d.textlength(t, font=f)) / 2, y), t, fill=col, font=f)
c.paste(qr, ((W - qr.width) // 2, 110)); c.save(f'{out}/qr-flyer-card.png')
print('ok', out)
