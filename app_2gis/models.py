from django.db import models


class TypeCoord(models.Model):
    """Тип маршрута не задаётся пользователем, только через админку"""
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, null=False, verbose_name="URL")

    class Meta:
        verbose_name = "Тип координат"
        verbose_name_plural = "Тип координат"

    def __str__(self):
        return self.title


class Coord(models.Model):
    """Несколько координат может использоваться для нескольких маршрутов"""
    title = models.CharField(max_length=255, verbose_name="Название", null=False)
    city = models.CharField(max_length=255, verbose_name="Город", null=False)
    latitude = models.DecimalField(decimal_places=6, verbose_name="Широта", max_digits=8)
    longitude = models.DecimalField(decimal_places=6, verbose_name="Долгота", max_digits=8)

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"

    def __str__(self):
        return self.title


class Path(models.Model):
    title = models.CharField(max_length=255, verbose_name="Маршрут")
    slug = models.SlugField(unique=True, verbose_name="url", null=False)
    describe = models.TextField(verbose_name="Описание")
    coord = models.ManyToManyField(Coord, verbose_name="Точки")
    type = models.ManyToManyField(TypeCoord, verbose_name="Тип маршрута")
    public = models.BooleanField(null=False, default=True, verbose_name="Публичный")

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"

    def __str__(self):
        return self.title
