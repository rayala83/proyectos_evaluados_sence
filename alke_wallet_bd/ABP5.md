# Evaluación Integradora: Alke Wallet (abp5)
## Fundamentos de bases de datos relacionales

### Paso 1 — Crear la Base de Datos

![Crear la base de datos AlkeWallet](capturas_abp_BD/imagen1.png)  
*Figura 1: Crear la base de datos AlkeWallet*

![Configuración inicial](capturas_abp_BD/imagen2.png)  
*Figura 2: Otorgar Permiso base de datos AlkeWallet*

![Otorgar Permiso base de datos AlkeWallet](capturas_abp_BD/imagen3.png)  
*Figura 3: Otorgar Permiso Shema Public base de datos AlkeWallet*

![Ver base de datos AlkeWallet](capturas_abp_BD/imagen4.png)  
*Figura 4: Ver base de datos AlkeWallet*

---

### Paso 2 — Crear las 3 Tablas (DDL)

![Tabla Usuarios base de datos AlkeWallet](capturas_abp_BD/imagen5.png)  
*Figura 5: DESCRIBE Tabla Usuarios base de datos AlkeWallet*

![Tabla Moneda base de datos AlkeWallet](capturas_abp_BD/imagen6.png)  
*Figura 6: DESCRIBE Tabla Moneda base de datos AlkeWallet*

![Tabla Transacción base de datos AlkeWallet](capturas_abp_BD/imagen7.png)  
*Figura 7: DESCRIBE Tabla Transacción base de datos AlkeWallet*

---

### Paso 3 — Insertar Datos de Prueba (DML)

![Inserción Monedas en tabla Moneda](capturas_abp_BD/imagen8.png)  
*Figura 8: Inserción Monedas en tabla Moneda, base de datos AlkeWallet*

![Inserción Usuarios en tabla Usuarios](capturas_abp_BD/imagen9.png)  
*Figura 9: Inserción Usuarios en tabla Usuarios, base de datos AlkeWallet*

![Inserción Transacciones en tabla Transacción](capturas_abp_BD/imagen10.png)  
*Figura 10: Inserción Transacciones en tabla Transacción, base de datos AlkeWallet*

---

### Paso 4 — Las 5 Consultas Requeridas

#### 1. Obtener el nombre de la moneda elegida por un usuario específico
![Resultados Consulta moneda usuario](capturas_abp_BD/imagen11.png)  
*Figura 11: Resultados Consulta moneda usuario específico*

#### 2. Obtener todas las transacciones registradas
![Resultados Consulta Transacciones](capturas_abp_BD/imagen12.png)  
*Figura 12: Resultados Consulta Transacciones*

#### 3. Obtener todas las transacciones realizadas por un usuario específico
![Resultados Consulta transacción usuario](capturas_abp_BD/imagen13.png)  
*Figura 13: Resultados Consulta transacción usuario específico*

#### 4. Modificar el correo electrónico de un usuario específico
![Resultados Consulta antes del Update](capturas_abp_BD/imagen14.png)  
*Figura 14: Resultados Consulta antes del Update*

![Consulta actualiza correo](capturas_abp_BD/imagen15.png)  
*Figura 15: Consulta actualiza correo usuario específico*

![Resultados Consulta después del Update](capturas_abp_BD/imagen16.png)  
*Figura 16: Resultados Consulta después de la actualización*

#### 5. Eliminar los datos de una transacción
![Resultados Consulta antes del delete](capturas_abp_BD/imagen17.png)  
*Figura 17: Resultados Consulta antes del delete*

![Consulta borrar transaccion](capturas_abp_BD/imagen18.png)  
*Figura 18: Consulta borrar transacción*

![Resultados Consulta después del delete](capturas_abp_BD/imagen19.png)  
*Figura 19: Resultados Consulta después de borrar transacción*

---

### Paso 5 — Transaccionalidad (ACID)

![Código de la transacción con COMMIT](capturas_abp_BD/imagen20.png)  
*Figura 20: Implementación de transferencia de fondos (COMMIT)*

![Código de la transacción con COMMIT](capturas_abp_BD/imagen21.png)  
*Figura 20: Resultados DBeaver (COMMIT)*

![Error provocado y ROLLBACK](capturas_abp_BD/imagen22.png)  
*Figura 21: Simulación de error de integridad y reversión (ROLLBACK)*

![Error provocado y ROLLBACK](capturas_abp_BD/imagen23.png)  
*Figura 21: Resultados DBeaver (ROLLBACK)*