from django.urls import path
from motivational import views

urlpatterns = [
    path('', views.message, name='index'),
    # path('message/', views.message, name='message')
]
