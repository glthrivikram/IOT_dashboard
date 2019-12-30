from django.db import models
class feild(models.Model):
 
    location = models.CharField(max_length=100)
    lId = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    fName = models.CharField(max_length=25)
    def __str__(self):   # __unicode__ on Python 2
        return str(self.lId)+":"+self.location

class data(models.Model):
    temperature = models.DecimalField(decimal_places=3, max_digits=9)
    humidity = models.DecimalField(decimal_places=3, max_digits=9)
    lId = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = 'time'
    def __str__(self):   # __unicode__ on Python 2
        return str(str(self.lId)+":"+ str(self.time))

'''
    data.objects.values_list('lId',flat = True).distinct()
    data.objects.filter(lId=2).latest()
    {'temperature': ['3'], 'humidity': ['3'], 'lId': ['2']}
'''