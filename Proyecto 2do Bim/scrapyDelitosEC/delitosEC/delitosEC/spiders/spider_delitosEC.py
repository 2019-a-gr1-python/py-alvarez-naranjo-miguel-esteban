import scrapy

class AraniaFiscaliaGeneralEstadoEC(scrapy.Spider):
    name = 'arania_delitosEC'
    
    def start_requests(self):
        urls = [
            'https://www.gestiondefiscalias.gob.ec/siaf/comunes/noticiasdelito/info_mod.php?businfo=a:2:{i:0;s:6:%22miguel%22;i:1;s:7:%22esteban%22;}',
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response):
        tablas = response.xpath('//*[@class="general"]//tbody').extract()
        for tabla in tablas:
            yield {
                tabla.xpath('tr//td//text()')[0].extract_first():tabla.xpath('tr//td//text()')[1]extract_first(),
                tabla.xpath('tr//td//text()')[2]extract_first():tabla.xpath('tr//td//text()')[3]extract_first(),
                tabla.xpath('tr//td//text()')[4]extract_first():tabla.xpath('tr//td//text()')[5]extract_first(),
                tabla.xpath('tr//td//text()')[11]extract_first():tabla.xpath('tr//td//text()')[12]extract_first(),

            }