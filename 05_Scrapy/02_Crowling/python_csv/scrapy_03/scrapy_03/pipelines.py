# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class FiltradoSoloTabletas(object):

    def process_item(self, item, spider):
        
        titulo = item['titulo']
        print(titulo)
        if('capsula' not in 'mi capsula'):
            raise DropItem('No tiene capsula en el titulo')
        else:
            return item

        return item


class TransformarTituloAMinusculas(object):
    def process_item(self, item, spider):
        item['titulo'] = item['titulo'].lower()
        return item


