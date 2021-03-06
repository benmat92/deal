from django.urls import path, include
from .views import HomeView, DealDetailView, AddDealView, UpdateDealView, DeleteDealView, CategoryView
from .views import like, CommentView, DealViewSet, CategoryViewSet, TemplateView, MyReactView, DealDetail, Deal, CreateDeal, AdminDealDetail, EditDeal, DeleteDeal
from accounts.views import BlacklistTokenUpdateView
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('', DealViewSet, basename='deal')
router.register(r'category', CategoryViewSet)
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve'
})
#urlpatterns = router.urls

urlpatterns = [
     path('index/', HomeView.as_view(), name="home"),
#    path('deal/<uuid:pk>/', DealDetailView.as_view(), name="deal_details"),
#    path('add_deal/', AddDealView.as_view(), name = 'add_deal'),
#    path('deal/edit/<uuid:pk>/', UpdateDealView.as_view(), name = 'update_deal'),
#    path('deal/<uuid:pk>/remove/', DeleteDealView.as_view(), name = 'delete_deal'),
#    path('category/<str:cats>/', CategoryView, name = 'category'),
#    path('like/<uuid:pk>/', like, name = 'like_deal'),
#    path('add_comment/<uuid:pk>/', CommentView.as_view(), name = 'add_comment'),
    path('', include(router.urls)),
    path('category/<int:pk>/', category_detail, name='category-detail'),
#    path('admin/edit/dealdetail/<int:pk>/', AdminDealDetail.as_view(), name='admindetaildeal'),
#    path('admin/edit/<int:pk>/', EditDeal.as_view(), name='editdeal'),
#    path('admin/delete/<int:pk>/', DeleteDeal.as_view(), name='deletedeal'),
#    path('test/', AddDealView.as_view(), name = 'test'),
    # this route catches the "naked" URL with no path specified. you can link to it in most places
#    path(r'my-react-page/', MyReactView.as_view(), name='react_app'),
    # this route catches any url below the main one, so the path can be passed to the front end
#    path(r'my-react-page/<path:path>', MyReactView.as_view(), name='react_app_with_path'),
#    path('', TemplateView.as_view(template_name="catalog/index.html")),
    #path('<uuid:pk>/', DealDetail.as_view(), name='detailcreate'),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
