Tracker
=======

Tracking system
***
Requirements:

* Postgre GIS
* virtualenv 1.9
Ubuntu/Debian:


    sudo aptitude install binutils libproj-dev gdal-bin libgeoip1 gdal-bin python-gdal 
    sudo pip install --upgrade pip

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

