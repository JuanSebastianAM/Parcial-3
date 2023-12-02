from django.db import models

class Nota (models.Model):
    

    """
    Modelo que representa de los elemnetos de las notas las cuales se veran en app notas
    """
    Titulo = models.CharField(max_length=30)
    Nota =  models.PositiveSmallIntegerField()
  
    
    
    def __str__(self) :
        return self.Titulo
    
  
    
   

    
    
    
     
    
    
    
    


