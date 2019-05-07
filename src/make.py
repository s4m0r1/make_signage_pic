from PIL import Image, ImageDraw, ImageFont
import logging
from logging import getLogger, StreamHandler, Formatter

# コンフィグを書く
FONT_DIR = ""
SAVE_SRC = ""
# LOG = True
# LOGGER_LEVEL = "DEBUG"
# 画像作成関数化

# 作成する画像コンフィグ
COLLOR = ""
LAN_NAME = ""
IP_ADDR = ""
HOST_NAME = ""
LEVEL = ""
TIME = ""
LEVEL_PING = ""
LEVEL_PING_ENG = ""
LEVEL_INFO = ""

'''
色は何色か

どこの回線
エラー元のIP
エラー元ホスト名

バツか三角か
発生時刻
疎通はできているか
できていない場合の英語

原因も作成
'''

def check_config():
    # if LOG:
    #     set_logger()
    #     logging.info("Save Log")
    if FONT_DIR == "":
        logging.error("No Set Font! Your Check \"FONT_DIR\"")
        exit()
    if SAVE_SRC == "":
        logging.error("No Set Save Source!Your Check \"SAVE_SRC\"")
        exit()


# def set_logger():
#     # loggerで受け取るレベル設定
#     # ハンドラで受け取るレベル設定
#     pass

def make_pic():
    pass


def main():
    check_config()
    make_pic()
    

if __name__ == "__main__":
    main()