from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('basics/', include('basics.urls')),
    path('selling/', include('selling.urls')),
    path('management/', include('management.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
