from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    coord_lng = models.CharField(max_length=20)
    coord_lat = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return f'{self.pk} {self.title}'
