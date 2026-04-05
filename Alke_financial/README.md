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
    │   └── contacts
    │       ├── deleted.html
    │       ├── detail.html
    │       ├── form.html
    │       └── list.html         
    └── static/
        └── style.css           
```
---

## 🧩 Flujo de una petición

Al momento de ingresar al navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000), mostrará la página principal del proyecto, la cual es el login que podras acceder con el susper ususario creado anterioemente, te pedira el correo y la contraseña, una vez en la pagina principal te mostrara un dashboard con el saldo y as accioes que puedes realizar, debes ingresarte dinero,ahi utilizaremos el service deposit_money que permitira tenr el saldo reflejado en el panel principa y en movimientos, tambien podras realizar transacciones, mediate transfer.html donde te permitia agregar un destinatario mostrando un form simple que registra un nuevo contacto al cual le podras enviar diner con el service transfer_money el cual descontara de tu saldo y se vera reflejado en los movimientos, y en el dashboard princial, finalmente si queires salir ted deslogueas en la barra de navegacion, enviando te fuera y dejandote en la pantall de login nuevamente.

---
## 5. Dificultades encontradas

Tube probleas para organizar los meodelos corretamente para poder reflejar movimientos ya sea de deposito o de transfeencias por que, en el abp 2 esto era estatico y se realiaba con javascript, y aca use servicios, lo cual me obligaba a que mis modelos fueran concordasntes con las accioes requeridas. tube confucion de abp y olvide el crud, pero use el modeo contacto para poder solucionar el problema a tiempo. 


---

## 6.  Preguntas de Cierre 

### Sobre los Modelos

#### ¿Qué modelos definiste y por qué elegiste esos? 
En mi aplicación definí tres modelos principales:

- User: representa a los usuarios de la plataforma, incluyendo su saldo (balance). Es el actor principal del sistema.
- Contact: permite a cada usuario guardar destinatarios frecuentes sin que necesariamente estén registrados en la plataforma. Esto simula el comportamiento real de una billetera digital.
- Transaction: modela todos los movimientos de dinero, incluyendo depósitos, transferencias entre usuarios y transferencias a contactos.

👉 Elegí estos modelos porque separan claramente las responsabilidades:
el usuario autentifica, los coantactos sirven para realiar movimientos, y las transacciones par realizar depositos y trasnferencias.


#### ¿Qué tipo de relación usaste entre tus modelos (ForeignKey, OneToOne, ManyToMany)? ¿Por qué esa y no otra?

Utilicé principalmente ForeignKey:

- Contact → User (owner)
- Transaction → User (sender y receiver)
- Transaction → Contact

👉 Elegí ForeignKey porque:

representa relaciones uno a muchos, donde un usuario puede tener muchos contactos y por otra parte un usuario puede tener muchas transacciones.

#### ¿Qué valor le pusiste a on_delete en tus relaciones y por qué?

- CASCADE en relaciones con User (por ejemplo sender/receiver)
- SET_NULL en contact dentro de Transaction

👉 Justificación:

CASCADE: si se elimina un usuario, sus transacciones asociadas también se eliminan para mantener consistencia.
SET_NULL: en el caso de contactos, si se elimina el contacto, la transacción sigue existiendo como historial, pero sin referencia directa.



### Sobre el ORM

#### ¿Qué métodos del ORM usaste para cada operación CRUD? Nombra al menos uno por operación.

👉 Metodos:

Para el create use save, al igual que para el update, para el leer get y filter y para eliminar el metodo delete.

#### ¿Qué método usaste en tu vista de filtro/búsqueda para construir la consulta?

👉 Metodos:
Para listar los contactos en las busquedas use filter() junto a Q() para construir consultas dinamicas.

#### ¿Cuál es la diferencia entre .get() y .filter()? ¿Cuándo usarías cada uno?

👉 Diferencias:

- .get():
devuelve un solo objeto
lanza error si no existe o hay más de uno

- .filter():
devuelve un QuerySet (lista)
puede traer cero, uno o muchos resultados

👉 Uso:

- .get() → cuando espero un único registro (por ID)
- .filter() → cuando busco múltiples resultados o filtros

### Sobre las Migraciones

#### ¿Qué pasaría si modificas un modelo pero NO generas una nueva migración?

👉 La base de datos queda desincronizada con el código.

Esto puede causar:

- errores al insertar datos
- campos que no existen
- fallos en tiempo de ejecución


#### ¿Dónde se almacenan los archivos de migración y para qué sirven?

Se almacenan en:

wallet/migrations/

👉 Sirven para:

versionar cambios en la base de datos, ademas de permitir que Django aplique esos cambios automáticamente y asi mantener consistencia entre entornos.


### Sobre la Arquitectura

#### ¿Por qué es importante que la lógica de base de datos esté en las VISTAS y no en los TEMPLATES?

Principalmente  porque los templates son solo la presentacion, si se pone la logica  ahi se rompe con la separacion de responsabilidades, y hace dificil la mantencion de ese codigo, la logica siempre sebe estar e los view o en services.


#### ¿Cuál es el flujo completo de una solicitud en Django? (desde que el usuario hace clic hasta que ve el resultado)

👉 Flujo:

1. El usuario una vez en la pagina inicial da click en la barra de bavegacion  en la opcion contactos, luego en nuevo contacto y accede a la URL:/contacts/create/ 
2. Django busca esa ruta en urls.py y la asocia a la vista contact_create.
3. La vista revisa el método de la petición:
   - Si es GET → muestra el formulario vacío
   - Si es POST → procesa los datos enviados
4. Cuando el usuario envía el formulario:
   - La vista recibe los datos (request.POST)
   - Se crea un ModelForm (ContactForm)
5. Django guarda el registro en la base de datos.
6. La vista redirige al usuario a /contacts/.
7. El navegador muestra la lista actualizada.




