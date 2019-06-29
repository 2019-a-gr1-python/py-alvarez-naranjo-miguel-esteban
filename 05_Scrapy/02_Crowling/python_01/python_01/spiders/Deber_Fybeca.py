import scrapy
import pandas as pd
import re
class IntroSpider(scrapy.Spider):
    name = 'deber_fybeca'

    def start_requests(self):
        urls = [
            'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25'            
        ]

        for url in urls:
            #yield nos permite hacer sincrona para que se ejecute en secuencia y no en paralelo
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        productosFy = response.xpath('/html/body/div/div/div/div/div/ul/li/@data-name').extract()
        print(productosFy)

        preciosFy = response.xpath('//div[contains(@class,"price-member")]/div[@data-bind]').extract()
        print(preciosFy)

        # Limpiar datos en Precios
        for precio in range(len(preciosFy)):
            preciosFy[precio] = re.findall(r"\d+\.\d+", preciosFy[precio])

        print(preciosFy)

        df = pd.DataFrame(preciosFy,columns=['Precios'],
                          index=productosFy) 

        print(df)

        #De string a float
        df['Precios'] = df['Precios'].astype('float64')

        #Precio maximo
        
        print("Precio maximo ", df.loc[df['Precios'] == df['Precios'].max()])

        #Precio minimo
        
        print("Precio minimo ", df.loc[df['Precios'] == df['Precios'].min()])