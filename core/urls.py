
from django.contrib import admin
from django.urls import path
from account import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.account)
]
