from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'clothesapp'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('clothes/<int:pk>/', views.ClothesView.as_view(), name='clothes_detail'),
    path('cart',views.Cart.as_view(),name='cart')
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)