from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Deal, Category, Comment
import datetime
from .forms import DealForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .serializers import DealSerializer, CategorySerializer
from rest_framework import generics, permissions, renderers, viewsets
from accounts.models import CustomUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
# Create your views here.

"""
def LikeView(request, pk):
    deal = get_object_or_404(Deal, id=request.POST.get('deal_id'))
    liked=False
    if deal.likes.filter(id=request.user.id).exists():
        deal.likes.remove(request.user)
        liked = False
    else:
        deal.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('deal_details', args=[str(pk)]))
"""

def like(request, pk):
    result = ''
    if request.POST.get('action') =='post':
        id = request.POST.get('postid')
        deal = get_object_or_404(Deal, id=id)
        liked=False
        if deal.likes.filter(id=request.user.id).exists():
            deal.likes.remove(request.user)
            deal.like_count -= 1
            liked = False
            result = deal.like_count
            deal.save()
        else:
            deal.likes.add(request.user)
            deal.like_count += 1
            liked = True
            result = deal.like_count
            deal.save()
        return JsonResponse({'result': result,})
    else:
        return JsonResponse({'result': result,})

class CommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_URL(self):
        return reverse('deal_details', kwargs=[str(pk)])

    def form_valid(self, form):
    #    deal = get_object_or_404(Deal, slug = self.kwargs['slug'])
        form.instance.name = self.request.user
        form.instance.deal_id = self.kwargs['pk']
        return super().form_valid(form)




class HomeView(ListView):
    model = Deal
#    queryset = Deal.objects.filter(date_posted__gte=datetime.datetime.today())[:5]
    template_name = 'home.html'
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)

    #    stuff = get_object_or_404(Deal, id=kwargs.get('id'))
    #    total_likes = stuff.like_count
    #    liked = False
    #    if stuff.likes.filter(id=self.request.user.id).exists():
    #        liked = True
        deals = Deal.objects.all()

        for deal in deals:
            liked = False
            if deal.likes.filter(id=self.request.user.id).exists():
                liked = True
        context["cat_menu"] = cat_menu
        context["liked"] = liked

        return context
def CategoryView(request, cats):
#    print("Querying for category: " + cats)
#    check = Deal.objects.filter(category__name__contains=cats)
#    print(check.count())
    category_deals = Deal.objects.filter(category__name__icontains=cats.replace('-', ' '))
    cat_menu = Category.objects.all()

    return render(request, 'categories.html', { 'cats':cats.title().replace('-', ' '), 'category_deals':category_deals, 'cat_menu':cat_menu })


class DealDetailView(DetailView):
    model = Deal
    template_name = 'deal_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DealDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Deal, id = self.kwargs['pk'])
        total_likes = stuff.like_count

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context ['comment'] = Comment.objects.all()
        context['form'] = CommentForm()
        context["cat_menu"] = cat_menu
        #context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddDealView(CreateView):
    model = Deal
    form_class = DealForm
    template_name = 'add_deal.html'
    template_name = 'test.html'


    #fields = '__all__'
    #fields = ('title', 'store', 'brand', 'price', 'summary', 'url', 'category')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddDealView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdateDealView(UpdateView):
    model = Deal
    form_class = EditForm
    template_name = 'update_deal.html'
#    fields = ('title', 'store', 'brand', 'price', 'summary', 'url', 'category')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateDealView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeleteDealView(DeleteView):
    model = Deal
    template_name = 'delete_deal.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteDealView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
"""
class DealViews(APIView):

    def get(self, request, format=None):
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DealDetailViews(APIView):
    def get_object(self, pk):
        try:
            return Deal.objects.get(pk=pk)
        except Deal.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deal = self.get_object(pk)
        serializer = DealSerializer(deal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deal = self.get_object(pk)
        serializer = DealSerializer(deal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deal = self.get_object(pk)
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""



"""
class DealViews(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class DealDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
class DealHighlight(generics.GenericAPIView):
    queryset = Deal.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        deal = self.get_object()
        return Response(deal.highlighted)
"""

class DealUserWritePermission(BasePermission):
    message = 'Editing deals is restricted to the author only'
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class DealViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DealDetail(generics.RetrieveUpdateDestroyAPIView, DealUserWritePermission):
    permission_classes = [DealUserWritePermission]
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MyReactView(TemplateView):
    template_name = 'react_app.html'

    def get_context_data(self, **kwargs):
        return {'context_variable': 'value'}
