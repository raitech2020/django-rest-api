from django.urls import path
from .views import get_data, get_items, add_item

urlpatterns = [
    path('', get_data),
    path('items/', get_items),
    path('add/', add_item),
]
