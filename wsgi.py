import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horilla.settings')

application = get_wsgi_application()
app = application  # Add this line for Vercel