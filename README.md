## REPOSITORIO DEL CURSO PYTHON DATA DEV

A partir de la clase del dia 05-abr comenzamos con el uso de GIT

**weather_api.ipynb:** es un ejercicio en el que ponemos en juego el uso de un api de clima y otra de geolocalizacion

Resolvemos mediante ambas, consultar el clima en cada una de las ciudades donde se encuentra una sucursal de la cadena de hoteles (*sucursales_sol_360.csv*)

**mongo_estaciones.ipynb:** es un ejercicio en el que comenzamos a usar bases no estructuradas

Tomamos un geojson de BsAs Data con las estaciones saludables y creamos una coleccion en la que cada documento es una estacion

**scrap_top100.ipynb:** es un ejercicio de web scraping, tomamos la pagina de los 100 libros mas vendidos de Cuspide, scrapeamos la informacion basica de cada uno y con *MySQLConnector* creamos una tabla donde cada registro sera uno de esos libros

**scrap_cuspide.py:** es otro ejercicio similar, esta vez con Selenium. Como en este caso, libros de Cs Naturales, la cantidad de libros es grande el desafio pasa por la paginacion. El resultado es un .json donde cada libro es un objeto/diccionario

**scrap_carrefour.ipynb:** es un ejercicio en el que el desafio pasa por scrollear y clickear un boton de cargar mas productos y por otro lado acceder al modal de cada item usando Selenium. En este caso el resultado es un CSV con todas las cervezas.

**twee.ipynb** es el primer ejercicio jugando con la API de Twitter. En principio, tomamos algunos tweets y los subimos a MongoDB Atlas.

**Analytics** la segunda parte del programa se basa en Analitica con Python, las primeras clases se desarollan entorno a la Analitica Descriptica con la libreria Pandas