import configparser
import os
import wordcloud
import jieba
import sys

abs = os.path.abspath(__file__)
ROOT = os.path.dirname(abs)

def path(file_name):
    return os.path.join(ROOT, file_name)

def get_config(key, type=str):
    configs = configparser.ConfigParser()
    configs.read(path("config.ini"))
    return type(configs["programme"][key])

def create_cloud(file, out="ciyun.png"):
    sourceFile = open(path(file), encoding='utf-8')
    txt = sourceFile.read()
    txtlist = jieba.lcut(txt)
    words = " ".join(txtlist)
    stopwords = set()
    content = [line.strip() for line in open('stop_words.txt', 'r', encoding="utf-8").readlines()]
    stopwords.update(content)
    w = wordcloud.WordCloud(background_color='white',
                            font_path=path(get_config("font")), 
                            stopwords=stopwords, 
                            width=get_config("image_width", int), 
                            height=get_config("image_height", int),
                            mode="RGBA")
    w.generate(words)
    w.to_file(path(out))
    return path(path(out))

# def call(argv):
#     if len(argv) == 2:
#         return create_cloud(path(argv[0]), argv[1])
#     elif len(argv) == 1:
#         return create_cloud(path(argv[0]))

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 3:
        create_cloud(path(argv[1]), argv[2])
    else:
        print("缺少参数")