import pkuseg
import wordcloud
from collections import Counter
# 读取文本
with open("database.txt",encoding="utf-8") as f:
    s = f.readlines()
s = ''.join([e[6:]+'。' for e in s])

print(s)
seg = pkuseg.pkuseg()

ls = seg.cut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串
counter = Counter(ls)
stopwords = open('stop words.txt',encoding='utf-8').readlines() # 去掉不需要显示的词
stopwords = {e.strip() for e in stopwords}

results = []
for k, v in counter.items():
    if k in stopwords:
        continue
    else:
        results.append((k,v))
results = sorted(results,key=lambda x:x[1],reverse=True)
with open("keyword.txt",'w', encoding='utf-8') as F:
    for k,v in results:
        F.write('{}\t{}\n'.format(k,v))




wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=500,stopwords=stopwords)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("NLP.png") # 保存词云文件