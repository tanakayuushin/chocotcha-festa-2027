from PIL import Image, ImageDraw, ImageFont
import sys
import os
F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts')+'/'
dela=lambda s: ImageFont.truetype(F+'Dela.ttf', s)
zen=lambda s,w=900: ImageFont.truetype(F+'Zen%d.ttf'%w, s)
CHOCO=(90,42,23); INK=(74,28,15); RED=(227,23,26); CREAM=(255,244,230); PAPER=(255,253,249); PINK=(244,167,185); ORANGE=(243,154,30); MUTED=(112,88,78)
W,H=1200,630
im=Image.new('RGB',(W,H),PAPER); d=ImageDraw.Draw(im)
# 背景の丸
for (cx,cy,r,c) in [(80,80,150,(255,236,208)),(1110,70,90,(253,233,238)),(1120,560,170,(255,228,199)),(120,560,120,(255,236,208))]:
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=c)
# 枠
d.rounded_rectangle((20,20,W-20,H-20),radius=28,outline=CHOCO,width=4)
# 包装ストライプ（下端の細帯）
band=Image.new('RGB',(W-48,12),CREAM); bd=ImageDraw.Draw(band)
for x in range(-20,W,36):
    bd.polygon([(x,12),(x+10,0),(x+20,0),(x+10,12)],fill=RED)
    bd.polygon([(x+20,12),(x+30,0),(x+36,0),(x+26,12)],fill=PINK)
# ロゴ（原本をそのまま）
logo=Image.open('logo-icon-t.png').convert('RGBA').resize((440,440),Image.LANCZOS)
im.paste(logo,(58,96),logo)
d=ImageDraw.Draw(im)
X=560
# スタンプ
st='開催予定 ・ 入場無料'; f=zen(26)
tw=d.textlength(st,font=f)
d.rounded_rectangle((X+4,74+4,X+tw+44+4,74+50+4),radius=10,fill=RED)
d.rounded_rectangle((X,74,X+tw+44,74+50),radius=10,fill=(255,255,255),outline=RED,width=3)
d.text((X+22,74+9),st,font=f,fill=RED)
# 見出し
d.text((X,150),'バレンタインって、',font=dela(52),fill=CHOCO)
d.text((X,218),'こんなに楽しい。',font=dela(52),fill=RED)
d.text((X,298),'知らなかった味やお店、楽しみ方に出会う一日。',font=zen(25),fill=INK)
# 日付カード（入場券風：左に赤い半券、切り取り線、角にリボン）
cx0,cy0,cx1,cy1=X,350,1150,515; stub=118
card=Image.new('RGBA',(cx1-cx0+40,cy1-cy0+40),(0,0,0,0)); cd=ImageDraw.Draw(card)
ox,oy=10,10; w,h=cx1-cx0,cy1-cy0
cd.rounded_rectangle((ox,oy+7,ox+w,oy+h+7),radius=20,fill=RED)
cd.rounded_rectangle((ox-3,oy-3,ox+w+3,oy+h+3),radius=22,fill=CHOCO)
cd.rounded_rectangle((ox,oy,ox+w,oy+h),radius=19,fill=(255,255,255))
cd.rounded_rectangle((ox,oy,ox+stub,oy+h),radius=19,fill=(189,22,25)); cd.rectangle((ox+stub-20,oy,ox+stub,oy+h),fill=(189,22,25))
for y in range(oy+14,oy+h-10,12): cd.line([(ox+stub+1,y),(ox+stub+1,y+6)],fill=(138,74,44),width=3)
# リボン（右上の角）
rib=Image.new('RGBA',(220,26),(0,0,0,0)); rd=ImageDraw.Draw(rib)
rd.rectangle((0,0,220,26),fill=PINK); rd.rectangle((0,4,220,22),fill=RED)
rib=rib.rotate(-38,expand=True,resample=Image.BICUBIC)
ribmask=Image.new('L',card.size,0); ImageDraw.Draw(ribmask).rounded_rectangle((ox,oy,ox+w,oy+h),radius=19,fill=255)
layer=Image.new('RGBA',card.size,(0,0,0,0)); layer.paste(rib,(ox+w-125,oy-70),rib)
layer.putalpha(Image.composite(layer.getchannel('A'),Image.new('L',card.size,0),ribmask))
card=Image.alpha_composite(card,layer); cd=ImageDraw.Draw(card)
for (nx,ny) in [(ox+stub,oy-3),(ox+stub,oy+h+3)]:
    cd.ellipse((nx-13,ny-13,nx+13,ny+13),fill=CHOCO); cd.ellipse((nx-10,ny-10,nx+10,ny+10),fill=PAPER)
im.paste(card,(cx0-ox,cy0-oy),card); d=ImageDraw.Draw(im)
f=zen(22)
for i,ch in enumerate('開催予定'): d.text((cx0+stub//2-10,cy0+16+i*23),ch,font=zen(20),fill=(255,255,255))
d.rounded_rectangle((cx0+16,cy0+h-38,cx0+stub-16,cy0+h-10),radius=14,outline=(255,255,255),width=2)
d.text((cx0+26,cy0+h-34),'入場無料',font=zen(17),fill=(255,255,255))
bx=cx0+stub+26
d.text((bx+3,cy0+12+3),'2.14',font=dela(66),fill=PINK); d.text((bx,cy0+12),'2.14',font=dela(66),fill=CHOCO)
d.text((bx+d.textlength('2.14',font=dela(66))+14,cy0+44),'SUN',font=dela(26),fill=(189,22,25))
d.text((bx,cy0+98),'2027年2月14日（日）10:00〜20:00',font=zen(22,700),fill=INK)
d.text((bx,cy0+128),'こんこんパークを中心に計画中（山口市）',font=zen(21,700),fill=INK)
# 下のピル
pill='十人十色のバレンタイン'; f=zen(22); pw=d.textlength(pill,font=f)
d.rounded_rectangle((W-48-pw-40+5,545+5,W-48+5,545+46+5),radius=23,fill=PINK)
d.rounded_rectangle((W-48-pw-40,545,W-48,545+46),radius=23,fill=CHOCO)
d.text((W-48-pw-20,545+9),pill,font=f,fill=(255,255,255))


im.save(sys.argv[1],optimize=True)
