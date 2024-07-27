from django.db import models
from users.models import CustomUser

class Blog(models.Model):
    user = models.ForeignKey(CustomUser ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} created {self.title}'
        
