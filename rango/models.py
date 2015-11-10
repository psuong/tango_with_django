from django.db import models
# import the slugify library for readable URLs
from django.template.defaultfilters import slugify

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#
#     # Returns the string version of "name"
#     def __unicode__(self):
#         return self.name

# Updated Category models to use slugify for readable URLS
class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name


class Page(models.Model):
    category = models.ForeignKey(Category) # Allows Django to create a one to many relation
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # Returns the title as a string output
    def __unicide__(self):
        return self.title
