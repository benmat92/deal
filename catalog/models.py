from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
import uuid
from datetime import datetime, date
from newhomewhothis import settings
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    """Model representing a category."""
    living_room = 'living room'
    dining_room = 'dining room'
    kithen = 'kitchen'
    bedroom = 'bedroom'
    hallway = 'hallway'
    CATEGORY_CHOICES = [
        (living_room, 'Living Room'),
        (dining_room, 'Dining Room'),
        (kithen, 'Kitchen'),
        (bedroom, 'Bedroom'),
        (hallway, 'Hallway'),
    ]
    name = models.CharField(max_length=200, choices=CATEGORY_CHOICES, help_text='Enter a category')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    pinterest_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

DEFAULT_USER_ID = 1
class Deal(models.Model):
    """Model representing a deal"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=25)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=200, default="Shared Hallway")
    store = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    #store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)

#    summary = models.TextField(max_length=1000)
    summary = RichTextField(blank=True, null=True)
    url = models.CharField('URL', max_length=250)
    category = models.ManyToManyField(Category)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='deals', default=None, blank=True)
    like_count = models.BigIntegerField(default ='0')



    DEAL_STATUS = (
        ('a', 'Active'),
        ('e', 'Expired'),
        ('i', 'Issue'),
        ('b', 'Broken'),
    )

    status = models.CharField(
        max_length=1,
        choices=DEAL_STATUS,
        blank=True,
        default='a',
        help_text='Deal availability',
    )

    class Meta:
        ordering = ['date_posted']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this deal."""
        #return reverse('deal_details', args=[str(self.id)])
        return reverse('deal_details', args=[str(self.id)])

class Comment(models.Model):
    deal = models.ForeignKey(Deal, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(settings.AUTH_USER_MODEL, max_length=255)
    content = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return '%s - %s' % (self.deal.title, self.name)

    def get_absolute_url(self):
        return reverse('deal_details', args=[str(self.deal.id)])
