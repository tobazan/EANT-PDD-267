import time
from selenium import webdriver

#VOY HACIA LA PAGINA PRINCIPAL CON SELENIUM
url = '''https://www.cuspide.com/resultados.aspx?c=
Biolog%c3%ada%2c+Ciencias+de+la+Tierra(T%c3%a9cnicos)
&tema=2173&por=Tema&orden=fecha'''

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='../../chrDriver/chromedriver.exe',
                        options=options)

driver.get(url)

#DEFINO LA FUNCION SCRAPEAR
titulos = []
valores = []

def scrap():
    libros = driver.find_elements_by_xpath('//div[@class="md-datos"]')
    precios = driver.find_elements_by_xpath('//div[@class="precio"]')
    
    for libro in libros:
        titulos.append(libro.text)
    for precio in precios:
        valores.append(precio.text)
    
    return

#DEFINO UN BUCLE DE PAGINACION Y SCRAPEO
while True:
    time.sleep(4)
    scrap()
    try:
        boton = driver.find_element_by_xpath(
            '//a[@class="paginadorLinkSiguiente"]')
        boton.click()
    except: 
        #estamos en la ultima pagina por eso falla al buscar el boton
        #entonces corto el loop y cierro el driver
        break

driver.quit()

#EXPORTO LA INFO SCRAPEADA A UN JSON

# me traia por cada pagina el valor del carrito de compra
valores = list(filter(lambda x: x != '', valores))

import json
libros_cs = []

with open('./cs_naturales.json','w', encoding='utf-8') as out:
    for i in range(len(titulos)):
        try:
            t_a = titulos[i].split('\n')
            
            l = {'ID': i,
                'TITULO': t_a[0],
                'AUTOR': t_a[1],
                'AR$': valores[i]}
        except:
            #no todos los titulos scrapeados traen el autor
            l = {'ID': i,
                'TITULO': titulos[i],
                'AUTOR': '',
                'AR$': valores[i]}
        
        libros_cs.append(l)

    json.dump(libros_cs, out, indent=3)