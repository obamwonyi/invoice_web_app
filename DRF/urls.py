from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('invoice_web_app.urls')),
    path('api/v1/', include('client.urls')),
    path('api/v1/', include('invoice.urls')),
    path('api/v1', include('teams.urls'))
]
