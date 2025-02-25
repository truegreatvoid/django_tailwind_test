from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dj_tailwind.urls', namespace='dj_tailwind')),
    
    path("__reload__/", include("django_browser_reload.urls")),
]
