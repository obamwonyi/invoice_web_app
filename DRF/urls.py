from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoice_web_app.urls')),
    path('api/v1/', include('client.urls')),
]
