-- 1. Crear tabla de monedas primero (porque usuarios la referenciará)
CREATE TABLE moneda (
    currency_id SERIAL PRIMARY KEY,
    currency_name VARCHAR(50) NOT NULL UNIQUE,
    currency_symbol VARCHAR(10) NOT NULL 
);

-- 2. Crear tabla de usuarios
CREATE TABLE usuarios (
    user_id SERIAL PRIMARY KEY, 
    nombre VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    saldo DECIMAL(10, 2) DEFAULT 0.00,
    currency_id INT,
    CONSTRAINT fk_usuario_moneda 
        FOREIGN KEY (currency_id) REFERENCES moneda(currency_id)
);

-- 3. Crear tabla de transacciones
CREATE TABLE transaccion (
    transaction_id SERIAL PRIMARY KEY,
    sender_user_id INT NOT NULL,
    receiver_user_id INT NOT NULL,
    importe DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_emisor FOREIGN KEY (sender_user_id) 
        REFERENCES usuarios(user_id),
    
    CONSTRAINT fk_receptor FOREIGN KEY (receiver_user_id) 
        REFERENCES usuarios(user_id)
);

---
--- INSERCIÓN DE DATOS ---
---

INSERT INTO moneda (currency_name, currency_symbol) VALUES 
('Dólar Estadounidense', 'US$'),
('Euro', '€'),
('Peso Chileno', '$');

-- Insertamos usuarios asignándoles un currency_id 
INSERT INTO usuarios (nombre, correo_electronico, contraseña, saldo, currency_id) VALUES 
('Alejandro García', 'ale.garcia@email.com', 'hash_secreto_1', 1500.50, 1),
('Beatriz López', 'b.lopez@email.com', 'hash_secreto_2', 2800.00, 1),
('Carlos Ruiz', 'cruiz@email.com', 'hash_secreto_3', 50.75, 2),
('Diana Pérez', 'diana.p@email.com', 'hash_secreto_4', 10200.00, 3);

INSERT INTO transaccion (sender_user_id, receiver_user_id, importe) VALUES 
(1, 2, 100.00), 
(2, 3, 50.00),  
(4, 1, 500.00), 
(3, 4, 10.25),  
(2, 4, 250.00);

---
--- CONSULTAS Y OPERACIONES ---
---

-- Consultar nombre de usuario y su moneda
SELECT u.nombre, m.currency_name 
FROM usuarios u
JOIN moneda m ON u.currency_id = m.currency_id
WHERE u.user_id = 1;

-- Ver todas las transacciones
SELECT * FROM transaccion;

-- Ver transacciones de un emisor específico
SELECT * FROM transaccion 
WHERE sender_user_id = 1;

-- Actualizar correo
UPDATE usuarios 
SET correo_electronico = 'nuevo_correo@email.com' 
WHERE user_id = 2;

-- Borrar una transacción
DELETE FROM transaccion 
WHERE transaction_id = 5;



--Demostración de Transacción Exitosa 

BEGIN; -- Inicia la transacción

-- 1. Restar saldo al emisor (Alejandro)
UPDATE usuarios 
SET saldo = saldo - 100.00 
WHERE user_id = 1 AND saldo >= 100.00;

-- 2. Sumar saldo al receptor (Beatriz)
UPDATE usuarios 
SET saldo = saldo + 100.00 
WHERE user_id = 2;

-- 3. Registrar el movimiento
INSERT INTO transaccion (sender_user_id, receiver_user_id, importe) 
VALUES (1, 2, 100.00);

COMMIT; -- Confirma todos los cambios


--Simulación de Error y ROLLBACK

BEGIN;

-- Intentamos restar saldo a un usuario real
UPDATE usuarios SET saldo = saldo - 50.00 WHERE user_id = 1;

-- SIMULAMOS EL ERROR: Intentamos enviar dinero a un usuario ID 999 (que no existe)
-- Esto disparará un error de "Foreign Key Violation"
INSERT INTO transaccion (sender_user_id, receiver_user_id, importe) 
VALUES (1, 999, 50.00); 

-- Al fallar la línea de arriba, PostgreSQL "aborta" la transacción.
-- Ningún cambio (ni siquiera el UPDATE del paso 1) se aplicará.

ROLLBACK; -- Deshace el descuento de los 50.00 del paso 1