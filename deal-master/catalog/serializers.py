from rest_framework import serializers
from .models import Deal, Category
import uuid
from ckeditor.fields import RichTextField
from accounts.models import CustomUser
from newhomewhothis import settings


class DealSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4)

#    highlight = serializers.HyperlinkedIdentityField(view_name='deal-highlight', format='html')

    class Meta:
        model = Deal
        fields='__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields='__all__'



class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'username')
        extra_kwargs = {'password': {'write_only': True}}
    """Model representing a deal"""
"""
    id = serializers.UUIDField(primary_key=True, default=uuid.uuid4)
    title = serializers.CharField(max_length=25)
    header_image = serializers.ImageField(required=False, allow_blank=True)
    author = serializers.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_tag = serializers.CharField(max_length=200, default="Shared Hallway")
    store = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    date_posted = serializers.DateTimeField(auto_now_add=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    #store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)

#    summary = models.TextField(max_length=1000)
    summary = serializers.RichTextField(blank=True, null=True)
    url = serializers.CharField('URL', max_length=250)
    category = serializers.ManyToManyField(Category)
    likes = serializers.ManyToManyField(settings.AUTH_USER_MODEL, related_name='deals', default=None, blank=True)
    like_count = serializers.BigIntegerField(default ='0')
"""
