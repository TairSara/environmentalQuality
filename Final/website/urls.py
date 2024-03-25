from django.urls import path
from .import views
urlpatterns=[
     path('master/',views.master, name='master'),
     path('contact_view/', views.contact_view, name='contact_view'),
     path('display_contacts/',views.display_contacts, name='display_contacts'),
     path('register/',views.register, name='register'),
     path('privateuser_register/',views.privateuser_register.as_view(), name='privateuser_register'),
     path('corpuser_register/',views.corpuser_register.as_view(), name='corpuser_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('login/register.php', views.register_view, name='register'),
     path('searchProduct/', views.searchProduct, name='searchProduct'),
     path('addproduct/', views.addproduct, name='addproduct'),
     path('productslist/', views.productslist, name='productslist'),
     path('updateproduct/<int:pk>/', views.updateproduct, name='updateproduct'),
     path('changestatus/<int:pk>/', views.changestatus, name='changestatus'),
     path('userform/', views.userform, name='userform'),
     path('recycling_bin/', views.recycling_bin, name='recycling_bin'),
     path('my_authority/', views.my_authority, name='my_authority'),
     path('userEditform/', views.userEditform, name='userEditform'),
     path('userrecycling/', views.userRecyclingform, name='userrecycling'),
     path('User_point/', views.Userpointform, name='User_point'),
     
]