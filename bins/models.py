from django.db import models
#from datetime import datetime
#from datetime import date

# Create your models here.
class bin_record(models.Model):
	location_id = models.CharField(max_length=60)
	longitude=models.DecimalField(max_digits=15,decimal_places=10)
	latitude=models.DecimalField(max_digits=15,decimal_places=10)

	class Meta:
			ordering = ['id']

class bin_updates(models.Model):
	location_id = models.ForeignKey(bin_record)
	bin_id = models.CharField(max_length=30,blank=True,null=True)
	#date_id = models.DateField(_("Date"), default=date.today)
	date = models.DateField( auto_now_add=True)
	fill_level = models.IntegerField()
	humidity = models.IntegerField()
	temperature = models.IntegerField()

	class Meta:
			ordering = ['date']




# from django.db import models

# # Create your models here.

# class binAdded(models.Model):
# 	bin_id=models.CharField(max_length=20,blank=False,unique=True)
# 	date_added=models.DateField(auto_now_add=True)
# 	longitude=models.DecimalField(max_digits=20,decimal_places=13)
# 	latitude=models.DecimalField(max_digits=20,decimal_places=13)

# 	def __str__(self):
# 		return self.bin_id
# 	class Meta:
# 		verbose_name = 'bin'
# 		verbose_name_plural='bins'

# class bin_updates(models.Model):
# 	bin_id=models.ForeignKey(binAdded)
# 	current_date=models.DateField()
# 	fill_level=models.DecimalField(max_digits=5, decimal_places=3)
# 	temperature=models.IntegerField()
# 	humidity = models.IntegerField()

# 	def __str__(self):
# 		return self.bin_id.bin_id
