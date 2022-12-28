from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   
    # khác với Charfield là trong admin panel, text area sẽ to hơn
    # null là null trong db, blank là cho phép rỗng khi create, add bằng python...
    # participants = models
    updated_at = models.DateTimeField(auto_now=True)  # take a snapshot EVERY TIME we update a row
    created_at = models.DateTimeField(auto_now_add=True) # take a snapshot ONLY THE FIRST TIME we create a row
    
    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)   
    # SET_NULL: xóa th cha, đám con vẫn trong db (lúc này sẽ cần nullable để chuyển gtri thành null)
    # CASCADE: xóa cha sẽ xóa luôn những th con tham chiếu tới
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)  # take a snapshot EVERY TIME we update a row
    created_at = models.DateTimeField(auto_now_add=True) # take a snapshot ONLY THE FIRST TIME we create a row

    def __str__(self) -> str:
        return self.body[:50]
