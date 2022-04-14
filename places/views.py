import json
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.detail import SingleObjectMixin, BaseDetailView

from .models import Place


class IndexView(TemplateView):
    http_method_names = ['get', ]
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        data = {
            "type": "FeatureCollection",
            "features": []
        }

        if places_list := Place.objects.all():
            for place in places_list:
                data['features'].append(place.serialize())

        context['data'] = data
        return self.render_to_response(context)


class PlaceView(BaseDetailView, SingleObjectMixin):
    http_method_names = ['get', ]
    model = Place

    def get(self, request, *args, **kwargs):
        place = self.get_object()
        return HttpResponse(json.dumps(place.serialize_details()))


