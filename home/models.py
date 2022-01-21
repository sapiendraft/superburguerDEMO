from django.db import models

# main page posts

class IndexCards(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    paragraph = models.CharField(max_length=256)
    observation = models.CharField(max_length=128)
    image_link = models.CharField(max_length=512)
    reference_link = models.CharField(max_length=512)

    def __str__(self):
        return self.title