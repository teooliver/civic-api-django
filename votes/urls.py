from django.urls import path

from . import views as vote_views

urlpatterns = [
    path('votes/', vote_views.VoteList.as_view(), name='vote_list'),
    path('votes/<int:pk>/', vote_views.VoteDetail.as_view(), name='vote_detail'),
]