from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, LoginView, UserViewSet
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('login/', LoginView.as_view(), name='login'),
#    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('register/password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='customuser-detail'),
    path('', include(router.urls)),




]
#urlpatterns = format_suffix_patterns(urlpatterns)
