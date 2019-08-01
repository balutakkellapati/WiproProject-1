from django.contrib import admin
from .models import Category, Question, Organization, Assessment


admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Organization)
admin.site.register(Assessment)