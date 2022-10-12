from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('consume/', views.consume, name='consume'),
    path('<int:account_pk>/', views.detail, name='detail')
]