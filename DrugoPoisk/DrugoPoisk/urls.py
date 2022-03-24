from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from BestSite import views
from users.views import SignUpView, show_profile, change_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('testingDB/', views.testingDB),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', show_profile, name='profile'),
    path('change_profile/', change_profile, name='change_profile'),
]
