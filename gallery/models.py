from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(max_length=500)
    image_location = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                                       null=False,
                                       blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

    #first version of slug
    # def save(self, *args, **kwargs):  #create a slug base on the product name (Dynamic--will change if name is changed)
    #     self.slug = slugify(self.name)
    #     super(Gallery, self).save(*args, **kwargs)
    #=====================

    def get_absolute_url(self):
        return reverse("gallery:details", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):  #to loop slug if already exists
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Gallery.objects.filter(slug=slug).order_by("-timestamp")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_gallery_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_gallery_receiver, sender=Gallery)