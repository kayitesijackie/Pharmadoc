from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^about$', views.about, name='about'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^single$', views.single, name='single'),
    url('products/', views.products, name='products'),
    url('contact/', views.contact, name='contact'),
    url('sale/', views.sale, name='sale'),
    
 
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)