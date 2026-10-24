import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            
            # --- 1. EXTRA OPCIONAL: INSERTAR UN NUEVO REGISTRO DESDE PYTHON ---
            cur.execute(
                "INSERT INTO peliculas (titulo, genero, anio_estreno) VALUES (%s, %s, %s)",
                ("Matrix", "Ciencia Ficción", 1999)
            )
            # Confirmar los cambios en la base de datos
            connection.commit()

            # --- 2. CONSULTA SELECT (SE MANTIENE IGUAL) ---
            cur.execute("SELECT * FROM peliculas;")
            filas = cur.fetchall()

            for fila in filas:
                print(fila)

except Exception as e:
    print("Error:", e)
    raise