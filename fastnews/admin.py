from django.contrib import admin
from . import models

admin.site.register(models.Article)
admin.site.register(models.ArticleLike)
admin.site.register(models.Attachment)
admin.site.register(models.Comment)
admin.site.register(models.CommentLike)
admin.site.register(models.Debate)
admin.site.register(models.Notification)
admin.site.register(models.Settlement)
admin.site.register(models.User)
admin.site.register(models.UserSubscribe)
