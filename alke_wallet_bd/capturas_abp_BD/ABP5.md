# Evaluación Integradora: Alke Wallet (abp5)
## Fundamentos de bases de datos relacionales

### Paso 1 — Crear la Base de Datos

![Crear la base de datos AlkeWallet](imagen1.png)

![Otorgar Permiso base de datos AlkeWalletl](imagen2.png)

![Otorgar Permiso Shema base de datos AlkeWallet](imagen3.png)

![Ver base de datos AlkeWallet](imagen4.png)

---

### Paso 2 — Crear las 3 Tablas (DDL)

![Tabla Usuarios base de datos AlkeWallet](imagen5.png)

![Tabla Moneda base de datos AlkeWallet](imagen6.png)

![Tabla Transacción base de datos AlkeWallet](imagen7.png)

---

### Paso 3 — Insertar Datos de Prueba (DML)

![Inserción Monedas en tabla Moneda](imagen8.png)

![Inserción Usuarios en tabla Usuarios](imagen9.png)

![Inserción Transacciones en tabla Transacción](imagen10.png)

---

### Paso 4 — Las 5 Consultas Requeridas

#### 1. Obtener el nombre de la moneda elegida por un usuario específico
![Resultados Consulta moneda usuario](imagen11.png)

#### 2. Obtener todas las transacciones registradas
![Resultados Consulta Transacciones](imagen12.png)

#### 3. Obtener todas las transacciones realizadas por un usuario específico
![Resultados Consulta transacción usuario](imagen13.png)

#### 4. Modificar el correo electrónico de un usuario específico
![Resultados Consulta antes del Update](imagen14.png)
![Consulta actualiza correo](imagen15.png)
![Resultados Consulta después del Update](imagen16.png)

#### 5. Eliminar los datos de una transacción
![Resultados Consulta antes del delete](imagen17.png)
![Consulta borrar transaccion](imagen18.png)
![Resultados Consulta después del delete](imagen19.png)

---

### Paso 5 — Transaccionalidad (ACID)

![Código de la transacción con COMMIT](imagen20.png)
![Error provocado y ROLLBACK](imagen22.png)