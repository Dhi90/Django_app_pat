import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_analysis_project.settings')

application = get_wsgi_application()