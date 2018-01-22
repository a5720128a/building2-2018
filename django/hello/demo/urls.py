from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.index, name='index'),
    path('time/', views.showtime, name='time'),
    path('test1/', views.testError1, name='testError1'),
    path('test2/', views.testError2, name='testError2'),
]
