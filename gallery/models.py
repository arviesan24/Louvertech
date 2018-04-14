from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from tinymce import HTMLField

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=120)
    description = HTMLField('Content')
    image_location = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                                       null=False,
                                       blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):  #return name instead of the object itself when calling single object from the tbl
        return self.name

    #first version of slug
    # def save(self, *args, **kwargs):  #create a slug base on the product name (Dynamic--will change if name is changed)
    #     self.slug = slugify(self.name)
    #     super(Gallery, self).save(*args, **kwargs)
    #=====================

    def get_absolute_url(self):
        return reverse("gallery_app:details", kwargs={"slug": self.slug})

def pre_save_gallery_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_gallery_receiver, sender=Gallery)