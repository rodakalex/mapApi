from django.db import models


class Coord(models.Model):
    name = models.CharField(max_length=255, verbose_name="")
    latitude = models.DecimalField(decimal_places=6, verbose_name="Широта", max_digits=8)
    longitude = models.DecimalField(decimal_places=6, verbose_name="Долгота", max_digits=8)

    def __str__(self):
        return self.name


class Path(models.Model):
    title = models.CharField(max_length=255, verbose_name="Маршрут")
    slug = models.SlugField(unique=True, verbose_name="url")
    describe = models.TextField(verbose_name="Описание")
    coord = models.ManyToManyField(Coord)

    def __str__(self):
        return self.title
