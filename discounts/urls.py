from django.urls import path

from discounts import views

app_name = 'discounts'

urlpatterns = [
    path('apply/', views.discount_apply, name='apply'),
]