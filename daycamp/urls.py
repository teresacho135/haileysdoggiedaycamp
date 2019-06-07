from django.urls import path
from . import views

urlpatterns = [
  # Template Views
  path('', views.landing, name='landing'),
  # path('question/<int:pk>', views.card_show, name='question_show'),
  # path('deck/<slug:tag>', views.deck_create, name='deck_create'),
  # path('deck/<slug:tag>/<int:idx>', views.card_show, name='deck_show'),
  # path('question/<slug:tag>/<int:idx>/community', views.card_community, name='card_community'),
  # path('community', views.community_home, name='community'),
  # path('question/<int:pk>/community', views.card_community, name='card_community'),

  # API Views
  path('camper/', views.camper, name='camper'),
  # path('answer', views.send_answer, name='send_answer'),
  # path('vote', views.send_vote, name='send_vote'),
  # path('comment', views.send_comment, name='send_comment'),
]