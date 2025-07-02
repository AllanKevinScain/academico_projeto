from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academico.urls')),
    path('contato/', include('contato.urls')),
    path('login/', include('login.urls')),
    path('disciplinas/', include('disciplinas.urls')),
]
