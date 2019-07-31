import scrapy

class AraniaFiscaliaGeneralEstadoEC(scrapy.Spider):
    name = 'arania_delitosEC'
    
    def start_requests(self):
        urls = [
            'https://www.gestiondefiscalias.gob.ec/siaf/comunes/noticiasdelito/info_mod.php?businfo=a:2:{i:0;s:6:%22miguel%22;i:1;s:7:%22esteban%22;}',
        ]

        