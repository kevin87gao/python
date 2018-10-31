# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline
from urllib import parse
from os.path import dirname,basename,join

class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        path = parse.urlparse(request.url).path
        #print('###################', path)
        #print('###################',basename(path))
        #print('###################',basename(dirname(path)))
        return join(basename(dirname(path)), basename(path))


class FilesdownloadPipeline(object):
    def process_item(self, item, spider):
        return item
