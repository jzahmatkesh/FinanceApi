from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    img_url=models.URLField()
    note=models.CharField(max_length=1000, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.note }'
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'