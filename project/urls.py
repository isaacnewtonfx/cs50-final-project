from django.urls import include,path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [

    path('', include('app_homepage.urls')),
    path('users/', include('app_users.urls')),
    path('contacts/', include('app_contacts.urls')),
    path('admin/', admin.site.urls),
    
] 

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)