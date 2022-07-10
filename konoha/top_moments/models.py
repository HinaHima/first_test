from django.db import models
from embed_video.fields import EmbedVideoField

class Top(models.Model):
    """Тема с различными топами."""
    topname = models.CharField(max_length=200)

    def __str__(self):
        """Строковое представление модели."""
        return self.topname

class TheTop(models.Model):
    """Конкретные топы."""
    top = models.ForeignKey(Top, on_delete=models.CASCADE, blank=True)
    name = models.TextField(max_length=50, blank=True)
    text = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='A:/Python_projects/konoha/konoha/media/', blank=True)
    url = EmbedVideoField(blank=True)

    def __str__(self):
            return self.name