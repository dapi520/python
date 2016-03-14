import urllib.request
import gzip

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read
    return html

def ungzip(data):
    print('正在解压')
    data = gzip.decompress(data)
    print('解压完成')
    return data

html = getHtml("https://www.zhihu.com/")

#print (ungzip(html))
print (type(html))
