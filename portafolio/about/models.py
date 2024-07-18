from django.db import models

# Create your models here.
# Modelo para Formación
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    degree_title = models.CharField(max_length=300, verbose_name='Título Obtenido')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    # Pasos para convertir en español la aplicación en el admin y ordenación de los registros
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'formación'
        verbose_name_plural = 'formaciones'
        ordering = ['-created']
    
    # Con esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su título
    def __str__(self):
        return self.title


# Modelo para Skills
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Título')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')

    # Pasos para convertir en español la aplicación en el admin y ordenación de los registros
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created']
    
    # Con esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su título
    def __str__(self):
        return self.title