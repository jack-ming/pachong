import urllib
import urllib.request
import re

#data = {}
#data['word'] = 'Jecvay Notes'

#url_values = urllib.parse.urlencode(data)
url = "http://tieba.baidu.com/p/1753935195"
#full_url = url + url_values

#data = urllib.request.urlopen(full_url).read()
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

reg = r'src="(.+?\.jpg)" width'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(data)#进行匹配
x = 0
for img in imglist:
     print(img)
     urllib.request.urlretrieve(img, '%s.jpg' %x)
     x += 1