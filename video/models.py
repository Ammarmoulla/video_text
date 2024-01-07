from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.



def videoFile(instance, filename):
    return '/'.join( ['video_editors', str(instance.slug), filename])

class Video(models.Model):

    slug = models.SlugField(max_length=250, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(timezone.now()))
        super().save(*args, **kwargs)

    video = models.FileField(upload_to=videoFile, 
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("video:video_detail", args=[self.slug])




