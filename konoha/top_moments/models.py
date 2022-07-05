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
    top = models.ForeignKey(Top, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    video = EmbedVideoField()

    def __str__(self):
        return self.text