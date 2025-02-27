"""
URL configuration for TechScope_cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

handler403 = 'apps.news.views.tr_handler403'
handler404 = 'apps.news.views.tr_handler404'
handler500 = 'apps.news.views.tr_handler500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.news.urls')),
    path('', include('apps.accounts.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

#Для работы media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]