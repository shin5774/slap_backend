from django.contrib import admin
from .models import PlantsSection
from user.models import User
# Register your models here.

admin.site.register(PlantsSection)
admin.site.register(User)