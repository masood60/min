from unicodedata import name
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class food(models.Model):
    name=models.CharField(_("نام غذا"), max_length=50)
    descreption=models.CharField(_("توضیحات"), max_length=50)
    rate=models.IntegerField(_("امتیاز"),default=0)
    price=models.IntegerField(_("قیمت"))
    time=models.IntegerField(_("زمان لازم"),default=30)
    pub_date=models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo=models.ImageField( upload_to='media/food/')
    def __str__(self):
        return self.name