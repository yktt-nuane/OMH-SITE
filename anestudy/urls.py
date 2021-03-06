from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index),
    path("tags/<slug:slug>", views.tags),
    path("<slug:pk>/", views.posted_article),
    path("posted_article/<slug:pk>/", views.posted_article),
    path("<slug:postarticle_id>/edit/postarticle/", views.edit_post),
    path("tags/add/postarticle", views.add_post, name="add_post"),
]
