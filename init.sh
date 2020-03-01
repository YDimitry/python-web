#!/bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s ~/web/etc/helloapp /etc/init.d/helloapp
#sudo ln -s ~/web/etc/gunicorn.service /etc/systemd/system/gunicorn.service
sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate

sudo /etc/init.d/helloapp start
sudo /etc/init.d/nginx restart
sudo apt update
sudo apt install python3.5
sudo apt install mc

virtualenv -p python3.5 env
source env/bin/activate
pip install gunicorn django==2.1
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi



#sudo systemctl restart nginx

#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start