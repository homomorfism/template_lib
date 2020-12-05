from django.db import models


# Create your models here.

class Category(models.Model):
    text = models.CharField(max_length=30, help_text="Choose any categories book belongs", null=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text', ]
