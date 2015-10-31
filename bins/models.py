from django.db import models
 
#Create your models here.
class bin_record(models.Model):
	location_id = models.CharField(max_length=60)
	longitude=models.DecimalField(max_digits=15,decimal_places=10)
	latitude=models.DecimalField(max_digits=15,decimal_places=10)

	def __str__(self):
		return self.location_id
	class Meta:
			ordering = ['id']


class bin_updates(models.Model):
	location_id = models.ForeignKey(bin_record)
	bin_id = models.CharField(max_length=30,blank=True,null=True)	
	date = models.DateField()
	fill_level = models.IntegerField()
	humidity = models.IntegerField()
	temperature = models.IntegerField()

	class Meta:
			ordering = ['date']

 