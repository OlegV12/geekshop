import basketapp.views as basketapp
from django.urls import path

app_name = 'basketapp'


urlpatterns = [
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('', basketapp.basket, name='view'),

    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]
