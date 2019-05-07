from PIL import Image, ImageDraw, ImageFont

# 背景作成
im = Image.new('RGB', (1280, 720), (255, 255, 255))
# 絵をかけるように引き渡す
draw = ImageDraw.Draw(im)

# 四角
draw.rectangle((0, 0, 200, 720), fill=(153,51,255), outline=(255, 255, 255))

# 線
draw.line((200, 350, 1280, 350), fill=(0, 0, 0), width=3)
draw.line((200, 550, 1280, 550), fill=(0, 0, 0), width=3)

# バツ
# draw.line((250, 500, 350, 400), fill=(255, 0, 0), width=23)
# draw.line((350, 500, 250, 400), fill=(255, 0, 0), width=23)

# 三角
# draw.polygon(((230, 530), (305, 380), (380, 530)), fill=(0, 230, 0), outline=(255, 255, 255))
# draw.polygon(((250, 520), (305, 405), (360, 520)), fill=(255, 255, 255), outline=(255, 255, 255))

# 丸
draw.ellipse((230, 380, 380, 530), fill=(255, 0, 51), outline=(255, 0, 51))
draw.ellipse((250, 400, 360, 510), fill=(255, 255, 255), outline=(255, 0, 51))



# フォント設定
title_font = ImageFont.truetype('./img/font/yasasisa.ttf', 128)
sub_title_font = ImageFont.truetype('./img/font/yasasisa.ttf', 72)
eng_title_font = ImageFont.truetype('./img/font/yasasisa.ttf', 52)
time_title_font = ImageFont.truetype('./img/font/yasasisa.ttf', 45)
infomation = ImageFont.truetype('./img/font/yasasisa.ttf', 62)
eng_infomation = ImageFont.truetype('./img/font/yasasisa.ttf', 32)
genin = ImageFont.truetype('./img/font/yasasisa.ttf', 45)
genin_infomation = ImageFont.truetype('./img/font/yasasisa.ttf', 32)

# 文字配置
draw.multiline_text((250,30), 'ラボ回線', fill=(0, 0, 0), font=title_font)
draw.multiline_text((250,165), '内部', fill=(0, 0, 0), font=sub_title_font)
draw.multiline_text((250,250), 'LAB=01', fill=(0, 0, 0), font=eng_title_font)
draw.multiline_text((400,370), '16:30', fill=(0, 0, 0), font=time_title_font)
draw.multiline_text((400,420), '疎通不可', fill=(0, 0, 0), font=infomation)
draw.multiline_text((400,500), 'BAD Communication', fill=(0, 0, 0), font=eng_infomation)
draw.multiline_text((250,610), '原因:', fill=(0, 0, 0), font=genin)
draw.multiline_text((400,610), 'パケットループ検知', fill=(0, 0, 0), font=genin)



# 図形のセーブ
im.save('./img/pillow_imagedraw.jpg', quality=100)