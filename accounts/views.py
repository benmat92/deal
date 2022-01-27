from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm, EditProfileForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth.forms import PasswordChangeForm
from catalog.models import Profile, Category
from accounts.models import CustomUser
from rest_framework import generics, viewsets, status
from accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
#email activation




# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditProfilePageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        cat_menu = Category.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        context["cat_menu"] = cat_menu

        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context



class UserEditView(generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class LoginView(LoginView):
    form_class = LoginForm
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


"""
class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
"""
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
