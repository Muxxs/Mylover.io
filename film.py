#coding=utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
import re,jieba,jieba.analyse,os
num=5 #每+1 评论收集多加20个
main_word=[]
for i in range(0,num):
    resp=request.urlopen("https://movie.douban.com/review/best/?start="+str(i*20))
    html_data=resp.read()
    hl=bs(html_data)
    talk=hl.select(".title-link")
    for i in talk:
        i=str(i).split('"')


        #开始新的遍历网页
        resp = request.urlopen(i[3])
        html_data = resp.read()
        hl = bs(html_data)
        main_text=hl.select("#link-report")
        try:
            i = str(main_text).split("<p>")[1]
            talk_text=i.split("</p>")[0]
            #下面引用jieba分词提取关键词
            for i in jieba.analyse.extract_tags(talk_text, topK=20, withWeight=False, allowPOS=()):
                main_word.append(i)
        except:
            pass
print(main_word)
#最后利用词云显示一波- - 懒得按电影分类了

import matplotlib.pyplot as plt
from wordcloud import WordCloud


wc = WordCloud(
    background_color="white",
    width=1080,
    height=960,
    font_path="font.ttc",#不加这一句显示口字形乱码
    margin=2)

#乱码解决办法源自http://www.cnblogs.com/fanyuchen/p/7156959.html


split = " ".join(main_word)
pic=wc.generate(split)
plt.imshow(pic)
plt.axis("off")
plt.show()

#当然可以优化一下分词以及对电影的分类展示，但是- = 我懒