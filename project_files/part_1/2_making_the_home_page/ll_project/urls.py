from django.contrib import admin
#Mapping a URl
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('learning_logs.urls')),
]

