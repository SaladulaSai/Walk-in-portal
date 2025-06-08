from django.db import models

class WalkInDrive(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()  # New field
    end_time = models.TimeField() 
    venue = models.TextField()

    def __str__(self):
        return f"{self.company} - {self.role}"
    
    

