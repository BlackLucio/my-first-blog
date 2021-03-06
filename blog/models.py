from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',  on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    precio = models.IntegerField()
    archivo = models.FileField(upload_to='documents/', blank=True, null=True)
    componentes = models.CharField(
        max_length=20,
        choices=(('Procesadores','Procesadores'), ('Placa Video', 'Placa Video'), ('Otros', 'Otros')),
        )
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title