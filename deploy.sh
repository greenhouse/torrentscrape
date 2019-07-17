sudo pkill -f uwsgi -9
sudo uwsgi --enable-threads --ini ./src/deploy.ini
