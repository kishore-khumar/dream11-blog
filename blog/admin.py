from django.contrib import admin
from .models import Matches,Update,Comment

# Register your models here.
admin.site.register(Matches)
admin.site.register(Update)
admin.site.register(Comment)