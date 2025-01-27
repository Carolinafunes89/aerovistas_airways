## Aerovista Airways Final Proyect
#### Members : 
##### Eduardo Villalba Bianqueri ( Data Scientist  )
##### Carolina Funes (project coordinator and quality control)
##### Nicolas Carrasco ( Data Engeneer)
#####  Alejandro Gutierrez ( Bi Consultant)
<p>
Algunas de las herramientas que se utilizó
</p>

![Image](https://github.com/user-attachments/assets/eda5ee04-4971-478b-8a02-385c3c91603c)

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

##### CREATE TABLE aircrafts (
    aircraft_code NVARCHAR(50) PRIMARY KEY,   -- Clave primaria
    model NVARCHAR(100),          -- Modelo del avión
    range INT                     -- Alcance del avión (en kilómetros o el tipo de unidad que prefieras)
);
CREATE TABLE airports (
    airport_code NVARCHAR(50) PRIMARY KEY,    -- Clave primaria
    airport_name NVARCHAR(100),                -- Nombre del aeropuerto
    city NVARCHAR(100),                        -- Ciudad donde está el aeropuerto
    coordinates NVARCHAR(100),                 -- Coordenadas geográficas (latitud, longitud)
    timezone NVARCHAR(50)                      -- Zona horaria
);
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,                 -- Clave primaria
    flight_no NVARCHAR(50),                    -- Número de vuelo
    scheduled_departure DATETIME,             -- Fecha y hora programada para la salida
    scheduled_arrival DATETIME,               -- Fecha y hora programada para la llegada
    departure_airport NVARCHAR(50),           -- Nombre del aeropuerto de salida
    arrival_airport NVARCHAR(50),             -- Nombre del aeropuerto de llegada
    status NVARCHAR(50),                      -- Estado del vuelo
    aircraft_code NVARCHAR(50),               -- Código del avión
    actual_departure DATETIME,                -- Fecha y hora real de salida
    actual_arrival DATETIME,                  -- Fecha y hora real de llegada
    FOREIGN KEY (departure_airport) REFERENCES airports(airport_code),  -- Relación con la tabla airports
    FOREIGN KEY (arrival_airport) REFERENCES airports(airport_code),    -- Relación con la tabla airports
    FOREIGN KEY (aircraft_code) REFERENCES aircrafts(aircraft_code)     -- Relación con la tabla aircrafts
);
CREATE TABLE seats (
    aircraft_code NVARCHAR(50),        -- Código del avión
    seat_no NVARCHAR(50),              -- Número de asiento
    fare_conditions NVARCHAR(100),     -- Condiciones tarifarias
    PRIMARY KEY (aircraft_code, seat_no),  -- Clave primaria compuesta
    FOREIGN KEY (aircraft_code) REFERENCES aircrafts(aircraft_code)  -- Relación con la tabla aircrafts
);

CREATE TABLE booking (
    book_ref NVARCHAR(50) PRIMARY KEY,      -- Referencia de la reserva
    book_date DATETIME NOT NULL,            -- Fecha de la reserva
    total_amount DECIMAL(18, 2) NOT NULL    -- Monto total de la reserva
);
CREATE TABLE tickets (
    ticket_no NVARCHAR(50) PRIMARY KEY,    -- Número de ticket
    book_ref NVARCHAR(50),                  -- Referencia de la reserva
    passenger_id INT,                       -- ID del pasajero
    FOREIGN KEY (book_ref) REFERENCES booking(book_ref)  -- Relación con la tabla booking
);
CREATE TABLE ticket_flights (
    ticket_no NVARCHAR(50),
    flight_id INT,
    fare_conditions NVARCHAR(50),
    amount DECIMAL(18, 2),
    PRIMARY KEY (ticket_no, flight_id),   -- Clave primaria compuesta
    FOREIGN KEY (ticket_no) REFERENCES tickets(ticket_no),   -- Relación con la tabla tickets
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)    -- Relación con la tabla flights
);
CREATE TABLE boarding_passes (
    ticket_no NVARCHAR(50),    -- Número de ticket
    flight_id INT,             -- ID del vuelo
    boarding_no NVARCHAR(50),  -- Número de embarque
    seat_no NVARCHAR(50),      -- Número de asiento
    PRIMARY KEY (ticket_no, flight_id),  -- Clave primaria compuesta
    FOREIGN KEY (ticket_no) REFERENCES tickets(ticket_no),         -- Relación con la tabla tickets
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),         -- Relación con la tabla flights
    FOREIGN KEY (seat_no) REFERENCES seats(seat_no)               -- Relación con la tabla seats
);
CREATE TABLE seats (
    aircraft_code NVARCHAR(50),        -- Código del avión
    seat_no NVARCHAR(50),              -- Número de asiento
    fare_conditions NVARCHAR(100),     -- Condiciones tarifarias
    PRIMARY KEY (aircraft_code, seat_no),  -- Clave primaria compuesta
    FOREIGN KEY (aircraft_code) REFERENCES aircrafts(aircraft_code)  -- Relación con la tabla aircrafts
);
CREATE TABLE boarding_passes (
    ticket_no NVARCHAR(50),    -- Número de ticket
    flight_id INT,             -- ID del vuelo
    boarding_no NVARCHAR(50),  -- Número de embarque
    aircraft_code NVARCHAR(50), -- Código del avión (relación con la tabla seats)
    seat_no NVARCHAR(50),      -- Número de asiento
    PRIMARY KEY (ticket_no, flight_id),  -- Clave primaria compuesta
    FOREIGN KEY (ticket_no) REFERENCES tickets(ticket_no),         -- Relación con la tabla tickets
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),         -- Relación con la tabla flights
    FOREIGN KEY (aircraft_code, seat_no) REFERENCES seats(aircraft_code, seat_no) -- Relación con la tabla seats
); 
Relaciones entre las tablas:
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
