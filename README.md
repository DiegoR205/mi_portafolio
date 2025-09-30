# Mi Portafolio

## Descripción
Este es un sitio web de portafolio personal desarrollado con Django. Permite mostrar información personal, proyectos, preguntas frecuentes (FAQ), elementos abiertos (como ideas o proyectos abiertos), y un formulario de contacto.

## Características
- **Página de Inicio**: Muestra el perfil personal y una lista de proyectos.
- **Contacto**: Formulario para enviar mensajes de contacto.
- **Preguntas Frecuentes (FAQ)**: Lista de preguntas y respuestas.
- **Elementos Abiertos**: Lista de ideas o proyectos abiertos con detalles.
- **Administración**: Panel de administración de Django para gestionar contenido.
- **Responsive**: Diseño adaptable a diferentes dispositivos.

## Tecnologías Utilizadas
- **Backend**: Django 4.2
- **Base de Datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Imágenes**: Pillow para manejo de imágenes
- **Email**: Configurado con Gmail SMTP

## Instalación
1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd mi_portafolio
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración:
   ```
   python manage.py createsuperuser
   ```

6. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

7. Abre tu navegador y ve a `http://127.0.0.1:8000/`

## Uso
- **Página de Inicio**: `http://127.0.0.1:8000/`
- **Contacto**: `http://127.0.0.1:8000/contactame/`
- **FAQ**: `http://127.0.0.1:8000/fyq/`
- **Elementos Abiertos**: `http://127.0.0.1:8000/open/`
- **Administración**: `http://127.0.0.1:8000/admin/`

Para agregar contenido, inicia sesión en el panel de administración y crea instancias de Profile, Project, FAQ, OpenItem.

## Estructura del Proyecto
```
mi_portafolio/
├── core/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── contactame.html
│   │   ├── fyq.html
│   │   ├── open.html
│   │   ├── open_detail.html
│   │   └── contact_success.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── mi_portafolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
└── .gitignore
```

## Configuración de Email
Para que el formulario de contacto envíe emails, configura las credenciales en `settings.py`:
- EMAIL_HOST_USER: Tu email de Gmail
- EMAIL_HOST_PASSWORD: Tu contraseña de aplicación de Gmail

## Contribución
Si deseas contribuir:
1. Haz un fork del proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-feature`).
3. Commit tus cambios (`git commit -am 'Agrega nueva feature'`).
4. Push a la rama (`git push origin feature/nueva-feature`).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Autor
Diego Rojas Martínez - diegorojasmartinez20@gmail.com
