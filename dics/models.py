from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=200)
    urdu = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
      
def __str__(self):
        return self.word


    