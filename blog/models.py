from django.db import models

# Create your models here.

from django.db import models

# clase tag, se crea una subclase de models.Model
class Tag(models.Model):
    # campo tag de tipo caracter
    tag = models.CharField(max_length=100, unique=True, db_index=True)

    # permite dar un nombre mas significativo a las instancias
    def __unicode__(self):
        return self.tag

# clase post
class Post(models.Model):
    # relacion many to many entre Post y Tag
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    #fecha de publicacion, se agrega automaticamente
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    #cada comentario pertenece a un post
    post = models.ForeignKey(Post)

    #nombre es opcional (blank) y por defecto es Anonimus (default)
    name = models.CharField(max_length=100, blank=True, default="Anonimus")

    #el cuerpo del comentario
    body = models.TextField(verbose_name="comment")
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "Por " + self.name + " en " + self.post.title


