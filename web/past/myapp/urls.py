
from django.urls import path
from .views import index

app_name = "myapp"

urlpatterns = [
    path('', index, name='index'),
]
