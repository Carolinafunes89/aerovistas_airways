## Aerovista Airways Final Proyect
#### Members : 
##### Eduardo Villalba Bianqueri ( Data Scientist  )
##### Carolina Funes (project coordinator and quality control)
##### Nicolas Carrasco ( Data Engeneer)
#####  Alejandro Gutierrez ( Bi Consultant)
<p>
Algunas de las herramientas que se utilizó
</p>
![Img Alt] (https://github.com/Apocalypsemind/Aerovistas-Airways/blob/main/Black%20and%20Purple%20Modern%20Programming%20Presentation.png)
- Github Desktop
- Data Browbser
- My Sql Server ( Microsoft)
- Microsoft Visual Studio
- PowerBi
- Canvas
- Chatgtp(Image Creator)
- Microsoft Word 
 ** Entre otros**
##  Proceso en accion 
#####  Comenzamos utilizando la herramienta de data browser para transformar el archivo de origen por el cual tiene de nombre "travel.sqlite".
Al utilizar dicha herramientas se transformarón en 8 archivos de tipo csv por el cual comienza el verdadero reto 
## Limpieza del archivo 
##### Mediante la ayuda de la tabla de visualizacíones Powerbi pudimos identificar entre ellos factores por el cual corrompia el archivo y lo hacia en partes ilegible 
* aircrafts_data_
Extraída la columna model_en con los nombres en inglés de los modelos.
Eliminada la columna JSON model.

* airports_data_
Extraídos los nombres (airport_name_en) y ciudades (city_en) en inglés.
Separadas las coordenadas en latitude y longitude.

* boarding_passes_
Eliminados duplicados, estructura de datos intacta.

* bookings
Convertida la columna book_date a un formato de fecha estándar.
Filtrados valores negativos en total_amount.

* flights.csv
Los valores \N se reemplazaron por NaN.
Las columnas de fecha se convirtieron al formato datetime.

* seats.csv
Se eliminaron posibles duplicados.

* ticket_flights.csv
La columna amount se convirtió en numérica.

* tickets.csv
Se eliminaron duplicados basados en ticket_no y book_ref.
## Creacion De Tablas en Mysql Server

