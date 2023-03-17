from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo_api.views import TodoViewset

router = DefaultRouter()
router.register('todo', TodoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
