from django.urls import path
from .views import analise_list, analise_new, analise_delete, analise_update

app_name = "analise"

urlpatterns = [
    path('analise_list/', analise_list ,name='analise_list'),
    path('analise_new/', analise_new, name='analise_new'),
    path('analise_delete/<int:pk>/', analise_delete, name='analise_delete'),
    path('analise_update/<int:pk>/', analise_update, name='analise_update'),
]