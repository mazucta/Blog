from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tag/<int:pk>/', tag_detail, name='tag_detail_url'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)