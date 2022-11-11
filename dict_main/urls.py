from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dict_app.urls'))
]

handler404 = 'dict_app.views.error_404_view'