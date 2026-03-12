from django.db import models

# Create your models here.

class Producto(models.Model): # Modelo para representar un producto
    # Definimos los campos del modelo
    codigo = models.CharField(max_length=10, unique=True, editable=False)
    descripcion = models.TextField()# descripción larga
    nombre_activo = models.TextField()
    accion_requerrida = models.TextField()     
    criticidad = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = Solicitud.objects.order_by('-id').first()
            if ultimo:
                numero = ultimo.id + 1
            else:
                numero = 1

            self.codigo = f"RQ-{numero:03d}"

        super().save(*args, **kwargs)
        
    class Meta:
        db_table = 'solicitudFalla'  # aquí definimos el nombre exacto de la tabla

