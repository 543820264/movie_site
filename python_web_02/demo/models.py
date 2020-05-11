from django.db import models


# Create your models here.
class List_1(models.Model):
    name = models.CharField(max_length=10)
    desc = models.TextField(max_length=50, blank=True)
    url = models.URLField(max_length=100)
    file_path = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'list_1'


class List_2(models.Model):
    name = models.CharField(max_length=10)
    parent = models.ForeignKey('List_1', on_delete=models.CASCADE)
    desc = models.TextField(max_length=50, blank=True)
    url = models.URLField(max_length=100)
    file_path = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'list_2'


class Movies(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=388, blank=True)
    column = models.ForeignKey('List_2', on_delete=models.CASCADE)
    image = models.ImageField(max_length=50, blank=True)
    image_url = models.CharField(max_length=100, blank=True)
    url_1 = models.URLField(max_length=255, blank=True)
    url_2 = models.URLField(max_length=255, blank=True)
    years = models.IntegerField(blank=True)
    director = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    actor = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=10, blank=True)
    statics_files = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movies_content'
