from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # header_image = models.ImageField(default='default_header.png', upload_to='post_pics')
    header_image = models.ImageField(default='default.jpeg', upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        img = Image.open(self.header_image.path)
        if img.height > 1280 or img.width > 960:
            output_size = (1280, 960)
            img.thumbnail(output_size)
            img.save(self.header_image.path)