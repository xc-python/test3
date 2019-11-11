from django.urls import path
from test11 import views
urlpatterns = [
    path('run/', views.run),


]