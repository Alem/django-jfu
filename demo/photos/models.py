from django.db import models
from demo.settings import MEDIA_ROOT

# Create your models here.

class Photo( models.Model ):
    file = models.FileField( upload_to = MEDIA_ROOT )
