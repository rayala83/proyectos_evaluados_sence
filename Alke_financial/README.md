# 💰 Wallet App - Django

Aplicación web de billetera digital desarrollada con Django, como parte del proyecto ABP 7.

---

## 🚀 Descripción del Proyecto

Este proyecto simula el comportamiento básico de una billetera digital, permitiendo, el registro mediate autentificacion del usuario, permitiendole gestionar su saldo contable, agreagndo usaurios para transferir dinero y a su vez la pisibilidad de realizar depositos en su cuenta, tambien cuenta con un visor de movimeintos y un dashboard en la pagina inicial, sus paginas principales son:

- dashboard
- deposit
- transfer
- transactions

---

## ▶️ ¿Cómo instalar y correr?

```bash
Antes de empezar necesitas tener instalado:

- **Python 3.12+** — [Descargar aquí](https://www.python.org/downloads/)
- **Git** — [Descargar aquí](https://git-scm.com/downloads)

Para verificar que los tienes, abre una terminal y escribe:

```bash
python3 --version   # Debería mostrar 3.12 o superior
git --version        # Debería mostrar la versión de git
```

---
### levantar el proyecto

#### 1. Clonar el repositorio

```bash
git clone https://github.com/rayala83/proyectos_evaluados_sence.git
cd Alke_financial
```

```bash
o descargar el zip y copiarlo en su computadora
```

#### 2. Crear el entorno virtual

Un entorno virtual es una "caja aislada" donde instalamos las dependencias del proyecto sin afectar el resto de tu computador.

```bash
python3 -m venv venv
```

#### 3. Activar el entorno virtual

**Cada vez** que abras una terminal nueva para trabajar en el proyecto, debes activar el entorno:

```bash
# En Linux / Mac:
source vrnv/bin/activate

# En Windows:
venv\Scripts\activate
```

> 💡 **¿Cómo sé que está activo?** Vas a ver `(venv)` al inicio de la línea en tu terminal.

#### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 5. Configurar las variables de entorno (archivo `.env`)

El archivo `.env` contiene las credenciales y configuraciones sensibles del proyecto. **Nunca se sube a git.**

Crea tu propio archivo .env en la raiz del proyecto
```bash
cd Alke_financial
touch .env
```

Genera tu propia `DJANGO_SECRET_KEY`:

```bash
# Con el entorno virtual activo:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copia la clave generada y pégala en tu archivo `.env` en la línea de `DJANGO_SECRET_KEY`.

#### 6. Ejecutar las migraciones

Las migraciones crean las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Crear un superusuario (admin)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla (te pedirá nombre de usuario, email y contraseña).
Este usuario sera para ingresar al login de la app

#### 8. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Para entrar al panel de administración: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
```
```

---
## 🏗️ Estructura del proyecto

El proyecto sigue una arquitectura basada en separación de responsabilidades:

```bash
proyecto wallet
└── alke_financial/
    ├── manage.py
    ├── requirements.txt 
    ├── README-md      
    ├── .gitignore 
    ├── config
    │   ├── settings.py
    │   └── urls.py
    ├── wallet/
    │   ├── views.py      ← Manejo de requests y responses
    │   ├── admin.py
    │   ├── forms.py      ← registro de ususario para trasnferir
    │   ├── models.py     ← Representación de datos (User, Contact, Transaction)
    │   ├── services.py   ← Lógica de negocio desacoplada (transferencias, depósitos)
    │   └── urls.py
    ├── templates/       ← Interfaz de usuario con Django Templates + Bootstrap
    |   ├── base.html  
    │   └── wallet
    │       ├── dashboard.html
    │       ├── deposit.html
    │       ├── login.html
    │       ├── transactions.html
    │       └── transfer.html           
    └── static/
        └── style.css           
```
---

## 🧩 Flujo de una petición

Al momento de ingresar al navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000), mostrará la página principal del proyecto, la cual es el login que podras acceder con el susper ususario creado anterioemente, te pedira el correo y la contraseña, una vez en la pagina principal te mostrara un dashboard con el saldo y as accioes que puedes realizar, debes ingresarte dinero,ahi utilizaremos el service deposit_money que permitira tenr el saldo reflejado en el panel principa y en movimientos, tambien podras realizar transacciones, mediate transfer.html donde te permitia agregar un destinatario mostrando un form simple que registra un nuevo contacto al cual le podras enviar diner con el service transfer_money el cual descontara de tu saldo y se vera reflejado en los movimientos, y en el dashboard princial, finalmente si queires salir ted deslogueas en la barra de navegacion, enviando te fuera y dejandote en la pantall de login nuevamente.


## 5. Dificultades encontradas

Tube probleas para organizar los meodelos corretamente para poder reflejar movimientos ya sea de deposito o de transfeencias por que, en el abp 2 esto era estatico y se realiaba con javascript, y aca use servicios, lo cual me obligaba a que mis modelos fueran concordasntes con las accioes requeridas. 

