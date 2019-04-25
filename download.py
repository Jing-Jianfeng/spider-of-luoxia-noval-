#coding=utf-8
import urllib

from urllib import request,error
from lxml import etree
import os
def get_page(url):
    try:
        page_src = request.urlopen(url).read().decode("utf-8", "ignore")
        return page_src

    except error.URLError as e:
        print(url,"error,please try again")
        print(e.reason)
        return None


def get_pri_list(url):
    page_src=get_page(url)
    #print(page_src)
    pri_li_xpath=etree.HTML(page_src)
    ol_list=pri_li_xpath.xpath("//div[@class=\"hot-books clearfix\"]//ol")
    for ol in ol_list:
        dirname=ol.xpath(r"./li/h2/text()")[0].replace("：","")
        os.system("mkdir D:\\\\WORK\\Scrapy_item\\myScrapy\\luoxia\\luoxia\\download\\" + dirname)
        results=ol.xpath(r"./li[position()>1]/a")
        for result in results:
            title=result.xpath(r"./@title")[0]
            href=result.xpath(r"./@href")[0]
            dirpath="D:\\\\WORK\\Scrapy_item\\myScrapy\\luoxia\\luoxia\\download\\" + dirname+"\\"+title
            os.system("mkdir " + dirpath)
            get_sec_dir(href, dirpath)


def get_sec_dir(url,dirpath):
   chapter_page=get_page(url)
   #print(chapter_page)
   chapters=etree.HTML(chapter_page)
   chapter_list=chapters.xpath("//div[@class=\"book-list clearfix\"]/ul//li/a")
   print("start   downloading--------------")
   for chapter in chapter_list:
       huiname=chapter.xpath("./text()")[0]
       huiurl=chapter.xpath("./@href")[0]
       novel_content=get_content(huiurl).encode("utf-8","ignore")
       filepath=dirpath+"\\"+huiname+".txt"
       print("start writing  novel:  ",huiname)
       savefile=open(filepath,"wb")
       savefile.write(novel_content)
       savefile.close()

def get_content(url):
    novel_content=""
    content_src=get_page(url)
    content_src=etree.HTML(content_src)
    #contents=content_src.xpath("")
    nr_title=content_src.xpath("//article[@class=\"post clearfix\"]/header/h1/text()")
    novel_content+=nr_title[0]+"\r\n"
    auther=content_src.xpath("//article[@class=\"post clearfix\"]/header/p/b/text()")
    post_time=content_src.xpath("//article[@class=\"post clearfix\"]/header/p/text()")
    novel_content += auther[0] + "  "
    novel_content += post_time[0] + "\r\n"

    summary=content_src.xpath("//article[@class=\"post clearfix\"]/div[@id=\"nr1\"]//p/text()")
    for position in summary:
        novel_content += position + "\r\n"

    return novel_content




def main():
    url="http://www.luoxia.com/"
    get_pri_list(url)
    #filepath=r"D:\WORK\Scrapy_item\myScrapy\luoxia\luoxia\download\历史是个什么玩意儿"
    #get_sec_dir(url2,filepath)
    #get_content(url3)
    #print(get_page(url))
if __name__=="__main__":

    main()