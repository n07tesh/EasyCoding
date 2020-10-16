from django.db import models
#from django.contrib.auth.models import User
#from django.utils.text import slugify

# Create your models here.
#import misaka

# Create your models here.
#database koi data fetch krne k liye
#databasse ---> Excel workbook /// models in django  Table ---> sheet

class Contact(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email 
    
    #def# save(self,*args,**kwargs):
     #   self.slug = slugify(self.name)
      #  self.description_html = misaka.html(self.description)
       # super().save(*args,**kwargs)
