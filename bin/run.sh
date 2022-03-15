cd mysite

# Run migrations
./manage.py migrate --noinput

gunicorn --bind 0.0.0.0:8080 mysite.wsgi -w 9 -t 200
