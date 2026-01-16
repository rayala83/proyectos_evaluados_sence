# 🏦 Alke Wallet - Sistema de Gestión Bancaria (Prototipo)

Este es un proyecto de billetera digital (E-Wallet) desarrollado como un prototipo funcional para prácticas de desarrollo web del curso talento Digital de SENCE. Permite gestionar ingresos, egresos y visualizar el historial de transacciones utilizando almacenamiento local.

## 🚀 Cómo ejecutar el proyecto

Este proyecto está diseñado a nivel de **pruebas y desarrollo local**, por lo que no requiere de un servidor backend real.

1. **Requisito previo:** Tener instalado [Visual Studio Code](https://code.visualstudio.com/).
2. **Extensión necesaria:** Instala la extensión **"Live Server"** de VS Code.
3. **Instrucciones:**
   - Abre la carpeta del proyecto en VS Code.
   - Haz clic derecho sobre el archivo  `login.html`.
   - Selecciona la opción **"Open with Live Server"**.
   - El navegador se abrirá automáticamente en la dirección `http://127.0.0.1:5500`.

---

## 🔑 Credenciales de Acceso

Para ingresar al sistema, utiliza las siguientes credenciales configuradas en el script de validación:

* **Email:** `email@email.com`
* **Password:** `12345`

---

## 🛠️ Funciones Principales

El sistema cuenta con las siguientes funcionalidades operativas:

* **Autenticación de Usuario:** Validación simple para el acceso al menú principal.
* **Gestión de Saldo:** Visualización dinámica del dinero disponible en la cuenta.
* **Depósito de Dinero:** Permite sumar montos al saldo actual y actualiza el almacenamiento en tiempo real.
* **Transferencia a Contactos:** * Selección de contactos predefinidos.
    * Validación de saldo suficiente antes de realizar el envío.
    * Posibilidad de agregar nuevos contactos mediante un formulario modal(**solo como simulacion**).
* **Historial de Movimientos:** * Registro automático de cada operación (Depósitos y Transferencias).
    * Diferenciación visual (Verde para ingresos, Rojo para egresos).
    * Opción para limpiar el historial de transacciones.

---

## 💻 Tecnologías Utilizadas

* **HTML5 / CSS3:** Estructura y diseño personalizado con un marco moderno.
* **Bootstrap 5 (CDN):** Framework para el diseño responsivo, componentes (cards, modales, botones) y espaciados.
* **jQuery 3.7:** Manipulación del DOM, manejo de eventos y lógica del negocio.
* **LocalStorage:** Persistencia de datos para que el saldo y los movimientos no se pierdan al recargar la página.

---

> **Nota:** Este proyecto es estrictamente para fines educativos. Las contraseñas y datos se manejan en el lado del cliente (frontend) y no deben ser utilizados para aplicaciones reales que requieran seguridad de datos sensible.
