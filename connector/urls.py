"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from core import views
from users import views as users_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('map/', views.map, name="map"),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="home"), name='logout'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('profile/edit', users_views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/',
         users_views.view_other_profile, name='view_other_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
