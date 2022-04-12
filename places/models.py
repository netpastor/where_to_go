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


def place_image_path(instance, filename):
    return 'place_{0}/{1}'.format(instance.place.id, filename)


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='images')
    image = models.ImageField(upload_to=place_image_path)
    order = models.IntegerField()

    class Meta:
        verbose_name = 'фотография места'
        verbose_name_plural = 'фотографии места'

    def __str__(self):
        return f'{self.order} {self.place.title}'
