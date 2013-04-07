Tracker
=======

Tracking system

Requirements:
Postgre GIS
vertualenv 1.9

To install:
cd /opt/
mkdir Tracker
virtualenv --distribute Tracker/v1
source source Tracker/v1/bin/activate 

git clone git://github.com/WFP-Dubai/Tracker.git

cd Tracker/tracer
pip install -r requirements.txt

Edit settings.py for db

edit Apache/nginx etc.

