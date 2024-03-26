"""
v1.0 20240326
编写一个从文件读取数据、分词、生成词云图片的程序
1. 从resource.txt文件中读取数据
2. 从https://raw.githubusercontent.com/goto456/stopwords/master/baidu_stopwords.txt读取停用词表
3. 对读取的数据进行分词
4. 对分词的结果进行去除停用词操作，然后统计剩余词的词频
5. 对词频为TOP20的词生成词云图片
"""

import requests
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# 从文件读取数据
def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return ""

# 从URL下载停用词表
def download_stopwords(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

# 对文本进行分词
def tokenize(text):
    return jieba.lcut(text)

# 去除停用词并统计词频
def remove_stopwords_and_count(words, stopwords):
    word_counts = Counter()
    for word in words:
        if word not in stopwords:
            word_counts[word] += 1
    return word_counts

# 获取词频为TOP20的词
def get_top_20_words(word_counts):
    return word_counts.most_common(300)

# 生成词云图片
def generate_wordcloud(top_20_words):
    #./SimHei.ttf
    #wc = WordCloud(font_path='./hier_officeFontsPreview_4_23.ttf', width=800, height=600, max_words=20).generate_from_frequencies(dict(top_20_words))
    wc = WordCloud(font_path='./SimHei.ttf',width=800,height=600,max_words=100,max_font_size=100,background_color='white').generate_from_frequencies(dict(top_20_words))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# 主程序
if __name__ == "__main__":
    # 从resource.txt文件中读取数据
    file_path = './resource.txt'
    text = read_text(file_path)
    
    # 从在线地址读取停用词表
    stopwords_url = "https://raw.githubusercontent.com/goto456/stopwords/master/cn_stopwords.txt"
    stopwords = download_stopwords(stopwords_url)
    #stopwords增加\n
    stopwords.append('\n')
    
    # 对文本进行分词
    words = tokenize(text)
    
    # 去除停用词并统计词频
    word_counts = remove_stopwords_and_count(words, stopwords)

    # 获取词频为TOP20的词
    top_20_words = get_top_20_words(word_counts)
    print(top_20_words)

    # 生成词云图片
    generate_wordcloud(top_20_words)
