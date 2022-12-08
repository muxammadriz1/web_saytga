from django.db import models

# Create your models here.

class Type(models.Model):
    nomi= models.CharField(max_length=30)
    def __str__(self):
        return self.nomi


class Portfolio(models.Model):
    nomi = models.CharField(max_length=20)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm= models.ImageField(upload_to='media')
    vaqt=models.DateTimeField(auto_now=True)



class Team(models.Model):
    Ism=models.CharField(max_length=50)
    martaba=models.CharField(max_length=50)
    rasmi=models.ImageField(upload_to='media')
    Instagram = models.CharField(max_length=20)
    Twiter = models.CharField(max_length=20)
    Facebok= models.CharField(max_length=50)
    Linced=models.CharField(max_length=50)

class Message(models.Model):
    name= models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    time=models.DateTimeField(auto_now=True)