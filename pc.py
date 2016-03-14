import urllib.request
import re

#localpos = 'H:\python\temp\'
def getHtml(url):
    response = urllib.request.urlopen(url)
    page = bytes.decode(response.read())
    return page

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    image = re.compile(reg)
    imglist = re.findall(image,html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x += 1
    return imglist
#   urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
#  
html = getHtml('http://tieba.baidu.com/p/3907275859')
# html = getHtml(input('网址是：'))
imglist = getImg(html)
# print(imglist,len(imglist))
