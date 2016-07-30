sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
sudo gunicorn --bind 127.0.0.1:8000 SnabService.wsgi:application
