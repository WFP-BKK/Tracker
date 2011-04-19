import os
import sys
sys.path.append('/Users/carlander/projects/epic/python_workspace/tracker')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()