from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('index.html', include('homepage.urls', namespace='homepage')),
    path('about.html', include('about.urls', namespace='about')),
    path('ice_cream_list.html', include('ice_cream.urls', namespace='ice_cream')),
    path('admin/', admin.site.urls),
]
