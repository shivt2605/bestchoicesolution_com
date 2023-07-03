from email.policy import default
from enum import auto
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils import timezone
from  embed_video.fields  import  EmbedVideoField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Categories(models.Model):
    icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('-id')
    

class Plat_Form(models.Model):
    author_profile = models.ImageField(upload_to="author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name



class Service(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )


    title = models.CharField(max_length=500)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="featuredimg",null=True)
    featured_video = models.CharField(max_length=300,null=True)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Plat_Form,on_delete=models.CASCADE,null=True)
    description = models.TextField()
    full_description = RichTextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("service_details", kwargs={'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Service.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, Service)


 

class Feature(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    feature = models.CharField(max_length=500)
    def __str__(self):
        return self.feature
    

class Fqa(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    questioned  = models.CharField(max_length=200)
    answers  = models.TextField()
    def __str__(self):
        return self.questioned
 

class UserService(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    paid = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.first_name + " - " + self.service.title
    
    

class Payment(models.Model):
    order_id = models.CharField(max_length=100,null=True,blank=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    user_service = models.ForeignKey(UserService,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " - " + self.service.title




