from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    slave = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slaves_pics",blank=True,null=True)
    experience = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.slave)

class TrishaSlave(models.Model):
    name = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trisha_slaves')
    description = models.CharField(max_length=500,default="GoddessTrisha Slave")
    
    def __str__(self):
        return str(self.name)+"@"+str(self.image)


class Devotees(models.Model):
    name = models.CharField(max_length=500)
    picture = models.ImageField(upload_to = 'devotee_pics',default="Picture")
    religion = models.CharField(max_length=100)
    story = models.TextField(default="భగవాన్ త్రిషకృష్ణన్ దేవత భక్తుడిని అయినందుకు నేను గర్విస్తున్నాను")

    def __str__(self):
        return self.name

class Seva(models.Model):
    devotee = models.ForeignKey(Devotees,related_name='devotees',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name