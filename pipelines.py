# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import os

class LuoxiaPipeline(object):
    rootpath="D:\\\\WORK\\Scrapy_item\\myScrapy\\luoxia\\luoxia\\download\\"
    def process_item(self, item, spider):
        pri_dir_path=self.rootpath+item["dirlevel1"]
        if not os.path.exists(pri_dir_path):
            os.mkdir(pri_dir_path)
            print(item["dirlevel1"] )
        sec_dir_path = pri_dir_path +"\\"+ item["dirlevel2"]
        if not os.path.exists(sec_dir_path):
            os.mkdir(sec_dir_path)
            print("----" + item["dirlevel2"])

        filepath=sec_dir_path+"\\"+item["title"][0]+".txt"
        print("--------" + item["title"])
        savefile = open(filepath,"wb")
        savefile.write(str(item["content"]).encode("utf-8","ignore"))
        savefile.close()
        return item

    """
class LuoxiaPipeline(object):

    def process_item(self, item, spider):
        print(item["dirlevel1"]+"----")
        print("----"+item["dirlevel2"]+"----")
        print("--------"+item["title"]+"----")
        return item
    """