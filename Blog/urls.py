from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 包含blogs应用的urls
    path('', include('blogs.urls')), 
    # 包含Django内置的身份验证URL (login/logout)
    path('users/', include('django.contrib.auth.urls')),
]