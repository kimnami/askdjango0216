import re
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ValidationError
from django.contrib.auth.models import User


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    #DB server에서는 문자열이 두가지로 나누어짐
    #char는 문자열의 길이 제한이 있고
    #text는 길이 제한이 없음
    user = models.ForeignKey(User, related_name='blog_post_set')
    title = models.CharField(max_length=100, verbose_name='제목', help_text='포스팅 제목으로 노출됩니다. 최대 100자까지 지원됩니다.', choices=[('val1','lable1'),('val2','lable2')],validators=[MinLengthValidator(10)]) #descriptor syntex
    content = models.TextField(verbose_name='내용')
    author = models.CharField(max_length=30)
    lnglat = models.CharField(max_length=50, blank=True, validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True) #최초저장시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField('Tag',blank=True, null=True)
    #최후수정시간을 자동으로 저장
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return self.message


class Tag(models.Model):
    tag = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.tag