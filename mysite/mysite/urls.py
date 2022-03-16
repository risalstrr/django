
from django.contrib import admin
from django.urls import path, include
from . import view
from django.conf.urls.static import static
from django.conf import settings
from .view import loginView, logoutView

urlpatterns = [
    path('artikel/',include('artikel.urls')),
    path('about/',view.about,name = 'about'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', view.index, name='home'),
    path('login/',loginView, name="login"),
    path('logout/',logoutView, name="logout")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)