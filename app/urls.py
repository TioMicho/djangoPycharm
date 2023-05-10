from django.urls import path
from app import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('person/<int:person_id>', views.person_view, name="person-detail"),
    path('person/delete/<int:person_id>', views.person_delete, name="person-delete"),
    path('person/all', views.persons_view, name="person-all"),
    path('person/create', views.person_create, name="person-create"),

    path('tweet/all', views.tweets_view, name="tweet-all"),

]
