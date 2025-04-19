from django.contrib import admin
from .models import *
from mainapp.models import ContactMessage

admin.site.register(ContactMessage)
