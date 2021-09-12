from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Deal, Category, Comment
import datetime
from .forms import DealForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse

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
