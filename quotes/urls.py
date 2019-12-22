from django.urls import path
from . import views

#create path to home page, one path is home and one is for the about or addtl page
urlpatterns = [
	path('', views.home, name="home"),
	path('Page2', views.Page2, name="Page2"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),
   
]