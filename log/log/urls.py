"""log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from dailylog.views import Home, SignUp, LogListView, QuestionCreateView, LogDetailView, log, save_log
from django.contrib.auth import views as auth_views
# from dailylog.views import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/log', log, name='create_log'),
    path('save/log', save_log, name='save_log'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log_detail'),
    path('logs', LogListView.as_view(), name='logs'),
    path('create/question', QuestionCreateView.as_view(), name='create_question'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html', success_url = 'logs'), name='login'),
    path('signup', SignUp.as_view(), name='signup'),
    path('admin/', admin.site.urls),
]
