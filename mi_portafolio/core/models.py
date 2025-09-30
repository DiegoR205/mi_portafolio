from django.db import models
from django.utils import timezone

class Profile(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resumen = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    skills = models.TextField(help_text='Lista separada por comas', blank=True)

    def __str__(self):
        return self.nombre

class Project(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo

class FAQ(models.Model):
    pregunta = models.CharField(max_length=300)
    respuesta = models.TextField()
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.pregunta

class OpenItem(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='openitems/', blank=True, null=True)
    resumen = models.CharField(max_length=300, blank=True)
    descripcion = models.TextField(blank=True)
    palabras_clave = models.CharField(max_length=300, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    asunto = models.CharField(max_length=200, blank=True)
    mensaje = models.TextField()
    enviado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
