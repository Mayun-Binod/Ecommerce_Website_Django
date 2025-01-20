from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Binod Admin"
admin.site.site_title = "Binod Admin Portal"
admin.site.index_title = "Welcome to Binod Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
