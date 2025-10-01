# TODO: Deploy Django Project to Railway

## Completed
- [x] Update requirements.txt with production dependencies (psycopg2-binary, gunicorn, whitenoise, dj-database-url)
- [x] Update settings.py for production:
  - [x] Import dj_database_url
  - [x] Set SECRET_KEY from env
  - [x] Set DEBUG from env (default False)
  - [x] Set ALLOWED_HOSTS to ['*']
  - [x] Configure DATABASES with dj_database_url
  - [x] Add whitenoise middleware
  - [x] Add STATIC_ROOT
  - [x] Update EMAIL_HOST_USER and EMAIL_HOST_PASSWORD to env only

## Pending
- [ ] Commit changes to git
- [ ] Push to GitHub repository
- [ ] Create Railway project and connect to GitHub repo
- [ ] Set environment variables in Railway:
  - SECRET_KEY: Generate a new secret key
  - DEBUG: False
  - DATABASE_URL: Provided by Railway PostgreSQL
  - EMAIL_HOST_USER: Your Gmail
  - EMAIL_HOST_PASSWORD: Your Gmail app password
- [ ] Run migrations on Railway (if needed, Railway may auto-run)
- [ ] Test the deployed site: home, contact, FAQ, products
- [ ] Verify static files and styles are loading
- [ ] Verify email functionality
