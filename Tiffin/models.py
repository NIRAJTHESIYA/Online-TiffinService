from django.db import models
from django.utils import timezone

# Create your models here.

# City Table 
class City(models.Model):
    idcity = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=45,null=True)

    class Meta:
        managed = True
        db_table = 'City'
    
    def __str__(self):
        return self.city_name   
    
    
# Area Table
class Area(models.Model):
    pincode = models.DecimalField(primary_key=True, max_digits=6, decimal_places=0)
    area_name = models.CharField(max_length=45)
    delivery_charges = models.IntegerField()
    city_name = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,db_column='_idcity')

    class Meta:
        managed = True
        db_table = 'Area'
    
    def __str__(self):
        return self.area_name


# User Table
class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45,blank=False)
    email = models.EmailField(max_length=45,unique=True)
    contact = models.CharField(max_length=10, unique=True, null=True)
    password = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    registration_date = models.DateTimeField(default=timezone.now)
    city_id = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,db_column='city_id')
    area_id = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, db_column='area_id')
    address = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'User'
    
    def __str__(self):
        return self.first_name
    
    def reg(self):
        self.save()   
      
      
# Month Table  
class Month(models.Model):
    month_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'Month'
        
    def __str__(self):
        return self.name

    
# Day Table
class Day(models.Model):
    day_id = models.AutoField(primary_key=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, db_column='name')
    day = models.PositiveSmallIntegerField()

    class Meta:
        managed = True
        db_table = 'Day'
        
    def __str__(self):
        return f"{self.month.name} {self.day}"
    
# Menu_Items
class MenuItem(models.Model):
    MenuItem_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = True
        db_table = 'MenuItem'

    def __str__(self):
        return self.name
    
# Day_Menu
    
# class DayMenu(models.Model):
#     DayMenu_id = models.AutoField(primary_key=True)
#     day = models.ForeignKey(Day, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.day} - {self.menu_item.name}"
