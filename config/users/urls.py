from django.contrib import admin
from django.urls import path, include
from .views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
