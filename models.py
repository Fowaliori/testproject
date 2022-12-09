from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Автор', max_length=250)
    full_text = models.TextField('Краткое описание аниме')
    date = models.DateField('Дата публикации')
    series = models.CharField('Количество серий', max_length=10)

    def __str__(self):
        return self.title



