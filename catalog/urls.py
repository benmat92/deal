from django.urls import path
from .views import HomeView, DealDetailView, AddDealView, UpdateDealView, DeleteDealView, CategoryView, like, CommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('deal/<uuid:pk>/', DealDetailView.as_view(), name="deal_details"),
    path('add_deal/', AddDealView.as_view(), name = 'add_deal'),
    path('deal/edit/<uuid:pk>/', UpdateDealView.as_view(), name = 'update_deal'),
    path('deal/<uuid:pk>/remove/', DeleteDealView.as_view(), name = 'delete_deal'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('like/<uuid:pk>/', like, name = 'like_deal'),
    path('add_comment/<uuid:pk>/', CommentView.as_view(), name = 'add_comment'),

]
