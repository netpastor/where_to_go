from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from places.views import IndexView, PlaceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('place/<int:pk>/', PlaceView.as_view(), name='place'),
    path('tinymce/', include('tinymce.urls')),
    path('', IndexView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
