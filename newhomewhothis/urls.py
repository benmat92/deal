"""sharedhallway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from allauth.account.views import confirm_email
from django.urls import path
from django.urls import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.documentation import include_docs_urls
from catalog.views import DealListDetailFilter, CreateDeal, AdminDealDetail, EditDeal, DeleteDeal, like
from rest_framework.schemas import get_schema_view
from django.views.decorators.csrf import csrf_exempt





urlpatterns = [
    #oauth
    url('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # Post Admin URLs
    path('admin/', admin.site.urls),
    path('api/like/<uuid:pk>/', like, name = 'like_deal'),
    path('apiadmin/create/', CreateDeal.as_view(), name='createdeal'),
    path('apiadmin/edit/dealdetail/<uuid:pk>/', AdminDealDetail.as_view(), name='admindetaildeal'),
    path('apiadmin/edit/<uuid:pk>/', EditDeal.as_view(), name='editdeal'),
    path('apiadmin/delete/<uuid:pk>/', DeleteDeal.as_view(), name='deletedeal'),
#    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', get_schema_view(
        title="Deals API",
        description="API for the Deals",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/', include_docs_urls(title='My API service'), name='api-docs'),
    path('search/', DealListDetailFilter.as_view(), name='dealsearch'),
    path('', include('catalog.urls')),
#    url(r'^rest-auth/', include('rest_auth.urls')),
#    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
#    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
#    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
