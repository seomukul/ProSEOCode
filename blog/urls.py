from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('blog/', views.Blog, name='blog'),
    path('<slug:slug>/', views.single_post, name='single_post'),
    path('category/<slug:category_slug>/', views.category_page, name='category_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)