from django.urls import path
#from .views import UserAPIView
from . import views

urlpatterns = [
    path('display/',views.login,name="display"),
    path('submit/',views.SubmitUser,name="submitb")
]