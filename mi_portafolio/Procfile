release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata core/fixtures/initial_data.json
web: gunicorn mi_portafolio.wsgi --log-file -
