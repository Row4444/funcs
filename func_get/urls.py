from django.contrib import admin
from django.urls import path

from func_get.views import StartAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', StartAPIView.as_view())
]
