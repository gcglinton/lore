from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(SBDA)
admin.site.register(People)
admin.site.register(Experiment)
