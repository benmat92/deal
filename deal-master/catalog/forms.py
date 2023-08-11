from django import forms
from .models import Deal, Category, Comment


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'author', 'store', 'brand', 'price', 'summary', 'url', 'category', 'header_image')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'benji', 'value': '', 'type':'hidden'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'store': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the final price of the deal'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of the deal'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),

        }
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)

class EditForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('title', 'store', 'brand', 'price', 'summary', 'url', 'category', 'header_image')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        #    'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'store': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the final price of the deal'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief description of the deal'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),


        }

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            }
