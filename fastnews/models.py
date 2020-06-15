from django.db import models


class Article(models.Model):
    reporter = models.ForeignKey('User', models.DO_NOTHING)
    debate = models.ForeignKey('Debate', models.DO_NOTHING, blank=True, null=True)
    category = models.CharField(max_length=2)
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_cnt = models.IntegerField()
    dislike_cnt = models.IntegerField()
    views = models.IntegerField()
    created_at = models.DateTimeField()


class ArticleLike(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    is_like = models.IntegerField()
    created_at = models.DateTimeField()


class Attachment(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    uuid = models.CharField(max_length=36)
    size = models.BigIntegerField()
    created_at = models.DateTimeField()


class Comment(models.Model):
    debate = models.ForeignKey('Debate', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    content = models.TextField()
    like_cnt = models.IntegerField()
    dislike_cnt = models.IntegerField()
    created_at = models.DateTimeField()


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    is_like = models.IntegerField()
    created_at = models.DateTimeField()


class Debate(models.Model):
    name = models.CharField(max_length=50)
    comment_cnt = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Notification(models.Model):
    uesr = models.ForeignKey('User', models.DO_NOTHING)
    article = models.ForeignKey(Article, models.DO_NOTHING, blank=True, null=True)
    comment = models.ForeignKey(Comment, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    read_at = models.DateTimeField(blank=True, null=True)


class Settlement(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    amount = models.IntegerField()
    created_at = models.DateTimeField()
    received_at = models.DateTimeField(blank=True, null=True)
    bank_code = models.CharField(max_length=2, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    real_name = models.CharField(max_length=7, blank=True, null=True)


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=77)
    nickname = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class UserSubscribe(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    keyword = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
