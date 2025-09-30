# Mi Portafolio

Sitio web de portafolio desarrollado con Django como CMS.

## Requisitos

- Python 3.8+
- Django 4.2

## Instalación

1. Clona o descarga el proyecto.
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Ejecuta las migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```
7. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```

## Configuración

### Google Tag Manager y Google Analytics

1. Reemplaza 'GTM-XXXXXXX' en `base.html` con tu ID de GTM real.
2. Configura GA4 en GTM.
3. Añade eventos personalizados para los banners.

### Contenido

- Accede al admin en `/admin/` para gestionar FAQs y productos.
- Sube imágenes de productos en el admin.
- Añade tu foto de perfil en `core/static/images/profile.jpg`.

## Despliegue

El proyecto está preparado para desplegar en plataformas como Vercel, Railway o Netlify.

Para producción, configura:
- `DEBUG = False`
- Variables de entorno para SECRET_KEY
- ALLOWED_HOSTS
- Base de datos externa si es necesario

## Estructura del Proyecto

- `core/`: App principal
- `mi_portafolio/`: Configuración del proyecto
- `templates/`: Plantillas HTML
- `static/`: Archivos CSS y JS
