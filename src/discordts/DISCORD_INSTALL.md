# install discord bot 
## install all via shell scripts
    #install python3.7 if needed
        $ ./python37-install.sh
    
    #install discord.py and project dependencies
        $ ./discord-install.sh
    
## install Python 3.7 install (ubuntu 14.0.4)
    #ref: https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
    #install python3.7 if needed
        $ sudo apt-get install build-essential checkinstall
        $ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
        $ cd /usr/src
        $ sudo wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
        $ sudo tar xzf Python-3.7.3.tgz
        $ cd Python-3.7.3
        $ sudo ./configure --enable-optimizations
        $ sudo make altinstall

## install dependencies
    #install discord.py and project dependencies
        $ python3.7 -m pip install discord.py
        $ python3.7 -m pip install PyMySQL
        $ python3.7 -m pip install python-binance
    
## run
    $ python3.7 server_join.py
