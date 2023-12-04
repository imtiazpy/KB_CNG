from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('teams/', include('team.urls')),
    path('contact/', include('contact.urls')),
    path('kbdash/', include('management.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG == True:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
