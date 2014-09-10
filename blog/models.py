from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class EntryQueryset(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    objects = EntryQueryset.as_manager()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ['-created']
