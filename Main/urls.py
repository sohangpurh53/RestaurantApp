# from django.urls import path
# from Main.views import MainPage

# urlpatterns = [
#     path('', MainPage.Home, name="home"),
#     path('about/', MainPage.About, name="about"),
#     path('menu/', MainPage.Menu, name="menu"),
#     path('book/', MainPage.Book, name="book")
# ]

from django.urls import path
from .views import MainPage, AboutPage, MenuPage, BookPage,SingleMenuPage

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('menu/', MenuPage.as_view(), name='menu'),
    path('menu/<int:id>', SingleMenuPage.as_view(), name='singlemenu'),
    path('about/', AboutPage.as_view(), name='about'),
    path('book/', BookPage.as_view(), name='book'),
]