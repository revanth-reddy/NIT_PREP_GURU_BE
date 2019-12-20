from rest_framework import routers
from prepapp import views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('slideshow', views.SlideViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)