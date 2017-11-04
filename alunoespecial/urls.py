from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^core/', include('alunoespecial.core.urls', namespace='core')),
    url(r'^conta/', include('alunoespecial.accounts.urls', namespace='accounts')),
    url(r'^avaliacao/', include('alunoespecial.avaliacao.urls', namespace='avaliacao')),
    url(r'', include('alunoespecial.accounts.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
