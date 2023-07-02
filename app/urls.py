from django.urls import path,include
from app import views,user_login
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [    
    path('', views.HOME, name='home'),
    path('base', views.BASE, name='base'),
    path('about', views.ABOUT_US,name='about'),
    path('contact', views.CONTCAT,name='contact'),
    path('404', views.PAGE_NOTFOUND,name='404'),

    
    path('service', views.SINGLE_COURS,name='service'),
    path('service/filter-data',views.filter_data,name="filter-data"),
    path('search',views.SEARCH_SERVICE,name='search_service'),    
    path('service/<slug:slug>',views.SERVICE_DETAILS,name='service_details'),

    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my_service', views.MY_SERVICE, name='my_service'),




    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user_login.REGISTER,name='register'),
    path('do_login', user_login.DO_LOGIN,name='do_login'),
    
    path('accounts/profile', user_login.PROFILE,name='profile'),
    path('accounts/profile_update', user_login.Profile_Update,name='profile_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)