from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.onGetLogin, name='login'),
    path('onPostLogin/', views.onPostLogin, name='onPostLogin'),
    path('logout/', views.onPostLogout, name='logout'),
]
