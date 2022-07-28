from django.urls import path
from board.views import card

app_name = 'board'

urlpatterns = [
    path('create/', card.CreateCaredAPIView.as_view()),
    path('delete/', card.DeleteCardAPIView.as_view()),
    path('detail/<card_id>/', card.GetCardDetailAPIView.as_view()),
]
