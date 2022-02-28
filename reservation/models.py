from django.db import models


# Create your models here.
class contact(models.Model):
    yourname=models.CharField(max_length=200,verbose_name='نام و نام خانوادگی')
    youremail=models.EmailField(verbose_name='ایمیل',max_length=250)
    yourtell=models.PositiveIntegerField(verbose_name='تلفن',max_length=15)
    def __str__(self):
        return self.yourname

    
class tabla(models.Model):
    contact=models.ForeignKey(contact,on_delete=models.CASCADE)
    select=(
        (1,'یک نفره'),
        (2,'دو نفره'),
        
    )
    selectperson=models.IntegerField(choices=select,verbose_name='میز چند نفره',max_length=1,default=2)
    
    numbertable=models.CharField(verbose_name="شماره صندلی",choices=selectperson,max_length=)
    def __str__(self):
        return self.selectperson    
    
        
        
    