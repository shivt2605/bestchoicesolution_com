from django.db import models

# Create your models here.

class Call_Status(models.Model):    
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Industry(models.Model):    
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class City(models.Model):    
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Locality(models.Model):    
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True, blank=True) 
    def __str__(self):
        return self.city.name + " -- " + self.name
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Visit_Response(models.Model):    
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------



class Visit(models.Model):
    visit_for = models.CharField(max_length=500)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE)
    form_name = models.CharField(max_length=500)
    locality = models.ForeignKey(Locality,on_delete=models.CASCADE,null=True, blank=True)
    full_address = models.CharField(max_length=12)
    contact_person = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    email_id = models.CharField(max_length=100,null=True, blank=True)
    featured_image = models.ImageField(upload_to="featuredimg",null=True)
    map_link = models.TextField(null=True, blank=True)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    visit_response = models.ForeignKey(Visit_Response,on_delete=models.CASCADE,null=True, blank=True)
    call_status = models.ForeignKey(Call_Status,on_delete=models.CASCADE,null=True, blank=True)   
    def __str__(self):
        return self.form_name + " -- " + self.full_address + " -- " + self.contact_person + " -- " + self.number + " -- " + self.comment
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

class Image(models.Model): 
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE,null=True, blank=True)
    featured_image = models.ImageField(upload_to="featuredimg",null=True)

    def __str__(self):
        return self.name
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------



class Meeting(models.Model):
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    comment = models.CharField(max_length=500,null=True, blank=True)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

