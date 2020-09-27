import os
import django 
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings.pro')
django.setup()
application = get_asgi_application()
