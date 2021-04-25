migrate: python manage.py migrate
web: daphne -b 0.0.0.0 -p $PORT connector.asgi:application 
worker: python manage.py runworker channels
