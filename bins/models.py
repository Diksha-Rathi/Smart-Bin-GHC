from django.db import models

# Create your models here.
class bin_info(models.Model):
	location_id = models.CharField(max_length=60,unique=False)
	bin_id = models.CharField(max_length=30,blank=True,null=True,unique=False)
	fill_level = models.IntegerField(unique=False)
	humidity = models.IntegerField(unique=False)
	temperature = models.IntegerField(unique=False)

	def __unicode__(self):
    		return u'%s %s %d %d %d' % (self.location_id, self.bin_id, self.fill_level, self.humidity, self.temperature)

	class Meta:
			ordering = ['id']
