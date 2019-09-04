from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100)
    image =models.FileField(null= True, blank =True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add= True)
    update = models.DateTimeField(auto_now=True, auto_now_add =False)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id})

    class Meta:
        ordering =["-timestamp","-update"]