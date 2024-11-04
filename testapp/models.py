from django.db import models

class Event_model(models.Model):
    eventname=models.CharField(max_length=100)
    date=models.DateField()
    location = models.CharField(max_length=100)
    image=models.ImageField( upload_to="images/", default='images/favicon.jpeg')    
    type_of_event=models.TextField()
    
    def __str__(self):
        return self.eventname
   
    
from django.contrib.auth.models import User


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event_model, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.eventname}"
