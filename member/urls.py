from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.index, name="home"),
    path("member-list/", views.members, name="member-list"),
]
