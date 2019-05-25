from django.db import models
from django.utils.safestring import mark_safe

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, verbose_name='标题')
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    checked = models.BooleanField(default=False, verbose_name="是否审阅")


    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    def get_absolute_url(self):

        return '/entry/%s/' % self.id


    def color_headline(self):
        return mark_safe('<span style="color:red">%s</span>' % self.headline)
    color_headline.short_description = '红色的标题'

