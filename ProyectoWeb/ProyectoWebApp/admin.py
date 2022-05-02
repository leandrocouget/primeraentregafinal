from django.contrib import admin

# Register your models here.
from .models import register, articles, contact

admin.site.register(register)
admin.site.register(articles)
admin.site.register(contact)

