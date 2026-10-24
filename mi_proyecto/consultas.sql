-- 1. Creación de la tabla
CREATE TABLE peliculas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    genero VARCHAR(50),
    anio_estreno INT
);

-- 2. Registros iniciales que insertaste
INSERT INTO peliculas (titulo, genero, anio_estreno) VALUES
('Inception', 'Ciencia Ficción', 2010),
('El Padrino', 'Drama', 1972),
('Interstellar', 'Ciencia Ficción', 2014);

-- 3. Consulta de comprobación
SELECT * FROM peliculas;