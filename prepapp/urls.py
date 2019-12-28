from rest_framework import routers
from prepapp import views
from django.conf.urls import url,include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('slideshow', views.SlideViewSet)
router.register('news', views.NewsViewSet)
router.register('companies', views.CompViewSet)
router.register('exp', views.ExpViewSet)


urlpatterns = [
    url('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^FTE/(?P<company>[-\w\.]+)/', views.FTE_list),
    url(r'^INTERN/(?P<company>[-\w\.]+)/', views.intern_list),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)