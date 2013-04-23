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

run:
    ./manage.py

edit Apache/nginx etc.

uWSGI:

in /etc/uwsgi/apps-available:


    sudo nano trackme.xml


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