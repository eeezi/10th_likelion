from django.contrib import admin
from django.urls import path, include
from snsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #snsapp
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    #detail
    path('<int:board_id>/', views.detail, name='detail'),
    path('create_comment/<int:board_id>/', views.create_comment, name='create_comment'),
    #login
    path('accounts/', include('allauth.urls')),
]
