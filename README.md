Tracker
=======

Tracking system
***
Requirements:

* Postgre GIS
* uWSGI
* virtualenv 1.9

Ubuntu/Debian:



    sudo aptitude install binutils libproj-dev gdal-bin libgeoip1 gdal-bin python-gdal 
    sudo pip install --upgrade pip
    sudo pip install virtualenv

****
To install:


    cd /opt/
    mkdir Tracker
    virtualenv --distribute Tracker/v1
    source Tracker/v1/bin/activate
    git clone git://github.com/WFP-Dubai/Tracker.git
    cd Tracker/tracker
    pip install -r requirements.txt

Edit settings.py for db


edit Apache/nginx etc.

uWSGI:

in /etc/uwsgi/apps-available:


    sudo nano trackme.xml

enter:

    <uwsgi>
      <plugin>python</plugin>
      <socket>:3032</socket>
      <chdir>/opt/Tracker/tracker</chdir>
      <pythonpath>..</pythonpath>
      <module>wsgi</module>
      <virtualenv>/opt/Tracker/v1</virtualenv>
    </uwsgi>

sudo ln -s /etc/uwsgi/apps-available/trackme.xml /etc/uwsgi/apps-enabled/trackme.xml

NGINX:

in /etc/nginx/sites-available

    sudo nano trackme

enter:

    server {
      listen 80;
      server_name qa.trackme.pro trackme-qa.globalepic.lu trackme-qa.globalepic.org trackme-qa; 

      access_log /var/log/nginx/trackme-qa_access.log;
      error_log /var/log/nginx/trackme-qa_error.log;
      location /static/ {
        alias /opt/Tracker/tracker/static_root/;
        expires 5d;
      }

      location /media/ {
        alias /opt/Tracker/tracker/media/;
        expires 5d;
      }


      location / {
    uwsgi_pass 127.0.0.1:3032;
    include uwsgi_params;  

      }

    }

Do:
    sudo ln -s /etc/nginx/sites-available/trackme /etc/nginx/sites-enabled/trackme
    
    
run:


    ./manage.py