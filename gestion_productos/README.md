# Sistema de Gestión de Inventario (Python CLI)

Este es un sistema de gestión de productos desarrollado en Python, diseñado bajo principios de modularidad, código limpio (PEP 8) y estructuras de datos eficientes. Permite administrar un catálogo de productos de manera dinámica a través de una interfaz de consola.

## 🚀 Funcionalidades

- **Gestión de Stock:** Permite agregar nuevos productos o actualizar la cantidad de los existentes.
- **Eliminación:** Borrado selectivo de productos mediante su identificador (nombre).
- **Reportes:** Visualización estructurada y formateada del inventario actual.
- **Validación de Datos:** Control de errores para evitar ingresos de datos no numéricos en precios o cantidades.

---

## 🛠️ Arquitectura del Sistema

El sistema está dividido en dos módulos para separar la lógica de negocio de la interfaz:

1.  **`inventario.py`**: Contiene la lógica pura del sistema (funciones de procesamiento de datos).
2.  **`main.py`**: Contiene el bucle principal, el menú interactivo y la gestión de entrada/salida.



---

## 📊 Documentación Técnica

### Estructura de Datos
El núcleo del sistema utiliza un **Diccionario de Diccionarios**. Esta estructura permite búsquedas rápidas con una complejidad de $O(1)$.

**Ejemplo de organización:**
```python
{
    "Producto": {
        "cantidad": int,
        "precio": float
    }
}