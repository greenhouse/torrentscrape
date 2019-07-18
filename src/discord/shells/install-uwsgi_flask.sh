#set -e

#ref: uwsgi_common_tasks.txt
# install uwsgi
sudo apt-get install uwsgi
sudo apt-get install uwsgi-plugins-all
sudo apt-get install uwsgi-extra

# install flask w/ python3.7
sudo apt-get install python3-pip
python3.7 -m pip install --upgrade pip
python3.7 -m pip install flask

# install flask w/ python2
sudo apt-get install python-pip
python2 -m pip install --upgrade pip
python2 -m pip install flask


