from PIL import Image, ImageDraw, ImageFont
import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数読み込み
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

FONT_DIR = os.environ.get("FONT_DIR")
SAVE_SRC = os.environ.get("SAVE_SRC")
FONT = os.environ.get("FONT")
R = int(os.environ.get("R"))
G = int(os.environ.get("G"))
B = int(os.environ.get("B"))
LAN_NAME = os.environ.get("LAN_NAME")
IP_ADDR = os.environ.get("IP_ADDR")
HOST_NAME = os.environ.get("HOST_NAME")
LEVEL = os.environ.get("LEVEL")
TIME = os.environ.get("TIME")
LEVEL_PING = os.environ.get("LEVEL_PING")
LEVEL_PING_ENG = os.environ.get("LEVEL_PING_ENG")
LEVEL_INFO = os.environ.get("LEVEL_INFO")


def main():
    save_point = make_pic()
    print(save_point)
    print("Done!")


def make_pic():
    # フォント設定
    yasasisa = FONT_DIR + FONT
    # 出力
    save_src = SAVE_SRC + str(datetime.datetime.utcnow()) + ".png"
    
    # 背景作成
    im = Image.new("RGB", (1280, 720), (255, 255, 255))
    # 絵をかけるように引き渡す
    draw = ImageDraw.Draw(im)
    # 四角
    draw.rectangle((0, 0, 200, 720), fill=(R,G,B), outline=(255, 255, 255))

    # 線
    draw.line((200, 350, 1280, 350), fill=(0, 0, 0), width=3)
    draw.line((200, 550, 1280, 550), fill=(0, 0, 0), width=3)

    # 上から☓、△、○、☓
    if LEVEL == "WARN":
        draw.line((250, 500, 350, 400), fill=(255, 0, 0), width=23)
        draw.line((350, 500, 250, 400), fill=(255, 0, 0), width=23)
    elif LEVEL == "INFO":
        draw.polygon(((230, 530), (305, 380), (380, 530)), fill=(0, 230, 0), outline=(255, 255, 255))
        draw.polygon(((250, 520), (305, 405), (360, 520)), fill=(255, 255, 255), outline=(255, 255, 255))
    elif LEVEL == "OK":
        draw.ellipse((230, 380, 380, 530), fill=(255, 0, 51), outline=(255, 0, 51))
        draw.ellipse((250, 400, 360, 510), fill=(255, 255, 255), outline=(255, 0, 51))
    else:
        draw.line((250, 500, 350, 400), fill=(255, 0, 0), width=23)
        draw.line((350, 500, 250, 400), fill=(255, 0, 0), width=23)
    
    # フォント設定
    title_font = ImageFont.truetype(yasasisa, 128)
    sub_title_font = ImageFont.truetype(yasasisa, 72)
    eng_title_font = ImageFont.truetype(yasasisa, 52)
    time_title_font = ImageFont.truetype(yasasisa, 45)
    infomation = ImageFont.truetype(yasasisa, 62)
    eng_infomation = ImageFont.truetype(yasasisa, 32)
    genin = ImageFont.truetype(yasasisa, 45)
    genin_infomation = ImageFont.truetype(yasasisa, 32)

    # 文字配置
    draw.multiline_text((250,30), LAN_NAME, fill=(0, 0, 0), font=title_font)
    draw.multiline_text((250,165), IP_ADDR, fill=(0, 0, 0), font=sub_title_font)
    draw.multiline_text((250,250), HOST_NAME, fill=(0, 0, 0), font=eng_title_font)
    draw.multiline_text((400,370), TIME, fill=(0, 0, 0), font=time_title_font)
    draw.multiline_text((400,420), LEVEL_PING, fill=(0, 0, 0), font=infomation)
    draw.multiline_text((400,500), LEVEL_PING_ENG, fill=(0, 0, 0), font=eng_infomation)
    draw.multiline_text((250,610), '原因:', fill=(0, 0, 0), font=genin)
    draw.multiline_text((400,610), LEVEL_INFO, fill=(0, 0, 0), font=genin)
    # 図形のセーブ
    im.save(save_src, quality=100)
    return save_src


if __name__ == "__main__":
    main()
