!pip install pandas sqlite3 matplotlib seaborn

import sqlite3

# Conectar a la base de datos (si no existe, la crea)
conn = sqlite3.connect("data_analytics.db")
cursor = conn.cursor()

# Crear una tabla de usuarios con roles
cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL
);
""")

# Insertar usuarios con diferentes roles
usuarios = [
    ("Juan", "Data Engineer"),
    ("Ana", "Data Analyst"),
    ("Carlos", "BI Consultant"),
    ("Maria", "Data Scientist")
]

cursor.executemany("INSERT INTO Usuarios (nombre, rol) VALUES (?, ?)", usuarios)
conn.commit()
print("Usuarios creados correctamente.")