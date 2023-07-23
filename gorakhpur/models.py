from django.db import models

# Create your models here.
#----------------------------------------------------------------------------
class Status(models.Model):    
    status = models.CharField(max_length=500)
    def __str__(self):
        return self.status
#------------------------------------------------------------------------------------
class Call_Status(models.Model):    
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
#----------------------------------------------------------------------------



class Response(models.Model):
    response_from = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=12)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    call_status = models.ForeignKey(Call_Status,on_delete=models.CASCADE,null=True, blank=True)    
    def __str__(self):
        return self.response_from + " -- " + self.name + " -- " + self.number + " -- " + self.comment
#----------------------------------------------------------------------------


class Interested (models.Model):
    INTERESTED_TYPE = (
        ('DIGITAL MARKETING','DIGITAL MARKETING'),
        ('SOFTWARE','SOFTWARE'),
        ('WEBSITE','WEBSITE'),
        ('MOBILE APP', 'MOBILE APP'),
        ('GAME', 'GAME'),
        ('OTHERS', 'OTHERS'),
    )
    response = models.ForeignKey(Response,on_delete=models.CASCADE)
    interested_type = models.CharField(choices=INTERESTED_TYPE,max_length=100,null=True, blank=True)
    comment = models.TextField()
    follow_up = models.DateTimeField(null=True, blank=True)
    call_status = models.ForeignKey(Call_Status,on_delete=models.CASCADE,null=True, blank=True) 

    def __str__(self):
        return self.comment
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------   
class For_Job(models.Model):
    response = models.ForeignKey(Response,on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.comment


#----------------------------------------------------------------------------  
class For_Coaching(models.Model):
    response = models.ForeignKey(Response,on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.comment
    
#----------------------------------------------------------------------------