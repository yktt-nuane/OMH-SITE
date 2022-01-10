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
    path('blogs/', views.blogs),
    #path('blogs/', include('anestudy.urls')),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.contact),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
