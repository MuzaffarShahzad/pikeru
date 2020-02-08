
from django.urls import path
from users import views
from . import views as prod_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('P=<slug>/', prod_views.productView, name='prod_view'),
    path('list/', prod_views.ProductListView.as_view(), name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
