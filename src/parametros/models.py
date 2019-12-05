from django.db import models

# Create your models here.
# Los modelos son una clase que devuelve un objeto por lo que crearemos una clase
# con el nombre de la entidad o coleccion y definiremos los atributos

# Clase para el modelo etnia, esta clase se encargará: 
class Etnia(models.Model):
    NombreEtni=models.CharField(max_length=50)

    # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Grupo Etnico"
        verbose_name_plural = "Grupos Etnicos"

    def __str__(self):
        return self.NombreEtni

class EstaCivil(models.Model):
    NombreEsta=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estado civil"

    def __str__(self):
        return self.NombreEsta
        
class TipoDocu(models.Model):
    NombreTiDo=models.CharField(max_length=50)

     # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Documento"
        verbose_name_plural = "Tipo De Documentos"

    def __str__(self):
        return self.NombreTiDo
        
class TipoLogr(models.Model):
    NombreTiLo=models.CharField(max_length=50)

  # Clase para los meta archivos de la clase:
    class Meta:
        verbose_name = "Tipo De Logro"
        verbose_name_plural = "Tipo De Logros"

    def __str__(self):
        return self.NombreTiLo
    

