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
        tablas = response.xpath('//*[@class="general"]//tbody')
        for tabla in tablas:
            yield {
                tablas.xpath('tr//td//text()')[0]:tablas.xpath('tr//td//text()')[1],
                tablas.xpath('tr//td//text()')[2]:tablas.xpath('tr//td//text()')[3],
                tablas.xpath('tr//td//text()')[4]:tablas.xpath('tr//td//text()')[5],
                tablas.xpath('tr//td//text()')[11]:tablas.xpath('tr//td//text()')[12],

            }