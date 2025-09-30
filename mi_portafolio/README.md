# Mi Portafolio - Proyecto Corte 1 (skeleton)

## Qué contiene
Estructura base de un proyecto Django con una app `core` que incluye:
- Modelos: Profile, Project, FAQ, OpenItem, ContactMessage
- Templates: base, home, contactame, fyq, open, open_detail
- Static: css and js minimal
- Integración preparada para GTM/GA4 (placeholders)

## Instrucciones rápidas (desarrollo local)
1. Crear entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # linux/mac
   .venv\Scripts\activate    # windows
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Migraciones y superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Ejecutar servidor:
   ```bash
   python manage.py runserver
   ```
5. Cargar datos en admin:
   - Accede a `/admin/` y crea un `Profile`, algunos `Project`, `FAQ`, `OpenItem`.
   - Sube imágenes si quieres (asegúrate de configurar MEDIA settings si usas producción).

## Enlaces útiles para entrega
- Agrega tu snippet de Google Tag Manager en `templates/base.html` (marcado como REEMPLAZAR_GTM_HEAD y REEMPLAZAR_GTM_BODY).
- Asegúrate de usar URLs con UTM para los banners en `templates/home.html`.
- Para producción, configura variables de entorno y un almacenamiento para `media/`.

## Notas
Este repositorio es un esqueleto. Modifica `mi_portafolio/settings.py` para tus valores y para producción (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB config).
