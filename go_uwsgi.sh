sudo apt install python3.6 python3.6-dev uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev
cd ~
export PYTHON=python3.6
uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36"
sudo mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so
sudo chmod 644 /usr/lib/uwsgi/plugins/python36_plugin.so
