from django.urls import path
from.import views
urlpatterns=[
    path("leo/",views.leo,name="leo"),
    path("",views.index,name="index"),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('product/', views.product, name='product'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload_product, name='upload_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),


]
