from django.db import models
from django.db.models import Max
from django.urls import reverse

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.SlugField(blank=True, verbose_name='slug')
    description_short = HTMLField(verbose_name='краткое описание')
    description_long = HTMLField(verbose_name='полное описание')
    coord_lng = models.CharField(max_length=20, verbose_name='долгота')
    coord_lat = models.CharField(max_length=20, verbose_name='широта')

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return f'{self.pk} {self.title}'

    def serialize(self):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(self.coord_lng),
                    float(self.coord_lat)
                ]
            },
            "properties": {
                "title": self.title,
                "placeId": self.slug,
                "detailsUrl": reverse('place', args=(self.pk,))
            }
        }

    def serialize_details(self):
        return {
            "title": self.title,
            "imgs": [img.image.url for img in self.images.all()],
            "description_short": self.description_short,
            "description_long": self.description_long,
            "coordinates": {
                "lng": float(self.coord_lng),
                "lat": float(self.coord_lat)
            }
        }


def place_image_path(instance, filename):
    return 'place_{0}/{1}'.format(instance.place.id, filename)


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=place_image_path, verbose_name='картинка')
    order_number = models.IntegerField(blank=True, null=True, verbose_name='позиция')

    class Meta:
        verbose_name = 'фотография места'
        verbose_name_plural = 'фотографии места'
        ordering = ('order_number',)

    def __str__(self):
        return f'{self.order_number} {self.place.title}'

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_max_number = PlaceImage.objects \
                .filter(place=self.place) \
                .aggregate(Max('order_number'))['order_number__max']
            self.order_number = last_max_number + 1 if last_max_number else 1
        super().save(*args, **kwargs)
