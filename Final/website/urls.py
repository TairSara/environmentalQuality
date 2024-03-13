from django.urls import path
from .import views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('privateuser_register/',views.privateuser_register.as_view(), name='privateuser_register'),
     path('corpuser_register/',views.corpuser_register.as_view(), name='corpuser_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('login/register.php', views.register_view, name='register'),
     path('addproduct/', views.addproduct, name='addproduct'),
     path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
     path('searchProduct/', views.searchProduct, name='searchProduct'),
]