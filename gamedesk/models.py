from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/desk/{self.id}'

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1600)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.datetime}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'