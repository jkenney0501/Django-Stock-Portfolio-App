from django.contrib import admin
from .models import Stock

# Register your models here.
# this file handles the admin area, to add stock quotes to db
admin.site.register(Stock)
