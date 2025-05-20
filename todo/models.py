from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=50)
    desciption=models.TextField(blank=True, null=True)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.is_completed}"
    
    

    