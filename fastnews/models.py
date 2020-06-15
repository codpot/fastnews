from django.db import models


class Article(models.Model):
    reporter = models.ForeignKey('User', models.DO_NOTHING)
    debate = models.ForeignKey('Debate', models.DO_NOTHING, blank=True, null=True)
    category = models.CharField(max_length=2)
    title = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField()
    created_at = models.DateTimeField()


class Comment(models.Model):
    debate = models.ForeignKey('Debate', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField()


class Debate(models.Model):
    name = models.CharField(max_length=50)
    comment_cnt = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


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
