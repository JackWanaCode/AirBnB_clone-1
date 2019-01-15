#!/bin/bash
#sets up your web servers for the deployment of web_static
setup NGINX and directory for web static
sudo apt-get update
sudo apt-get -y install nginx
echo "Holberton School" | sudo tee /usr/share/nginx/html/index.html
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo "fake content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "/^\tserver_name localhost;/a location \/hbnb_static \{\n\t\talias \
/data/web_static/current/;\n\t\}" /etc/nginx/sites-available/default
sudo service nginx reload
