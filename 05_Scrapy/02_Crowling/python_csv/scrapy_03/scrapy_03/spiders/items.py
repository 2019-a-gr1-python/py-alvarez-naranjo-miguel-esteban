import scrapy
import re
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def FiltrarPrecio(texto):
    texto = re.findall(r"\d+\.\d+", texto)
    return texto

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()
    precio = scrapy.Field(
        input_processor = MapCompose(
            FiltrarPrecio
        )
    )
