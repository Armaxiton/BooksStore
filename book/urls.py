from django.urls import path

from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:cat_id>/', cat_view, name='category'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book')
]