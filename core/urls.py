from cmath import pi
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

app_name ='core'

urlpatterns = [
    path("",views.LoginPage, name='loginpage'),
    path('dashboard/', views.DashBoard, name='dashboard'),
    path('dashboard/add', views.AddImage, name='addimage'),
    path('dashboard/edit/<int:pk>', views.EditImage, name='editimage'),
    path('dashboard/delete/<int:pk>', views.DeleteImage, name='deleteimage'),
    
    path("accounts/login/",views.LoginPage, name='loginpage'),
    path('logout/', views.LogoutPage, name='logoutpage'),
    
    
    
]


# Only for Development propouse
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)