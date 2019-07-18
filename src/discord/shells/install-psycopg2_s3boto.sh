#set -e

# install psycopg2 w/ python2
sudo apt-get install python-psycopg2
sudo apt-get install python-pip
python2 -m pip install psycopg2

# install psycopg2 w/ python3
sudo apt-get install python3-psycopg2
sudo apt-get install python3-pip
python3 -m pip install psycopg2
# NOTE: install psycopg2 w/ python3.7 throws error
#  $ python3.7 -m pip install psycopg2

# install AWS s3 boto w/ python2
python2 -m pip install -U boto

# install AWS s3 boto w/ python3.7
python3.7 -m pip install -U boto


