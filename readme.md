<h2>main.py: 爬取代码</h2>

<h3>主要需要修改的地方：</h3>

```python
# 修改为你的电脑的edge浏览器的启动的地方，主要是改那串数据
options.binary_location = r'C:\Program Files (x86)\Microsoft\EdgeCore\106.0.1370.42\msedge.exe'
# executetable_path修改为你下载的edge驱动器的路径，百度搜索edge driver即可下载，要注意于浏览器版本号对应
driver = Edge(options=options,executable_path=r'X:\Code\Scrapy\Crawl\edge_driver\msedgedriver.exe')
# 修改你想要爬的职位的，把最后的kd=NLP改为kd=xx即可
driver.get('https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=NLP')
```
修改完成后，直接运行，结果在当前目录下的*database.txt*里面

<h2>data ananlyze: 里面有我爬好的数据以及词云图</h2>
