"""digimed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('doctorregister', views.doctor_signup_view,name='doctorregister'),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('doctorclick', views.doctorclick_view),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),

]