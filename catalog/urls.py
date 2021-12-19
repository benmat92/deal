from django.urls import path, include
from .views import HomeView, DealDetailView, AddDealView, UpdateDealView, DeleteDealView, CategoryView, like, CommentView, DealViewSet, CategoryViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'deal', DealViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    #path('', HomeView.as_view(), name="home"),
    path('deal/<uuid:pk>/', DealDetailView.as_view(), name="deal_details"),
    path('add_deal/', AddDealView.as_view(), name = 'add_deal'),
    path('deal/edit/<uuid:pk>/', UpdateDealView.as_view(), name = 'update_deal'),
    path('deal/<uuid:pk>/remove/', DeleteDealView.as_view(), name = 'delete_deal'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('like/<uuid:pk>/', like, name = 'like_deal'),
    path('add_comment/<uuid:pk>/', CommentView.as_view(), name = 'add_comment'),
    path('', include(router.urls)),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
