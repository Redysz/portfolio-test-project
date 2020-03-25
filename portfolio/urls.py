from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
    path('', jobs.views.home, name='home'),
    path('donate/', jobs.views.donate, name='donate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
