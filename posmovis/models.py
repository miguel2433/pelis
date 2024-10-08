from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from login.models import pelicula
from django.utils import timezone
from datetime import date
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perfiles/" )
    sexo = models.CharField(max_length=10, choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], default='otro')
    country = CountryField(default="NZ")
    
    
    
    
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        if not self.imagen:
            self.imagen = 'user.jpg'
        super(Profile, self).save(*args, **kwargs)

        

class Comment(models.Model):
    DEFAULT_CONTENT_TYPE = 1 
    contentype = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=DEFAULT_CONTENT_TYPE)
    object_id = models.PositiveIntegerField(default=DEFAULT_CONTENT_TYPE)
    content_objec = GenericForeignKey('contentype','object_id')
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='autor')
    text = models.TextField()
    creat_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'comentario de {self.author.username} en {self.content_objec}'
    
    
    
