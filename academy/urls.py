
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', include('academy.core.urls')),
    path('conta/', include('academy.accounts.urls')),
    path('index/', include('academy.courses.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

