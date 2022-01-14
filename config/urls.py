from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from anestudy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('posted_articles/', views.posted_articles),
    path('posted_articles_top/', views.posted_articles_top),
    path('anestudy/', include('anestudy.urls')),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.contact),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('add/postarticle', views.add_post, name='add_post'),
    path('edit/postarticle/<int:postarticle_id>/', views.edit_post, name='edit_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
