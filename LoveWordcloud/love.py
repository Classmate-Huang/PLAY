import warnings
import jieba
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
warnings.filterwarnings('ignore')


# 读取数据文件
df = pd.read_csv('record.csv', encoding='utf-8', names=['id', 'content'])
df = df['content']
df = df.dropna()
content = df.values.tolist()
segment = []
for line in content:
    try:
        segs = jieba.lcut(line)
        for seg in segs:
            if len(seg) > 1 and seg !='\r\n':
                segment.append(seg)
    except:
        print(line)
        continue

# 去除停用词
words_df = pd.DataFrame({'segment':segment})
stopwords = pd.read_csv('stopwords.txt', index_col=False, quoting=3, sep='\t', names=['stopword'], encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
# print(words_df.head())


words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
words_stat = words_stat.reset_index().sort_values(by=['计数'], ascending=False)
words_stat.drop(2)
# print(words_stat.head())

# 可视化
bimg = imread('love.jpeg')
wordcloud = WordCloud(font_path='simhei.ttf', mask=bimg, background_color='white', max_font_size=120,
                      width=500, height=300)
word_frequence = {x[0]: x[1] for x in words_stat.head(500).values}
wordcloud = wordcloud.fit_words(word_frequence)
wordcloud.to_file('Love.png')
plt.imshow(wordcloud)
plt.show()
