#!/bin/bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s ~/web/etc/helloapp /etc/init.d/helloapp
#sudo ln -s ~/web/etc/gunicorn.service /etc/systemd/system/gunicorn.service
sudo /etc/init.d/helloapp start
sudo /etc/init.d/nginx restart
#sudo systemctl restart nginx

#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start