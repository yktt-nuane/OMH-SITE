from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('tags/<slug:slug>', views.tags),
    path('<slug:pk>/', views.posted_article),
    path('posted_article/<slug:pk>/', views.posted_article),
    path('<slug:postarticle_id>/edit/postarticle/', views.edit_post),
]

