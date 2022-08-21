from django.contrib import admin
from .models import Entry, UserProfile,Project

admin.site.register(Entry)
admin.site.register(UserProfile)
admin.site.register(Project)