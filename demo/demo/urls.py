from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from photos import views

urlpatterns = patterns('',
    url( r'^$', views.Home.as_view(), name = 'home' ),

    url( r'upload/', views.upload, name = 'jfu_upload' ),
    url( r'^delete/(?P<pk>\d+)$', views.upload_delete, name = 'jfu_delete' ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
