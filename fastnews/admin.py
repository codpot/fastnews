from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.Debate)
admin.site.register(models.Settlement)
admin.site.register(models.User)
