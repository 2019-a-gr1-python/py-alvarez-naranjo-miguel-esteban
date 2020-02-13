import scrapy
from scrapy.spider import CrawlSpider 
import re

class AraniaFiscaliaGeneralEstadoEC(CrawlSpider):
    name = 'arania_delitosEC'
    
    def start_requests(self):
        urls = [
            'https://www.gestiondefiscalias.gob.ec/siaf/comunes/noticiasdelito/info_mod.php?businfo=a:2:{i:0;s:6:%22miguel%22;i:1;s:7:%22esteban%22;}',
            'https://www.gestiondefiscalias.gob.ec/siaf/comunes/noticiasdelito/info_mod.php?businfo=a:2:{i:0;s:5:%22paola%22;i:1;s:5:%22maria%22;}',
            'https://www.gestiondefiscalias.gob.ec/siaf/comunes/noticiasdelito/info_mod.php?businfo=a:2:{i:0;s:4:%22juan%22;i:1;s:4:%22jose%22;}',
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response):
        
        for tabla in response.xpath('//*[@class="general"]//tbody'):
            existe_tabla = len(tabla.xpath('tr//td//text()').extract())
            lugar = re.search('LUGAR', tabla.xpath('tr//td//text()')[0].extract())
            print(existe_tabla)
            if(existe_tabla > 13 and lugar):
                yield {
                    tabla.xpath('tr//td//text()')[0].extract():tabla.xpath('tr//td//text()')[1].extract(),
                    tabla.xpath('tr//td//text()')[2].extract():tabla.xpath('tr//td//text()')[3].extract(),
                    tabla.xpath('tr//td//text()')[4].extract():tabla.xpath('tr//td//text()')[5].extract(),
                    tabla.xpath('tr//td//text()')[11].extract():tabla.xpath('tr//td//text()')[12].extract(),

                }
            else:
                print('la tabla no contiene informacion')
                