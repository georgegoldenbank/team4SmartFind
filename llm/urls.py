from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='llm.index'),
]