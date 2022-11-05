import sqlite3 as sql


DB_PATH = "D:/Malena/Informatica/Planeta-Mascotas/App/database/productos.db"


def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE productos (
        id integer,
        nombre varchar,
        cantidad integer,
        precio integer,
        imagen varchar )""")
    conn.commit()
    conn.close()


def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1, 'Agility Cats', 1, 1000, 'alimento_gato1.png'),
        (2, 'Mon Ami', 1, 1000, 'alimento_gato2.jpg'),
        (3, 'Excellent', 1, 1000, 'alimento_gato3.png'),
        (4, 'Pro Plan', 1, 1000, 'alimento_gato4.png'),
        (5, 'Royal Canin', 1, 1000, 'alimento_gato5.jpg'),
        (6, 'Sabrositos', 1, 1000, 'alimento_gato6.jpg'),
        (7, 'Alta Gama', 1, 1000, 'alimento_gato7.jpg'),
        (8, 'Balanced', 1, 1000, 'alimento_perro1.jpg'),
        (9, 'Old Prince', 1, 1000, 'alimento_perro2.jpg'),
        (10, 'Royal Canin', 1, 1000, 'alimento_perro3.jpg'),
        (11, 'Pedigree', 1, 1000, 'alimento_perro4.jpg'),
        (12, 'Nutribon', 1, 1000, 'alimento_perro5.png'),
        (13, 'MiMaskot', 1, 1000, 'alimento_perro6.jpg'),
        (14, 'Agility', 1, 1000, 'alimento_perro7.png'),
        (15, 'Pet Dry pañales', 1, 1000, 'panales-para-perro.jpg'),
        (16, 'Dentalife', 1, 1000, 'dentalife-perro.png'),
        (17, 'Clean dog', 1, 1000, 'pipeta_perros.jpg'),
        (18, 'Goofy Huesitos', 1, 1000, 'huesitos_perro.jpg'),
        (19, 'Pelota gatos', 1, 1000, 'juguete1.jpg'),
        (20, 'Plumas gatos', 1, 1000, 'juguete2.jpg'),
        (21, 'Rueda gatos', 1, 1000, 'juguete3.jpg'),
        (22, 'Mordillo de goma', 1, 1000, 'juguete4.jpg'),
        (23, 'Mordillo de tela', 1, 1000, 'juguete5.jpg'),
        (24, 'Mordillo huesitos', 1, 1000, 'cepillo-de-dientes.jpg'),
        (25, 'Frontline Gato', 1, 1000, 'frontline-plus-gato.png'),
        (26, 'Power Met', 1, 1000, 'pipeta-gato1.png'),
        (27, 'Piedritas The best', 1, 1000, 'piedritas-sanitarias1.jpg'),
        (28, 'Piedritas Absorsol', 1, 1000, 'piedritas-sanitarias3.jpg'),
    ]
    cursor.executemany("""INSERT INTO productos (id, nombre, cantidad, precio, imagen) VALUES (?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    createDB()
    addValues()