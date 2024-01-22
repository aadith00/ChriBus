from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('df-admin/', admin.site.urls),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('admin/', include('authentication.urls')),
    path('', include('base.urls')),
    path('', include('rentals.urls')),
]
