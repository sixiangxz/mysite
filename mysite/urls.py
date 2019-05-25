"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views as blog_views
from django.contrib.sitemaps.views import sitemap
from blog.blog_sitemap import BlogSitemap
sitemaps = {
    'blog': BlogSitemap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('polls/', include('polls.urls')),
    # path('signal/', blog_views.create_signal),
    # path('uploads/', include('uploads.urls')),
    path('admin/', admin.site.urls),
    path('blog/', blog_views.index),
    path('blog/name', blog_views.get_name),
    path('blog/contact', blog_views.contact),
    path('blog/entry', blog_views.entry),
    path('blog/list', blog_views.listing),
    re_path(r'^blog/page(?P<num>[0-9]+)/$', blog_views.page),
    re_path(r'^blog/detail/(?P<num>[0-9]+)/$', blog_views.detail, name='detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

