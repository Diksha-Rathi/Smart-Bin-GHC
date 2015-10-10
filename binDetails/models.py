from django.db import models

# Create your models here.

class binAdded(models.Model):
	bin_id=models.CharField(max_length=20,blank=False,unique=True)
	date_added=models.DateTimeField(auto_now_add=True)
	longitude=models.DecimalField(max_digits=20,decimal_places=13)
	latitude=models.DecimalField(max_digits=20,decimal_places=13)

	def __str__(self):
		return self.bin_id
	class Meta:
		verbose_name = 'bin'
		verbose_name_plural='bins'

class binDescription(models.Model):
	bin_id=models.ForeignKey(binAdded)
	current_date=models.DateTimeField()
	fill_level=models.DecimalField(max_digits=5, decimal_places=3)
	temperature=models.IntegerField()

	def __str__(self):
		return self.bin_id.bin_id
