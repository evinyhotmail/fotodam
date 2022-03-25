import os
import re
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    #esta opción elimina todos los caracteres especiales
    #espacios en blanco tambien
    filename = re.sub ( '[^A-Za-z0-9_.]+', '', filename )
     # used to save avatar of user
    return 'user_{0}/{1}'.format ( str ( instance.user.username ) + '/images', filename )


# fk	field	models.ForeignKey()
# m2m	field	models.ManyToManyField()
# o2o	field	models.OneToOneField()

class ImageCategory(models.Model):
    description = models.CharField(max_length=120, blank=False)
    created_at = models.DateTimeField ( auto_now_add=True)

    def __str__(self):
        return self.description


class ImageBank(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    categories = models.ManyToManyField(ImageCategory)
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=120,  blank=True, default="Coloque aquí una breve descripción de la imagen")
    image = models.ImageField(
         upload_to = user_directory_path, 
         blank=False,
         default=None,
         verbose_name="Imagen"
     )
    created_at = models.DateTimeField ( auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.user)} | {self.title}'

    # return all categories asociated to the images.
    @property
    def data_category(self):
        qs = self.categories.all()
        value=""
        for x in qs:
            value += f'{x.pk},' 
        return value[:-1]
    
    @property
    def file_ext(self):
        # unpacking the tuple
        f_name, f_ext = os.path.splitext(str(self.image))
        return f_ext

    # Method used to delete the file into the disk
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)













    

