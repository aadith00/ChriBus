from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),

    path('admin_tools/', include('admin_tools.urls')),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),

    path('', include('base.urls')),
    path('', include('bus.urls')),
    path('', include('rentals.urls')),
    path('', include('admin_soft.urls')),

]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)