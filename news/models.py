from django.db import models
from django.utils import timezone

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(BaseModel):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    published_at = models.DateTimeField(timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    category = models.ForeignKey('news.Category', related_name='news_category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title