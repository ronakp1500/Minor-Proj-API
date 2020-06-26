from django.urls import path
from .views import UsersAPIView

urlpatterns = [
    path('login/',UsersAPIView.as_view()),
    path('login/<int:pk>', UsersAPIView.as_view()),
]