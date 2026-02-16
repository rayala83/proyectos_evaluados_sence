# Sistema de Gestión de Clientes (POO)

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar diferentes tipos de clientes (Regulares, Premium y Corporativos) aplicando los pilares de la Programación Orientada a Objetos y persistencia de datos en formato JSON.

## 📂 Estructura de Archivos

La carpeta del proyecto está organizada de la siguiente manera:

* **`main.py`**: Es el punto de entrada del programa. Contiene el menú interactivo y la lógica de captura de datos por consola.
* **`cliente.py`**: Contiene la definición de la clase base `Cliente` y las subclases `ClientePremium` y `ClienteCorporativo`. Aquí se aplica la herencia y el polimorfismo.
* **`gestion.py`**: Contiene la clase `GestionClientes`, encargada de administrar la lista de objetos, realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y manejar la lectura/escritura del archivo JSON.
* **`utilidades.py`**: Incluye funciones de validación (nombre, email, teléfono, montos) que aseguran la integridad de los datos mediante el manejo de excepciones.
* **`clientes.json`**: Archivo donde se almacenan los datos de forma permanente. Se crea automáticamente al ejecutar el programa por primera vez.

## 🚀 Cómo ejecutar el proyecto

Para poner en marcha el sistema, no necesitas instalar librerías externas ni configurar rutas complejas. Sigue estos pasos:

1. Abre la carpeta completa del proyecto en **Visual Studio Code**.
2. Abre el archivo **`main.py`** en el editor.
3. Presiona el botón **Run** (el icono de "Play" en la esquina superior derecha de VS Code) o presiona la tecla `F5`.

## ✨ Características Principales

* **Validación Robusta:** Uso de `try-except` y `raise` para evitar ingresos de datos erróneos.
* **Persistencia:** Los datos se guardan automáticamente en un archivo JSON cada vez que se agrega, edita o elimina un registro.
* **Escalabilidad:** Gracias a la arquitectura POO, es sencillo añadir nuevos tipos de clientes o funcionalidades sin afectar el código existente.

---

### Notas de uso

* Asegúrate de tener instalada una versión de **Python 3.x**.
* Al actualizar un cliente, puedes presionar **Enter** para mantener el valor actual del campo.