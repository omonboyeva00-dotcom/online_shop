from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.logout_,name='logout'),
    path('verify_email/',views.Verify_EmailView.as_view(),name='verify_email'),
    path('set-new-password/', views.SetNewPasswordView.as_view(), name='set_new_password'),

]
