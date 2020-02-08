"""pikeru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from users.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
from products import views as prod_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('product/', include('products.urls')),
    # path('', prod_views.dashboard, name='dashboard'),
    path('product/<slug>/', prod_views.productView, name='prod_view'),
    path('category/<str:cat_name>/', prod_views.CategoryListView.as_view(), name='cat_view'),
    path('user-product-list/', prod_views.UserProductList.as_view(), name='user_product_list'),
    path('product/<int:pk>/update', prod_views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', prod_views.ProductDeleteView.as_view(), name='product-delete'),

    path('checkout/', prod_views.checkout, name='checkout'),
    path('products/', prod_views.ProductListView.as_view(), name='product_list'),
    path('contact/', user_views.contact, name='contact'),
    path('', user_views.main_index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), {'authentication_form': LoginForm}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('notes/<int:pk>/delete', user_views.NoteDeleteView.as_view(), name='note-delete'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('settings/', user_views.profile, name='profile'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-process/', prod_views.process_payment, name='payment_process'),
    path('payment-done/', prod_views.payment_done, name='payment_done'),
    path('payment-cancelled/', prod_views.payment_canceled, name='payment_cancelled'),


    path('post-product/', prod_views.ProductCreateView.as_view(), name='post_product'),

    # path('inbox/notifications/', include('notifications.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
