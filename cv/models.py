from django.conf import settings
from django.db import models



class Cv_section(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:56]+'.....'

    class Meta:
        verbose_name_plural = "cv_sections"
