# -*- coding: utf-8 -*-
"""
@author: 91523/YaoJiong

"""


import pandas as pd
import nltk
from wordcloud import wordcloud #注意大小写

#数据加载
data=pd.read_csv('./Market_Basket_Optimisation.csv',header = None)
#print(data)
#print(data.shape)

#将数据存放到transaction中
transaction=[]
#存储字典key:value
item_count={}

for i in range(data.shape[0]):
    temp=[]
    for j in range(data.shape[1]):
        item=str(data.values[i,j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item]=1
            else:
                item_count[item] += 1
    transaction.append(temp)
#print(transaction)

#去掉词云中不显示的单词列表（如虚词，你好，我的。。。）
def remove_stop_words(f):
    stop_words=[]
    for stop_word in stop_words:
        f=f.replace(stop_word,'')
    return f

def create_word_cloud(f):
    f=remove_stop_words(f)
    cut_text=nltk.word_tokenize(f)
    cut_text=" ".join(cut_text)
    wc = wordcloud.WordCloud(max_words=100,width=2000,height=1200)

    wc.generate(cut_text)
    wc.to_file("WordCloud.jpg")
    
#生成词云
all_word=' '.join('%s'%item for item in transaction)
#print(all_word)
create_word_cloud(all_word)

#Top10商品排序
print(sorted(item_count.items(),key=lambda x:x[1],reverse=True))
    