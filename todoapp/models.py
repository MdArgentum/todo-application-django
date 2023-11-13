from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=None)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Todo."""
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.name
