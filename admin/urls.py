from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('discount_code/', include('dummy_svc.urls'))
]