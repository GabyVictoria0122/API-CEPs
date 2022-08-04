from django.urls import path

from cep import views

urlpatterns = [
    path('cep/<cep>', views.api_cep, name='api_cep'),
]
