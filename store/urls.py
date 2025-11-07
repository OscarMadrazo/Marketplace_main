from django.urls import path

from.views import contact, detail
ulpatterns = [
    path('contact/', contact, name = 'contact'),
    path('detail/<int:pk>/', detail, name = 'detail'),
]