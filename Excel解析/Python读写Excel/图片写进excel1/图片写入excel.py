# coding=utf-8

import urllib2     # 导入urllib2模块
import xlsxwriter



listurl = ['https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-3-original.jpg','https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-original.jpg',]

#根据图片链接列表，把图片保存到本地
i = 0
for url in listurl:
    f = open(str(i)+'.jpg',"wb")    #打开文件
    req = urllib2.urlopen(url)
    buf = req.read()              #读出文件
    f.write(buf)                  #写入文件
    i = i + 1


#将图片一次导入到表格的1，2...行
i -= 1
for j in range(0,i):
    book = xlsxwriter.Workbook('pict.xls')
    sheet = book.add_worksheet('demo')
    sheet.insert_image('D'+str(j), str(j)+'.jpg')
book.close()