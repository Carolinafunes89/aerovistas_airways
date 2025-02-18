✈️ # Proyecto: Aerovistas Airways

![Image](https://github.com/Carolinafunes89/aerovistas_airways/blob/main/Night%20Presentation%20-%20Cover.png)

# 👥 Miembros del Equipo

- **Eduardo Villalba Bianqueri** - *Data Scientist*  
  Experto en modelado predictivo y técnicas avanzadas de análisis de datos para generar soluciones basadas en datos.

- **Carolina Funes** - *Data Analyst & Project Coordinator*  
  Especialista en análisis de datos, con experiencia en la gestión de proyectos y la transformación de datos en insights clave para la toma de decisiones estratégicas.

- **Nicolás Carrasco** - *Data Engineer*  
  Ingeniero de datos con experiencia en el diseño y construcción de infraestructuras de datos eficientes, asegurando la calidad y accesibilidad de los datos.

- **Alejandro Gutiérrez** - *BI Consultant*  
  Consultor en Business Intelligence, enfocado en el diseño e implementación de soluciones analíticas y de visualización para mejorar la toma de decisiones empresariales.
<p>
🔧 ##Algunas de las herramientas que se utilizó
</p>

![Image](https://github.com/Carolinafunes89/aerovistas_airways/blob/main/Night%20Presentation%20-%20Success%20marketing.png)

- 🖥️ Github Desktop
- 🔍 Data Browbser
- 🗄️ My Sql Server ( Microsoft)
- 🐍 Microsoft Visual Studio
- 📊 PowerBi
-🎨 Canvas
- 🤖🎨 Chatgtp(Image Creator)
- 📝Microsoft Word 
 ** Entre otros**
🚀 ## Proceso en accion 
#####  Comenzamos utilizando la herramienta de data browser para transformar el archivo de origen por el cual tiene de nombre "travel.sqlite".
Al utilizar dicha herramientas se transformarón en 8 archivos de tipo csv por el cual comienza el verdadero reto 

🧹 ##Limpieza del archivo 
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
## Relacíones De Tablas en Mysql Server


**Relaciones entre las tablas**:
Relación entre flights y airports:
Un vuelo tiene un aeropuerto de salida y uno de llegada. Esto se refleja en las claves foráneas departure_airport y arrival_airport en la tabla flights, las cuales se refieren a la tabla airports.
Tipo de relación: Uno a muchos.
Un aeropuerto puede tener varios vuelos de salida y llegada.

Relación entre flights y aircrafts:
Un vuelo se asocia a un avión, el cual está representado por aircraft_code en la tabla flights.
Tipo de relación: Muchos a uno.
Un avión puede estar asignado a varios vuelos.

Relación entre seats y aircrafts:
Los asientos están asociados a un avión específico mediante aircraft_code.
Tipo de relación: Uno a muchos.
Un avión tiene varios asientos, y cada asiento pertenece a un avión.

Relación entre tickets y booking:
Un ticket está relacionado con una reserva específica. Esto se refleja mediante la clave foránea book_ref en la tabla tickets, que hace referencia a book_ref en la tabla booking.
Tipo de relación: Muchos a uno.
Una reserva puede generar varios tickets.

Relación entre ticket_flights y tickets:
Un ticket puede estar asociado a varios vuelos (por ejemplo, si el ticket cubre múltiples vuelos o escalas). Esto se refleja mediante la clave foránea ticket_no en la tabla ticket_flights, que hace referencia a ticket_no en la tabla tickets.
Tipo de relación: Uno a muchos.
Un ticket puede estar asociado a varios vuelos.

Relación entre ticket_flights y flights:
Un vuelo puede estar asociado a varios tickets. Esto se refleja mediante la clave foránea flight_id en la tabla ticket_flights, que hace referencia a flight_id en la tabla flights.
Tipo de relación: Uno a muchos.
Un vuelo puede estar asociado a varios tickets.

Relación entre boarding_passes y tickets:
Una tarjeta de embarque está asociada a un ticket. Esto se refleja mediante la clave foránea ticket_no en la tabla boarding_passes, que hace referencia a ticket_no en la tabla tickets.
Tipo de relación: Uno a muchos.
Un ticket puede generar varias tarjetas de embarque (por ejemplo, si un pasajero tiene varios vuelos).

Relación entre boarding_passes y flights:
Una tarjeta de embarque está asociada a un vuelo. Esto se refleja mediante la clave foránea flight_id en la tabla boarding_passes, que hace referencia a flight_id en la tabla flights.
Tipo de relación: Uno a muchos.
Un vuelo puede generar varias tarjetas de embarque.

Relación entre boarding_passes y seats:
Una tarjeta de embarque está asociada a un asiento. Esto se refleja mediante las claves foráneas aircraft_code y seat_no en la tabla boarding_passes, que hacen referencia a la tabla seats.
Tipo de relación: Muchos a uno.
Varios pasajeros pueden tener el mismo asiento.
## DIAGRAMA DE TELLO
![Image](https://github.com/user-attachments/assets/12267b8b-1ab1-48b9-bac2-427c534d1a9a)
## DIAGRAMA DE GANT
![Image](https://github.com/Carolinafunes89/aerovistas_airways/blob/main/Gray%20Colorful%20Modern%20Professional%20Social%20Media%20Marketing%20Plan%20Gantt%20Chart%20Graph.png)
