from django.db import models
from django.conf import settings
# Create your models here.
class Snippet(models.Model):
    title = models.CharField("タイトル", max_length=128)
    code = models.TextField("コード", blank=True)
    description = models.TextField("説明", blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    photo = models.ImageField("写真", upload_to='avatars/')
    
    def __str__(self):
        return self.title